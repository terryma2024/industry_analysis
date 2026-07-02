---
title: Bilibili AI Daily Run 2026-07-02
type: synthesis
date_created: 2026-07-02
last_updated: 2026-07-02
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-07-02

## Run Summary

- Candidate videos: 20
- First-phase duplicate skipped: 10
- Needs model review after first phase: 10
- Selected by Codex model judgment: 7
- Excluded by Codex model judgment: 3
- Duplicate skipped after partial processing: 13
- Newly processed with usable transcripts: 3
- Failed: 4

## Automation Notes

- First phase ran `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json`.
- Codex selected `BV1oPTq6SENP`, `BV1wCTu6nEF2`, `BV1bGxEz7EWa`, `BV1cL7p6VEH9`, `BV1UR7H6dEy5`, `BV1v17Y6aE2L`, and `BV161jy6MEwt`.
- Codex excluded `BV1aoLo6sEN2`, `BV1PC786TEE5`, and `BV1PCjA6bEi4` because the titles/metadata did not provide enough AI, robotics, embodied-intelligence, agent, infra, toolchain, chip, sensor, data, or software-stack relevance.
- The first selected batch used the default ASR timeout and was manually interrupted after two usable transcripts were written because the external ASR subprocess can wait up to 3600 seconds per video.
- A second selected batch with `--asr-timeout 300` wrote one additional usable transcript, then exited with `subprocess.TimeoutExpired` on `BV1UR7H6dEy5`.
- A final ASR-disabled run (`VOLCENGINE_ASR_COMMAND=`) produced structured failure records for four remaining selected videos without retrying long ASR.

## OpenCLI / Fetch Notes

- No fetch errors recorded.

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
| skipped_duplicate | 人形机器人究竟怎么进家庭？这是我听过最好的答案 | `BV1oPTq6SENP` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 智谱入局具身智能，26亿参数VLA模型ZR-0，用"思维链"打通跨实体迁移，单臂/双臂/人形一键通用 | `BV1orTv62E2j` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | VLA&世界模型数据基建：从原始传感器信号到可用训练资产 | `BV1ZFTq6pEA3` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 安了这5个skill，让Codex自动控制matlab | `BV1BBTv6UEaf` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（上） | `BV1wCTu6nEF2` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（下） | `BV1YwTg6TE1K` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 具身智能必备！TensorRT深度学习部署居然被计算机大佬用大白话讲明白了，比刷剧还爽！ | `BV1N8Kd6QEBE` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 【机器人ROS2】1小时跟着大佬搞懂激光雷达工具和相机使用进阶，菜鸟学完即学即用！雷达过滤器/点云数据/雷达融合/具身智能机器人 | `BV1LfTF6EEsG` | 0 | video identifier already appears in raw/ or knowledge/ |
| needs_model_review | 一口气看完，仙剑奇侠传全系列！横跨31年9部仙剑！爆肝9个月！ | `BV1aoLo6sEN2` | 0 | awaiting model relevance judgment; keyword score is diagnostic only |
| skipped_duplicate | 世界模型入门：LeWorldModel算法讲解 -- github 4k star的JEPA框架世界动作模型，1GB显存可运行 | `BV19pT36rEsN` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 这条机械臂视频，是我今年见过最离谱的操作 | `BV18w7P6uEk1` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | RoboSimPro全新升级 \| 机器人+双轴变位机协同焊接离线仿真 | `BV1ogTT6PE2s` | 0 | video identifier already appears in raw/ or knowledge/ |
| needs_model_review | 可可爱爱的包装再也不用舍不得扔了～ | `BV1PC786TEE5` | 0 | awaiting model relevance judgment; keyword score is diagnostic only |
| selected | A股机器人产业链，上中下游及其核心上市公司解读 | `BV1bGxEz7EWa` | 2 | selected by model relevance judgment |
| skipped_duplicate | 低成本采集指尖力数据！亚马逊推出ForceBand，让机器人学会精准施力 | `BV1CK7n66EpD` | 0 | video identifier already appears in raw/ or knowledge/ |
| skipped_duplicate | 绝对是B站最好的具身智能VLA入门教程，对新手超级友好！仿真、隐式端到端VLA、RT-1、OpenVLA、UniPi—机械臂、具身智能机器人 | `BV1cL7p6VEH9` | 0 | video identifier already appears in raw/ or knowledge/ |
| selected | 【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能 | `BV1UR7H6dEy5` | 8 | selected by model relevance judgment |
| selected | 浙大高飞发起 \| 登顶《Science Robotics》封面背后的数学问题！ | `BV1v17Y6aE2L` | 2 | selected by model relevance judgment |
| needs_model_review | 还写什么单片机代码啊？直接微信聊天就行！ | `BV1PCjA6bEi4` | 0 | awaiting model relevance judgment; keyword score is diagnostic only |
| selected | Ego、UMI具身智能数据从何而来？如何数据采集？数采技术演变与优劣势 | `BV161jy6MEwt` | 4 | selected by model relevance judgment |

## Processing Results

### Successful Text Packets

- `BV1oPTq6SENP` 人形机器人究竟怎么进家庭？这是我听过最好的答案: processed in interrupted selected batch; raw=`raw/_inbox/transcripts/2026-07-02-bilibili-bv1optq6senp-bilibili-video.json`; source=`knowledge/_sources/bilibili-bv1optq6senp-bilibili-video.md`; transcript chars: 5140.
- `BV1wCTu6nEF2` 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（上）: processed in short-timeout selected batch; raw=`raw/_inbox/transcripts/2026-07-02-bilibili-bv1wctu6nef2-genie-sim-3-0-vla.json`; source=`knowledge/_sources/bilibili-bv1wctu6nef2-genie-sim-3-0-vla.md`; transcript chars: 1716.
- `BV1cL7p6VEH9` 绝对是B站最好的具身智能VLA入门教程，对新手超级友好！仿真、隐式端到端VLA、RT-1、OpenVLA、UniPi—机械臂、具身智能机器人: processed in interrupted selected batch; raw=`raw/_inbox/transcripts/2026-07-02-bilibili-bv1cl7p6veh9-b-vla-vla-rt-1-openvla-unipi.json`; source=`knowledge/_sources/bilibili-bv1cl7p6veh9-b-vla-vla-rt-1-openvla-unipi.md`; transcript chars: 20944.

### Failed Text Packets

- `BV1bGxEz7EWa` A股机器人产业链，上中下游及其核心上市公司解读: failed; subtitle extraction failed: [INFO] Extracting subtitles for: https://www.bilibili.com/video/BV1bGxEz7EWa
[INFO] Detected platform: bilibili
[INFO] Bilibili video: A股机器人产业链，上中下游及其核心上市公司解读 (aid=115327941746166, cid=32883475125)
[INFO] Trying player v2 API with WBI signing...
[INFO] Trying B站 AI conclusion API...
[INFO] Trying yt-dlp subtitle extraction for bilibili...; ASR failed: VOLCENGINE_ASR_COMMAND is not configured; loaded credentials: VOLCENGINE_APP_ID, VOLCENGINE_ACCESS_TOKEN, VOLCENGINE_SECRET_KEY; raw=`-`; source=`-`
- `BV1UR7H6dEy5` 【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能: failed; subtitle extraction failed: [INFO] Extracting subtitles for: https://www.bilibili.com/video/BV1UR7H6dEy5
[INFO] Detected platform: bilibili
[INFO] Bilibili video: 【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能 (aid=116821600502995, cid=39453132546)
[INFO] Trying player v2 API with WBI signing...
[INFO] Trying B站 AI conclusion API...
[INFO] Trying yt-dlp subtitle extraction for bilibili...; ASR failed: VOLCENGINE_ASR_COMMAND is not configured; loaded credentials: VOLCENGINE_APP_ID, VOLCENGINE_ACCESS_TOKEN, VOLCENGINE_SECRET_KEY; raw=`-`; source=`-`
- `BV1v17Y6aE2L` 浙大高飞发起 | 登顶《Science Robotics》封面背后的数学问题！: failed; subtitle extraction failed: [INFO] Extracting subtitles for: https://www.bilibili.com/video/BV1v17Y6aE2L
[INFO] Detected platform: bilibili
[INFO] Bilibili video: 浙大高飞发起 | 登顶《Science Robotics》封面背后的数学问题！ (aid=116810460434618, cid=39414007960)
[INFO] Trying player v2 API with WBI signing...
[INFO] Trying B站 AI conclusion API...
[INFO] Trying yt-dlp subtitle extraction for bilibili...; ASR failed: VOLCENGINE_ASR_COMMAND is not configured; loaded credentials: VOLCENGINE_APP_ID, VOLCENGINE_ACCESS_TOKEN, VOLCENGINE_SECRET_KEY; raw=`-`; source=`-`
- `BV161jy6MEwt` Ego、UMI具身智能数据从何而来？如何数据采集？数采技术演变与优劣势: failed; subtitle extraction failed: [INFO] Extracting subtitles for: https://www.bilibili.com/video/BV161jy6MEwt
[INFO] Detected platform: bilibili
[INFO] Bilibili video: Ego、UMI具身智能数据从何而来？如何数据采集？数采技术演变与优劣势 (aid=116798297018032, cid=39344278867)
[INFO] Trying player v2 API with WBI signing...
[INFO] Trying B站 AI conclusion API...
[INFO] Trying yt-dlp subtitle extraction for bilibili...; ASR failed: VOLCENGINE_ASR_COMMAND is not configured; loaded credentials: VOLCENGINE_APP_ID, VOLCENGINE_ACCESS_TOKEN, VOLCENGINE_SECRET_KEY; raw=`-`; source=`-`

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Durable Research Output

- Updated synthesis: [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- Added source cards under `knowledge/_sources/` for `BV1oPTq6SENP`, `BV1wCTu6nEF2`, and `BV1cL7p6VEH9`.
- Added raw transcript JSON under `raw/_inbox/transcripts/` for the same three videos.
- Updated [[robotics-embodied-ai/sources|机器人来源表]], [[index|Knowledge Index]], and [[log|Wiki Log]].

## Important Insights

- Consumer home humanoids may need to start from single-point family needs, safety, small form factor, and fast PMF testing rather than full household AGI.
- VLA simulation platform evaluation should focus on interfaces, record/replay, geometry/physics validation, and failed-scene feedback loops.
- VLA tutorials are useful as learning-path scaffolding, but RT-1, OpenVLA, UniPi, and related model claims still need primary source cards.

## Manual Follow-up

- Fix `tools/bilibili_ai_daily_research.py` so external ASR `TimeoutExpired` becomes a per-video `failed` result instead of aborting the entire batch.
- Retry `BV1bGxEz7EWa`, `BV1UR7H6dEy5`, `BV1v17Y6aE2L`, and `BV161jy6MEwt` only after ASR timeout handling is fixed or a reliable subtitle/ASR path is available.
- Verify 乐享科技/家庭机器人、GENIE SIM 3.0、PaI0/OpenPI, and VLA model/paper claims against official sources before promoting them into industry facts.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
- [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]
