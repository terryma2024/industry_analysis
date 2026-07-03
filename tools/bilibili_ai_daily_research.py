#!/usr/bin/env python3
"""Daily Bilibili AI/embodied-intelligence research capture pipeline.

The script makes the deterministic parts of the scheduled workflow repeatable:

1. Pull candidate videos from a JSON file or OpenCLI.
2. Normalize Bilibili video metadata.
3. Skip videos already present in raw/ or knowledge/.
4. Keep only AI / robotics / embodied-intelligence candidates.
5. Extract transcripts through the local video-summarizer script.
6. Write raw transcript packets, source cards, sources.csv rows, and a run report.

The final industry synthesis is intentionally left to Codex: this script prepares
traceable source packets and a clear handoff instead of inventing analysis.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
VIDEO_SUBTITLE_SCRIPT = REPO_ROOT / ".agents/skills/video-summarizer/scripts/video_subtitle.py"
RAW_TRANSCRIPTS_DIR = REPO_ROOT / "raw/_inbox/transcripts"
SOURCES_DIR = REPO_ROOT / "knowledge/_sources"
SYNTHESIS_DIR = REPO_ROOT / "knowledge/_syntheses"
KNOWLEDGE_INDEX = REPO_ROOT / "knowledge/index.md"
KNOWLEDGE_LOG = REPO_ROOT / "knowledge/log.md"
SEARCH_ROOTS = (REPO_ROOT / "raw", REPO_ROOT / "knowledge")
DOTENV_PATHS = (
    Path.home() / ".env",
    REPO_ROOT / ".env",
)

TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
}

HIGH_RELEVANCE_PATTERNS = [
    r"\bai\b",
    r"\bagent(s)?\b",
    "codex",
    "openai",
    "chatgpt",
    "claude code",
    "cursor",
    r"\bllm(s)?\b",
    r"\bvla\b",
    r"\bvlm\b",
    r"\bworld model(s)?\b",
    r"\bembodied\b",
    r"\brobot(ic|ics|s)?\b",
    r"\bhumanoid(s)?\b",
    r"\ble?robot\b",
    r"\bisaac\b",
    r"\bgr00t\b",
    r"\bopenpi\b",
    r"\bros\s*2\b",
    "人工智能",
    "大模型",
    "基础模型",
    "多模态",
    "世界模型",
    "智能体",
    "智能体工具链",
    "具身",
    "具身智能",
    "机器人",
    "人形机器人",
    "机器人大脑",
    "机器人小脑",
    "自动驾驶",
    "自动标注",
    "数据闭环",
    "模型训练",
    "推理加速",
    "算力",
    "ai芯片",
    "昇腾",
    "寒武纪",
    "英伟达",
    "nvidia",
    "宇树",
    "unitree",
    "智元",
    "agibot",
    "逐际",
    "limx",
    "特斯拉",
    "optimus",
]

MEDIUM_RELEVANCE_PATTERNS = [
    "芯片",
    "gpu",
    "传感器",
    "激光雷达",
    "力传感",
    "仿真",
    "强化学习",
    "模仿学习",
    "扩散策略",
    "数据集",
    "开源模型",
    "模型部署",
    "端侧",
    "边缘计算",
    "aigc",
    "deepseek",
    "qwen",
    "通义",
    "智谱",
    "kimi",
    "文心",
]

ROBOTICS_PATTERNS = [
    "具身",
    "机器人",
    "人形机器人",
    "embodied",
    "robot",
    "humanoid",
    "vla",
    "lerobot",
    "isaac",
    "gr00t",
    "openpi",
    "宇树",
    "unitree",
    "智元",
    "agibot",
    "逐际",
    "limx",
]


@dataclasses.dataclass
class VideoCandidate:
    title: str
    url: str
    bvid: str = ""
    aid: str = ""
    video_id: str = ""
    author: str = ""
    published_at: str = ""
    favorited_at: str = ""
    description: str = ""
    tags: list[str] = dataclasses.field(default_factory=list)
    category: str = ""
    raw: dict[str, Any] = dataclasses.field(default_factory=dict)

    def canonical_id(self) -> str:
        return self.bvid or self.aid or self.video_id or stable_hash(self.url or self.title)

    def canonical_url(self) -> str:
        if self.url:
            return self.url
        if self.bvid:
            return f"https://www.bilibili.com/video/{self.bvid}"
        return ""

    def identifiers(self) -> list[str]:
        values = [
            self.bvid,
            self.aid,
            self.video_id,
            self.canonical_url(),
        ]
        seen: set[str] = set()
        idents: list[str] = []
        for value in values:
            clean = str(value or "").strip()
            if len(clean) < 6 or clean in seen:
                continue
            seen.add(clean)
            idents.append(clean)
        return idents

    def text_blob(self) -> str:
        return " ".join(
            part
            for part in [
                self.title,
                self.description,
                " ".join(self.tags),
                self.category,
                self.author,
            ]
            if part
        )


@dataclasses.dataclass
class CandidateDecision:
    candidate: VideoCandidate
    status: str
    reason: str
    relevance_score: int = 0
    matched_terms: list[str] = dataclasses.field(default_factory=list)
    duplicate_hits: list[str] = dataclasses.field(default_factory=list)
    target_industries: list[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ProcessResult:
    decision: CandidateDecision
    status: str
    reason: str
    raw_artifact: str = ""
    source_card: str = ""
    transcript_chars: int = 0
    extraction_method: str = ""


def stable_hash(text: str, length: int = 12) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:length]


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


def today_str() -> str:
    return dt.datetime.now().date().isoformat()


def slugify(text: str, fallback: str = "video") -> str:
    lowered = text.lower()
    lowered = re.sub(r"https?://", "", lowered)
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = lowered.strip("-")
    return (lowered or fallback)[:72].strip("-") or fallback


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_dotenv(paths: tuple[Path, ...] = DOTENV_PATHS) -> None:
    """Load simple KEY=VALUE lines without overriding the process environment."""
    for path in paths:
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


def run_command(args: list[str], cwd: Path = REPO_ROOT, timeout: int = 180) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            args,
            cwd=str(cwd),
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", errors="ignore")
        stderr = exc.stderr if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", errors="ignore")
        message = f"command timed out after {timeout} seconds"
        stderr = f"{stderr.rstrip()}\n{message}".strip() if stderr else message
        return subprocess.CompletedProcess(args=args, returncode=124, stdout=stdout, stderr=stderr)


def extract_items(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []

    likely_keys = (
        "medias",
        "archives",
        "videos",
        "items",
        "list",
        "result",
        "data",
    )
    for key in likely_keys:
        value = payload.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
        if isinstance(value, dict):
            nested = extract_items(value)
            if nested:
                return nested
    return []


def first_value(item: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        value = item.get(key)
        if value is None:
            continue
        if isinstance(value, (str, int, float)):
            return str(value).strip()
    return ""


def nested_name(item: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        value = item.get(key)
        if isinstance(value, dict):
            for name_key in ("name", "uname", "title"):
                name = value.get(name_key)
                if name:
                    return str(name).strip()
        elif isinstance(value, str):
            return value.strip()
    return ""


def normalize_timestamp(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, (int, float)):
        if value > 10_000_000_000:
            value = value / 1000
        try:
            return dt.datetime.fromtimestamp(value, dt.UTC).date().isoformat()
        except (OverflowError, OSError, ValueError):
            return str(value)
    return str(value).strip()


def normalize_tags(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [part.strip() for part in re.split(r"[,，;；\s]+", value) if part.strip()]
    if isinstance(value, list):
        tags: list[str] = []
        for item in value:
            if isinstance(item, dict):
                tag = first_value(item, ("tag_name", "name", "title"))
                if tag:
                    tags.append(tag)
            elif isinstance(item, (str, int, float)):
                tags.append(str(item).strip())
        return [tag for tag in tags if tag]
    return []


def normalize_candidate(item: dict[str, Any]) -> VideoCandidate:
    title = first_value(item, ("title", "name", "video_title", "archive_title"))
    url = first_value(item, ("url", "link", "uri", "arcurl", "short_link", "share_url"))
    bvid = first_value(item, ("bvid", "bv", "BV", "bvid_str"))
    if not bvid:
        match = re.search(r"(BV[0-9A-Za-z]+)", url)
        if match:
            bvid = match.group(1)
    aid = first_value(item, ("aid", "av", "id", "avid"))
    if aid.startswith("BV") and not bvid:
        bvid, aid = aid, ""
    video_id = first_value(item, ("video_id", "id_str", "media_id"))
    description = first_value(item, ("description", "desc", "intro", "summary"))
    category = first_value(item, ("category", "tname", "typename", "partition", "business"))
    author = first_value(item, ("author", "up", "upper_name", "owner_name", "uname"))
    if not author:
        author = nested_name(item, ("owner", "upper", "author", "up"))
    tags = normalize_tags(item.get("tags") or item.get("tag") or item.get("keywords"))
    published_at = normalize_timestamp(
        item.get("pubdate")
        or item.get("ctime")
        or item.get("published_at")
        or item.get("publish_time")
    )
    favorited_at = normalize_timestamp(
        item.get("fav_time")
        or item.get("favorite_time")
        or item.get("created_at")
        or item.get("mtime")
    )
    if not url and bvid:
        url = f"https://www.bilibili.com/video/{bvid}"
    return VideoCandidate(
        title=title or bvid or video_id or "Untitled Bilibili video",
        url=url,
        bvid=bvid,
        aid=aid,
        video_id=video_id,
        author=author,
        published_at=published_at,
        favorited_at=favorited_at,
        description=description,
        tags=tags,
        category=category,
        raw=item,
    )


def extract_bvid(value: str) -> str:
    if re.match(r"^BV[a-zA-Z0-9]+$", value):
        return value
    match = re.search(r"bilibili\.com/video/(BV[a-zA-Z0-9]+)", value)
    if match:
        return match.group(1)
    match = re.search(r"(BV[a-zA-Z0-9]{10,})", value)
    return match.group(1) if match else ""


def fetch_bilibili_candidate(url_or_bvid: str) -> tuple[VideoCandidate, str]:
    bvid = extract_bvid(url_or_bvid)
    canonical_url = f"https://www.bilibili.com/video/{bvid}" if bvid else url_or_bvid
    if not bvid:
        return normalize_candidate({"url": url_or_bvid}), "could not extract BV id from URL"

    api_url = "https://api.bilibili.com/x/web-interface/view?" + urllib.parse.urlencode({"bvid": bvid})
    request = urllib.request.Request(
        api_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
            "Referer": canonical_url,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        return normalize_candidate({"url": canonical_url, "bvid": bvid}), f"metadata fetch failed: {exc}"

    if payload.get("code") != 0 or not isinstance(payload.get("data"), dict):
        return normalize_candidate({"url": canonical_url, "bvid": bvid}), f"metadata API returned: {payload}"

    data = payload["data"]
    owner = data.get("owner") if isinstance(data.get("owner"), dict) else {}
    candidate = normalize_candidate(
        {
            "title": data.get("title", ""),
            "url": canonical_url,
            "bvid": data.get("bvid", bvid),
            "aid": data.get("aid", ""),
            "owner": owner,
            "description": data.get("desc", ""),
            "category": data.get("tname", ""),
            "pubdate": data.get("pubdate", ""),
            "tags": data.get("tag", []),
        }
    )
    return candidate, ""


def load_candidates_from_json(path: Path, limit: int) -> list[VideoCandidate]:
    items = extract_items(read_json(path))
    return [normalize_candidate(item) for item in items[:limit]]


def parse_opencli_json(stdout: str) -> Any:
    text = stdout.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("[")
        end = text.rfind("]")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        raise


def flatten_command_entries(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [entry for entry in payload if isinstance(entry, dict)]
    if isinstance(payload, dict):
        rows: list[dict[str, Any]] = []
        for value in payload.values():
            if isinstance(value, list):
                rows.extend(entry for entry in value if isinstance(entry, dict))
            elif isinstance(value, dict):
                rows.extend(flatten_command_entries(value))
        return rows
    return []


def fetch_candidates_with_opencli(limit: int) -> tuple[list[VideoCandidate], list[str]]:
    errors: list[str] = []
    override = os.environ.get("BILIBILI_FAVORITES_OPENCLI_COMMAND", "").strip()
    if override:
        args = shlex.split(override.format(limit=limit))
        proc = run_command(args, timeout=240)
        if proc.returncode != 0:
            return [], [f"override command failed: {proc.stderr.strip() or proc.stdout.strip()}"]
        payload = parse_opencli_json(proc.stdout)
        return [normalize_candidate(item) for item in extract_items(payload)[:limit]], []

    if not shutil.which("opencli"):
        return [], ["opencli binary not found; install/configure OpenCLI or pass --candidates-json"]

    list_proc = run_command(["opencli", "list", "-f", "json"], timeout=120)
    if list_proc.returncode != 0:
        return [], [f"opencli list failed: {list_proc.stderr.strip() or list_proc.stdout.strip()}"]

    try:
        entries = flatten_command_entries(parse_opencli_json(list_proc.stdout))
    except json.JSONDecodeError as exc:
        return [], [f"opencli list did not return JSON: {exc}"]

    scored: list[tuple[int, dict[str, Any]]] = []
    for entry in entries:
        haystack = " ".join(str(entry.get(key, "")) for key in ("site", "name", "aliases", "description")).lower()
        if not any(token in haystack for token in ("bilibili", "bili", "哔哩", "b站")):
            continue
        score = 0
        for token in ("favorite", "favorites", "fav", "collection", "folder", "收藏", "默认收藏夹"):
            if token in haystack:
                score += 3
        if "video" in haystack or "视频" in haystack:
            score += 1
        if score:
            scored.append((score, entry))
    scored.sort(key=lambda row: row[0], reverse=True)

    for _, entry in scored[:5]:
        site = str(entry.get("site") or "").strip()
        name = str(entry.get("name") or "").strip()
        if not site or not name:
            continue
        help_proc = run_command(["opencli", site, name, "--help"], timeout=60)
        args = ["opencli", site, name, "-f", "json"]
        if "--limit" in help_proc.stdout or "--limit" in help_proc.stderr:
            args.extend(["--limit", str(limit)])
        proc = run_command(args, timeout=240)
        if proc.returncode != 0:
            errors.append(f"{site} {name} failed: {proc.stderr.strip() or proc.stdout.strip()}")
            continue
        try:
            payload = parse_opencli_json(proc.stdout)
            candidates = [normalize_candidate(item) for item in extract_items(payload)[:limit]]
        except json.JSONDecodeError as exc:
            errors.append(f"{site} {name} returned non-JSON output: {exc}")
            continue
        if candidates:
            return candidates, errors
        errors.append(f"{site} {name} returned no video-like items")

    if not scored:
        errors.append("no Bilibili favorite-like OpenCLI command found; set BILIBILI_FAVORITES_OPENCLI_COMMAND")
    return [], errors


def rg_search(repo_root: Path, identifiers: list[str]) -> list[str]:
    if not shutil.which("rg"):
        return []
    hits: list[str] = []
    for ident in identifiers:
        proc = run_command(
            [
                "rg",
                "-n",
                "--fixed-strings",
                "--glob",
                "!knowledge/_syntheses/bilibili-ai-daily-run-*.md",
                ident,
                "raw",
                "knowledge",
            ],
            cwd=repo_root,
            timeout=60,
        )
        if proc.returncode == 0:
            for line in proc.stdout.splitlines()[:5]:
                hits.append(line)
        elif proc.returncode not in (0, 1):
            continue
    return hits


def fallback_search(repo_root: Path, identifiers: list[str]) -> list[str]:
    hits: list[str] = []
    for root in (repo_root / "raw", repo_root / "knowledge"):
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                rel_path = path.relative_to(repo_root).as_posix()
            except ValueError:
                rel_path = path.as_posix()
            if re.match(r"knowledge/_syntheses/bilibili-ai-daily-run-\d{4}-\d{2}-\d{2}\.md$", rel_path):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for ident in identifiers:
                idx = text.find(ident)
                if idx >= 0:
                    rel = path.relative_to(repo_root)
                    line_no = text[:idx].count("\n") + 1
                    hits.append(f"{rel}:{line_no}:{ident}")
                    break
            if len(hits) >= 5:
                return hits
    return hits


def find_duplicate_hits(repo_root: Path, candidate: VideoCandidate) -> list[str]:
    identifiers = candidate.identifiers()
    if not identifiers:
        return []
    hits = rg_search(repo_root, identifiers)
    if hits:
        return hits
    return fallback_search(repo_root, identifiers)


def pattern_matches(blob: str, patterns: list[str]) -> list[str]:
    lowered = blob.lower()
    matches: list[str] = []
    for pattern in patterns:
        if pattern.startswith(r"\b") or "\\" in pattern:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                matches.append(pattern)
        elif pattern.lower() in lowered:
            matches.append(pattern)
    return matches


def relevance(candidate: VideoCandidate) -> tuple[int, list[str], list[str]]:
    blob = candidate.text_blob()
    high = pattern_matches(blob, HIGH_RELEVANCE_PATTERNS)
    medium = pattern_matches(blob, MEDIUM_RELEVANCE_PATTERNS)
    score = len(high) * 2 + len(medium)
    robotics = pattern_matches(blob, ROBOTICS_PATTERNS)
    industries = ["ai"]
    if robotics:
        industries.insert(0, "robotics-embodied-ai")
    return score, high + medium, list(dict.fromkeys(industries))


def selected_id_matches(candidate: VideoCandidate, selected_ids: set[str]) -> bool:
    if not selected_ids:
        return False
    return any(identifier in selected_ids for identifier in candidate.identifiers())


def decide_candidate(
    repo_root: Path,
    candidate: VideoCandidate,
    selected_ids: set[str] | None = None,
    process_all_non_duplicates: bool = False,
) -> CandidateDecision:
    duplicate_hits = find_duplicate_hits(repo_root, candidate)
    if duplicate_hits:
        return CandidateDecision(
            candidate=candidate,
            status="skipped_duplicate",
            reason="video identifier already appears in raw/ or knowledge/",
            duplicate_hits=duplicate_hits,
        )

    score, terms, industries = relevance(candidate)
    selected_ids = selected_ids or set()
    if selected_id_matches(candidate, selected_ids):
        return CandidateDecision(
            candidate=candidate,
            status="selected",
            reason="selected by model relevance judgment",
            relevance_score=score,
            matched_terms=terms,
            target_industries=industries or ["ai"],
        )
    if process_all_non_duplicates:
        return CandidateDecision(
            candidate=candidate,
            status="selected",
            reason="selected by --process-all-non-duplicates",
            relevance_score=score,
            matched_terms=terms,
            target_industries=industries or ["ai"],
        )
    return CandidateDecision(
        candidate=candidate,
        status="needs_model_review",
        reason="awaiting model relevance judgment; keyword score is diagnostic only",
        relevance_score=score,
        matched_terms=terms,
        target_industries=industries if score else [],
    )


def extract_transcript(candidate: VideoCandidate, timeout: int) -> tuple[str, str, str]:
    url = candidate.canonical_url()
    if not url:
        return "", "", "missing video URL"
    proc = run_command(
        ["uv", "run", "python", str(VIDEO_SUBTITLE_SCRIPT.relative_to(REPO_ROOT)), url],
        cwd=REPO_ROOT,
        timeout=timeout,
    )
    if proc.returncode != 0:
        return "", "", proc.stderr.strip() or proc.stdout.strip() or "video_subtitle.py failed"
    try:
        payload = parse_opencli_json(proc.stdout)
    except json.JSONDecodeError as exc:
        return "", "", f"video_subtitle.py returned non-JSON output: {exc}"
    if isinstance(payload, dict) and payload.get("error"):
        return "", "", str(payload.get("error"))
    if isinstance(payload, dict):
        text = str(payload.get("subtitle_text") or payload.get("transcript") or "").strip()
        if text:
            method = str(payload.get("method") or payload.get("platform") or "video_subtitle.py")
            return text, method, ""
    return "", "", "no subtitle text returned"


def run_external_asr(candidate: VideoCandidate, timeout: int) -> tuple[str, str, str]:
    template = os.environ.get("VOLCENGINE_ASR_COMMAND", "").strip()
    if not template:
        available = [
            key
            for key in ("VOLCENGINE_APP_ID", "VOLCENGINE_ACCESS_TOKEN", "VOLCENGINE_SECRET_KEY")
            if os.environ.get(key)
        ]
        suffix = f"; loaded credentials: {', '.join(available)}" if available else ""
        return "", "", "VOLCENGINE_ASR_COMMAND is not configured" + suffix

    primary_model = os.environ.get("VOLCENGINE_ASR_MODEL_PRIMARY", "volc.seedasr.auc").strip()
    fallback_model = os.environ.get("VOLCENGINE_ASR_MODEL_FALLBACK", "volc.bigasr.auc").strip()
    models = [model for model in dict.fromkeys([primary_model, fallback_model]) if model]
    failures: list[str] = []

    for model in models:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "asr-output.txt"
            values = {
                "url": candidate.canonical_url(),
                "bvid": candidate.bvid,
                "video_id": candidate.canonical_id(),
                "output": str(output_path),
                "model": model,
            }
            args = shlex.split(template.format(**values))
            proc = run_command(args, cwd=REPO_ROOT, timeout=timeout)
            text = output_path.read_text(encoding="utf-8", errors="ignore") if output_path.exists() else proc.stdout
            if proc.returncode != 0:
                reason = proc.stderr.strip() or text.strip() or "external ASR command failed"
                failures.append(f"{model}: {reason}")
                continue
        text = text.strip()
        if not text:
            failures.append(f"{model}: external ASR command returned empty transcript")
            continue
        try:
            payload = json.loads(text)
            if isinstance(payload, dict):
                for key in ("subtitle_text", "transcript", "text", "result"):
                    value = payload.get(key)
                    if isinstance(value, str) and value.strip():
                        return value.strip(), f"volcengine-external-command:{model}", ""
        except json.JSONDecodeError:
            pass
        return text, f"volcengine-external-command:{model}", ""
    return "", "", "; ".join(failures) or "external ASR command failed for all configured models"


def transcript_excerpt(text: str, max_chars: int = 1800) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= max_chars:
        return compact
    return compact[:max_chars].rstrip() + "..."


def source_card_markdown(
    candidate: VideoCandidate,
    raw_artifact_rel: str,
    transcript_text: str,
    extraction_method: str,
    industries: list[str],
) -> str:
    date = today_str()
    title = candidate.title.replace('"', "'")
    tags = ["bilibili", "video", "ai-research"]
    if "robotics-embodied-ai" in industries:
        tags.extend(["robotics", "embodied-ai"])
    else:
        tags.append("ai")
    related = [
        "[[ai/00-index|AI]]",
    ]
    if "robotics-embodied-ai" in industries:
        related.insert(0, "[[robotics-embodied-ai/00-index|机器人与具身智能]]")
    tag_yaml = "\n".join(f"  - {tag}" for tag in tags)
    source_url = candidate.canonical_url()
    return f"""---
title: "{title}"
type: source
date_created: {date}
last_updated: {date}
source_urls:
  - {source_url}
evidence_grade: B
sources:
  - {raw_artifact_rel}
tags:
{tag_yaml}
status: draft
---

# {candidate.title}

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | {source_url} |
| BV / video id | `{candidate.canonical_id()}` |
| Author | {candidate.author or 'unknown'} |
| Published | {candidate.published_at or 'unknown'} |
| Favorited | {candidate.favorited_at or 'unknown'} |
| Category | {candidate.category or 'unknown'} |
| Tags | {', '.join(candidate.tags) or 'unknown'} |
| Extraction method | {extraction_method} |
| Raw artifact | `{raw_artifact_rel}` |

## Transcript Excerpt

{transcript_excerpt(transcript_text)}

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `{raw_artifact_rel}`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

{chr(10).join(f'- {link}' for link in related)}
"""


def write_artifacts(result: ProcessResult, transcript_text: str, extraction_method: str) -> ProcessResult:
    candidate = result.decision.candidate
    date = today_str()
    ident = slugify(candidate.canonical_id(), fallback=stable_hash(candidate.canonical_url()))
    title_slug = slugify(candidate.title, fallback="bilibili-video")
    base = f"{date}-bilibili-{ident}-{title_slug}"[:120].rstrip("-")

    raw_path = RAW_TRANSCRIPTS_DIR / f"{base}.json"
    raw_payload = {
        "captured_at": utc_now().isoformat(),
        "platform": "bilibili",
        "video": dataclasses.asdict(candidate),
        "target_industries": result.decision.target_industries,
        "relevance": {
            "score": result.decision.relevance_score,
            "matched_terms": result.decision.matched_terms,
        },
        "extraction_method": extraction_method,
        "transcript_text": transcript_text,
    }
    write_json(raw_path, raw_payload)
    raw_rel = str(raw_path.relative_to(REPO_ROOT))

    source_stem = f"bilibili-{ident}-{title_slug}"[:110].rstrip("-")
    source_path = SOURCES_DIR / f"{source_stem}.md"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_text(
        source_card_markdown(
            candidate,
            raw_rel,
            transcript_text,
            extraction_method,
            result.decision.target_industries,
        ),
        encoding="utf-8",
    )

    result.status = "processed"
    result.reason = "transcript captured and source card written"
    result.raw_artifact = raw_rel
    result.source_card = str(source_path.relative_to(REPO_ROOT))
    result.transcript_chars = len(transcript_text)
    result.extraction_method = extraction_method
    return result


def next_source_id(csv_path: Path, slug: str, bvid: str) -> str:
    compact = re.sub(r"[^A-Za-z0-9]", "", bvid or stable_hash(str(csv_path)))[:24]
    return f"SRC-{slug}-bili-{compact}"


def append_sources_csv(results: list[ProcessResult]) -> None:
    for result in results:
        if result.status != "processed":
            continue
        candidate = result.decision.candidate
        for industry in result.decision.target_industries:
            csv_path = REPO_ROOT / "knowledge" / industry / "sources.csv"
            if not csv_path.exists():
                continue
            existing_text = csv_path.read_text(encoding="utf-8", errors="ignore")
            if candidate.canonical_id() in existing_text or candidate.canonical_url() in existing_text:
                continue
            with csv_path.open("a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        next_source_id(csv_path, industry, candidate.canonical_id()),
                        candidate.title,
                        "video",
                        candidate.author or "Bilibili",
                        candidate.published_at or "待验证",
                        candidate.canonical_url(),
                        "B",
                        f"Daily Bilibili AI/embodied pipeline; raw={result.raw_artifact}; source_card={result.source_card}",
                    ]
                )


def append_once(path: Path, marker: str, line: str, section_heading: str | None = None) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in text:
        return
    if section_heading and section_heading in text:
        updated = text.replace(section_heading, section_heading + "\n\n" + line, 1)
    else:
        updated = text.rstrip() + "\n" + line + "\n"
    path.write_text(updated, encoding="utf-8")


def update_knowledge_index(results: list[ProcessResult]) -> None:
    for result in results:
        if result.status != "processed" or not result.source_card:
            continue
        stem = Path(result.source_card).with_suffix("").as_posix().removeprefix("knowledge/")
        title = result.decision.candidate.title
        line = f"- [[{stem}|{title}]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis."
        append_once(KNOWLEDGE_INDEX, stem, line, "## Sources")


def write_run_report(decisions: list[CandidateDecision], results: list[ProcessResult], opencli_errors: list[str]) -> Path:
    date = today_str()
    path = SYNTHESIS_DIR / f"bilibili-ai-daily-run-{date}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for decision in decisions:
        counts[decision.status] = counts.get(decision.status, 0) + 1
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1

    rows = []
    for decision in decisions:
        c = decision.candidate
        rows.append(
            "| {status} | {title} | `{vid}` | {score} | {reason} |".format(
                status=decision.status,
                title=(c.title or "").replace("|", "\\|"),
                vid=c.canonical_id(),
                score=decision.relevance_score,
                reason=decision.reason.replace("|", "\\|"),
            )
        )
    processed_lines = []
    for result in results:
        c = result.decision.candidate
        processed_lines.append(
            f"- `{c.canonical_id()}` {c.title}: {result.status}; {result.reason}; "
            f"raw=`{result.raw_artifact or '-'}`; source=`{result.source_card or '-'}`"
        )

    report = f"""---
title: Bilibili AI Daily Run {date}
type: synthesis
date_created: {date}
last_updated: {date}
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run {date}

## Run Summary

- Candidate videos: {len(decisions)}
- Selected for transcript extraction: {counts.get('selected', 0)}
- Duplicate skipped: {counts.get('skipped_duplicate', 0)}
- Needs model review: {counts.get('needs_model_review', 0)}
- Processed: {counts.get('processed', 0)}
- Failed: {counts.get('failed', 0)}

## OpenCLI / Fetch Notes

{chr(10).join(f'- {err}' for err in opencli_errors) if opencli_errors else '- No fetch errors recorded.'}

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
{chr(10).join(rows) if rows else '| none | none | `-` | 0 | no candidates |'}

## Processing Results

{chr(10).join(processed_lines) if processed_lines else '- No videos processed.'}

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
"""
    path.write_text(report, encoding="utf-8")
    return path


def append_log(report_path: Path, results: list[ProcessResult]) -> None:
    date = today_str()
    processed = [r for r in results if r.status == "processed"]
    if not processed:
        return
    log_entry = f"""
## [{date}] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/{report_path.stem}|Bilibili AI Daily Run {date}]]；处理 {len(processed)} 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。
"""
    existing = KNOWLEDGE_LOG.read_text(encoding="utf-8") if KNOWLEDGE_LOG.exists() else ""
    marker = f"## [{date}] ingest | Bilibili AI/具身智能每日视频采集"
    if marker not in existing:
        KNOWLEDGE_LOG.write_text(existing.rstrip() + "\n\n" + log_entry.strip() + "\n", encoding="utf-8")


def process_selected(decisions: list[CandidateDecision], args: argparse.Namespace) -> list[ProcessResult]:
    results: list[ProcessResult] = []
    selected = [decision for decision in decisions if decision.status == "selected"]
    if args.max_process is not None:
        selected = selected[: args.max_process]

    for decision in selected:
        result = ProcessResult(decision=decision, status="failed", reason="")
        if args.skip_transcripts:
            result.status = "skipped_transcript"
            result.reason = "--skip-transcripts enabled"
            results.append(result)
            continue

        transcript_text, method, error = extract_transcript(decision.candidate, args.transcript_timeout)
        if not transcript_text:
            transcript_text, method, asr_error = run_external_asr(decision.candidate, args.asr_timeout)
            if not transcript_text:
                result.reason = f"subtitle extraction failed: {error}; ASR failed: {asr_error}"
                results.append(result)
                continue
        results.append(write_artifacts(result, transcript_text, method))
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=20, help="number of favorite videos to load as candidates")
    parser.add_argument("--candidates-json", type=Path, help="offline JSON payload from OpenCLI/Bilibili for testing")
    parser.add_argument("--candidate-url", help="single Bilibili URL/BV id to run through the same pipeline")
    parser.add_argument(
        "--selected-video-ids",
        help="comma-separated BV/video ids that the model judged relevant and should be processed",
    )
    parser.add_argument(
        "--process-all-non-duplicates",
        action="store_true",
        help="testing escape hatch: process every non-duplicate candidate without model selection",
    )
    parser.add_argument("--dry-run", action="store_true", help="classify candidates but do not write files")
    parser.add_argument("--skip-transcripts", action="store_true", help="do not call video_subtitle.py or ASR")
    parser.add_argument("--max-process", type=int, help="maximum selected videos to transcript in this run")
    parser.add_argument("--transcript-timeout", type=int, default=900, help="seconds for each subtitle extraction")
    parser.add_argument("--asr-timeout", type=int, default=3600, help="seconds for each external ASR command")
    parser.add_argument("--json", action="store_true", help="print machine-readable run summary")
    return parser


def parse_selected_ids(value: str | None) -> set[str]:
    if not value:
        return set()
    return {part.strip() for part in value.split(",") if part.strip()}


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_arg_parser().parse_args(argv)
    opencli_errors: list[str] = []
    if args.candidate_url:
        candidate, warning = fetch_bilibili_candidate(args.candidate_url)
        candidates = [candidate]
        if warning:
            opencli_errors.append(warning)
    elif args.candidates_json:
        candidates = load_candidates_from_json(args.candidates_json, args.limit)
    else:
        candidates, opencli_errors = fetch_candidates_with_opencli(args.limit)

    selected_ids = parse_selected_ids(args.selected_video_ids)
    decisions = [
        decide_candidate(
            REPO_ROOT,
            candidate,
            selected_ids=selected_ids,
            process_all_non_duplicates=args.process_all_non_duplicates,
        )
        for candidate in candidates
    ]
    results: list[ProcessResult] = []
    report_path = Path("")

    if not args.dry_run:
        results = process_selected(decisions, args)
        append_sources_csv(results)
        update_knowledge_index(results)
        report_path = write_run_report(decisions, results, opencli_errors)
        append_log(report_path, results)

    summary = {
        "candidates": len(candidates),
        "decisions": dataclasses.asdict(decisions) if False else [
            {
                "status": d.status,
                "video_id": d.candidate.canonical_id(),
                "title": d.candidate.title,
                "reason": d.reason,
                "relevance_score": d.relevance_score,
                "matched_terms": d.matched_terms,
                "target_industries": d.target_industries,
                "duplicate_hits": d.duplicate_hits,
            }
            for d in decisions
        ],
        "results": [
            {
                "status": r.status,
                "video_id": r.decision.candidate.canonical_id(),
                "title": r.decision.candidate.title,
                "reason": r.reason,
                "raw_artifact": r.raw_artifact,
                "source_card": r.source_card,
                "transcript_chars": r.transcript_chars,
            }
            for r in results
        ],
        "opencli_errors": opencli_errors,
        "report": str(report_path.relative_to(REPO_ROOT)) if report_path else "",
    }

    if args.json or args.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"Report: {summary['report']}")
        for result in summary["results"]:
            print(f"{result['status']}: {result['video_id']} {result['title']} - {result['reason']}")

    if not candidates:
        return 2
    if any(result.status == "failed" for result in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
