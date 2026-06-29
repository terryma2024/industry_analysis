#!/usr/bin/env python3
"""Link backticked SRC ids in knowledge notes to raw source artifacts."""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC_RE = re.compile(r"(?<!\[)`(SRC-[A-Za-z0-9-]+-\d{3})`")
MOC_RE = re.compile(r"\[\[00-source-capture-index\|(SRC-[A-Za-z0-9-]+-\d{3})\]\]")


def load_raw_paths(industry: str) -> dict[str, Path]:
    manifest = ROOT / "raw" / industry / "documents" / "source_capture_manifest.csv"
    paths: dict[str, Path] = {}
    if not manifest.exists():
        return paths
    with manifest.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            source_id = row.get("source_id", "")
            raw_path = row.get("raw_path", "")
            if not source_id or not raw_path:
                continue
            candidate = ROOT / raw_path
            if candidate.exists():
                paths[source_id] = candidate
    return paths


def replacement(note_path: Path, raw_paths: dict[str, Path], source_id: str) -> str:
    raw_path = raw_paths.get(source_id)
    if raw_path:
        rel = os.path.relpath(raw_path, note_path.parent)
        return f"[`{source_id}`]({rel})"
    return f"[[00-source-capture-index|{source_id}]]"


def link_note(note_path: Path, raw_paths: dict[str, Path]) -> bool:
    text = note_path.read_text(encoding="utf-8")
    updated = MOC_RE.sub(lambda match: replacement(note_path, raw_paths, match.group(1)), text)
    updated = SRC_RE.sub(lambda match: replacement(note_path, raw_paths, match.group(1)), updated)
    if updated == text:
        return False
    note_path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--industry", required=True)
    args = parser.parse_args()

    notes_dir = ROOT / "knowledge" / args.industry
    raw_paths = load_raw_paths(args.industry)
    changed = []
    for note_path in sorted(notes_dir.rglob("*.md")):
        if note_path.name == "00-source-capture-index.md":
            continue
        if link_note(note_path, raw_paths):
            changed.append(note_path.relative_to(ROOT))

    for path in changed:
        print(path)
    print(f"linked {len(changed)} notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
