---
title: Bilibili AI Daily Run 2026-07-18
type: synthesis
date_created: 2026-07-18
last_updated: 2026-07-18
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-07-18

## Run Summary

- Candidate videos: 20
- Duplicate skipped: 18
- Needs model review: 2
- Model selected: 2
- Processed source packets: 2
- Failed selected videos: 0

## Model Relevance Decisions

| Video ID | Title | Decision | Rationale |
|---|---|---|---|
| `BV1HkKG69EeD` | 李飞飞、Jim Fan新作！RoboTTT把上下文拉到8K，机器人终于不再转头就忘 | selected | 机器人策略长上下文、测试时训练与具身智能研究。 |
| `BV1JhNC6zE8X` | GPT 5.6 Sol 操控 Blender 有多强？社区案例、MCP 安装与真实实测 | selected | Agent 经 MCP/headless 工具调用 3D 软件，属于 AI 工具链与应用工程。 |

其余 18 条候选在抓取前已命中既有 BV/URL/source-card/raw 证据，因此未重复下载、ASR 或新建 source card。

## Processing Results

| Video ID | Status | Raw transcript | Source card |
|---|---|---|---|
| `BV1HkKG69EeD` | processed | [ASR JSON](../../raw/_inbox/transcripts/2026-07-18-bilibili-bv1hkkg69eed-jim-fan-robottt-8k.json) | [[_sources/bilibili-bv1hkkg69eed-jim-fan-robottt-8k\|RoboTTT source card]] |
| `BV1JhNC6zE8X` | processed | [ASR JSON](../../raw/_inbox/transcripts/2026-07-18-bilibili-bv1jhnc6ze8x-gpt-5-6-sol-blender-mcp.json) | [[_sources/bilibili-bv1jhnc6ze8x-gpt-5-6-sol-blender-mcp\|Blender MCP source card]] |

## TOS Audio Check And Retry Note

- Prefix: `asr-audio/2026/07/18`
- Objects found: 4
- Four objects exist for two successful source packets. A controlled retry was triggered while the wrapper had not yet surfaced the completed result, then failed at Volcengine query with transient TLS/remote-disconnect errors for both ASR models; exact object-to-attempt mapping was not independently inspected.
- The retry wrote no transcript or source card and does not change either video's `processed` result. No further retry was run. Retain the two surplus objects for storage-lifecycle inspection before deletion.

## Codex Synthesis Completed

| Video | Deep research | Classification | Primary-source boundary |
|---|---|---|---|
| `BV1HkKG69EeD` | [[bilibili-robottt-long-context-robot-policy-deep-dive-2026-07-18\|RoboTTT 长上下文机器人策略视频深度调研]] | R04; R07 | `SRC-robotics-307` verifies the preprint's 8K/fast-weight mechanism and reported task results, not production deployment. |
| `BV1JhNC6zE8X` | [[bilibili-codex-blender-mcp-toolchain-deep-dive-2026-07-18\|Codex 与 Blender MCP 工具链视频深度调研]] | R05; R07 | `SRC-ai-082` verifies BlenderMCP architecture, not the ASR model branding or video quality/cost claims. |

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
