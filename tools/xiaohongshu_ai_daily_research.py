#!/usr/bin/env python3
"""Daily Xiaohongshu AI/embodied-intelligence research capture pipeline.

The script mirrors the deterministic part of the Bilibili daily workflow, but
adapts it for Xiaohongshu note sources:

1. Pull candidate notes from a JSON file, one URL, or OpenCLI.
2. Normalize title, URL, note id, author, tags, timestamps, text, and media URLs.
3. Skip notes already present in raw/ or knowledge/.
4. Mark non-duplicate notes as needing Codex/model review by default.
5. Process only explicitly selected notes.
6. Write raw note packets, source cards, sources.csv rows, and a run report.

The script prepares traceable social-media source packets. It does not treat
Xiaohongshu content as primary evidence for company, policy, financial, or
market-size claims.
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
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_ARTICLES_DIR = REPO_ROOT / "raw/_inbox/articles"
SOURCES_DIR = REPO_ROOT / "knowledge/_sources"
SYNTHESIS_DIR = REPO_ROOT / "knowledge/_syntheses"
KNOWLEDGE_INDEX = REPO_ROOT / "knowledge/index.md"
KNOWLEDGE_LOG = REPO_ROOT / "knowledge/log.md"
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
NON_DUPLICATE_EVIDENCE_PATTERNS = [
    r"knowledge/_syntheses/xiaohongshu-ai-daily-run-\d{4}-\d{2}-\d{2}\.md$",
    r"knowledge/log\.md$",
]

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
class NoteCandidate:
    title: str
    url: str
    note_id: str = ""
    author: str = ""
    published_at: str = ""
    favorited_at: str = ""
    description: str = ""
    tags: list[str] = dataclasses.field(default_factory=list)
    note_type: str = ""
    image_urls: list[str] = dataclasses.field(default_factory=list)
    video_url: str = ""
    raw: dict[str, Any] = dataclasses.field(default_factory=dict)

    def canonical_id(self) -> str:
        return self.note_id or extract_note_id(self.url) or stable_hash(self.url or self.title)

    def canonical_url(self) -> str:
        if self.url:
            return self.url
        if self.note_id:
            return f"https://www.xiaohongshu.com/explore/{self.note_id}"
        return ""

    def identifiers(self) -> list[str]:
        values = [
            self.note_id,
            extract_note_id(self.url),
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

    def content_text(self) -> str:
        return "\n\n".join(
            part
            for part in [
                self.title,
                self.description,
                " ".join(f"#{tag}" for tag in self.tags),
            ]
            if part
        ).strip()

    def text_blob(self) -> str:
        return " ".join(
            part
            for part in [
                self.title,
                self.description,
                " ".join(self.tags),
                self.note_type,
                self.author,
            ]
            if part
        )


@dataclasses.dataclass
class CandidateDecision:
    candidate: NoteCandidate
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
    content_chars: int = 0
    extraction_method: str = ""
    media_errors: list[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ImageOcrResult:
    index: int
    url: str
    text: str
    method: str
    error: str = ""


@dataclasses.dataclass
class VideoTranscriptResult:
    url: str
    text: str
    method: str
    frames: list[dict[str, str]] = dataclasses.field(default_factory=list)
    error: str = ""


@dataclasses.dataclass
class MediaExtractionResult:
    content_text: str
    extraction_method: str
    image_ocr: list[ImageOcrResult] = dataclasses.field(default_factory=list)
    video_transcript: VideoTranscriptResult | None = None
    errors: list[str] = dataclasses.field(default_factory=list)


def stable_hash(text: str, length: int = 12) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:length]


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


def today_str() -> str:
    return dt.datetime.now().date().isoformat()


def slugify(text: str, fallback: str = "note") -> str:
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


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_dotenv(paths: tuple[Path, ...] = DOTENV_PATHS) -> None:
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
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", errors="ignore")
        stderr = exc.stderr if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", errors="ignore")
        message = f"command timed out after {timeout} seconds"
        stderr = f"{stderr.rstrip()}\n{message}".strip() if stderr else message
        return subprocess.CompletedProcess(args=args, returncode=124, stdout=stdout, stderr=stderr)


def extract_text_from_payload(payload: Any) -> str:
    if isinstance(payload, str):
        return payload.strip()
    if isinstance(payload, list):
        parts = [extract_text_from_payload(item) for item in payload]
        return "\n".join(part for part in parts if part)
    if not isinstance(payload, dict):
        return ""

    for key in (
        "text",
        "ocr_text",
        "image_text",
        "transcript",
        "subtitle_text",
        "content",
        "result",
        "description",
    ):
        value = payload.get(key)
        text = extract_text_from_payload(value)
        if text:
            return text
    return ""


def parse_command_text(stdout: str, output_path: Path) -> str:
    text = output_path.read_text(encoding="utf-8", errors="ignore") if output_path.exists() else stdout
    text = text.strip()
    if not text:
        return ""
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return text
    return extract_text_from_payload(payload)


def parse_command_payload(stdout: str, output_path: Path) -> Any:
    text = output_path.read_text(encoding="utf-8", errors="ignore") if output_path.exists() else stdout
    text = text.strip()
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"text": text}


def format_template_command(template: str, values: dict[str, str]) -> list[str]:
    return shlex.split(template.format(**values))


def extract_items(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []

    likely_keys = (
        "notes",
        "items",
        "list",
        "result",
        "data",
        "feeds",
        "collects",
        "favorites",
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
            for name_key in ("name", "nickname", "nick_name", "user_name", "title"):
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
        return [part.strip().lstrip("#") for part in re.split(r"[,，;；\s#]+", value) if part.strip()]
    if isinstance(value, list):
        tags: list[str] = []
        for item in value:
            if isinstance(item, dict):
                tag = first_value(item, ("tag_name", "name", "title", "text"))
                if tag:
                    tags.append(tag.lstrip("#"))
            elif isinstance(item, (str, int, float)):
                tags.append(str(item).strip().lstrip("#"))
        return [tag for tag in tags if tag]
    return []


def normalize_url_list(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    if isinstance(value, list):
        urls: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip():
                urls.append(item.strip())
            elif isinstance(item, dict):
                url = first_value(item, ("url", "src", "link", "image_url", "original"))
                if url:
                    urls.append(url)
        return urls
    return []


def extract_note_id(value: str) -> str:
    if not value:
        return ""
    parsed = urllib.parse.urlparse(value)
    query = urllib.parse.parse_qs(parsed.query)
    for key in ("note_id", "noteId", "id", "source_note_id"):
        vals = query.get(key)
        if vals and re.match(r"^[0-9a-fA-F]{16,32}$", vals[0]):
            return vals[0]
    patterns = [
        r"/explore/([0-9a-fA-F]{16,32})",
        r"/discovery/item/([0-9a-fA-F]{16,32})",
        r"/item/([0-9a-fA-F]{16,32})",
        r"\b([0-9a-fA-F]{24})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return match.group(1)
    return ""


def normalize_candidate(item: dict[str, Any]) -> NoteCandidate:
    title = first_value(item, ("title", "name", "display_title", "note_title", "headline"))
    url = first_value(item, ("url", "link", "uri", "share_url", "web_url", "note_url"))
    note_id = first_value(item, ("note_id", "noteId", "id", "id_str", "source_note_id"))
    if not note_id:
        note_id = extract_note_id(url)
    description = first_value(item, ("description", "desc", "content", "text", "summary", "body"))
    note_type = first_value(item, ("type", "note_type", "media_type", "kind"))
    author = first_value(item, ("author", "user", "nickname", "user_name", "creator"))
    if not author:
        author = nested_name(item, ("user", "author", "creator", "owner"))
    tags = normalize_tags(item.get("tags") or item.get("tag_list") or item.get("hash_tags") or item.get("keywords"))
    image_urls = normalize_url_list(item.get("image_urls") or item.get("images") or item.get("image_list"))
    video_url = first_value(item, ("video_url", "video", "media_url"))
    if not video_url and isinstance(item.get("video"), dict):
        video_url = first_value(item["video"], ("url", "src", "link"))
    published_at = normalize_timestamp(
        item.get("time")
        or item.get("publish_time")
        or item.get("published_at")
        or item.get("created_at")
        or item.get("timestamp")
    )
    favorited_at = normalize_timestamp(
        item.get("fav_time")
        or item.get("favorite_time")
        or item.get("collected_at")
        or item.get("saved_at")
        or item.get("mtime")
    )
    if not url and note_id:
        url = f"https://www.xiaohongshu.com/explore/{note_id}"
    return NoteCandidate(
        title=title or note_id or "Untitled Xiaohongshu note",
        url=url,
        note_id=note_id,
        author=author,
        published_at=published_at,
        favorited_at=favorited_at,
        description=description,
        tags=tags,
        note_type=note_type,
        image_urls=image_urls,
        video_url=video_url,
        raw=item,
    )


def field_value_payload_to_dict(payload: Any) -> dict[str, Any]:
    if isinstance(payload, dict):
        return payload
    if not isinstance(payload, list):
        return {}
    result: dict[str, Any] = {}
    for item in payload:
        if not isinstance(item, dict):
            continue
        field = item.get("field")
        if field is None:
            continue
        result[str(field)] = item.get("value", "")
    return result


def fetch_note_detail(candidate: NoteCandidate, args: argparse.Namespace) -> tuple[dict[str, Any], str]:
    if args.skip_note_detail:
        return {}, ""
    template = os.environ.get(
        "XIAOHONGSHU_NOTE_DETAIL_COMMAND",
        "opencli xiaohongshu note {url} -f json",
    ).strip()
    if not template:
        return {}, ""
    url = candidate.canonical_url()
    if not url:
        return {}, "missing note URL for detail fetch"
    values = {
        "url": url,
        "note_url": url,
        "note_id": candidate.canonical_id(),
        "output": "",
    }
    proc = run_command(format_template_command(template, values), timeout=args.note_detail_timeout)
    if proc.returncode != 0:
        return {}, proc.stderr.strip() or proc.stdout.strip() or "note detail command failed"
    try:
        payload = parse_opencli_json(proc.stdout)
    except json.JSONDecodeError as exc:
        return {}, f"note detail command returned non-JSON output: {exc}"
    detail = field_value_payload_to_dict(payload)
    if not detail:
        return {}, "note detail command returned no detail fields"
    return detail, ""


def enrich_candidate_with_detail(candidate: NoteCandidate, detail: dict[str, Any]) -> NoteCandidate:
    if not detail:
        return candidate
    title = str(detail.get("title") or candidate.title).strip()
    author = str(detail.get("author") or candidate.author).strip()
    description = str(
        detail.get("content")
        or detail.get("description")
        or detail.get("desc")
        or candidate.description
    ).strip()
    tags = normalize_tags(detail.get("tags") or candidate.tags)
    note_type = str(detail.get("type") or candidate.note_type).strip()
    image_urls = normalize_url_list(
        detail.get("image_urls")
        or detail.get("images")
        or detail.get("image_list")
        or candidate.image_urls
    )
    video_url = str(detail.get("video_url") or detail.get("video") or candidate.video_url).strip()
    merged_raw = dict(candidate.raw)
    merged_raw["note_detail"] = detail
    return dataclasses.replace(
        candidate,
        title=title or candidate.title,
        author=author,
        description=description,
        tags=tags,
        note_type=note_type,
        image_urls=image_urls,
        video_url=video_url,
        raw=merged_raw,
    )


def load_candidates_from_json(path: Path, limit: int) -> list[NoteCandidate]:
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


def fetch_candidates_with_opencli(limit: int) -> tuple[list[NoteCandidate], list[str]]:
    errors: list[str] = []
    override = os.environ.get("XIAOHONGSHU_FAVORITES_OPENCLI_COMMAND", "").strip()
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
        if not any(token in haystack for token in ("xiaohongshu", "xhs", "rednote", "小红书")):
            continue
        score = 0
        for token in ("favorite", "favorites", "fav", "collection", "collect", "saved", "收藏"):
            if token in haystack:
                score += 3
        for token in ("note", "notes", "post", "posts", "笔记"):
            if token in haystack:
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
        errors.append(f"{site} {name} returned no note-like items")

    if not scored:
        errors.append("no Xiaohongshu favorite-like OpenCLI command found; set XIAOHONGSHU_FAVORITES_OPENCLI_COMMAND")
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
                "!knowledge/_syntheses/xiaohongshu-ai-daily-run-*.md",
                "--glob",
                "!knowledge/log.md",
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


def is_non_duplicate_evidence_path(rel_path: str) -> bool:
    return any(re.match(pattern, rel_path) for pattern in NON_DUPLICATE_EVIDENCE_PATTERNS)


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
            if is_non_duplicate_evidence_path(rel_path):
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


def find_duplicate_hits(repo_root: Path, candidate: NoteCandidate) -> list[str]:
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


def relevance(candidate: NoteCandidate) -> tuple[int, list[str], list[str]]:
    blob = candidate.text_blob()
    high = pattern_matches(blob, HIGH_RELEVANCE_PATTERNS)
    medium = pattern_matches(blob, MEDIUM_RELEVANCE_PATTERNS)
    score = len(high) * 2 + len(medium)
    robotics = pattern_matches(blob, ROBOTICS_PATTERNS)
    industries = ["ai"]
    if robotics:
        industries.insert(0, "robotics-embodied-ai")
    return score, high + medium, list(dict.fromkeys(industries))


def selected_id_matches(candidate: NoteCandidate, selected_ids: set[str]) -> bool:
    if not selected_ids:
        return False
    return any(identifier in selected_ids for identifier in candidate.identifiers())


def decide_candidate(
    repo_root: Path,
    candidate: NoteCandidate,
    selected_ids: set[str] | None = None,
    process_all_non_duplicates: bool = False,
    refresh_existing: bool = False,
) -> CandidateDecision:
    duplicate_hits = find_duplicate_hits(repo_root, candidate)
    selected_ids = selected_ids or set()
    if duplicate_hits and not (refresh_existing and selected_id_matches(candidate, selected_ids)):
        return CandidateDecision(
            candidate=candidate,
            status="skipped_duplicate",
            reason="note identifier already appears in raw/ or knowledge/",
            duplicate_hits=duplicate_hits,
        )

    score, terms, industries = relevance(candidate)
    if selected_id_matches(candidate, selected_ids):
        return CandidateDecision(
            candidate=candidate,
            status="selected",
            reason="selected by model relevance judgment" + ("; refreshing existing artifact" if duplicate_hits else ""),
            relevance_score=score,
            matched_terms=terms,
            duplicate_hits=duplicate_hits,
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


def content_excerpt(text: str, max_chars: int = 1800) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= max_chars:
        return compact
    return compact[:max_chars].rstrip() + "..."


def should_attempt_video_transcript(candidate: NoteCandidate, mode: str) -> bool:
    if mode == "never":
        return False
    if mode == "always":
        return True
    blob = " ".join(
        str(part or "").lower()
        for part in [
            candidate.note_type,
            candidate.video_url,
            candidate.raw.get("type") if isinstance(candidate.raw, dict) else "",
            candidate.raw.get("note_type") if isinstance(candidate.raw, dict) else "",
            candidate.raw.get("media_type") if isinstance(candidate.raw, dict) else "",
        ]
    )
    return bool(candidate.video_url or re.search(r"\bvideo\b|视频|short|clip", blob))


def run_image_ocr(candidate: NoteCandidate, args: argparse.Namespace) -> list[ImageOcrResult]:
    if args.skip_image_ocr or not candidate.image_urls:
        return []
    template = os.environ.get("XIAOHONGSHU_IMAGE_OCR_COMMAND", "").strip()
    if not template:
        return [
            ImageOcrResult(
                index=-1,
                url="",
                text="",
                method="not-configured",
                error="XIAOHONGSHU_IMAGE_OCR_COMMAND is not configured",
            )
        ]

    results: list[ImageOcrResult] = []
    for index, image_url in enumerate(candidate.image_urls[: args.max_images]):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "ocr-output.txt"
            values = {
                "url": image_url,
                "image_url": image_url,
                "index": str(index),
                "note_id": candidate.canonical_id(),
                "output": str(output_path),
            }
            proc = run_command(format_template_command(template, values), timeout=args.image_ocr_timeout)
            if proc.returncode != 0:
                results.append(
                    ImageOcrResult(
                        index=index,
                        url=image_url,
                        text="",
                        method="external-command",
                        error=proc.stderr.strip() or proc.stdout.strip() or "image OCR command failed",
                    )
                )
                continue
            text = parse_command_text(proc.stdout, output_path)
            results.append(
                ImageOcrResult(
                    index=index,
                    url=image_url,
                    text=text,
                    method="external-command",
                    error="" if text else "image OCR command returned empty text",
                )
            )
    return results


def parse_video_subtitle_payload(payload: Any) -> tuple[str, list[dict[str, str]], str]:
    text = extract_text_from_payload(payload)
    frames: list[dict[str, str]] = []
    if isinstance(payload, dict):
        raw_frames = payload.get("frames")
        if isinstance(raw_frames, list):
            for frame in raw_frames:
                if not isinstance(frame, dict):
                    continue
                path = str(frame.get("path") or "").strip()
                timestamp = str(frame.get("timestamp") or "").strip()
                if path:
                    frames.append({"path": path, "timestamp": timestamp})
        method = str(payload.get("source") or payload.get("method") or payload.get("platform") or "video_subtitle.py")
    else:
        method = "video_subtitle.py"
    return text, frames, method


def run_video_subtitle(candidate: NoteCandidate, url: str, args: argparse.Namespace) -> VideoTranscriptResult:
    template = os.environ.get(
        "XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND",
        "uv run --group video-ytdlp python .agents/skills/video-summarizer/scripts/video_subtitle.py {url}",
    ).strip()
    if not template:
        return VideoTranscriptResult(url=url, text="", method="disabled", error="XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND is disabled")

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "video-subtitle-output.json"
        values = {
            "url": url,
            "note_url": candidate.canonical_url(),
            "video_url": candidate.video_url,
            "note_id": candidate.canonical_id(),
            "output": str(output_path),
        }
        proc = run_command(format_template_command(template, values), timeout=args.video_transcript_timeout)
        payload = parse_command_payload(proc.stdout, output_path)
        text, frames, method = parse_video_subtitle_payload(payload)
        if proc.returncode == 0 and text:
            return VideoTranscriptResult(url=url, text=text, method=method, frames=frames)
        if isinstance(payload, dict) and payload.get("error"):
            error = str(payload.get("error"))
        else:
            error = proc.stderr.strip() or proc.stdout.strip() or "video subtitle command returned no transcript"
        return VideoTranscriptResult(url=url, text="", method=method, frames=frames, error=error)


def run_external_asr(candidate: NoteCandidate, url: str, args: argparse.Namespace) -> VideoTranscriptResult:
    template = (
        os.environ.get("XIAOHONGSHU_ASR_COMMAND", "").strip()
        or os.environ.get("VOLCENGINE_ASR_COMMAND", "").strip()
    )
    if not template:
        return VideoTranscriptResult(
            url=url,
            text="",
            method="not-configured",
            error="XIAOHONGSHU_ASR_COMMAND or VOLCENGINE_ASR_COMMAND is not configured",
        )

    primary_model = os.environ.get(
        "XIAOHONGSHU_ASR_MODEL_PRIMARY",
        os.environ.get("VOLCENGINE_ASR_MODEL_PRIMARY", "volc.seedasr.auc"),
    ).strip()
    fallback_model = os.environ.get(
        "XIAOHONGSHU_ASR_MODEL_FALLBACK",
        os.environ.get("VOLCENGINE_ASR_MODEL_FALLBACK", "volc.bigasr.auc"),
    ).strip()
    models = [model for model in dict.fromkeys([primary_model, fallback_model]) if model]
    failures: list[str] = []

    for model in models:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "asr-output.txt"
            values = {
                "url": url,
                "note_url": candidate.canonical_url(),
                "video_url": candidate.video_url,
                "note_id": candidate.canonical_id(),
                "video_id": candidate.canonical_id(),
                "model": model,
                "output": str(output_path),
            }
            proc = run_command(format_template_command(template, values), timeout=args.asr_timeout)
            text = parse_command_text(proc.stdout, output_path)
            if proc.returncode == 0 and text:
                return VideoTranscriptResult(
                    url=url,
                    text=text,
                    method=f"external-asr-command:{model}",
                )
            reason = proc.stderr.strip() or proc.stdout.strip() or "external ASR command returned empty transcript"
            failures.append(f"{model}: {reason}")

    return VideoTranscriptResult(url=url, text="", method="external-asr-command", error="; ".join(failures))


def run_video_transcript(candidate: NoteCandidate, args: argparse.Namespace) -> VideoTranscriptResult | None:
    if not should_attempt_video_transcript(candidate, args.video_transcript_mode):
        return None
    url = candidate.video_url or candidate.canonical_url()
    if not url:
        return VideoTranscriptResult(url="", text="", method="missing-url", error="missing note/video URL")

    subtitle_result = run_video_subtitle(candidate, url, args)
    if subtitle_result.text:
        return subtitle_result

    asr_result = run_external_asr(candidate, url, args)
    if asr_result.text:
        return asr_result

    errors = [err for err in [subtitle_result.error, asr_result.error] if err]
    return VideoTranscriptResult(
        url=url,
        text="",
        method="video-subtitle+asr",
        frames=subtitle_result.frames,
        error="; ".join(errors) or "video transcript extraction failed",
    )


def extract_media_content(candidate: NoteCandidate, args: argparse.Namespace) -> MediaExtractionResult:
    sections: list[str] = []
    base_text = candidate.content_text()
    if base_text:
        sections.append(base_text)

    image_ocr = run_image_ocr(candidate, args)
    image_text_parts = [
        f"[Image {result.index + 1} OCR]\n{result.text}"
        for result in image_ocr
        if result.index >= 0 and result.text
    ]
    sections.extend(image_text_parts)

    video_transcript = run_video_transcript(candidate, args)
    if video_transcript and video_transcript.text:
        sections.append(f"[Video Transcript]\n{video_transcript.text}")

    errors = [
        f"image {result.index + 1}: {result.error}" if result.index >= 0 else result.error
        for result in image_ocr
        if result.error
    ]
    if video_transcript and video_transcript.error:
        errors.append(f"video: {video_transcript.error}")

    methods = ["base-note-text"] if base_text else []
    if any(result.text for result in image_ocr):
        methods.append("image-ocr")
    if video_transcript and video_transcript.text:
        methods.append(video_transcript.method)
    extraction_method = "+".join(methods) if methods else "metadata-only"

    return MediaExtractionResult(
        content_text="\n\n".join(sections).strip(),
        extraction_method=extraction_method,
        image_ocr=image_ocr,
        video_transcript=video_transcript,
        errors=errors,
    )


def source_card_markdown(
    candidate: NoteCandidate,
    raw_artifact_rel: str,
    media: MediaExtractionResult,
    industries: list[str],
) -> str:
    date = today_str()
    title = candidate.title.replace('"', "'")
    tags = ["xiaohongshu", "social-media", "ai-research"]
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
    image_count = len(candidate.image_urls)
    image_ocr_count = len([result for result in media.image_ocr if result.text])
    video_method = media.video_transcript.method if media.video_transcript else "not attempted"
    video_chars = len(media.video_transcript.text) if media.video_transcript else 0
    media_error_lines = "\n".join(f"- {error}" for error in media.errors) if media.errors else "- None recorded."
    return f"""---
title: "{title}"
type: source
date_created: {date}
last_updated: {date}
source_urls:
  - {source_url}
evidence_grade: C
sources:
  - {raw_artifact_rel}
tags:
{tag_yaml}
status: draft
---

# {candidate.title}

> [!summary]
> Xiaohongshu note source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable social-media source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Xiaohongshu |
| URL | {source_url} |
| Note id | `{candidate.canonical_id()}` |
| Author | {candidate.author or 'unknown'} |
| Published | {candidate.published_at or 'unknown'} |
| Favorited | {candidate.favorited_at or 'unknown'} |
| Note type | {candidate.note_type or 'unknown'} |
| Tags | {', '.join(candidate.tags) or 'unknown'} |
| Images | {image_count} |
| Images OCR'd | {image_ocr_count} |
| Video URL | {candidate.video_url or 'unknown'} |
| Video transcript method | {video_method} |
| Video transcript chars | {video_chars} |
| Extraction method | {media.extraction_method} |
| Raw artifact | `{raw_artifact_rel}` |

## Note Excerpt

{content_excerpt(media.content_text) or 'No text content captured; inspect raw artifact and original URL before synthesis.'}

## Media Extraction Notes

{media_error_lines}

## Research Handoff

- Extract only traceable facts, estimates, judgments, and hypotheses from `{raw_artifact_rel}`.
- Treat Xiaohongshu as C-grade discovery evidence unless the note embeds primary-source screenshots or links that can be independently verified.
- Cross-check important company, policy, market-size, hiring, financing, and product claims against primary sources before promoting them into industry pages.
- Preserve source traceability using the Xiaohongshu URL and note id.

## Related Links

{chr(10).join(f'- {link}' for link in related)}
"""


def write_artifacts(result: ProcessResult, media: MediaExtractionResult) -> ProcessResult:
    candidate = result.decision.candidate
    date = today_str()
    ident = slugify(candidate.canonical_id(), fallback=stable_hash(candidate.canonical_url()))
    title_slug = slugify(candidate.title, fallback="xiaohongshu-note")
    base = f"{date}-xiaohongshu-{ident}-{title_slug}"[:120].rstrip("-")

    raw_path = RAW_ARTICLES_DIR / f"{base}.json"
    raw_payload = {
        "captured_at": utc_now().isoformat(),
        "platform": "xiaohongshu",
        "note": dataclasses.asdict(candidate),
        "target_industries": result.decision.target_industries,
        "relevance": {
            "score": result.decision.relevance_score,
            "matched_terms": result.decision.matched_terms,
        },
        "extraction_method": media.extraction_method,
        "content_text": media.content_text,
        "image_ocr": [dataclasses.asdict(item) for item in media.image_ocr],
        "video_transcript": dataclasses.asdict(media.video_transcript) if media.video_transcript else None,
        "media_errors": media.errors,
    }
    write_json(raw_path, raw_payload)
    raw_rel = display_path(raw_path)

    source_stem = f"xiaohongshu-{ident}-{title_slug}"[:110].rstrip("-")
    source_path = SOURCES_DIR / f"{source_stem}.md"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_text(
        source_card_markdown(
            candidate,
            raw_rel,
            media,
            result.decision.target_industries,
        ),
        encoding="utf-8",
    )

    result.status = "processed"
    result.reason = "note packet captured and source card written"
    result.raw_artifact = raw_rel
    result.source_card = display_path(source_path)
    result.content_chars = len(media.content_text)
    result.extraction_method = media.extraction_method
    result.media_errors = media.errors
    return result


def next_source_id(csv_path: Path, slug: str, note_id: str) -> str:
    compact = re.sub(r"[^A-Za-z0-9]", "", note_id or stable_hash(str(csv_path)))[:24]
    return f"SRC-{slug}-xhs-{compact}"


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
                        "social-media",
                        candidate.author or "Xiaohongshu",
                        candidate.published_at or "待验证",
                        candidate.canonical_url(),
                        "C",
                        f"Daily Xiaohongshu AI/embodied pipeline; raw={result.raw_artifact}; source_card={result.source_card}",
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
        line = f"- [[{stem}|{title}]] — Xiaohongshu note source packet captured by the daily AI/embodied research pipeline; C-grade discovery evidence pending synthesis."
        append_once(KNOWLEDGE_INDEX, stem, line, "## Sources")


def write_run_report(
    decisions: list[CandidateDecision],
    results: list[ProcessResult],
    opencli_errors: list[str],
) -> Path:
    date = today_str()
    path = SYNTHESIS_DIR / f"xiaohongshu-ai-daily-run-{date}.md"
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
            "| {status} | {title} | `{note_id}` | {score} | {reason} |".format(
                status=decision.status,
                title=(c.title or "").replace("|", "\\|"),
                note_id=c.canonical_id(),
                score=decision.relevance_score,
                reason=decision.reason.replace("|", "\\|"),
            )
        )
    processed_lines = []
    for result in results:
        c = result.decision.candidate
        media_suffix = f"; media_errors={len(result.media_errors)}" if result.media_errors else ""
        processed_lines.append(
            f"- `{c.canonical_id()}` {c.title}: {result.status}; {result.reason}; "
            f"method={result.extraction_method or '-'}; raw=`{result.raw_artifact or '-'}`; "
            f"source=`{result.source_card or '-'}`{media_suffix}"
        )

    report = f"""---
title: Xiaohongshu AI Daily Run {date}
type: synthesis
date_created: {date}
last_updated: {date}
sources:
  - raw/_inbox/articles/
tags:
  - operations
  - xiaohongshu
  - ai
  - embodied-ai
status: active
---

# Xiaohongshu AI Daily Run {date}

## Run Summary

- Candidate notes: {len(decisions)}
- Selected for source packet capture: {counts.get('selected', 0)}
- Duplicate skipped: {counts.get('skipped_duplicate', 0)}
- Needs model review: {counts.get('needs_model_review', 0)}
- Processed: {counts.get('processed', 0)}
- Failed: {counts.get('failed', 0)}

## OpenCLI / Fetch Notes

{chr(10).join(f'- {err}' for err in opencli_errors) if opencli_errors else '- No fetch errors recorded.'}

## Candidate Decisions

| Status | Title | Note ID | Score | Reason |
|---|---|---:|---:|---|
{chr(10).join(rows) if rows else '| none | none | `-` | 0 | no candidates |'}

## Processing Results

{chr(10).join(processed_lines) if processed_lines else '- No notes processed.'}

## Codex Research Handoff

- Read each new `knowledge/_sources/xiaohongshu-*.md` source card and the corresponding raw note JSON.
- Use Xiaohongshu primarily for discovery: practitioner experiences, product demos, hiring signals, event notes, screenshots, and lead generation.
- Cross-check important company, policy, market-size, financing, and product claims against primary sources before updating durable industry pages.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.

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
## [{date}] ingest | Xiaohongshu AI/具身智能每日笔记采集

- **变更**: 新增或更新 [[_syntheses/{report_path.stem}|Xiaohongshu AI Daily Run {date}]]；处理 {len(processed)} 个 Xiaohongshu note source packet。
- **来源**: `raw/_inbox/articles/` 与 `knowledge/_sources/` 中的小红书笔记采集产物。
- **限制**: 小红书默认是 C 级发现线索；脚本只完成候选筛选、去重和 source card 交接，关键事实仍需一级来源交叉验证。
"""
    existing = KNOWLEDGE_LOG.read_text(encoding="utf-8") if KNOWLEDGE_LOG.exists() else ""
    marker = f"## [{date}] ingest | Xiaohongshu AI/具身智能每日笔记采集"
    if marker not in existing:
        KNOWLEDGE_LOG.write_text(existing.rstrip() + "\n\n" + log_entry.strip() + "\n", encoding="utf-8")


def process_selected(decisions: list[CandidateDecision], args: argparse.Namespace) -> list[ProcessResult]:
    results: list[ProcessResult] = []
    selected = [decision for decision in decisions if decision.status == "selected"]
    if args.max_process is not None:
        selected = selected[: args.max_process]

    for decision in selected:
        result = ProcessResult(decision=decision, status="failed", reason="")
        detail, detail_error = fetch_note_detail(decision.candidate, args)
        if detail:
            decision.candidate = enrich_candidate_with_detail(decision.candidate, detail)
        media = extract_media_content(decision.candidate, args)
        if detail_error:
            media.errors.append(f"detail: {detail_error}")
        if not media.content_text and not args.allow_empty_content:
            suffix = f"; media errors: {'; '.join(media.errors)}" if media.errors else ""
            result.reason = (
                "no note text, image OCR text, or video transcript captured; rerun with a richer "
                "OpenCLI/JSON export, configure OCR/ASR hooks, or use --allow-empty-content"
                + suffix
            )
            result.media_errors = media.errors
            results.append(result)
            continue
        results.append(write_artifacts(result, media))
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=20, help="number of favorite notes to load as candidates")
    parser.add_argument("--candidates-json", type=Path, help="offline JSON payload from OpenCLI/Xiaohongshu for testing")
    parser.add_argument("--candidate-url", help="single Xiaohongshu note URL to run through the same pipeline")
    parser.add_argument(
        "--selected-note-ids",
        help="comma-separated note ids/URLs that the model judged relevant and should be processed",
    )
    parser.add_argument(
        "--process-all-non-duplicates",
        action="store_true",
        help="testing escape hatch: process every non-duplicate candidate without model selection",
    )
    parser.add_argument("--dry-run", action="store_true", help="classify candidates but do not write files")
    parser.add_argument("--max-process", type=int, help="maximum selected notes to capture in this run")
    parser.add_argument(
        "--refresh-existing",
        action="store_true",
        help="allow selected duplicate notes to be reprocessed and overwrite same-day source packets",
    )
    parser.add_argument("--skip-note-detail", action="store_true", help="do not call OpenCLI note detail before media extraction")
    parser.add_argument("--note-detail-timeout", type=int, default=240, help="seconds for each note detail command")
    parser.add_argument(
        "--allow-empty-content",
        action="store_true",
        help="write a source packet even when the candidate has only URL/id metadata",
    )
    parser.add_argument("--skip-image-ocr", action="store_true", help="do not run image OCR/vision extraction")
    parser.add_argument("--max-images", type=int, default=9, help="maximum images to OCR per selected note")
    parser.add_argument("--image-ocr-timeout", type=int, default=180, help="seconds for each image OCR command")
    parser.add_argument(
        "--video-transcript-mode",
        choices=("auto", "always", "never"),
        default="auto",
        help="when to try video subtitle/ASR extraction for selected notes",
    )
    parser.add_argument("--video-transcript-timeout", type=int, default=900, help="seconds for video subtitle extraction")
    parser.add_argument("--asr-timeout", type=int, default=3600, help="seconds for external ASR command")
    parser.add_argument("--json", action="store_true", help="print machine-readable run summary")
    return parser


def parse_selected_ids(value: str | None) -> set[str]:
    if not value:
        return set()
    selected: set[str] = set()
    for part in value.split(","):
        clean = part.strip()
        if not clean:
            continue
        selected.add(clean)
        note_id = extract_note_id(clean)
        if note_id:
            selected.add(note_id)
    return selected


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_arg_parser().parse_args(argv)
    opencli_errors: list[str] = []
    if args.candidate_url:
        candidates = [normalize_candidate({"url": args.candidate_url})]
    elif args.candidates_json:
        candidates = load_candidates_from_json(args.candidates_json, args.limit)
    else:
        candidates, opencli_errors = fetch_candidates_with_opencli(args.limit)

    selected_ids = parse_selected_ids(args.selected_note_ids)
    decisions = [
        decide_candidate(
            REPO_ROOT,
            candidate,
            selected_ids=selected_ids,
            process_all_non_duplicates=args.process_all_non_duplicates,
            refresh_existing=args.refresh_existing,
        )
        for candidate in candidates
    ]
    results: list[ProcessResult] = []
    report_path: Path | None = None

    if not args.dry_run:
        results = process_selected(decisions, args)
        append_sources_csv(results)
        update_knowledge_index(results)
        report_path = write_run_report(decisions, results, opencli_errors)
        append_log(report_path, results)

    summary = {
        "candidates": len(candidates),
        "decisions": [
            {
                "status": d.status,
                "note_id": d.candidate.canonical_id(),
                "title": d.candidate.title,
                "reason": d.reason,
                "relevance_score": d.relevance_score,
                "matched_terms": d.matched_terms,
                "target_industries": d.target_industries,
                "duplicate_hits": d.duplicate_hits,
            }
            for d in decisions
        ],
        "results": [dataclasses.asdict(result) for result in results],
        "opencli_errors": opencli_errors,
        "report": str(report_path.relative_to(REPO_ROOT)) if report_path else "",
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"Candidates: {summary['candidates']}")
        for decision in summary["decisions"]:
            print(
                f"- {decision['status']}: {decision['note_id']} "
                f"{decision['title']} ({decision['reason']})"
            )
        if report_path:
            print(f"Report: {report_path.relative_to(REPO_ROOT)}")
    failed = [result for result in results if result.status == "failed"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
