#!/usr/bin/env python3
"""Ensure raw source markdown files have Obsidian-friendly tags and aliases."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-") or "source"


def prop(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"?([^\"\n]+)\"?", frontmatter, re.M)
    return match.group(1).strip() if match else ""


def normalize(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    frontmatter = text[4:end]
    if re.search(r"^tags:", frontmatter, re.M):
        return False

    source_id = prop(frontmatter, "source_id") or path.stem
    source_type = prop(frontmatter, "source_type")
    grade = prop(frontmatter, "evidence_grade")

    additions = ["tags:", "  - raw/source"]
    if source_type:
        additions.append(f"  - source-type/{slugify(source_type)}")
    if grade:
        additions.append(f"  - evidence/{grade.lower()}")
    additions.extend(["aliases:", f"  - {source_id}"])

    path.write_text(text[:end] + "\n" + "\n".join(additions) + text[end:], encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--industry", required=True)
    args = parser.parse_args()

    docs_dir = ROOT / "raw" / args.industry / "documents"
    count = 0
    for path in docs_dir.glob("SRC-*.md"):
        if normalize(path):
            count += 1
    print(f"updated {count} raw markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
