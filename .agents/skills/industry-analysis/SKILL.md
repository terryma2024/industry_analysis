---
name: industry-analysis
description: Use when working in this repository on industry research, raw source organization, knowledge synthesis, investment analysis, career analysis, industry templates, or reusable research tooling.
---

# Industry Analysis

## Core Rule

Build durable research assets, not one-off chat summaries. Preserve source traceability from `raw/` to `knowledge/`. Treat this repository as a Karpathy-style LLM Wiki for China industry research: `raw/` is the immutable source layer, `knowledge/` is the compiled wiki layer, and `AGENTS.md` is the schema/governance layer. Focus on China and the 15th Five-Year Plan period unless the user explicitly asks for a global-only analysis.

## Workflow

1. Read `knowledge/index.md` first when the task depends on existing repository knowledge.
2. Identify the industry slug from `tools/industry_registry.json`; create a new slug only if no existing one fits.
3. Put original documents under `raw/<slug>/documents/` and raw datasets under `raw/<slug>/data/`. Use `raw/_inbox/` for uncategorized sources before assignment.
4. Record used sources in `knowledge/<slug>/sources.csv` with an evidence grade.
5. Compile durable knowledge into the appropriate wiki layer:
   - `knowledge/_sources/` for one-source or source-set summaries.
   - `knowledge/_entities/` for people, companies, institutions, tools, products, and projects.
   - `knowledge/_concepts/` for reusable concepts, frameworks, methods, and technologies.
   - `knowledge/_claims/` for important atomic facts, estimates, judgments, and hypotheses.
   - `knowledge/_syntheses/` for cross-source or cross-industry analysis and high-value query outputs.
   - `knowledge/<slug>/` for industry-specific synthesis using the standard files.
6. For each industry, keep the standard files:
   - `00-index.md`
   - `01-industry-map.md`
   - `02-technology-and-products.md`
   - `03-market-and-policy.md`
   - `04-companies.md`
   - `05-investment-view.md`
   - `06-career-view.md`
7. Separate facts, estimates, judgments, and hypotheses.
8. For each industry, explain its China policy position: why it matters to national strategy, which 15th Five-Year Plan themes it connects to, and where China has strengths, bottlenecks, or supply-chain dependencies.
9. For investment analysis, always include China-specific thesis, policy catalyst, risk, what would change the thesis, and monitoring indicators.
10. For career analysis, always include China role families, skill requirements, learning path, portfolio ideas, and hiring signals.
11. Treat `knowledge/` as an Obsidian vault. Use Obsidian-compatible Markdown, wikilinks, index/MOC notes, source backlinks, and `## 关联连接` sections when creating or maintaining knowledge artifacts.
12. After significant writes, update `knowledge/index.md` and append `knowledge/log.md`.

## LLM Wiki Operations

- `ingest`: compile sources from `raw/` or URLs into `_sources`, then update relevant entities, concepts, claims, syntheses, industry pages, `knowledge/index.md`, and `knowledge/log.md`.
- `query`: start from `knowledge/index.md`, read relevant pages, answer with wikilink citations, and ask whether to save high-value analysis into `_syntheses/` unless the user already requested persistence.
- `lint`: inspect `knowledge/` for dead links, orphan pages, pages missing from `knowledge/index.md`, weak source traceability, and unresolved `## 知识冲突`; report before fixing unless the user asks for automatic repair.
- `news`: create one Markdown file per ad hoc news/article/video/audio summary in `knowledge/news/`, then update `knowledge/news/00-index.md`, `knowledge/index.md`, and `knowledge/log.md` when the item is significant.

## Source Quality

Use primary sources first: Chinese national and local policy text, 15th Five-Year Plan related materials, ministry/commission releases, standards, company filings, financial reports, original statistics, papers, and product documentation. Use reports and media to triangulate or discover leads.

Evidence grades:

- S: official, regulatory, filing, standard, original statistical data, paper.
- A: reputable institutional report, association report, company white paper.
- B: media interview, conference transcript, job posting dataset.
- C: social media, unsourced chart, secondary repost.

## Useful Resources

- Read `references/research-framework.md` for the analysis checklist.
- Read `references/source-quality.md` when judging evidence quality.
- Run `uv run python .agents/skills/industry-analysis/scripts/check_workspace.py` to verify required project directories exist.
- Run `uv run python tools/new_industry_workspace.py <slug> <name>` to add a new industry workspace.
- Use `uv run python ...` for all project Python scripts; do not call system `python` or `python3` directly.

## Output Style

Write concise Markdown with tables where comparison matters. Avoid unsupported certainty. Mark missing data explicitly as `待验证` and state the next source to seek.
