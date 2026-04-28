---
name: industry-analysis
description: Use when working in this repository on industry research, raw source organization, knowledge synthesis, investment analysis, career analysis, industry templates, or reusable research tooling.
---

# Industry Analysis

## Core Rule

Build durable research assets, not one-off chat summaries. Preserve source traceability from `raw/` to `knowledge/`. Focus on China and the 15th Five-Year Plan period unless the user explicitly asks for a global-only analysis.

## Workflow

1. Identify the industry slug from `tools/industry_registry.json`; create a new slug only if no existing one fits.
2. Put original documents under `raw/<slug>/documents/` and raw datasets under `raw/<slug>/data/`.
3. Record used sources in `knowledge/<slug>/sources.csv` with an evidence grade.
4. Synthesize into `knowledge/<slug>/` using the standard files:
   - `00-index.md`
   - `01-industry-map.md`
   - `02-technology-and-products.md`
   - `03-market-and-policy.md`
   - `04-companies.md`
   - `05-investment-view.md`
   - `06-career-view.md`
5. Separate facts, estimates, judgments, and hypotheses.
6. For each industry, explain its China policy position: why it matters to national strategy, which 15th Five-Year Plan themes it connects to, and where China has strengths, bottlenecks, or supply-chain dependencies.
7. For investment analysis, always include China-specific thesis, policy catalyst, risk, what would change the thesis, and monitoring indicators.
8. For career analysis, always include China role families, skill requirements, learning path, portfolio ideas, and hiring signals.
9. Treat `knowledge/` as an Obsidian vault. Use Obsidian-compatible Markdown, wikilinks, index/MOC notes, and source backlinks when creating or maintaining knowledge artifacts.

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
