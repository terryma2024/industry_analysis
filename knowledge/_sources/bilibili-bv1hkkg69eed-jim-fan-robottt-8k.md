---
title: "李飞飞、Jim Fan新作！RoboTTT把上下文拉到8K，机器人终于不再转头就忘"
type: source
date_created: 2026-07-18
last_updated: 2026-07-18
source_urls:
  - https://www.bilibili.com/video/BV1HkKG69EeD
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-18-bilibili-bv1hkkg69eed-jim-fan-robottt-8k.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 李飞飞、Jim Fan新作！RoboTTT把上下文拉到8K，机器人终于不再转头就忘

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1HkKG69EeD |
| BV / video id | `BV1HkKG69EeD` |
| Author | 具身智能之心RoboTech |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-18-bilibili-bv1hkkg69eed-jim-fan-robottt-8k.json` |

## Transcript Excerpt

现在的机器人干一步忘一步，记忆不到0.1秒。英伟达刚发的 Robot TT 直接把记忆拉到5分钟，涨了1000倍。它怎么做到的？在模型里塞了一个小模型。每读一帧画面就更新一次自己的权重，历史全压进参数里，不占额外显存。所以他有了四个新本事。看一段演示视频，他照着做。注意，提示词全是同一句，Assemble circuit。 他得自己从视频里读出装哪个零件，什么顺序，光看一遍就会。中途被人碰了一下，他自己纠正回来。更狠的是边跑边学，人在旁边一纠正，他当场把错了怎么改塞进权重。这叫 Gagger 蒸馏，不用重训，越跑越强。对应的结果在这，一个10阶段要跑5分钟的装配任务，以前没有任何基线能完整跑完。 Robo TTT 从头到尾做下来了，Pop Go，Car Gear，Bot Circuit 三个任务平均完成分79%，比单步基线高87%。还有个反直觉的发现。上下文越长越强，从128帧到8000帧，性能一路往上走，完全没见顶。以前教机器人靠堆数据重训，现在给段视频、给句纠正，它就能现学。记忆一旦变长，机器人的本事自己就长出来了。

## Research Handoff

- 已完成单视频深研：[[../_syntheses/bilibili-robottt-long-context-robot-policy-deep-dive-2026-07-18|RoboTTT 长上下文机器人策略视频深度调研]]（R04 主分类，R07 次分类）。
- 核心机制与论文内指标已用 `SRC-robotics-307` 交叉核验；视频仍不是产品化、客户或现场可靠性的一级证据。

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
