---
title: Bilibili AI Daily Run 2026-07-02
type: synthesis
date_created: 2026-07-02
last_updated: 2026-07-02
sources:
  - raw/_inbox/transcripts/
  - knowledge/_sources/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-07-02

## Run Summary

| Metric | Count | Notes |
|---|---:|---|
| Candidate videos | 20 | From default Bilibili favorites via `tools/bilibili_ai_daily_research.py --limit 20 --json`. |
| Duplicate skipped | 1 | `BV1BBTv6UEaf` already existed in raw/knowledge and was not reprocessed. |
| Model selected for extraction | 17 | Excluded 2 clearly unrelated videos: Xianjian game recap and packaging content. |
| Selected but no final script result | 17 | Batch was interrupted after a long ASR wait, so the script did not emit final `results` JSON. |
| New source artifacts written before interrupt | 9 | Source card + raw transcript JSON existed for 9 selected videos. |
| Usable transcript texts | 8 | `BV1ogTT6PE2s` only contained `35828`, so it was not used for synthesis. |
| Durable synthesis pages updated/created | 1 | [[_syntheses/bilibili-embodied-ai-signals-2026-07-02]]. |

## Model Selection

Selected as AI / embodied-intelligence related:

| Video ID | Title | Rationale |
|---|---|---|
| `BV1orTv62E2j` | 智谱入局具身智能，26亿参数VLA模型ZR-0，用"思维链"打通跨实体迁移，单臂/双臂/人形一键通用 | VLA, embodied AI, cross-embodiment transfer. |
| `BV1ZFTq6pEA3` | VLA&世界模型数据基建：从原始传感器信号到可用训练资产 | Robot data infrastructure, VLA/world-model data pipeline. |
| `BV1wCTu6nEF2` | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（上） | Robot simulation and VLA workflow. |
| `BV1YwTg6TE1K` | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（下） | Robot simulation and VLA workflow. |
| `BV1N8Kd6QEBE` | 具身智能必备！TensorRT深度学习部署居然被计算机大佬用大白话讲明白了，比刷剧还爽！ | AI inference deployment / edge AI infra. |
| `BV1LfTF6EEsG` | 【机器人ROS2】1小时跟着大佬搞懂激光雷达工具和相机使用进阶 | ROS2, LiDAR, point-cloud robotics stack. |
| `BV19pT36rEsN` | 世界模型入门：LeWorldModel算法讲解 -- github 4k star的JEPA框架世界动作模型，1GB显存可运行 | World model, JEPA, robot control. |
| `BV18w7P6uEk1` | 这条机械臂视频，是我今年见过最离谱的操作 | Industrial robot safety and deployment constraints. |
| `BV1ogTT6PE2s` | RoboSimPro全新升级 \| 机器人+双轴变位机协同焊接离线仿真 | Industrial robot simulation/offline programming. |
| `BV1bGxEz7EWa` | A股机器人产业链，上中下游及其核心上市公司解读 | Robot industry chain / investment lead. |
| `BV1CK7n66EpD` | 低成本采集指尖力数据！亚马逊推出ForceBand，让机器人学会精准施力 | Force/tactile robot demonstration data. |
| `BV1cL7p6VEH9` | 绝对是B站最好的具身智能VLA入门教程 | VLA educational material. |
| `BV1UR7H6dEy5` | 【2026最新机器人视觉SLAM】保姆级全套课程 | Robot SLAM and embodied AI engineering basics. |
| `BV1v17Y6aE2L` | 浙大高飞发起 \| 登顶《Science Robotics》封面背后的数学问题！ | Robotics research / Science Robotics lead. |
| `BV1PCjA6bEi4` | 还写什么单片机代码啊？直接微信聊天就行！ | Possible embedded AI / natural-language hardware control lead. |
| `BV161jy6MEwt` | Ego、UMI具身智能数据从何而来？如何数据采集？数采技术演变与优劣势 | UMI / embodied data collection. |
| `BV1PCjx6oEeJ` | Agent版Next.js来了？文件系统即Agent！拆解 eve | Software agent / AI toolchain lead. |

Excluded:

| Video ID | Title | Reason |
|---|---|---|
| `BV1aoLo6sEN2` | 一口气看完，仙剑奇侠传全系列！横跨31年9部仙剑！ | Game/media recap, not AI/robotics research. |
| `BV1PC786TEE5` | 可可爱爱的包装再也不用舍不得扔了～ | Packaging/lifestyle content, not AI/robotics research. |

Duplicate:

| Video ID | Title | Existing artifact |
|---|---|---|
| `BV1BBTv6UEaf` | 安了这5个skill，让Codex自动控制matlab | [[_sources/bilibili-bv1bbtv6ueaf-5-skill-codex-matlab]] and [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02]]. |

## Source Artifacts

| Status | Video ID | Source card | Raw transcript | Notes |
|---|---|---|---|---|
| usable | `BV1orTv62E2j` | [[_sources/bilibili-bv1ortv62e2j-26-vla-zr-0]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ortv62e2j-26-vla-zr-0.json` | Used in synthesis as B-grade ZR-0/VLA lead. |
| usable | `BV1ZFTq6pEA3` | [[_sources/bilibili-bv1zftq6pea3-vla]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json` | Used in synthesis for robot data pipeline SOP. |
| usable | `BV1YwTg6TE1K` | [[_sources/bilibili-bv1ywtg6te1k-genie-sim-3-0-vla]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ywtg6te1k-genie-sim-3-0-vla.json` | Used in synthesis for GENIE SIM limitations. |
| usable | `BV1N8Kd6QEBE` | [[_sources/bilibili-bv1n8kd6qebe-tensorrt]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1n8kd6qebe-tensorrt.json` | Used in synthesis for AI inference deployment learning path. |
| usable | `BV1LfTF6EEsG` | [[_sources/bilibili-bv1lftf6eesg-ros2-1]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1lftf6eesg-ros2-1.json` | Used in synthesis for ROS2/LiDAR tooling. |
| usable | `BV19pT36rEsN` | [[_sources/bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb.json` | Used in synthesis and cross-referenced to `SRC-ai-032`. |
| usable | `BV18w7P6uEk1` | [[_sources/bilibili-bv18w7p6uek1-bilibili-video]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv18w7p6uek1-bilibili-video.json` | Used in synthesis as industrial robot safety lead. |
| usable | `BV1CK7n66EpD` | [[_sources/bilibili-bv1ck7n66epd-forceband]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ck7n66epd-forceband.json` | Used in synthesis as ForceBand lead. |
| unusable transcript | `BV1ogTT6PE2s` | [[_sources/bilibili-bv1ogtt6pe2s-robosimpro]] | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ogtt6pe2s-robosimpro.json` | Transcript text was only `35828`; not used for synthesis. |

## Failure / Interruption Notes

- The second-stage command was interrupted with exit code `130` after a long wait inside external Volcengine ASR for `BV1cL7p6VEH9`.
- Because the batch was interrupted, the script did not write a final `results` array into stdout or refresh this report automatically.
- No transcript content was fabricated. Only source cards and raw transcripts already present on disk were used.
- Videos after the interrupted item, and selected videos that produced no durable artifact before interruption, need a later targeted retry with a smaller selected list or an ASR timeout policy.

## Durable Research Output

- New synthesis: [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- Updated source registries:
  - [[robotics-embodied-ai/sources|机器人来源表]]
  - [[ai/sources|AI 来源表]]
- Updated global index: [[index|Knowledge Index]].
- Updated append-only log: [[log|Wiki Log]].

## Important Insights

- Robot training data should be treated as synchronized `observation + action + language + quality + metadata` episode assets, not videos.
- VLA cross-embodiment work should be tracked for semantic/task representation alignment, but ZR-0 claims need primary-source verification.
- Latent world models / JEPA remain relevant to robot control because low-latency state prediction may matter more than pixel generation.
- Real-video-to-simulation workflows depend heavily on sensor quality, scene closure, segmentation, mesh cleanup and asset packaging.
- Force/tactile augmentation of demonstration data is a high-value lead, especially for fine manipulation.
- ROS2/LiDAR, TensorRT and industrial safety constraints remain practical career and deployment foundations.

## Manual Follow-up

- Retry `BV1cL7p6VEH9`, `BV1UR7H6dEy5`, `BV161jy6MEwt`, `BV1PCjx6oEeJ`, and any other selected item without artifact using smaller batches.
- Add an ASR timeout or per-video retry strategy if the daily task keeps blocking on long videos.
- Verify ZR-0, ForceBand, GENIE SIM, LeWorldModel and industrial robot safety claims against primary sources before promoting them into industry facts.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
- [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]
