---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-06-02
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

## [2026-06-02] ingest | Scale AI 与中国 AI 数据基础设施对标

- **变更**: 新增 [[ai/research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]、[[ai/research-notes/README|AI Research Notes]] 和 [[ai/00-source-capture-index|AI Source Capture Index]]；更新 [[ai/00-index|AI 相关 - 研究入口]]、[[ai/04-companies|AI 相关 - 公司与竞争]]、[[index|Knowledge Index]]。
- **来源**: 在 `knowledge/ai/sources.csv` 登记 Scale AI、Meta 交易、海天瑞声、数据堂、云测数据、标贝科技、曼孚科技、龙猫数据、GOMAX、Xpert、星尘数据、天衍奇点等公开来源，并运行 `tools/extract_sources_with_defuddle.py --industry ai --timeout 60` 抽取到 `raw/ai/documents/`。
- **待继续**: `SRC-ai-012` Axios 来源因 403 抓取失败；`SRC-ai-001`、`SRC-ai-003`、`SRC-ai-010`、`SRC-ai-016`、`SRC-ai-021`、`SRC-ai-022`、`SRC-ai-024` 为 fallback HTML，正式投资 memo 前应手工核验。

## [2026-06-02] ingest | Scale AI 公司发展史入库

- **变更**: 新增 [[ai/research-notes/scale-ai-company-history-2026-06-02|Scale AI 公司发展史]] 和 [[_entities/ScaleAI|Scale AI]] 实体卡；更新 [[ai/research-notes/README|AI Research Notes]]、[[ai/00-index|AI 相关 - 研究入口]]、[[index|Knowledge Index]]。
- **来源**: 复用 `knowledge/ai/sources.csv` 中 `SRC-ai-001` 至 `SRC-ai-012` 和 `raw/ai/documents/` 来源抽取结果。
- **待继续**: 正式投资 memo 前仍需对 `SRC-ai-012` Axios 403 失败项和部分 fallback HTML 来源做人工核验。
