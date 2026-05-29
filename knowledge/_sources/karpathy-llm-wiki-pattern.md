---
title: Karpathy LLM Wiki Pattern
type: source
date_created: 2026-05-29
last_updated: 2026-05-29
source_urls:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://jasonai.me/blog/claude-code-obsidian--karpathyllm-wiki/
evidence_grade: B
tags:
  - llm-wiki
  - knowledge-management
  - obsidian
sources:
  - web/karpathy-llm-wiki-gist
  - web/jason-claude-code-obsidian-karpathy-wiki
---

# Karpathy LLM Wiki Pattern

> [!summary]
> Karpathy 的 LLM Wiki 模式主张把个人/研究知识库从查询时 RAG 转向摄入时编译：LLM 读取原始来源，维护一个持久、结构化、相互链接的 Markdown wiki。Jason 的文章把这个理念实践化为 `raw/`、`wiki/`、`CLAUDE.md/AGENTS.md` 三层架构，以及 ingest/query/lint 三个循环。

## 核心信息

- `raw/` 是不可变来源层，LLM 只读，不改写事实源。
- `wiki/` 或本仓库的 `knowledge/` 是编译输出层，LLM 负责创建、更新、链接和维护一致性。
- `AGENTS.md` 是治理层，定义命名、frontmatter、索引、日志、冲突处理和工作流。
- `index.md` 是内容目录，LLM 查询时应先读它；`log.md` 是 append-only 时间线，记录 ingest/query/lint。
- 好的回答不应消失在聊天记录里，应回填为 synthesis、comparison、canvas、slide 或其他 durable artifact。
- 风险在于幻觉会被固化，因此必须强调来源追踪、冲突标注、人工复核和定期 lint。

## 对本仓库的迁移含义

- 保留 `raw/<industry>/documents/` 和 `raw/<industry>/data/`，并新增 `raw/_inbox/` 承接未归类来源。
- 保留 `knowledge/<industry>/` 行业工作台，并新增 `_sources/`、`_entities/`、`_concepts/`、`_claims/`、`_syntheses/` 作为跨行业编译层。
- 所有重要新增页面必须更新 [[index|Knowledge Index]] 和 [[log|Wiki Log]]。

## 关联连接

- [[_concepts/llm-wiki|LLM Wiki]]
- [[_concepts/knowledge-compilation|Knowledge Compilation]]
- [[_concepts/source-traceability|Source Traceability]]
- [[_entities/AndrejKarpathy|Andrej Karpathy]]
- [[_syntheses/karpathy-wiki-migration-plan|Karpathy Wiki Migration Plan]]
