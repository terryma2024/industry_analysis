---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - wiki
  - log
  - llm-wiki
---

# Wiki Log

本文件为 append-only 操作日志。每条记录使用 `## [YYYY-MM-DD] action | summary`，便于 `rg "^## \\[" knowledge/log.md` 快速检索。

## [2026-05-29] migration | 初始化 Karpathy LLM Wiki 结构

- **变更**: 新增 [[index]]、[[log]]、`_sources/`、`_entities/`、`_concepts/`、`_claims/`、`_syntheses/`，并保留现有行业目录作为 Industries/Syntheses 层；更新 `AGENTS.md` 和 `.agents/skills/industry-analysis/SKILL.md` 以固化新工作流。
- **登记**: 首批登记行业入口、新闻摘要、机器人训练数据深度调研、UMI 研究、LeRobot/UMI/具身智能相关概念和实体；为 10 个行业 `00-index.md` 增加 wiki frontmatter 和 `## 关联连接`。
- **冲突**: 无。当前迁移不重命名既有行业笔记，避免破坏已存在 wikilinks。
