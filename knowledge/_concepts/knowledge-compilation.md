---
title: Knowledge Compilation
type: concept
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - knowledge-management
  - llm-wiki
sources:
  - _sources/karpathy-llm-wiki-pattern.md
---

# Knowledge Compilation

Knowledge Compilation 指在来源进入知识库时就完成摘要、实体/概念抽取、冲突检查、双向链接和索引登记，而不是每次回答问题时重新从原文碎片里临时拼装答案。

## 本仓库规则

- 每次重要 ingest 需要生成或更新 `_sources/`、`_entities/`、`_concepts/`、`_syntheses/` 或行业页面。
- 高价值 query 输出应询问是否固化为 `_syntheses/`。
- 重要判断应能通过 `sources:`、正文证据链接或 `sources.csv` 回到原始来源。

## 关联连接

- [[llm-wiki]]
- [[source-traceability]]
- [[index|Knowledge Index]]
- [[log|Wiki Log]]
