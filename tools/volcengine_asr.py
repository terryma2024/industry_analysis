#!/usr/bin/env python3
"""Volcengine AUC ASR adapter for the Bilibili daily research pipeline.

This command is intentionally small and dependency-light. It downloads protected
video audio locally when needed, uploads that audio through a user-configured
command so Volcengine can fetch it, submits the public audio URL to AUC, polls
for completion, and writes transcript text to --output or stdout.
"""

from __future__ import annotations

import argparse
import http.client
import json
import mimetypes
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOTENV_PATHS = (Path.home() / ".env", REPO_ROOT / ".env")
DEFAULT_SUBMIT_ENDPOINT = "https://openspeech.bytedance.com/api/v3/auc/bigmodel/submit"
DEFAULT_QUERY_ENDPOINT = "https://openspeech.bytedance.com/api/v3/auc/bigmodel/query"
DIRECT_AUDIO_EXTENSIONS = (".mp3", ".m4a", ".aac", ".wav", ".flac", ".ogg", ".webm", ".mp4")
BILIBILI_NETLOCS = ("bilibili.com", "b23.tv")
BILIBILI_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)


def load_dotenv() -> None:
    for path in DOTENV_PATHS:
        if not path.exists():
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if key and key not in os.environ:
                os.environ[key] = value


def require_env() -> tuple[str, str, str]:
    app_id = os.environ.get("VOLCENGINE_APP_ID", "").strip()
    token = os.environ.get("VOLCENGINE_ACCESS_TOKEN", "").strip()
    secret = os.environ.get("VOLCENGINE_SECRET_KEY", "").strip()
    missing = [
        name
        for name, value in [
            ("VOLCENGINE_APP_ID", app_id),
            ("VOLCENGINE_ACCESS_TOKEN", token),
            ("VOLCENGINE_SECRET_KEY", secret),
        ]
        if not value
    ]
    if missing:
        raise SystemExit("missing required env vars: " + ", ".join(missing))
    return app_id, token, secret


def run(args: list[str], timeout: int = 300) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, timeout=timeout, check=False)


def add_yt_dlp_cookie_args(command: list[str]) -> None:
    cookies_file = os.environ.get("BILIBILI_YTDLP_COOKIES_FILE", "").strip()
    cookies_from_browser = os.environ.get("BILIBILI_YTDLP_COOKIES_FROM_BROWSER", "").strip()
    insert_at = 3
    if cookies_file:
        command[insert_at:insert_at] = ["--cookies", cookies_file]
        insert_at += 2
    elif cookies_from_browser:
        command[insert_at:insert_at] = ["--cookies-from-browser", cookies_from_browser]


def add_bilibili_headers(command: list[str]) -> None:
    command[3:3] = [
        "--add-header",
        "Referer:https://www.bilibili.com/",
        "--add-header",
        "User-Agent:" + BILIBILI_UA,
    ]


def is_bilibili_url(url: str) -> bool:
    lowered = url.lower()
    return any(netloc in lowered for netloc in BILIBILI_NETLOCS)


def is_direct_audio_url(url: str) -> bool:
    return url.lower().split("?", 1)[0].endswith(DIRECT_AUDIO_EXTENSIONS)


def force_upload() -> bool:
    value = os.environ.get("VOLCENGINE_ASR_FORCE_UPLOAD", "").strip().lower()
    return value in {"1", "true", "yes", "on"}


def resolve_audio_url(url: str) -> tuple[str, str]:
    command = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--no-update",
        "--no-playlist",
        "-f",
        "ba/bestaudio",
        "--get-url",
        url,
    ]
    if is_bilibili_url(url):
        add_bilibili_headers(command)
    add_yt_dlp_cookie_args(command)

    proc = run(
        command,
        timeout=180,
    )
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip()
        raise SystemExit(
            "yt-dlp failed to resolve audio URL. Run this command via "
            "`uv run --group video-ytdlp python tools/volcengine_asr.py ...`. "
            f"Detail: {detail}"
        )
    audio_url = proc.stdout.strip().splitlines()[-1].strip()
    if not audio_url:
        raise SystemExit("yt-dlp returned an empty audio URL")
    return audio_url, guess_format(audio_url)


def extract_bvid(url: str) -> str:
    if re.fullmatch(r"BV[a-zA-Z0-9]+", url):
        return url
    match = re.search(r"(BV[a-zA-Z0-9]{10,})", url)
    return match.group(1) if match else ""


def bilibili_api_json(url: str, referer: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": BILIBILI_UA,
            "Referer": referer,
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def select_bilibili_audio(play_payload: dict[str, Any]) -> str:
    dash = ((play_payload.get("data") or {}).get("dash") or {})
    audios = dash.get("audio") or []
    if not isinstance(audios, list) or not audios:
        return ""
    ranked = sorted(
        (item for item in audios if isinstance(item, dict)),
        key=lambda item: int(item.get("bandwidth") or 0),
        reverse=True,
    )
    for item in ranked:
        audio_url = item.get("baseUrl") or item.get("base_url")
        if isinstance(audio_url, str) and audio_url.startswith(("http://", "https://")):
            return audio_url
    return ""


def download_bilibili_audio_via_api(url: str, output_dir: Path) -> Path:
    bvid = extract_bvid(url)
    if not bvid:
        raise SystemExit("could not extract Bilibili BV id for API audio fallback")
    referer = f"https://www.bilibili.com/video/{bvid}"
    view_url = "https://api.bilibili.com/x/web-interface/view?" + urllib.parse.urlencode({"bvid": bvid})
    view_payload = bilibili_api_json(view_url, referer)
    if view_payload.get("code") != 0:
        raise SystemExit(f"Bilibili view API failed: {view_payload.get('message') or view_payload.get('code')}")
    data = view_payload.get("data") or {}
    cid = data.get("cid")
    if not cid:
        raise SystemExit("Bilibili view API returned no cid")
    play_url = "https://api.bilibili.com/x/player/playurl?" + urllib.parse.urlencode(
        {
            "bvid": bvid,
            "cid": cid,
            "fnval": 16,
            "fourk": 1,
        }
    )
    play_payload = bilibili_api_json(play_url, referer)
    if play_payload.get("code") != 0:
        raise SystemExit(f"Bilibili playurl API failed: {play_payload.get('message') or play_payload.get('code')}")
    audio_url = select_bilibili_audio(play_payload)
    if not audio_url:
        raise SystemExit("Bilibili playurl API returned no DASH audio URL")

    output_path = output_dir / "asr-audio.m4a"
    last_error = ""
    for attempt in range(3):
        request = urllib.request.Request(
            audio_url,
            headers={
                "User-Agent": BILIBILI_UA,
                "Referer": referer,
                "Origin": "https://www.bilibili.com",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                output_path.write_bytes(response.read())
            break
        except (http.client.IncompleteRead, TimeoutError, urllib.error.URLError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if output_path.exists():
                output_path.unlink()
            if attempt == 2:
                raise SystemExit(f"Bilibili API audio download failed after retries: {last_error}") from exc
            time.sleep(1.5 * (attempt + 1))
    if output_path.stat().st_size == 0:
        raise SystemExit("Bilibili API audio download produced an empty file")
    return output_path


def download_audio(url: str, output_dir: Path) -> Path:
    if is_bilibili_url(url):
        try:
            return download_bilibili_audio_via_api(url, output_dir)
        except Exception as exc:
            api_error = str(exc)
        else:
            api_error = ""
    else:
        api_error = ""

    output_template = str(output_dir / "asr-audio.%(ext)s")
    command = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--no-update",
        "--no-playlist",
        "-f",
        "ba/bestaudio",
        "-o",
        output_template,
        "--print",
        "after_move:filepath",
        url,
    ]
    if is_bilibili_url(url):
        add_bilibili_headers(command)
    add_yt_dlp_cookie_args(command)
    proc = run(command, timeout=900)
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip()
        cookie_hint = ""
        if is_bilibili_url(url) and "412" in detail:
            cookie_hint = (
                " Bilibili returned HTTP 412; set BILIBILI_YTDLP_COOKIES_FILE "
                "to an exported Netscape cookies file, or set "
                "BILIBILI_YTDLP_COOKIES_FROM_BROWSER when local browser-cookie "
                "access is explicitly allowed."
            )
        api_prefix = f"Bilibili API audio fallback failed: {api_error}. " if api_error else ""
        raise SystemExit(f"{api_prefix}yt-dlp failed to download audio. Detail: {detail}{cookie_hint}")

    for line in reversed(proc.stdout.splitlines()):
        candidate = Path(line.strip())
        if candidate.exists() and candidate.is_file():
            return candidate

    files = sorted(output_dir.glob("asr-audio.*"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not files:
        raise SystemExit("yt-dlp completed but no downloaded audio file was found")
    return files[0]


def content_type_for(path: Path) -> str:
    guessed = mimetypes.guess_type(path.name)[0]
    return guessed or "application/octet-stream"


def extract_url_from_upload_output(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return ""
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError:
        payload = None
    if isinstance(payload, dict):
        for key in ("url", "audio_url", "public_url", "uri"):
            value = payload.get(key)
            if isinstance(value, str) and value.startswith(("http://", "https://")):
                return value.strip()
    match = re.search(r"https?://\S+", stripped)
    if match:
        return match.group(0).strip().strip("'\"")
    return ""


def upload_audio(audio_path: Path) -> str:
    template = os.environ.get("VOLCENGINE_AUDIO_UPLOAD_COMMAND", "").strip()
    if not template:
        raise SystemExit(
            "VOLCENGINE_AUDIO_UPLOAD_COMMAND is required for Bilibili ASR. "
            "Volcengine AUC fetches audio server-side, and Bilibili signed audio "
            "URLs are not reliably downloadable by Volcengine. Configure a command "
            "that uploads the local audio file and prints a public HTTPS URL."
        )
    values = {
        "input": str(audio_path),
        "filename": audio_path.name,
        "content_type": content_type_for(audio_path),
    }
    args = shlex.split(template.format(**values))
    timeout = int(os.environ.get("VOLCENGINE_AUDIO_UPLOAD_TIMEOUT", "900"))
    proc = run(args, timeout=timeout)
    output = proc.stdout.strip() or proc.stderr.strip()
    if proc.returncode != 0:
        raise SystemExit(f"audio upload command failed: {output}")
    public_url = extract_url_from_upload_output(output)
    if not public_url:
        raise SystemExit("audio upload command did not print a public http(s) URL")
    return public_url


def prepare_audio_url(url: str) -> tuple[str, str]:
    if is_direct_audio_url(url) and not force_upload():
        return url, guess_format(url)

    if not is_bilibili_url(url) and not force_upload():
        resolved_url, audio_format = resolve_audio_url(url)
        return resolved_url, audio_format

    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = download_audio(url, Path(tmpdir))
        public_url = upload_audio(audio_path)
    return public_url, guess_format(public_url)


def guess_format(url: str) -> str:
    clean = url.lower().split("?", 1)[0]
    for ext in ("mp3", "m4a", "aac", "wav", "flac", "ogg", "webm"):
        if clean.endswith("." + ext):
            return ext
    return "m4a"


def http_json(url: str, headers: dict[str, str], payload: dict[str, Any] | None) -> tuple[dict[str, Any], dict[str, str]]:
    data = json.dumps(payload or {}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", errors="replace")
            response_headers = {key.lower(): value for key, value in response.headers.items()}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Volcengine HTTP {exc.code}: {body}") from exc
    try:
        parsed = json.loads(body) if body else {}
    except json.JSONDecodeError:
        parsed = {"raw": body}
    return parsed, response_headers


def build_headers(app_id: str, token: str, secret: str, model: str, request_id: str) -> dict[str, str]:
    return {
        "Content-Type": "application/json",
        "X-Api-App-Key": app_id,
        "X-Api-Access-Key": token,
        "X-Api-Secret-Key": secret,
        "X-Api-Resource-Id": model,
        "X-Api-Request-Id": request_id,
        "X-Api-Sequence": "-1",
    }


def submit(audio_url: str, audio_format: str, model: str, request_id: str) -> tuple[dict[str, Any], dict[str, str]]:
    app_id, token, secret = require_env()
    endpoint = os.environ.get("VOLCENGINE_ASR_SUBMIT_ENDPOINT", DEFAULT_SUBMIT_ENDPOINT).strip()
    headers = build_headers(app_id, token, secret, model, request_id)
    payload = {
        "user": {"uid": os.environ.get("USER", "codex")},
        "audio": {
            "url": audio_url,
            "format": audio_format,
        },
        "request": {
            "model_name": model,
            "enable_itn": True,
            "enable_punc": True,
            "enable_ddc": True,
        },
    }
    return http_json(endpoint, headers, payload)


def query(model: str, request_id: str) -> tuple[dict[str, Any], dict[str, str]]:
    app_id, token, secret = require_env()
    endpoint = os.environ.get("VOLCENGINE_ASR_QUERY_ENDPOINT", DEFAULT_QUERY_ENDPOINT).strip()
    headers = build_headers(app_id, token, secret, model, request_id)
    return http_json(endpoint, headers, {})


def status_from(payload: dict[str, Any], headers: dict[str, str]) -> str:
    header_status = headers.get("x-api-status-code", "")
    for key in ("status", "status_code", "code"):
        value = payload.get(key)
        if value not in (None, ""):
            return str(value)
    return header_status


def volc_message(headers: dict[str, str]) -> str:
    for key in ("x-api-message", "x-api-status-message", "x-tt-logid"):
        value = headers.get(key)
        if value:
            return f"{key}={value}"
    return ""


def extract_text(payload: Any) -> str:
    if isinstance(payload, str):
        return payload.strip()
    if isinstance(payload, list):
        parts = [extract_text(item) for item in payload]
        return "\n".join(part for part in parts if part)
    if not isinstance(payload, dict):
        return ""

    for key in ("text", "transcript", "subtitle_text"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    result = payload.get("result")
    if result is not None:
        text = extract_text(result)
        if text:
            return text

    utterances = payload.get("utterances") or payload.get("segments")
    if isinstance(utterances, list):
        parts = []
        for item in utterances:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("utterance") or "").strip())
            elif isinstance(item, str):
                parts.append(item.strip())
        return "\n".join(part for part in parts if part)

    for value in payload.values():
        text = extract_text(value)
        if text:
            return text
    return ""


def transcribe(url: str, model: str, poll_interval: float, timeout: int) -> str:
    require_env()
    audio_url, audio_format = prepare_audio_url(url)
    request_id = str(uuid.uuid4())
    submit_payload, submit_headers = submit(audio_url, audio_format, model, request_id)
    submit_status = status_from(submit_payload, submit_headers)
    if submit_status and submit_status not in {"20000000", "0", "success", "Success"}:
        message = volc_message(submit_headers)
        raise SystemExit(
            f"Volcengine submit failed status={submit_status} {message}: "
            f"{json.dumps(submit_payload, ensure_ascii=False)}"
        )

    deadline = time.monotonic() + timeout
    last_payload: dict[str, Any] = submit_payload
    while time.monotonic() < deadline:
        payload, headers = query(model, request_id)
        last_payload = payload
        text = extract_text(payload)
        if text:
            return text
        status = status_from(payload, headers)
        if status and status not in {"20000000", "20000001", "0", "running", "processing", "queued", "Success"}:
            message = volc_message(headers)
            raise SystemExit(
                f"Volcengine query failed status={status} {message}: "
                f"{json.dumps(payload, ensure_ascii=False)}"
            )
        time.sleep(poll_interval)
    raise SystemExit(f"Volcengine ASR timed out. Last payload: {json.dumps(last_payload, ensure_ascii=False)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="video page URL or direct audio URL")
    parser.add_argument("--model", default="volc.seedasr.auc", help="Volcengine resource/model id")
    parser.add_argument("--output", help="write transcript to this path")
    parser.add_argument("--poll-interval", type=float, default=3.0)
    parser.add_argument("--timeout", type=int, default=1800)
    return parser


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_parser().parse_args(argv)
    text = transcribe(args.url, args.model, args.poll_interval, args.timeout)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
