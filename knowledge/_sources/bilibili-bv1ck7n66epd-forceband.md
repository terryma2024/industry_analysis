---
title: "低成本采集指尖力数据！亚马逊推出ForceBand，让机器人学会精准施力"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1CK7n66EpD
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1ck7n66epd-forceband.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 低成本采集指尖力数据！亚马逊推出ForceBand，让机器人学会精准施力

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1CK7n66EpD |
| BV / video id | `BV1CK7n66EpD` |
| Author | 具身智能之心RoboTech |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ck7n66epd-forceband.json` |

## Transcript Excerpt

人类演示数据是训练机器人操作策略具备规模化数据供给的有效途径。但目前主流的人类演示数据源，例如动作捕捉轨迹、网络视频。大多只能记录动作与外观信息，缺失对力敏感型操控至关重要的接触力数据。Force Band，一款低成本腕带式表面肌电采集设备。可将人体肌肉活动转化为带有力度信息的演示样本。首先构建一套时长10小时的多模态数据集，涵盖第一视角视频、表面肌电信号。惯性测量单元数据与指尖力测量值，包含各类操作动作与不同物体交互场景。基于该数据集，我们预训练 EMG Force 模型。仅依靠机电与惯性信号即可预测每根手指的受累变化。完成简短的用户专属校准后，使用者仅需佩戴 ForceBand 并搭配拍摄视频，就能采集目标任务的演示数据。 EMGR Force 会自动为这些演示数据标注主旨，受累曲线生成增广力度信息的演示样本，用于机器人策略训练。实验结果表明，相较于纯视觉基线方案。 Force Band 还原精细指尖交互时的力度预测误差降低50%以上。针对拾取、挤压、放置类任务，实现87%的任务成功率。

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ck7n66epd-forceband.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
