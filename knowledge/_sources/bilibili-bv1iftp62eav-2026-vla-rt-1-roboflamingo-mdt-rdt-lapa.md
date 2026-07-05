---
title: "【2026最新具身智能VLA入门教程】一口气讲透RT-1、RoboFlamingo、MDT、RDT、LAPA等核心算法，从零基础到进阶实战，算法原理+代码实战！"
type: source
date_created: 2026-07-05
last_updated: 2026-07-05
source_urls:
  - https://www.bilibili.com/video/BV1ifTp62EaV
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-05-bilibili-bv1iftp62eav-2026-vla-rt-1-roboflamingo-mdt-rdt-lapa.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【2026最新具身智能VLA入门教程】一口气讲透RT-1、RoboFlamingo、MDT、RDT、LAPA等核心算法，从零基础到进阶实战，算法原理+代码实战！

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Synthesized in [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1ifTp62EaV |
| BV / video id | `BV1ifTp62EaV` |
| Author | AI人工智能课程 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-05-bilibili-bv1iftp62eav-2026-vla-rt-1-roboflamingo-mdt-rdt-lapa.json` |

## Transcript Excerpt

挑战两周入门人工智能，全民 ai 时代，要问现在什么领域最火，那非人工智能莫属。手机秒识万物、自动驾驶穿行、机器人精准抓取，这些酷炫场景背后都是同一个词，人工智能。众所周知，人工智能门槛高、难度高，又很卷。不过没关系，今天我来带大家挑战两周。快速入门人工智能，从基础原理到论文源码讲解到代码实现，一口气干到工业级实战项目。完整的视频教程、配套课件、源码已经放在评论区了，有需要的宝子三连加关注，一起上车吧！天，我给大家带来的这样的一个专题呢，是关于。具身智能这个任务里面的这个视觉动，语言动作模型，VOA 模型。它其实顾名思义啊，就是说去。根据我输入的这个视觉啊，语言的信息，去生成我对应的激情，可执行的动作。这个呢，在我们去深圳领域呢，现现在一个非常。重要的一个研究方向。所以呢，这个我们来去把这个单独去，拉开一个课题，去去单独拎出来去讲它。然后主要的内容包括这以下几个方面。那么首先我去跟大家去讲一下关于什么叫做 VOA 模型。另外呢，就是说在我们了解了这个模型之后，我要去了解，我要去训练模型所需要的一些数据基础。由于这个机器人任务啊，和这个传统的 CV 的任务不一样，它可能更加需要的是一个这个仿真和真实的环境。仿真环境呢，是用来去在一个相对公平啊，相对简单，相对廉价的一个场景去验证你的想法。然后在真实的场景里面呢，是要去克服仿真到真实的一些。Same to real gap，然后去真正的让我的机器人在真机场景中去应用。所以这两点也都非常重要，所以把它分开去讲。嗯，最后呢，当我们了解了一个训练的时候的一个模型和数据的需求之后，我们再去了解一下我们如何去评判这个模型训练的是否好，也就是它的评测指标。以及我们训完模型之后，如何快速地去部署到真机上面。然后呢主要是一些这些的一些内容。那么其中呢，第一个是关于这个 V O A 模型的这个概述啊。那么首先我们去这个回顾一下这个我们的 VA 模型的这个背景，其实是在这个具身智能领域嘛。但是这个具身智能领域啊，其实发展的是相对的，比较的，怎么说呢，是相对比较的快的。也就是前两年，刚刚开始在我们的这个跟那领域火起来。像我们以以往的这种传统的事情，现在就像我们现在。上半年的工作，我们，我们的机械，对，我们参加另外一个机械，我们去吃晚饭。其实每个，每个学生的技能啊，它都是独立的。单一的，然后呢再去由一些规定好的一些规则，然后去决定我分别去执行什么样的动作，或者执行什么样的技能。那这就是我们传统机器人的决策系统所做的一些事情。但是呢，我们可以了，你理解到就这样的决策系统，它往往它是规则化，它的这些规则就都会人为去设定，它其实就没有具有很好的泛化性。然后呢，但是我们从另外一方面来看，就现在像 ChatGPT 大模型的这种发展啊，其实让我们这种多模态语言这个这样的工作在数字世界里已经极大的程度上呢去赋能了我们这样日常生活和工作。那其实呢，这也是通用的人工智能在这个这个世界的这个大家的这个生活中体现出来的一个对我们生生活的意义。那是其实那我们现在就讲，就说诶，既然我传统的这个激情角色系统，它存在着这样的这个。一个问题就是我的翻画性和通用性或智能性不足的问题。然后呢我的这种传统数字世界的智能系统，其实也没有办法去这个应用到真正的去或者赋能到我的这样的激情领域去，会让我的真实的机器被产生动作。那么因此呢，进而就产生了现在大家研究一个比较热门的一个话题，就是感知决策的一体化的这样一个全智能系统。也就是说，我们希望去将这样一个通用人工智能啊，从这个数字世界去拓展到这个物理世界去。也就是所谓的这个 VLA 这其实我们的 VOA 这个理解可能会更加更加好一点，让大家去直观的去理解我们为什么要去做 VLA 这个模型。嗯，这个 v o a 模型是新成智能的一个例子啊。其实你看到根据我的一个语言指令，可以去智能化的去决定我要去做什么事情，并且对这个任务啊，去做一些拆解，对吧？福利业啊，然后等等等等。他们就说通过 vola 的模型，然后呢去展现了一些非常惊艳的 demo 展现了我们这个人情金钱，或者是我们金钱在这个未来的智能家居的市场，以及一些工厂领域的 2C和 2B的市场上的一个应用前景。然后也获得了相当多的融资。也就是说，其实现在的 Vol 它是一个从未来的发展上来讲，是一个非常有意义的一个一个方向。那么另外呢，在学术界上呢，其实在不同...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-05-bilibili-bv1iftp62eav-2026-vla-rt-1-roboflamingo-mdt-rdt-lapa.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]]
