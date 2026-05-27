#!/usr/bin/env python3
"""Extract PDF sources into durable Markdown/JSON research artifacts.

The tool is intentionally dependency-light. It tries optional local PDF
engines in this order when ``--engine auto`` is used:

1. Docling
2. PyMuPDF4LLM
3. PyMuPDF
4. the ``pdftotext`` command-line tool

It then writes:

- ``raw/<industry>/documents/<SRC-ID>-<slug>.pdf`` when a URL must be downloaded
- ``raw/<industry>/documents/<SRC-ID>-<slug>.md`` as the durable raw extract
- ``raw/<industry>/documents/<SRC-ID>-<slug>.json`` as structured metadata/text
- ``raw/<industry>/documents/<SRC-ID>-<slug>.key-info.md`` as an analyst draft
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
CAPTURED_AT = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()
MANIFEST_FIELDS = [
    "source_id",
    "title",
    "url",
    "method",
    "status",
    "raw_path",
    "captured_at",
    "error",
]


@dataclass
class PageText:
    page: int
    text: str


@dataclass
class ExtractionResult:
    engine: str
    markdown: str
    pages: list[PageText]
    metadata: dict[str, object]


class ExtractionError(RuntimeError):
    """Raised when a PDF extraction engine cannot extract useful text."""


def slugify(value: str, max_len: int = 80) -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "source"


def is_pdf_reference(value: str) -> bool:
    parsed = urllib.parse.urlparse(value)
    path = parsed.path or value
    return path.lower().endswith(".pdf")


def filename_for(row: dict[str, str], suffix: str) -> str:
    title = row.get("title") or row.get("url_or_path") or "source"
    source_id = row.get("id") or row.get("source_id") or "SRC"
    return f"{source_id}-{slugify(title)}.{suffix}"


def frontmatter(row: dict[str, str], method: str, original_url: str, extra: dict[str, str] | None = None) -> str:
    fields = {
        "source_id": row.get("id", row.get("source_id", "")),
        "title": row.get("title", "").replace('"', '\\"'),
        "source_type": row.get("source_type", ""),
        "publisher": row.get("publisher", "").replace('"', '\\"'),
        "source_date": row.get("date", ""),
        "url": original_url,
        "evidence_grade": row.get("evidence_grade", ""),
        "capture_method": method,
        "captured_at": CAPTURED_AT,
    }
    if extra:
        fields.update(extra)
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f'{key}: "{value}"')
    lines.append("tags:")
    lines.append("  - raw/source")
    lines.append("  - raw/pdf")
    if row.get("source_type"):
        lines.append(f"  - source-type/{slugify(row['source_type'], 50)}")
    if row.get("evidence_grade"):
        lines.append(f"  - evidence/{row['evidence_grade'].lower()}")
    lines.append("aliases:")
    lines.append(f"  - {fields['source_id']}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def load_rows(source_csv: Path) -> list[dict[str, str]]:
    with source_csv.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def select_pdf_rows(rows: list[dict[str, str]], selected_ids: set[str]) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for row in rows:
        source_id = row.get("id", "")
        if selected_ids and source_id not in selected_ids:
            continue
        if is_pdf_reference(row.get("url_or_path", "")):
            selected.append(row)
    return selected


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def merge_manifest(path: Path, new_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    if not path.exists():
        return new_rows
    with path.open(encoding="utf-8", newline="") as fh:
        existing = list(csv.DictReader(fh))
    by_id: dict[str, dict[str, str]] = {}
    order: list[str] = []
    for row in existing:
        source_id = row.get("source_id", "")
        if not source_id:
            continue
        if source_id not in by_id:
            order.append(source_id)
        by_id[source_id] = {field: row.get(field, "") for field in MANIFEST_FIELDS}
    for row in new_rows:
        source_id = row.get("source_id", "")
        if source_id and source_id not in by_id:
            order.append(source_id)
        by_id[source_id] = {field: row.get(field, "") for field in MANIFEST_FIELDS}
    return [by_id[source_id] for source_id in order]


def ensure_local_pdf(row: dict[str, str], docs_dir: Path, force_download: bool) -> tuple[Path, str]:
    value = row.get("url_or_path", "")
    if value.startswith(("http://", "https://")):
        pdf_path = docs_dir / filename_for(row, "pdf")
        if pdf_path.exists() and not force_download:
            return pdf_path, value
        request = urllib.request.Request(value, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=180) as response:
            pdf_path.write_bytes(response.read())
        return pdf_path, value

    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        raise FileNotFoundError(f"PDF path does not exist: {path}")
    return path, value


def extract_with_docling(pdf_path: Path) -> ExtractionResult:
    try:
        from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions  # type: ignore[import-not-found]
        from docling.datamodel.base_models import InputFormat  # type: ignore[import-not-found]
        from docling.datamodel.pipeline_options import PdfPipelineOptions  # type: ignore[import-not-found]
        from docling.document_converter import DocumentConverter  # type: ignore[import-not-found]
        from docling.document_converter import PdfFormatOption  # type: ignore[import-not-found]
    except Exception as exc:  # noqa: BLE001
        raise ExtractionError(f"docling unavailable: {exc}") from exc

    pipeline_options = PdfPipelineOptions(
        accelerator_options=AcceleratorOptions(device=AcceleratorDevice.CPU)
    )
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    converted = converter.convert(str(pdf_path))
    document = converted.document
    markdown = document.export_to_markdown()
    metadata: dict[str, object] = {"engine": "docling"}
    try:
        metadata["document"] = document.export_to_dict()
    except Exception:  # noqa: BLE001
        metadata["document"] = {}
    if len(markdown.strip()) < 40:
        raise ExtractionError("docling produced less than 40 characters")
    return ExtractionResult(
        engine="docling",
        markdown=markdown,
        pages=[PageText(page=0, text=markdown)],
        metadata=metadata,
    )


def extract_with_pymupdf4llm(pdf_path: Path) -> ExtractionResult:
    try:
        import pymupdf4llm  # type: ignore[import-not-found]
    except Exception as exc:  # noqa: BLE001
        raise ExtractionError(f"pymupdf4llm unavailable: {exc}") from exc

    markdown = pymupdf4llm.to_markdown(str(pdf_path))
    if len(markdown.strip()) < 40:
        raise ExtractionError("pymupdf4llm produced less than 40 characters")
    pages = split_markdown_pages(markdown)
    return ExtractionResult(
        engine="pymupdf4llm",
        markdown=markdown,
        pages=pages,
        metadata={"engine": "pymupdf4llm"},
    )


def extract_with_pymupdf(pdf_path: Path) -> ExtractionResult:
    try:
        import fitz  # type: ignore[import-not-found]
    except Exception as exc:  # noqa: BLE001
        raise ExtractionError(f"pymupdf unavailable: {exc}") from exc

    pages: list[PageText] = []
    with fitz.open(pdf_path) as document:
        for index, page in enumerate(document, start=1):
            pages.append(PageText(page=index, text=page.get_text("text").strip()))
    markdown = "\n\n".join(format_page(page) for page in pages if page.text.strip())
    if len(markdown.strip()) < 40:
        raise ExtractionError("pymupdf produced less than 40 characters")
    return ExtractionResult(
        engine="pymupdf",
        markdown=markdown,
        pages=pages,
        metadata={"engine": "pymupdf", "page_count": len(pages)},
    )


def extract_with_pdftotext(pdf_path: Path) -> ExtractionResult:
    if shutil.which("pdftotext") is None:
        raise ExtractionError("pdftotext command unavailable")
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "out.txt"
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(out_path)],
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode != 0:
            raise ExtractionError((result.stderr or result.stdout).strip())
        text = out_path.read_text(encoding="utf-8", errors="replace").strip()
    if len(text) < 40:
        raise ExtractionError("pdftotext produced less than 40 characters")
    pages = split_form_feed_pages(text)
    markdown = "\n\n".join(format_page(page) for page in pages if page.text.strip())
    return ExtractionResult(
        engine="pdftotext",
        markdown=markdown,
        pages=pages,
        metadata={"engine": "pdftotext", "page_count": len(pages)},
    )


def split_form_feed_pages(text: str) -> list[PageText]:
    chunks = text.split("\f")
    return [PageText(page=index, text=chunk.strip()) for index, chunk in enumerate(chunks, start=1) if chunk.strip()]


def split_markdown_pages(markdown: str) -> list[PageText]:
    page_marker = re.compile(r"^-{3,}\s*$", re.M)
    chunks = [chunk.strip() for chunk in page_marker.split(markdown) if chunk.strip()]
    if len(chunks) <= 1:
        return [PageText(page=0, text=markdown.strip())]
    return [PageText(page=index, text=chunk) for index, chunk in enumerate(chunks, start=1)]


def format_page(page: PageText) -> str:
    label = "Unpaginated" if page.page == 0 else f"Page {page.page}"
    return f"## {label}\n\n{page.text.strip()}"


def extract_pdf(pdf_path: Path, engine: str) -> ExtractionResult:
    engines: dict[str, Callable[[Path], ExtractionResult]] = {
        "docling": extract_with_docling,
        "pymupdf4llm": extract_with_pymupdf4llm,
        "pymupdf": extract_with_pymupdf,
        "pdftotext": extract_with_pdftotext,
    }
    if engine != "auto":
        return engines[engine](pdf_path)

    errors: list[str] = []
    for name in ("docling", "pymupdf4llm", "pymupdf", "pdftotext"):
        try:
            return engines[name](pdf_path)
        except ExtractionError as exc:
            errors.append(f"{name}: {exc}")
    raise ExtractionError("; ".join(errors))


def write_source_markdown(path: Path, row: dict[str, str], result: ExtractionResult, original_url: str, pdf_path: Path) -> None:
    title = row.get("title") or row.get("id") or pdf_path.stem
    extra = {
        "pdf_file": str(pdf_path.relative_to(ROOT)) if pdf_path.is_relative_to(ROOT) else str(pdf_path),
        "page_count": str(len(result.pages)),
    }
    body = frontmatter(row, f"pdf-extract-{result.engine}", original_url, extra)
    body += f"# {title}\n\n"
    body += result.markdown.strip() + "\n"
    path.write_text(body, encoding="utf-8")


def write_structured_json(path: Path, row: dict[str, str], result: ExtractionResult, pdf_path: Path) -> None:
    payload = {
        "source_id": row.get("id", row.get("source_id", "")),
        "title": row.get("title", ""),
        "url_or_path": row.get("url_or_path", ""),
        "pdf_path": str(pdf_path.relative_to(ROOT)) if pdf_path.is_relative_to(ROOT) else str(pdf_path),
        "captured_at": CAPTURED_AT,
        "engine": result.engine,
        "pages": [asdict(page) for page in result.pages],
        "metadata": result.metadata,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def extract_tables_from_pages(pages: list[PageText]) -> list[tuple[int, str]]:
    tables: list[tuple[int, str]] = []
    lines: list[str] = []
    page_number = 0
    for page in pages:
        for line in page.text.splitlines():
            if "|" in line and line.count("|") >= 2:
                if not lines:
                    page_number = page.page
                lines.append(line.rstrip())
            elif lines:
                tables.append((page_number, "\n".join(lines)))
                lines = []
        if lines:
            tables.append((page_number, "\n".join(lines)))
            lines = []
    return tables


def lead_sentences(text: str, limit: int = 4) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return []
    candidates = re.split(r"(?<=[.!?。！？])\s+", cleaned)
    leads: list[str] = []
    for sentence in candidates:
        sentence = sentence.strip()
        if len(sentence) < 20:
            continue
        leads.append(sentence[:350])
        if len(leads) >= limit:
            break
    if leads:
        return leads
    return [cleaned[:350]]


def build_key_info_draft(row: dict[str, str], pages: list[PageText], source_markdown_path: Path) -> str:
    source_id = row.get("id", row.get("source_id", ""))
    title = row.get("title") or source_id or "PDF Source"
    front = frontmatter(
        row,
        "pdf-key-info-draft",
        row.get("url_or_path", ""),
        {"source_markdown": str(source_markdown_path)},
    )
    lines = [
        front + f"# {title} - Key Information Draft",
        "",
        "> [!warning]",
        "> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.",
        "",
        "## Source Trace",
        "",
        f"- Source ID: `{source_id}`",
        f"- Raw Markdown: [{source_markdown_path.name}]({source_markdown_path.name})",
        f"- Evidence grade: `{row.get('evidence_grade', '') or 'needs-verification'}`",
        "",
        "## Page-Level Leads",
        "",
    ]

    for page in pages:
        label = "unpaginated" if page.page == 0 else f"p. {page.page}"
        for sentence in lead_sentences(page.text, limit=2):
            lines.append(f"- [{label}] {sentence}")
    if lines[-1] == "":
        lines.append("- needs-verification: no extractable page text found.")

    tables = extract_tables_from_pages(pages)
    lines.extend(["", "## Extracted Tables", ""])
    if tables:
        for index, (page_number, table) in enumerate(tables, start=1):
            label = "unpaginated" if page_number == 0 else f"p. {page_number}"
            lines.append(f"### Table {index} ({label})")
            lines.append("")
            lines.append(table)
            lines.append("")
    else:
        lines.append("- needs-verification: no Markdown-style tables detected.")

    lines.extend(
        [
            "",
            "## Analyst Checklist",
            "",
            "- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.",
            "- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.",
            "- Judgments: separate source judgments from your own investment/career analysis.",
            "- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.",
            "",
        ]
    )
    return "\n".join(lines)


def process_row(row: dict[str, str], docs_dir: Path, engine: str, force: bool) -> dict[str, str]:
    source_id = row.get("id", "")
    original = row.get("url_or_path", "")
    md_path = docs_dir / filename_for(row, "md")
    json_path = docs_dir / filename_for(row, "json")
    draft_path = docs_dir / filename_for(row, "key-info.md")

    if md_path.exists() and json_path.exists() and draft_path.exists() and not force:
        return {
            "source_id": source_id,
            "title": row.get("title", ""),
            "url": original,
            "method": "pdf-extract",
            "status": "exists",
            "raw_path": str(md_path.relative_to(ROOT)),
            "captured_at": CAPTURED_AT,
            "error": "",
        }

    pdf_path, original_url = ensure_local_pdf(row, docs_dir, force_download=force)
    result = extract_pdf(pdf_path, engine)
    write_source_markdown(md_path, row, result, original_url, pdf_path)
    write_structured_json(json_path, row, result, pdf_path)
    draft = build_key_info_draft(row, result.pages, source_markdown_path=Path(md_path.name))
    draft_path.write_text(draft, encoding="utf-8")

    return {
        "source_id": source_id,
        "title": row.get("title", ""),
        "url": original,
        "method": f"pdf-extract-{result.engine}",
        "status": "ok",
        "raw_path": str(md_path.relative_to(ROOT)),
        "captured_at": CAPTURED_AT,
        "error": "",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--industry", required=True, help="Industry slug, e.g. robotics-embodied-ai")
    parser.add_argument("--source-id", action="append", default=[], help="Specific source id to extract. Repeatable.")
    parser.add_argument(
        "--engine",
        choices=["auto", "docling", "pymupdf4llm", "pymupdf", "pdftotext"],
        default="auto",
        help="PDF extraction backend.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing extracted files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_csv = ROOT / "knowledge" / args.industry / "sources.csv"
    if not source_csv.exists():
        print(f"source CSV not found: {source_csv}", file=sys.stderr)
        return 2

    docs_dir = ROOT / "raw" / args.industry / "documents"
    docs_dir.mkdir(parents=True, exist_ok=True)

    selected_ids = set(args.source_id)
    rows = select_pdf_rows(load_rows(source_csv), selected_ids)
    if selected_ids and not rows:
        print(f"no matching PDF source rows found for: {', '.join(sorted(selected_ids))}", file=sys.stderr)
        return 2

    manifest: list[dict[str, str]] = []
    for row in rows:
        try:
            manifest_row = process_row(row, docs_dir, args.engine, args.force)
        except Exception as exc:  # noqa: BLE001
            manifest_row = {
                "source_id": row.get("id", ""),
                "title": row.get("title", ""),
                "url": row.get("url_or_path", ""),
                "method": f"pdf-extract-{args.engine}",
                "status": "failed",
                "raw_path": "",
                "captured_at": CAPTURED_AT,
                "error": str(exc),
            }
        manifest.append(manifest_row)
        print(f"{manifest_row['source_id']}: {manifest_row['status']} -> {manifest_row['raw_path']}")

    manifest_path = docs_dir / "source_capture_manifest.csv"
    manifest = merge_manifest(manifest_path, manifest)
    write_manifest(manifest_path, manifest)
    return 1 if any(row["status"] == "failed" for row in manifest if row.get("method", "").startswith("pdf-extract")) else 0


if __name__ == "__main__":
    raise SystemExit(main())
