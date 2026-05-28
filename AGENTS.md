# AGENTS.md

## Project Purpose

This repository is an industry analysis workspace for learning, investing, and career exploration, focused on China's strategic industries in the 15th Five-Year Plan period.

## Required Repository Skill

When working on industry research, source organization, knowledge synthesis, investment analysis, career analysis, or tooling in this repository, use the project skill at:

`/.agents/skills/industry-analysis/SKILL.md`

When the user provides a video/audio URL or asks for video notes, use:

`/.agents/skills/video-summarizer/SKILL.md`

## Repository Conventions

- Store source documents and raw datasets under `raw/<industry>/documents/` and `raw/<industry>/data/`.
- Store synthesized knowledge under `knowledge/<industry>/`.
- Treat `knowledge/` as the Obsidian vault for this project. Create, manage, and maintain knowledge-base content in Obsidian-compatible Markdown.
- When creating or editing knowledge notes, prefer Obsidian conventions: wikilinks, stable headings, note properties when useful, backlinks, tags, and index/MOC notes.
- When Obsidian-specific syntax or vault operations matter, use the installed Obsidian skills such as `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `obsidian-canvas-creator`, `mermaid-visualizer`, and `excalidraw-diagram`.
- Store reusable scripts and templates under `tools/`.
- Run Python scripts with `uv run python ...`; do not call system `python` or `python3` directly for project scripts.
- Focus analysis on China unless the user explicitly asks for a global view. Use global comparisons only to clarify China's position, gaps, supply chain dependencies, export opportunities, or competitive pressure.
- Preserve source traceability. Important claims should point back to filenames, URLs, page numbers, tables, or dataset names whenever available.
- For web sources recorded in `knowledge/<industry>/sources.csv`, extract durable Markdown/raw artifacts into `raw/<industry>/documents/` using `tools/extract_sources_with_defuddle.py` and keep `source_capture_manifest.csv` updated. Follow `docs/source_capture_sop.md`, and maintain Obsidian-friendly source-capture MOC notes under `knowledge/<industry>/`.
- Follow `docs/obsidian_knowledge_sop.md` for the user's preferred knowledge-production style: durable research assets over chat-only answers, no fabricated data, source-traceable claims, Obsidian-first wikilinks/MOCs/callouts/backlinks, readable link text, explicit task status, and table-safe wikilink aliases using escaped pipes (`\|`).
- Prefer durable Markdown/CSV artifacts over transient chat summaries.
- Use stable English slugs for directories and Chinese names in headings and tables.

## Research Standards

- Separate facts, estimates, judgments, and hypotheses.
- Prefer primary sources first: policy text, filings, annual reports, official statistics, papers, standards, product docs, and company disclosures.
- For policy analysis, prioritize national and local Chinese policy documents, 15th Five-Year Plan related materials, ministry/commission releases, exchange filings, industry standards, and official statistics.
- Use secondary sources to triangulate, not as the only basis for important conclusions.
- For investment views, include uncertainty, downside risks, key monitoring indicators, and what would change the thesis.
- For career views, include role families, required skills, portfolio/project ideas, and hiring signals.
