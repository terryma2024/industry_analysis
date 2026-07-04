---
title: Bilibili AI Daily Run 2026-07-04
type: synthesis
date_created: 2026-07-04
last_updated: 2026-07-04
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-07-04

## Run Summary

- Candidate videos: 20
- Selected for transcript extraction: 1
- Duplicate skipped: 19
- Needs model review: 0
- Processed: 1
- Failed: 0

## OpenCLI / Fetch Notes

- No fetch errors recorded.

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
| selected | 【此话当真】Agent 元年第 500 天：什么在消失，什么在诞生，为什么我们不该再投资 GUI 思维的软件？ | `BV1bKTk69EDD` | 2 | selected by model relevance judgment |
| skipped_duplicate | 机械臂一碰就穿模？北大英伟达 PhysisForcing 纠正视频生成物理盲区 | `BV12pTq6qECg` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 人形机器人究竟怎么进家庭？这是我听过最好的答案 | `BV1oPTq6SENP` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 智谱入局具身智能，26亿参数VLA模型ZR-0，用"思维链"打通跨实体迁移，单臂/双臂/人形一键通用 | `BV1orTv62E2j` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | VLA&世界模型数据基建：从原始传感器信号到可用训练资产 | `BV1ZFTq6pEA3` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 安了这5个skill，让Codex自动控制matlab | `BV1BBTv6UEaf` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（上） | `BV1wCTu6nEF2` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（下） | `BV1YwTg6TE1K` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 具身智能必备！TensorRT深度学习部署居然被计算机大佬用大白话讲明白了，比刷剧还爽！ | `BV1N8Kd6QEBE` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【机器人ROS2】1小时跟着大佬搞懂激光雷达工具和相机使用进阶，菜鸟学完即学即用！雷达过滤器/点云数据/雷达融合/具身智能机器人 | `BV1LfTF6EEsG` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 一口气看完，仙剑奇侠传全系列！横跨31年9部仙剑！爆肝9个月！ | `BV1aoLo6sEN2` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 世界模型入门：LeWorldModel算法讲解 -- github 4k star的JEPA框架世界动作模型，1GB显存可运行 | `BV19pT36rEsN` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 这条机械臂视频，是我今年见过最离谱的操作 | `BV18w7P6uEk1` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | RoboSimPro全新升级 \| 机器人+双轴变位机协同焊接离线仿真 | `BV1ogTT6PE2s` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 可可爱爱的包装再也不用舍不得扔了～ | `BV1PC786TEE5` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | A股机器人产业链，上中下游及其核心上市公司解读 | `BV1bGxEz7EWa` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 低成本采集指尖力数据！亚马逊推出ForceBand，让机器人学会精准施力 | `BV1CK7n66EpD` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 绝对是B站最好的具身智能VLA入门教程，对新手超级友好！仿真、隐式端到端VLA、RT-1、OpenVLA、UniPi—机械臂、具身智能机器人 | `BV1cL7p6VEH9` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能 | `BV1UR7H6dEy5` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 浙大高飞发起 \| 登顶《Science Robotics》封面背后的数学问题！ | `BV1v17Y6aE2L` | 0 | video identifier already appears in raw/ or knowledge/ |

## Processing Results

- `BV1bKTk69EDD` 【此话当真】Agent 元年第 500 天：什么在消失，什么在诞生，为什么我们不该再投资 GUI 思维的软件？: processed; transcript captured and source card written; raw=`raw/_inbox/transcripts/2026-07-04-bilibili-bv1bktk69edd-agent-500-gui.json`; source=`knowledge/_sources/bilibili-bv1bktk69edd-agent-500-gui.md`

## Codex Synthesis Outputs

- [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]] — single-video deep research page for `BV1bKTk69EDD`, cross-checked with MCP, Claude Code skills, and Vercel AI SDK official docs.

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
