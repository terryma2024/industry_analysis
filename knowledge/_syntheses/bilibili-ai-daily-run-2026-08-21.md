---
title: Bilibili AI Daily Run 2026-08-21
type: synthesis
date_created: 2026-08-21
last_updated: 2026-08-21
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-08-21

## Run Summary

- Candidate videos: 20
- Selected for transcript extraction: 0
- Duplicate skipped: 18
- Needs model review: 2
- Processed: 0
- Failed: 0

## OpenCLI / Fetch Notes

- No fetch errors recorded.

## TOS Audio Check

- Check enabled: True
- Prefix: `asr-audio/2026/08/21`
- Objects found: 0

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
| skipped_duplicate | ROS2 运行在机器人的哪里？ | `BV1fTu96zENg` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 圆桌正当时：聊聊具身领域三大代表性数据集 | `BV1Di546YEfR` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【双语】李飞飞最新访谈：机器人学了十年还是笨？因为我们连"训练场"都没建好 | `BV1CU3B6VEc4` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 具身探索-CodeX控制ROS2机器人 | `BV1o5ud6kE7G` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 耗时两年半，我们做了一个让机器人“摸得到”的开源触觉系统 | `BV19kXHBmE5F` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【ICML 2025】🎓SAM2Act：视觉基础模型 × 记忆架构的机器人操作 | `BV1Cuuj6CE5b` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【arXiv 2026】🥇TurboVLA：<1 GB 显存、RTX 4090 上 32 Hz 实时运行的视觉-语言-动作模型 | `BV14FMk6QECv` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【青稞Talk 144期】从 端到端 VLA 到 Harness VLA：面向具身智能与机器人操作任务的记忆增强式执行框架 | `BV1HNu26ZEbe` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | EtherCAT通讯原理讲解 | `BV1uCJj62EQ4` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | B站强推！2025公认最通俗易懂的【 Isaac Lab】教程，全套付费课程（附资料）NVIDIA_Isaac_Lab | `BV1R3Yiz4E2s` | 0 | video identifier already appears in raw/ or knowledge/ |
| needs_model_review | 70分钟完整版！质疑苏度，理解苏度，成为苏度 | `BV1s43t6UEaW` | 0 | awaiting model relevance judgment; keyword score is diagnostic only |
| skipped_duplicate | 人形机器人研究方法及心得 2026.8 | `BV1DXG36SEN1` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | “偷师”人类数据，机器人在光模块工位干活了！ | `BV1iyNR68EMQ` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 2026智源大会丨清华于超主讲：具身智能为什么需要强化学习？面向具身智能的高灵活大规模强化学习框架RLinf！—具身智能机器人/PPO算法 | `BV1uwgf6VEeh` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 开源机器人与机械臂成套方案选型调研 | `BV1z33L6gE9y` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 对话DYNA机器人联创York Yang | `BV1DKMt6HEvk` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 人形机器人运控算法概览 | `BV17ooSB2E93` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【教程】具身智能实操，蚂蚁灵波VLA上手体验 | `BV1X45w6YENG` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | PI0.7再次引用MemoryVLA，聊一聊 VLA 中的“记忆" | `BV17doLBJEBt` | 0 | video identifier already appears in raw/ or knowledge/ |
| needs_model_review | 985哲学系，大厂离职，旅居20个国家后的人生感悟 | `BV1cvTq68E5g` | 0 | awaiting model relevance judgment; keyword score is diagnostic only |

## Processing Results

- No videos processed.

## Model Relevance Judgment

The two non-duplicate candidates were reviewed by model judgment rather than keyword filtering. Neither was selected for the second-stage pipeline:

| Video ID | Judgment | Basis | Action |
|---|---|---|
| `BV1s43t6UEaW` | 不相关 | 标题与语境显示为对“苏度”的通用讨论，未显示 AI、具身智能、机器人、智能体、模型、算力或相关产业链主题。 | 不下载、不转录、不创建 source card 或深研页。 |
| `BV1cvTq68E5g` | 不相关 | 个人离职、旅行与人生感悟内容，未显示本自动化的研究范围。 | 不下载、不转录、不创建 source card 或深研页。 |

因此，本日模型选中数为 0，实际深研数为 0；`Needs model review: 2` 保留为第一阶段脚本的候选状态计数。

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
