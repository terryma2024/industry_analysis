#!/usr/bin/env python3
"""Check that the industry analysis workspace has the expected structure."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_TOP_LEVEL = ["raw", "knowledge", "tools", "docs", ".agents/skills/industry-analysis"]


def main() -> int:
    root = Path.cwd()
    missing = [path for path in REQUIRED_TOP_LEVEL if not (root / path).exists()]
    registry_path = root / "tools" / "industry_registry.json"

    if not registry_path.exists():
        missing.append("tools/industry_registry.json")
        registry = []
    else:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))

    for item in registry:
        slug = item["slug"]
        for path in [
            root / "raw" / slug / "documents",
            root / "raw" / slug / "data",
            root / "knowledge" / slug,
        ]:
            if not path.exists():
                missing.append(str(path.relative_to(root)))

    if missing:
        print("Missing workspace paths:")
        for path in missing:
            print(f"- {path}")
        return 1

    print(f"Workspace OK: {len(registry)} industries configured.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
