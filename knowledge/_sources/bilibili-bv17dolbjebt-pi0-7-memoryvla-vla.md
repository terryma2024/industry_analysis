---
title: "PI0.7再次引用MemoryVLA，聊一聊 VLA 中的“记忆'"
type: source
date_created: 2026-07-24
last_updated: 2026-07-24
source_urls:
  - https://www.bilibili.com/video/BV17doLBJEBt
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-24-bilibili-bv17dolbjebt-pi0-7-memoryvla-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# PI0.7再次引用MemoryVLA，聊一聊 VLA 中的“记忆"

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV17doLBJEBt |
| BV / video id | `BV17doLBJEBt` |
| Author | Dexmal原力灵机 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-24-bilibili-bv17dolbjebt-pi0-7-memoryvla-vla.json` |

## Transcript Excerpt

啊，那时间差不多，然后我们就开始吧。大家好，我是清华大学的石浩，然后是在云粒灵机，Daximo 实习。然后我今天给大家汇报一下这个。rethinking memory，voa。就是，some insight about memory modeling in voa。然后这个主页的几个二维码呢，是我们这个论文的这个项目主页，还有 paper 和 code 的网站，还有我个人的微信。然后首先做一下自我介绍吧。然后我叫石浩，然后现在是在清华的 DeepLab 读研三，然后在港大的 ML 9月份之后会去读 PhD。然后也是戴西姆的实习生，主要是做这个机器人学习，还有 VOA 然后我今天要分享的文章呢，就是我们之前在 X26上的那个 Memory VOA 的工作。最近 MemoryOA 被派的那个派0.7和派 Memory 两次引用。然后公司就让我来再做一个这个技术分享。然后首先说明一下，就为什么这个题目叫 Rethinking 虽然就是今天开始吧，还是昨天开始在那个 AgilE 26开始开会。但是我我们这个文章大概是25年的8月份挂的 iCal，其实就是也没有很长时间。但是呢现在巨声太卷了，相关的工作太，层出不穷。所以说，就除了分享这个可能已经略微过时的 Memory VA 之外呢，还会分享一些 VA 的 Memory 的一些 insight 以及这个领域最新的一些进展。那么，然后我今天的报告呢，主要是从五个部分来展开。首先会讲一下，VOA当中什么东西比较重要。第二个呢，就介绍一下我们的这个 Memory VOA 的解决方案。第三个呢就分享一些，就是 Volta 的 Memory 相关的一些 insight 然后再介绍一下这个领域一些最新的前沿进展，最后是做一个总结。首先就是，VOA 当中什么东西重要？我们先对这个微微的背景做一个简单的介绍。你像最近的十几年呢，人工智能发展得非常的迅速。比如说16年的 AlphaGo 然后22年底的 ChatGPT。还有包括一些，比如说图像生成模型，SAM 这样一些视觉的模型，都取得了很大的进展。但是呢，这些模型都是在电子世界里面的。而我们要想人工智能真正的帮助人类的话，一定要到这个物理世界里面去，这就是尹伯力的 AI 具身智能。所谓具身智能呢，就是人工智能模型控制机械臂，然后去跟物理世界发生一些交互，来帮助人类干一些事情。那么这个巨声智能这个词呢，火起来可能是我的印象可能是从谷歌 DeepMind 在22年底的时候发布 RT 1模型。这个模型呢是一个 GenAI 的机器人基础模型。它是一个小模型，参数量大概只有35兆。但是在当时看来呢，是用了非常大量的一个真实机器人的数据。大概130K 的一条一个轨迹，他们收集了17个月，训了这么一个模型。那么之后呢，谷歌 DeepMind 在23年7月份又推出了 RTQ 的模型。就是扩展了，用 WLM 来作为这个。一个骨干的模型。这个某种意义上可以说是微微的开山之作。简单来讲呢，它就是基于 WLM，然后在 decoder 的时候。把那些用的最少的，那些词表里面的那些 token 换替换成这个离散的 action 的 tokens。 从而能够产生这个机器人的动作。那么好像哦，那个刚才有点卡了，不好意思。那么之后呢，就是学界，包括 Stanford UCB 然后在24年6月份提出了这个 Open VOA 的这样一个模型，相当于是对 RT two 的一个开源复现。那么它是第一个开源的 VOA 模型。但是呢它的真实机器人实验的表现比较一般。之后呢，就是又流行了另外一种，在这种经典的 VOA 之上，建立了一种大小脑的 VOA 比较有代表性的就是24年10月份。 Physics Intelligence 提出的派零模型，以及微软亚研院提出的 CoCaT 模型。这一系列模型呢，它跟之前的一个区别就是它加了一个 diffusion 的 policy 的。一个 head 来生成动作。这个呢就充当一个小脑的作用。现在的，即使到现在呢，这种主流的架构都是这样一种大小脑的架构。那么它有哪些优势呢？第一个就是它有这个能够建模多峰的动作行为这样一个能力。第二个呢就是它是一个连续的 Action Space。你像 OpenVLA 那种离散的 Action Space 它的这个 Action 的分辨率就...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-24-bilibili-bv17dolbjebt-pi0-7-memoryvla-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-memoryvla-temporal-memory-deep-dive-2026-07-24|MemoryVLA 时序记忆视频深度调研]]（R04 主分类，R07 次分类）。
