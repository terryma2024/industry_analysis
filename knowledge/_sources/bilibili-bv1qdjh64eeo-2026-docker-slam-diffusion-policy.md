---
title: "公认2026具身智能天花板教程！一套吃透大模型机器人，Docker、SLAM、Diffusion Policy、扩散学习全覆盖"
type: source
date_created: 2026-07-14
last_updated: 2026-07-14
source_urls:
  - https://www.bilibili.com/video/BV1qDjh64EEo
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-14-bilibili-bv1qdjh64eeo-2026-docker-slam-diffusion-policy.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 公认2026具身智能天花板教程！一套吃透大模型机器人，Docker、SLAM、Diffusion Policy、扩散学习全覆盖

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1qDjh64EEo |
| BV / video id | `BV1qDjh64EEo` |
| Author | CV前沿与深度学习 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-14-bilibili-bv1qdjh64eeo-2026-docker-slam-diffusion-policy.json` |

## Transcript Excerpt

是给大家上一个，就是那个大模型机器人的一个那个系列课程。就是主要是针对这个具身智能的目前的一个发展状况。进行一个综述，然后也讲解一下整个课程的整体的那个流程，以及就是我们会上哪些内容。然后我是那个主讲人那个姚老师，然后我们主要是通过这个课程，就是希望把这一系列的除除了那个基本原理，还有把这一系列的实战和算法，包括 docker 视觉 slam。diffusion 和那个模仿学习等等等等，非常多东西。就是说我们的课程不只是希望去简单地去那个把它给那个复现出来，这还包括了一切的它的一个基本原理，就是那个为什么，怎么做，以及我们接下来想做自己事情时候应该如何做的整一套的一套组合。这样的话是才能帮助你们之后去进行一个更好的一个那个研发。然后本次课程的话，今天的课程主要包含了大模型的机型一个发展状况，以及那个优密，以及 dexcap 的一个介绍，以及最后去整体的一个那个课程大纲。首先是我们开始讲一下那个大模型机器人的一个发展现状。然后前几天正好大概在7月4号，正好那个世界人，世界人工智能大会，它那个 wsc 上那个亮相了非常多的那个人形机器人，其实最有名的就是那个特斯拉的那个奥，就那奥特波特莫斯。然后它已，目前已经进行了两到三年的一个那个迭代了，并且它目前已经可以是完成，你像这种简单的就是那种。分拣工作，并且也可以看到它的整个视觉也采用的是那个鱼眼镜头，这样的话大家就能发现跟那个优米也是非常像的。并且它的整套的学习方案，你看可以看到啊，整套它现在那个公布出来的全部是那个模仿学习，这样的话就可以跟那个 dex cap 其实是那非常像的。然后并且你大家可以看它那个配置，现目前的话那个人形机器人，它都是一套那个标准的配置，头部基本上就是相机加那个激光雷达。然后每个胳膊都是基本现在都是七七自由度或者七个半自由度，然后再加上每，然后关节都像是那个谐波减速器啊，以及那个力矩电机，然后最多在末端加个那个那个六维力传感器。然后那个灵巧手基本上都十二个自由度的，包含了那个空心杯电机以及腿部。腿部我们就那个不多讲了，是因为腿部其实解决问题就是那个稳定性，它并没有说是通过那个它并没有可以说是功能上的一些非常复杂的东西，主要就是对腿部的运行稳定性。并且这样的话当时当时有些方案就会把这个腿部换成一个，就是那种 av 所以我们这个课程主要还是针对那个，就那个上半身进行一个展开的。然后第二个就是那个宇树科技。宇树科技的话，其，这现在确确实做的还挺厉害的，并且它的那个架构其实现在那个就跟我刚才说的那个人性都一样。就是脸部的一个那个三 d 激激光雷达，你像那个像那个深度相机都用的是 real sense 现在你可以发现基本上所有的那个研究所或者人形机器人成品。基本都是用的是那个 RealSense 或者 435，441，415都有。并且它现在也是用的那个强化学习，大家可以看出来，它现在一些公布的那官网的那个视频。基本上都是用那个模仿学习，加一些，再用那个仿真进行一个那个，就那强化训练。然后他们的每个胳膊的，是，两个胳膊，每个自由度基本都是。都是七自由度的那个胳膊，然后再加上腿部，并且它同时还公布了另外一个产品，是那个六自由度的那个机器人。我们可以简单看一下啊，确实还那个挺有意思的。就是它的机器人的话，其实也公布了另外一个那个六轴的，就是那种协作机器人。其实六轴的协作机器人是我们目前一个比较好的，工业上用的最多的，最稳定性的。因为它的正逆运动学和动力学已经构建，其实没什么动力学啊，主要是正逆运动学已经非常完善的一个东西，并且它非常稳定，精度非常高，精度现在的话，六轴协作机器人。基本都能做到0.03毫米到0.02毫米的一个精度。所以你你看他甚至可以把它放在那个机械狗上去完成非常多的那个任务。这个东西其实是也算是比较简单的一个事情了。我们接着讲。然后另外一个就是那个智元机器人。智元机器人它比较特殊啊，智元机器人它是唯一能在公开上面讲的，它已经跟工厂进行合作，已经开始你像工业级的那个应用了，包含了一些就是那种拧螺钉。以及那种质量检测，还有去涂胶啊，就那就那种打螺丝啊，是什么的。然后是我们看一下质检机器人，其实大家可以就那个看出来啊。他的东西其实跟那个东西是一模一样的。这时候你会发现每个人形机器人啊，其实整个架构是一模一样的。顶部它是用了大脑，中间的话就有一个那个 rgbd 杠起。相机嘛...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-14-bilibili-bv1qdjh64eeo-2026-docker-slam-diffusion-policy.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
