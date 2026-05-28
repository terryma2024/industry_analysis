---
title: Obsidian Knowledge Production SOP
date: 2026-05-28
tags:
  - workflow/obsidian
  - research/sop
  - knowledge-management
aliases:
  - Obsidian 知识生产 SOP
  - Knowledge Note SOP
  - 用户研究文档风格 SOP
---

# Obsidian Knowledge Production SOP

## Purpose

This SOP captures the user's preferred working style for this repository: build durable, source-traceable, Obsidian-friendly research assets that can be read, navigated, extended, and audited later.

> [!important]
> The user reads the repository mainly in Obsidian. Treat `knowledge/` as an Obsidian vault, not as a pile of Markdown files.

## User Style Profile

| Preference | What It Means In Practice |
|---|---|
| Durable over chat-only | Produce reusable notes, CSVs, MOCs, templates, and SOPs instead of only answering in chat. |
| No fabricated data | Do not invent numbers, customers, prices, success rates, baseline results, or source claims. Mark unknowns as `待验证`. |
| Source-traceable | Important claims should point to `SRC-*`, raw files, URLs, page/table names, or dataset filenames. |
| China-first industry lens | Focus on China unless explicitly asked for a global-only view; use global cases to clarify China's position, gaps, dependencies, exports, or pressure. |
| Obsidian-first reading | Use wikilinks, aliases, headings, MOCs, callouts, and backlinks so notes are easy to navigate in Obsidian. |
| Clear link text | Prefer readable link text like `T265`, `LeRobot 初学者教学`, or `SRC-robotics-053`; avoid exposing long path-like labels in reading view. |
| Connected documents | After creating a note, link it from relevant MOCs, index pages, parent notes, and glossary entries. |
| Explicit completion status | For task lists, say what is done, what is template-only, what still needs real-world verification, and what the next action is. |
| Beginner-friendly when requested | Add teaching notes, diagrams, term explanations, examples, and "common misunderstandings" sections. |
| Structured but not bloated | Use tables where comparison matters, callouts for summaries/warnings, and short paragraphs for reasoning. |

## Standard Workflow

### 1. Understand The Request

Before editing:

- Identify the industry slug, usually from `knowledge/<industry>/`.
- Read the target note and nearby MOC/index files.
- Search existing notes and raw files with `rg` before creating new content.
- Use the project skill at `.agents/skills/industry-analysis/SKILL.md`.
- If editing Obsidian notes, follow Obsidian Markdown conventions.

### 2. Classify The Output

Choose the artifact type intentionally:

| Need | Preferred Artifact |
|---|---|
| Synthesis / main industry knowledge | `knowledge/<industry>/<number>-<topic>.md` |
| Intermediate deep dive | `knowledge/<industry>/research-notes/<slug>-YYYY-MM-DD.md` |
| Source capture / evidence | `raw/<industry>/documents/SRC-*.md` |
| Machine-readable comparison | `raw/<industry>/data/*.csv` |
| Reusable workflow | `docs/*_sop.md` or `tools/` script |
| Beginner explanation | Dedicated teaching note plus links from glossary/main note |

### 3. Preserve Source Discipline

Use this evidence hierarchy:

- **S**: official docs, filings, standards, papers, original statistics, source code docs.
- **A**: institutional reports, association reports, company white papers.
- **B**: reputable media, interviews, job postings, conference transcripts.
- **C**: social media, reposted charts, unsourced commentary.

Rules:

- Facts must cite evidence.
- Estimates must be labeled as estimates.
- Judgments must be separated from facts.
- Hypotheses must say what would validate or falsify them.
- Missing data should be written as `待验证`, with the next source or action to seek.

### 4. Write Obsidian-Friendly Notes

Each knowledge note should usually include:

```yaml
---
title: Note Title
date: YYYY-MM-DD
tags:
  - industry/<slug>
  - research-note
aliases:
  - Useful Alias
---
```

Recommended structure:

- `# Title`
- `> [!summary]` one-paragraph summary.
- `> [!tip]` or `> [!warning]` when reader guidance matters.
- Short sections with stable headings.
- Tables for comparisons, status, schema, company fields, or checklist items.
- `## 相关笔记` for backlinks.
- `## 来源` for raw artifacts and official links.

### 5. Link Like An Obsidian Reader

Use wikilinks for notes inside `knowledge/`:

```markdown
[[07-training-data]]
[[research-notes/lerobot-beginner-guide-2026-05-28|LeRobot 初学者教学]]
[[10-umi-technical-terms-for-beginners#T265|T265]]
```

Use Markdown links for raw artifacts or files outside the vault:

```markdown
[umi_zarr_lerobot_schema_crosswalk.csv](../../raw/robotics-embodied-ai/data/umi_zarr_lerobot_schema_crosswalk.csv)
[`SRC-robotics-053`](../../raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md)
```

> [!warning] Table Link Rule
> In Markdown tables, escape wikilink alias pipes as `\|`, otherwise the table splits columns.

Correct inside a table:

```markdown
| Sensor | Meaning |
|---|---|
| [[10-umi-technical-terms-for-beginners#T265\|T265]] | Tracking camera / pose source. |
```

Outside tables, normal alias syntax is fine:

```markdown
[[10-umi-technical-terms-for-beginners#T265|T265]]
```

### 6. Always Connect New Notes

When creating a new note, update the relevant links:

- Industry `00-index.md`.
- Parent topic note, such as `07-training-data.md` or `08-umi-gripper-research-and-business-plan.md`.
- Deep-dive summary note, such as `09-training-data-deep-dive.md`.
- `research-notes/README.md` if the new note lives under `research-notes/`.
- Glossary or beginner terms note if the note explains a recurring term.
- Related CSV/table references where appropriate.

### 7. Use Status Tables For Task Follow-Up

For "review next tasks" requests, prefer this shape:

| Task | Status | Output / Link | Still Needs Verification |
|---|---|---|---|
| Example task | 已完成 / 模板已完成 / 待继续 | Link to note or CSV | Real data, customer proof, license check, baseline result, etc. |

Status meanings:

- `已完成`: The research artifact is complete enough for current use.
- `模板已完成`: A reusable template exists, but no real pilot data exists yet.
- `待继续`: More evidence, scraping, validation, or field work is needed.
- `不应声称完成`: Avoid implying completion because required real-world evidence is missing.

### 8. Beginner Teaching Pattern

When asked to explain a technology, use this pattern:

- `## 一句话理解`
- `## 它解决什么问题`
- `## 它怎么工作`
- `## 和本项目/业务的关系`
- `## 初学者学习路径`
- `## 常见误解`
- `## 相关笔记`
- `## 来源`

Use examples and small diagrams, but avoid unsupported details. If a command/API may have changed, verify against official docs or local raw captures.

### 9. Tables And CSVs

Use CSVs when the information is likely to be filtered, compared, or reused:

- Company verification tables.
- Dataset schema comparison.
- Hardware BOM and localization fields.
- SOP/QC templates.
- Source capture manifests.

Keep CSVs machine-readable:

- Stable English column names.
- One concept per column.
- No decorative Markdown inside CSV unless unavoidable.
- Use `待验证` instead of blank when an unknown is semantically meaningful.

### 10. Verification Checklist Before Finishing

Before saying work is complete:

- Search for broken or ugly links.
- Check table wikilinks do not contain unescaped alias pipes.
- Confirm new notes are linked from relevant MOCs/indexes.
- Confirm raw evidence links point to existing files.
- Confirm no fabricated metrics or results were introduced.
- Run CSV parse checks when CSV files were edited.
- Check `git status --short` and avoid staging unrelated local files such as `.obsidian/` state unless explicitly requested.

Useful checks:

```bash
rg -n "new-note-slug|important-term" knowledge/<industry>
perl -ne 'if(/^\|/){ while(/\[\[([^\]]+)\]\]/g){ print "$ARGV:$.:$1\n" if $1 =~ /(?<!\\)\|/ } }' knowledge/<industry>/**/*.md
uv run python - <<'PY'
import csv
from pathlib import Path
for path in [Path("raw/<industry>/data/example.csv")]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(path, len(rows), "rows")
PY
```

## Default Deliverable Shape

For a completed research-writing task, the final response should include:

- What was created or changed.
- The most important links to local files.
- What was verified.
- What remains `待验证`.
- Any intentionally excluded files, especially local Obsidian state.

Keep the response short; the durable content should live in the repository.
