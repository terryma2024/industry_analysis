# AGENTS.md

## Project Purpose

This repository is an industry analysis workspace for learning, investing, and career exploration, focused on China's strategic industries in the 15th Five-Year Plan period.

## Required Repository Skill

When working on industry research, source organization, knowledge synthesis, investment analysis, career analysis, or tooling in this repository, use the project skill at:

`/.agents/skills/industry-analysis/SKILL.md`

## Repository Conventions

- Store source documents and raw datasets under `raw/<industry>/documents/` and `raw/<industry>/data/`.
- Store synthesized knowledge under `knowledge/<industry>/`.
- Store reusable scripts and templates under `tools/`.
- Run Python scripts with `uv run python ...`; do not call system `python` or `python3` directly for project scripts.
- Focus analysis on China unless the user explicitly asks for a global view. Use global comparisons only to clarify China's position, gaps, supply chain dependencies, export opportunities, or competitive pressure.
- Preserve source traceability. Important claims should point back to filenames, URLs, page numbers, tables, or dataset names whenever available.
- Prefer durable Markdown/CSV artifacts over transient chat summaries.
- Use stable English slugs for directories and Chinese names in headings and tables.

## Research Standards

- Separate facts, estimates, judgments, and hypotheses.
- Prefer primary sources first: policy text, filings, annual reports, official statistics, papers, standards, product docs, and company disclosures.
- For policy analysis, prioritize national and local Chinese policy documents, 15th Five-Year Plan related materials, ministry/commission releases, exchange filings, industry standards, and official statistics.
- Use secondary sources to triangulate, not as the only basis for important conclusions.
- For investment views, include uncertainty, downside risks, key monitoring indicators, and what would change the thesis.
- For career views, include role families, required skills, portfolio/project ideas, and hiring signals.
