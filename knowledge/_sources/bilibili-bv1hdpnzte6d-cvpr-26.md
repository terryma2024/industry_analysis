---
title: "CVPR'26 | 浙江大学×宇树科技：首个具身智能终身学习的全生命周期闭环框架"
type: source
date_created: 2026-07-12
last_updated: 2026-07-12
source_urls:
  - https://www.bilibili.com/video/BV1hDPNztE6d
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-12-bilibili-bv1hdpnzte6d-cvpr-26.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# CVPR'26 | 浙江大学×宇树科技：首个具身智能终身学习的全生命周期闭环框架

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1hDPNztE6d |
| BV / video id | `BV1hDPNztE6d` |
| Author | 深蓝学院 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-12-bilibili-bv1hdpnzte6d-cvpr-26.json` |

## Transcript Excerpt

告别数据饥渴与泛化焦虑，这个框架让机器人在实战中边干边学，开启具身终身学习时代。来自浙江大学、宇树科技等单位的研究团队认为。具身学习从根本上讲是一个生命周期问题，而非单一阶段的优化问题。那些如数据收集、仿真、学习或部署等仅优化单个环节的系统。难以实现持续改进或在狭窄场景之外进行泛化。对此，该团队提出了 RKDA，这是一个通过紧密耦合四个阶段来实现具身持续学习的闭环框架。一、自演化探索与具身 grounding 用于在物理环境中自主获取数据。二、生成式场景重建与增强，用于创建逼真且可扩展的场景。三、共享的具身表征架构，在单个多模态骨干网络中统一导航与操作任务。四。仿真源于现实的评估与进化，通过基于仿真的自适应来闭合反馈环路。这种耦合是不可分割的，移除任何一个阶段都会破坏改进循环，使其退化为一次性训练。而 K d a 在导航和操作基准测试上取得了持续的提升。并能鲁棒的迁移到物理机器人上。这表明一个紧密耦合的生命周期，包括持续的真实世界数据采集、生成式仿真更新和共享表征学习。能够支持终身改进和端到端泛化。最后，该团队开源了标准化接口，支持在可复用环境中进行可重复的评估和跨模型比较，从而使 RKDI 成为构建通用具身智能体的可扩展基础。

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-12-bilibili-bv1hdpnzte6d-cvpr-26.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
