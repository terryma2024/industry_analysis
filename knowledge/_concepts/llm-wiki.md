---
title: LLM Wiki
type: concept
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - knowledge-management
  - llm-wiki
sources:
  - _sources/karpathy-llm-wiki-pattern.md
---

# LLM Wiki

LLM Wiki 是一种用 LLM 维护个人/研究知识库的模式：原始来源不只在查询时被检索，而是在摄入阶段被编译成持久、结构化、互链的 Markdown wiki。

## 本仓库实现

- `raw/`: 不可变来源层。
- `knowledge/`: 编译输出层，也是 Obsidian vault。
- `AGENTS.md`: schema/治理层。
- `knowledge/index.md`: LLM 查询和维护优先读取的全局内容索引。
- `knowledge/log.md`: append-only 操作日志。

## 关联连接

- [[_sources/karpathy-llm-wiki-pattern|Karpathy LLM Wiki Pattern]]
- [[knowledge-compilation]]
- [[source-traceability]]
- [[_syntheses/karpathy-wiki-migration-plan|Karpathy Wiki Migration Plan]]
