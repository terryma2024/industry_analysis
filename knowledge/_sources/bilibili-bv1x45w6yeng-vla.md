---
title: "【教程】具身智能实操，蚂蚁灵波VLA上手体验"
type: source
date_created: 2026-07-23
last_updated: 2026-07-23
source_urls:
  - https://www.bilibili.com/video/BV1X45w6YENG
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-23-bilibili-bv1x45w6yeng-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【教程】具身智能实操，蚂蚁灵波VLA上手体验

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1X45w6YENG |
| BV / video id | `BV1X45w6YENG` |
| Author | 陈老师具身xbotics |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-23-bilibili-bv1x45w6yeng-vla.json` |

## Transcript Excerpt

大家好，从今天这一期视频开始呢，我将带大家一起上手实操巨声智能，而且是从 VLA 来手把手带大家一起实操啊。那为什么要出这样的教学指导呢？是因为大家目前阶段总觉得巨声智能离我们还很远，似乎还没有在我们生活中落地。那问题来了，这个瓶颈到底卡在哪里呢？这个巨声行业的结构主要是这五个板块。上游供应链本体就是机械的硬件结构，还有模型、数据和场景。那我说一个观点，目前的瓶颈其实是卡在模型和数据上。上游的供应链没问题，这个是我们国家的一个优势啊，制造业，谐波减速器啊，行星滚柱丝杠啊，再加一些机加工的一些零件，并不是瓶颈。本体宇树已经向我们证明了，机器人的本体以及运动控制可以做到那么高超的水平，舞蹈、功夫、跑马拉松都可以了，所以其实本体能力目前也不是瓶颈，而真正的瓶颈就是机器人的大脑的能力。就是智能的部分，其实就是模型的能力，是相当薄弱的。机器人自己去任务拆解、任务规划，然后再驱动身体去完成一些物品的夹取啊、工厂中的干活，或者家庭场景的叠个衣服啥的，然后炒个菜、整理个卫生，目前成功率还并不高，这就是能力。不行所导致的。那为什么模型的能力不足呢？其实很大一部分原因是因为数据的缺乏。我们将具身智能和目前的 AI 做对比，大家用到的千问、豆包能力都很强。为什么他们的模型能力很强？是因为他们数据量非常大。这些在互联网上的数据的体量在 Trillion 级别，就是在万亿级别。而我们聚生智能的数据，真机数据也好，仿真数据也好，数量级在多少呢？在50万小时，百万条轨迹，折算下来其实是在 billion 级别，就十亿级别。那么相差了4~5个数量级，也就是说，巨声智能行业数据量就不够啊，这就导致了模型的能力练不出来。所以我们机器人在工厂中、 c 端家庭中应用还并不多。那么应用不多就导致也没有额外的产生更多的数据。所以我们说这个数据飞轮转不起来。什么叫数据飞轮？就是因为有数据，所以模型能力很强，模型能力强。就有更多的机器人在实际场景中运行，然后就产生了更多的数据，进而滚动让模型能力变得更强，这个飞轮就转起来了。而现在具身智能的飞轮，大家都希望它能够尽快转起来。当下还没有。至于说场景，其实也不是瓶颈，需求非常多，只要有人的地方，人干的活其实就可以被机器人代替，所以场景其实不缺的，缺的就这两部分。好，那么怎么解决呢？需要大量的开发者，而且主要是二次开发者去深入到一线的场景中，把具体的一个一个的功能实现。这个场景是数以万计的，那么这么多的场景其实不太可能有几家公司全部都解决掉。明星公司更多的专注于在做本体，和做一个基础的模型，基座模型。然后把这个接力棒交给二次开发者，在现场去进行数据的采集，真机数据采集，再进一步的训练模型，实现功能。这一定是未来的一个格局。本体要尽可能降低成本，你不能一套机器人要十几万、几十万，那这个门槛就有点高了。低成本且稳定，而模型呢，一定是要强大，还好用。方便使用。那么数据肯定是两块，一块呢是数据量一定要起来，那这个呢我们现在是有解决思路的，我待会马上讲。第二块呢就是现场是要采数据的。这三者合一起，我觉得聚生智能就会逐步落地的。机器人会变得越来越有用的，而不是只能跳个舞。所以陈老师从这个视频开始的一系列教程，我们更多的就从模型切入。我们会学习用一个 VOA 模型去采集一些数据，去完成一些具体场景的具体任务。那么模型用什么呢？我们先来用 VOA 啊，世界模型也是越来越重要了，后续也会出指导的啊，大家可以先点点关注。那么 VOA 模型到底是如何驱动一个机器人来干活的呢？我之前讲过一期视频啊，叫做什么是 VOA 啊？VOA 与世界模型，播放量也已经好几万了，在主页上是有的。那我这里再快速的回顾一下。BOA 你可以简单理解为就是抄作业啊，向谁抄作业呢？向大语言模型抄作业啊，这些呢其实就是比如说 Deepseek 啊。千问啊等等。输入文本，输出文本，它已经有推理很强的逻辑能力了。那么我们只需要做两件事。第一个，对于机器人来说，它更多的是视觉是吧，摄像头看到的画面。包括说会用到一些触觉啊，其他的一些模态。那么这些环境的信息呢，通过编码器也把它 token 化，变成文本，给到这个大语言模型不就好了？然后这个大语言模型的输出，其实也是输出一些文本。那么再通过运动解码器，最终通过运动控制器控制机器人去运动。因为其实驱动机身运动的也不过就是一些电机的角度、速度，它本质上...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-23-bilibili-bv1x45w6yeng-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## 已完成综合

- [[_syntheses/bilibili-lingbot-vla-hands-on-deep-dive-2026-07-23|LingBot-VLA 上手教程视频深度调研]]（R05 主分类，R04/R07 次分类）。

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
