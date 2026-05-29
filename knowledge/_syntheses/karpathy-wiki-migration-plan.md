---
title: Karpathy Wiki Migration Plan
type: synthesis
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - llm-wiki
  - migration
  - obsidian
sources:
  - _sources/karpathy-llm-wiki-pattern.md
---

# Karpathy Wiki Migration Plan

> [!summary]
> 本仓库采用“保留行业研究工作台 + 新增全局 LLM Wiki 编译层”的迁移路线。`raw/` 继续作为不可变来源层；`knowledge/` 继续作为 Obsidian vault，同时升级为 LLM 维护的编译层；`AGENTS.md` 作为 schema 管理 ingest/query/lint 工作流。

## 迁移原则

- 不把 `knowledge/` 改名为 `wiki/`，因为现有 Obsidian vault 和行业目录已经围绕 `knowledge/` 建立。
- 不一次性重命名既有行业笔记，避免破坏已有 wikilinks。
- 新增全局 `_sources/`、`_entities/`、`_concepts/`、`_claims/`、`_syntheses/`，用于跨行业沉淀。
- 行业目录继续承接中国十五五战略产业研究，作为 industry/synthesis 层。
- 新增 `knowledge/index.md` 和 `knowledge/log.md`，让 LLM 在 query 和维护时有稳定入口。

## 目标结构

```text
raw/
  _inbox/
  _archive/
  <industry>/
    documents/
    data/

knowledge/
  README.md
  index.md
  log.md
  _sources/
  _entities/
  _concepts/
  _claims/
  _syntheses/
  news/
  <industry>/
```

## 迁移状态

- 已完成：全局目录、首批索引、日志、LLM Wiki 概念、机器人训练数据概念、LeRobot/UMI/IO-AI 等实体和概念节点。
- 待推进：从 `knowledge/robotics-embodied-ai/sources.csv` 批量生成 `_sources/` source summary，抽取第一批 `_claims/`。
- 待推进：对所有行业 `00-index.md` 增加统一 frontmatter 和 `## 关联连接`。

## 关联连接

- [[_concepts/llm-wiki|LLM Wiki]]
- [[_concepts/knowledge-compilation|Knowledge Compilation]]
- [[_concepts/source-traceability|Source Traceability]]
- [[index|Knowledge Index]]
- [[log|Wiki Log]]
