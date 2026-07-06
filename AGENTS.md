# AGENTS.md

## Project Purpose

This repository is an industry analysis workspace for learning, investing, and career exploration, focused on China's strategic industries in the 15th Five-Year Plan period.

## Required Repository Skill

When working on industry research, source organization, knowledge synthesis, investment analysis, career analysis, or tooling in this repository, use the project skill at:

`/.agents/skills/industry-analysis/SKILL.md`

When the user provides a video/audio URL or asks for video notes, use:

`/.agents/skills/video-summarizer/SKILL.md`

## Repository Conventions

- Treat this repository as a Karpathy-style LLM Wiki adapted for China industry research:
  - `raw/` is the immutable source layer. Read from it, but do not rewrite source files unless the user explicitly asks to repair metadata or extraction artifacts.
  - `knowledge/` is the compiled wiki layer and Obsidian vault. Create, update, link, and maintain Markdown knowledge assets here.
  - `AGENTS.md` is the schema/governance layer. Update it when the wiki operating model changes.
- Store source documents and raw datasets under `raw/<industry>/documents/` and `raw/<industry>/data/`.
- Use `raw/_inbox/articles/`, `raw/_inbox/papers/`, `raw/_inbox/transcripts/`, and `raw/_inbox/news/` for uncategorized sources before they are assigned to an industry or compiled into `knowledge/`.
- Store synthesized knowledge under `knowledge/<industry>/`.
- Store complete industry-specific research documents under `knowledge/<industry>/research-notes/`. Use `knowledge/_syntheses/` mainly for cross-industry synthesis, migration plans, or high-value outputs without a clear single-industry home.
- Treat `knowledge/` as the Obsidian vault for this project. Create, manage, and maintain knowledge-base content in Obsidian-compatible Markdown.
- When creating or editing knowledge notes, prefer Obsidian conventions: wikilinks, stable headings, note properties when useful, backlinks, tags, and index/MOC notes.
- When Obsidian-specific syntax or vault operations matter, use the installed Obsidian skills such as `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `obsidian-canvas-creator`, `mermaid-visualizer`, and `excalidraw-diagram`.
- Store reusable scripts and templates under `tools/`.
- Run Python scripts with `uv run python ...`; do not call system `python` or `python3` directly for project scripts.
- Focus analysis on China unless the user explicitly asks for a global view. Use global comparisons only to clarify China's position, gaps, supply chain dependencies, export opportunities, or competitive pressure.
- Preserve source traceability. Important claims should point back to filenames, URLs, page numbers, tables, or dataset names whenever available.
- For web sources recorded in `knowledge/<industry>/sources.csv`, extract durable Markdown/raw artifacts into `raw/<industry>/documents/` using `tools/extract_sources_with_defuddle.py` and keep `source_capture_manifest.csv` updated. Follow `docs/source_capture_sop.md`, and maintain Obsidian-friendly source-capture MOC notes under `knowledge/<industry>/`.
- Follow `docs/obsidian_knowledge_sop.md` for the user's preferred knowledge-production style: durable research assets over chat-only answers, no fabricated data, source-traceable claims, Obsidian-first wikilinks/MOCs/callouts/backlinks, readable link text, explicit task status, and table-safe wikilink aliases using escaped pipes (`\|`).
- For ad hoc news, article, video, or audio summary requests, write the durable output under `knowledge/news/`: create one Markdown file per summary using `YYYY-MM-DD-english-slug.md`, include source URL, platform/publisher, date, extraction method or limitation, key facts, judgments, follow-up questions, and relevant industry wikilinks, and add an index row in `knowledge/news/00-index.md`. Keep `knowledge/README.md` linked to the News category.
- Maintain the global LLM Wiki files:
  - `knowledge/index.md` is the content-oriented global index. Before answering repository knowledge queries, read it first; after creating a significant page, add or update its index row.
  - `knowledge/log.md` is append-only. After significant ingest/query/lint/migration work, append `## [YYYY-MM-DD] action | summary` with changed pages and conflicts.
- Use the compiled wiki layer by page type:
  - `knowledge/_sources/`: one source-summary page per important source or source set.
  - `knowledge/_entities/`: people, companies, institutions, tools, products, projects.
  - `knowledge/_concepts/`: reusable concepts, frameworks, methods, technologies.
  - `knowledge/_claims/`: atomic source-backed facts, estimates, judgments, and hypotheses when a claim becomes important enough to track independently.
  - `knowledge/_syntheses/`: cross-source or cross-industry analysis, comparisons, migration plans, and high-value query outputs.
- For `ingest`-style requests, compile sources into the wiki instead of only summarizing in chat: create/update source, entity, concept, claim, synthesis, or industry pages; update `knowledge/index.md`; append `knowledge/log.md`; preserve source traceability.
- For `query`-style requests about this repository, start from `knowledge/index.md`, then read relevant pages deeply. If the answer is valuable and reusable, ask whether to save it to `knowledge/_syntheses/` unless the user has already asked to save it.
- For `lint` or health-check requests, inspect `knowledge/` for dead wikilinks, orphan pages, files missing from `knowledge/index.md`, missing source traceability, and unresolved `## 知识冲突` sections. Report first; only modify files after the user asks for fixes.
- Prefer durable Markdown/CSV artifacts over transient chat summaries.
- Use stable English slugs for directories and Chinese names in headings and tables.

## Wiki Page Schema

All new compiled wiki pages should include YAML frontmatter when practical:

```yaml
---
title:
type: source | entity | concept | claim | synthesis | industry | news-summary | index | log
date_created: YYYY-MM-DD
last_updated: YYYY-MM-DD
sources:
  - raw/... or knowledge/...
tags:
status: draft | active | needs-review
---
```

Every non-index compiled page should include a `## 关联连接` section with relevant wikilinks. If new evidence conflicts with an existing page, do not silently overwrite it; add or update a `## 知识冲突` section with both claims, sources, and next verification steps.

## Research Standards

- Separate facts, estimates, judgments, and hypotheses.
- Prefer primary sources first: policy text, filings, annual reports, official statistics, papers, standards, product docs, and company disclosures.
- For policy analysis, prioritize national and local Chinese policy documents, 15th Five-Year Plan related materials, ministry/commission releases, exchange filings, industry standards, and official statistics.
- Use secondary sources to triangulate, not as the only basis for important conclusions.
- For investment views, include uncertainty, downside risks, key monitoring indicators, and what would change the thesis.
- For career views, include role families, required skills, portfolio/project ideas, and hiring signals.
