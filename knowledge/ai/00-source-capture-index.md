---
title: AI Source Capture Index
type: index
date_created: 2026-06-02
last_updated: 2026-06-02
status: active
tags:
  - industry/ai
  - source-capture
sources:
  - ai/sources.csv
  - raw/ai/documents/source_capture_manifest.csv
---

# AI Source Capture Index

> [!summary]
> 本页登记 `knowledge/ai/sources.csv` 中网页来源的离线抓取状态。2026-06-02 已运行 `tools/extract_sources_with_defuddle.py --industry ai --timeout 60`：16 条 `ok`，7 条 `fallback_html`，1 条 `failed`。

## 状态说明

- `ok`: defuddle 抽取到可读 Markdown。
- `fallback_html`: defuddle 失败或内容过短，但已保留原始 HTML 或 sidecar Markdown。
- `failed`: 未能抓取，需后续用浏览器、替代来源、官方 PDF 或手工摘录补证。

## Source Capture Manifest

| Source ID | Title | Status | Raw artifact | Follow-up |
|---|---|---|---|---|
| SRC-ai-001 | Scale YC company post | fallback_html | [raw](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) | 检查 fallback HTML 是否足够；必要时手工浏览器捕获。 |
| SRC-ai-002 | Scale announces Series B funding | ok | [raw](../../raw/ai/documents/SRC-ai-002-scale-announces-series-b-funding.md) | 无。 |
| SRC-ai-003 | Scale AI Series C | fallback_html | [raw](../../raw/ai/documents/SRC-ai-003-scale-ai-series-c.md) | Scale 官网超时，必要时重跑或手工捕获。 |
| SRC-ai-004 | Scale AI breaking even after it scaled back hiring | ok | [raw](../../raw/ai/documents/SRC-ai-004-scale-ai-breaking-even-after-it-scaled-back-hiring.md) | 无。 |
| SRC-ai-005 | Scale AI scores 325 million to grow AI solution | ok | [raw](../../raw/ai/documents/SRC-ai-005-scale-ai-scores-325-million-to-grow-ai-solution.md) | 无。 |
| SRC-ai-006 | Scale AI awarded 250M AI contract by Department of Defense | ok | [raw](../../raw/ai/documents/SRC-ai-006-scale-ai-awarded-250m-ai-contract-by-department-of-defense.md) | 无。 |
| SRC-ai-007 | Scale AI Series F | ok | [raw](../../raw/ai/documents/SRC-ai-007-scale-ai-series-f.md) | 无。 |
| SRC-ai-008 | Scale AI announces next phase of company evolution | ok | [raw](../../raw/ai/documents/SRC-ai-008-scale-ai-announces-next-phase-of-company-evolution.md) | 无。 |
| SRC-ai-009 | Customer trust and Scale Meta deal | ok | [raw](../../raw/ai/documents/SRC-ai-009-customer-trust-and-scale-meta-deal.md) | 无。 |
| SRC-ai-010 | Scale AI not winding down following Meta deal interim CEO says | fallback_html | [raw](../../raw/ai/documents/SRC-ai-010-scale-ai-not-winding-down-following-meta-deal-interim-ceo-says.md) | CNBC fetch failed，必要时用浏览器或替代来源核验。 |
| SRC-ai-011 | Meta restructures its AI unit under Superintelligence Labs | ok | [raw](../../raw/ai/documents/SRC-ai-011-meta-restructures-its-ai-unit-under-superintelligence-labs.md) | 无。 |
| SRC-ai-012 | Meta Scale AI deal analysis | failed | manifest only | Axios 403，需浏览器/manual capture 或替代来源。 |
| SRC-ai-013 | 海天瑞声官网 | ok | [raw](../../raw/ai/documents/SRC-ai-013-source.md) | 无。 |
| SRC-ai-014 | 数据堂官网 | ok | [raw](../../raw/ai/documents/SRC-ai-014-source.md) | 无。 |
| SRC-ai-015 | 数据堂关于我们 | ok | [raw](../../raw/ai/documents/SRC-ai-015-source.md) | 无。 |
| SRC-ai-016 | Testin 云测官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-016-testin.md) | 页面超时，必要时浏览器捕获。 |
| SRC-ai-017 | 标贝科技数据服务 | ok | [raw](../../raw/ai/documents/SRC-ai-017-source.md) | 无。 |
| SRC-ai-018 | 曼孚科技官网 | ok | [raw](../../raw/ai/documents/SRC-ai-018-source.md) | 无。 |
| SRC-ai-019 | 龙猫数据关于我们 | ok | [raw](../../raw/ai/documents/SRC-ai-019-source.md) | 无。 |
| SRC-ai-020 | 龙猫数据 AutopilotGPT | ok | [raw](../../raw/ai/documents/SRC-ai-020-autopilotgpt.md) | 无。 |
| SRC-ai-021 | GOMAX LAB 官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-021-gomax-lab.md) | defuddle 未抽到内容，必要时手工核验。 |
| SRC-ai-022 | Xpert Studio 官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-022-xpert-studio.md) | defuddle 未抽到内容，必要时手工核验。 |
| SRC-ai-023 | Stardust AI smart education scenario | ok | [raw](../../raw/ai/documents/SRC-ai-023-stardust-ai-smart-education-scenario.md) | 无。 |
| SRC-ai-024 | 天衍奇点官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-024-source.md) | 页面超时，必要时浏览器捕获。 |

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[sources.csv|AI sources.csv]]
- [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]
