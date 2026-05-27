#!/usr/bin/env python3
"""Extract source URLs from sources.csv into raw/<industry>/documents/.

The script uses defuddle for standard web pages, downloads markdown-like files
directly, and stores PDFs as raw files with a small metadata sidecar.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAPTURED_AT = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def slugify(value: str, max_len: int = 80) -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "source"


def github_blob_to_raw(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc != "github.com":
        return url
    parts = parsed.path.strip("/").split("/")
    if len(parts) >= 5 and parts[2] == "blob":
        owner, repo, _, branch = parts[:4]
        path = "/".join(parts[4:])
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    return url


def is_markdown_url(url: str) -> bool:
    path = urllib.parse.urlparse(url).path.lower()
    return path.endswith((".md", ".mdx", ".markdown"))


def is_pdf_url(url: str) -> bool:
    return urllib.parse.urlparse(url).path.lower().endswith(".pdf")


def filename_for(row: dict[str, str], suffix: str) -> str:
    return f"{row['id']}-{slugify(row.get('title', 'source'))}.{suffix}"


def frontmatter(row: dict[str, str], method: str, original_url: str) -> str:
    fields = {
        "source_id": row.get("id", ""),
        "title": row.get("title", "").replace('"', '\\"'),
        "source_type": row.get("source_type", ""),
        "publisher": row.get("publisher", "").replace('"', '\\"'),
        "source_date": row.get("date", ""),
        "url": original_url,
        "evidence_grade": row.get("evidence_grade", ""),
        "capture_method": method,
        "captured_at": CAPTURED_AT,
    }
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f'{key}: "{value}"')
    lines.append("tags:")
    lines.append("  - raw/source")
    if row.get("source_type"):
        lines.append(f"  - source-type/{slugify(row['source_type'], 50)}")
    if row.get("evidence_grade"):
        lines.append(f"  - evidence/{row['evidence_grade'].lower()}")
    lines.append("aliases:")
    lines.append(f"  - {row.get('id', '')}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def write_markdown(out_path: Path, row: dict[str, str], method: str, body: str) -> None:
    title = row.get("title") or row.get("id") or "Source"
    content = frontmatter(row, method, row.get("url_or_path", "")) + f"# {title}\n\n" + body.strip() + "\n"
    out_path.write_text(content, encoding="utf-8")


def download_html_fallback(url: str, html_path: Path, sidecar_path: Path, row: dict[str, str], reason: str) -> tuple[str, str]:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=120) as response:
            html_path.write_bytes(response.read())
    except Exception as exc:  # noqa: BLE001
        return "failed", f"{reason}; fallback HTML download failed: {exc}"
    body = (
        f"Defuddle extraction failed: `{reason}`\n\n"
        f"Raw HTML preserved: [{html_path.name}]({html_path.name})\n\n"
        "Use this sidecar as the traceability record and revisit with a browser/PDF/manual capture if clean text is needed.\n"
    )
    write_markdown(sidecar_path, row, "defuddle-fallback-html", body)
    return "fallback_html", reason


def run_defuddle(url: str, out_path: Path, row: dict[str, str], timeout: int) -> tuple[str, str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "content.md"
        cmd = ["defuddle", "parse", url, "--md", "-o", str(tmp_path)]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if result.returncode != 0:
            reason = (result.stderr or result.stdout).strip()
            return download_html_fallback(url, out_path.with_suffix(".html"), out_path, row, reason)
        body = tmp_path.read_text(encoding="utf-8", errors="replace").strip()
        if len(body) < 80:
            return download_html_fallback(
                url,
                out_path.with_suffix(".html"),
                out_path,
                row,
                "defuddle output shorter than 80 characters",
            )
        write_markdown(out_path, row, "defuddle", body)
        return "ok", ""


def download_text(url: str, out_path: Path, row: dict[str, str]) -> tuple[str, str]:
    raw_url = github_blob_to_raw(url)
    try:
        with urllib.request.urlopen(raw_url, timeout=60) as response:
            data = response.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return "failed", str(exc)
    write_markdown(out_path, row, "direct-download", data)
    return "ok", ""


def download_pdf(url: str, pdf_path: Path, sidecar_path: Path, row: dict[str, str]) -> tuple[str, str]:
    try:
        with urllib.request.urlopen(url, timeout=120) as response:
            pdf_path.write_bytes(response.read())
    except Exception as exc:  # noqa: BLE001
        return "failed", str(exc)
    body = (
        f"Downloaded PDF: [{pdf_path.name}]({pdf_path.name})\n\n"
        "This source is a PDF, so it is preserved as a raw file rather than extracted with defuddle.\n"
    )
    write_markdown(sidecar_path, row, "pdf-download", body)
    return "ok", ""


def load_rows(source_csv: Path) -> list[dict[str, str]]:
    with source_csv.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "source_id",
        "title",
        "url",
        "method",
        "status",
        "raw_path",
        "captured_at",
        "error",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def merge_manifest(path: Path, new_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    if not path.exists():
        return new_rows
    with path.open(encoding="utf-8", newline="") as fh:
        existing = list(csv.DictReader(fh))
    by_id = {row["source_id"]: row for row in existing if row.get("source_id")}
    for row in new_rows:
        by_id[row["source_id"]] = row
    return list(by_id.values())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--industry", required=True, help="Industry slug, e.g. robotics-embodied-ai")
    parser.add_argument("--source-id", action="append", default=[], help="Specific source id to extract. Repeatable.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing extracted files.")
    parser.add_argument("--timeout", type=int, default=120, help="Defuddle timeout per URL in seconds.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if shutil.which("defuddle") is None:
        print("defuddle is not installed. Run: npm install -g defuddle", file=sys.stderr)
        return 2

    source_csv = ROOT / "knowledge" / args.industry / "sources.csv"
    docs_dir = ROOT / "raw" / args.industry / "documents"
    docs_dir.mkdir(parents=True, exist_ok=True)

    selected = set(args.source_id)
    rows = [
        row for row in load_rows(source_csv)
        if (not selected or row.get("id") in selected)
    ]

    manifest: list[dict[str, str]] = []
    for row in rows:
        source_id = row.get("id", "")
        url = row.get("url_or_path", "")
        if not url.startswith(("http://", "https://")):
            manifest.append({
                "source_id": source_id,
                "title": row.get("title", ""),
                "url": url,
                "method": "skip",
                "status": "skipped",
                "raw_path": "",
                "captured_at": CAPTURED_AT,
                "error": "not an HTTP URL",
            })
            continue

        base_md = docs_dir / filename_for(row, "md")
        method = "defuddle"
        if is_pdf_url(url):
            pdf_path = docs_dir / filename_for(row, "pdf")
            if pdf_path.exists() and base_md.exists() and not args.force:
                status, error = "exists", ""
            else:
                status, error = download_pdf(url, pdf_path, base_md, row)
            raw_path = str(pdf_path.relative_to(ROOT))
            method = "pdf-download"
        elif is_markdown_url(url):
            if base_md.exists() and not args.force:
                status, error = "exists", ""
            else:
                status, error = download_text(url, base_md, row)
            raw_path = str(base_md.relative_to(ROOT))
            method = "direct-download"
        else:
            if base_md.exists() and not args.force:
                status, error = "exists", ""
            else:
                status, error = run_defuddle(url, base_md, row, args.timeout)
            raw_path = str(base_md.relative_to(ROOT))

        manifest.append({
            "source_id": source_id,
            "title": row.get("title", ""),
            "url": url,
            "method": method,
            "status": status,
            "raw_path": raw_path,
            "captured_at": CAPTURED_AT,
            "error": error,
        })
        print(f"{source_id}: {status} -> {raw_path}")

    manifest_path = docs_dir / "source_capture_manifest.csv"
    if selected:
        manifest = merge_manifest(manifest_path, manifest)
    write_manifest(manifest_path, manifest)
    return 1 if any(row["status"] == "failed" for row in manifest) else 0


if __name__ == "__main__":
    raise SystemExit(main())
