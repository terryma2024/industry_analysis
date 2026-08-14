---
title: "圆桌正当时：聊聊具身领域三大代表性数据集"
type: source
date_created: 2026-08-13
last_updated: 2026-08-13
source_urls:
  - https://www.bilibili.com/video/BV1Di546YEfR
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-13-bilibili-bv1di546yefr-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 圆桌正当时：聊聊具身领域三大代表性数据集

> [!summary]
> Bilibili video source packet; its claims are separated and cross-checked in the linked deep research.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1Di546YEfR |
| BV / video id | `BV1Di546YEfR` |
| Author | 具身智能之心RoboTech |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-13-bilibili-bv1di546yefr-bilibili-video.json` |

## Transcript Excerpt

好，那欢迎大大家在周五晚上来到我们这个聚生开源数据集大赏。我们邀请了领域非常具有代表性的三大数据集的一一座。来齐聚我们的直播间来分享他们的工作。那么呢，其实2026年大家都可以看到，这是其实已经算是巨深的数据元年了。因为在2025年经过一年的打磨和迭代，特别是本体和一些素材的方式，那么从业者对从哪里采，如何采。采集之后如何对齐和标注，其实已经有了很大的一，很大的一步的认知和那个沉淀。所以在今年大家可以看到领域高质量的数据集不断地涌现哈，下载量也在呈现很大程度的飙升。大家也非常坚定地认识到驱动聚生智能核心技术突破的中间力量一定是有这个高质量数据集的一大份功劳。那么我们本次圆桌也非常有幸邀请到了。数据集领域的三大，三三位核心贡献者，他们分别身后都站着自己的代表作。那么我们今天跟他们一起聊一聊数据集的制作历程、方法论以及他们在各自突破性工作中发挥的重要力量。那么我们首先欢迎 RoboMaster 1.0和2.0的一作侯博。哦好，那完了我就给大家介绍一下那个我们这个数据集吧。我就我现在是就读于北京大学，那个我我先共享一下屏幕，就是我先。我目前就读于北京大学计算机学院，是程宽老师的博士生。完了，主要的研究方向就是具身智能以及这个强化学习。细化一些方向，就是机器人的多模态数据以及强化学习机器人操作这方面。完了，我就很开心跟大家去分享我我最近的这个工作吧，就 RoboMaster 的2.0。完了，一，不，以及后面会跟大家讨论一下，就是我们的关于数据集一些的想法。那么我这里就开启演讲者模式，完了大大家开始这样。就是我我们的，这个数据集呢，主要的一个特点是它是。有，还有6种本体的一种双臂操作数据集，因为它更，双臂操作更加拟人化嘛。那么我们可以看到这张图里呢，它的那个左上角呢，主要是我们一些操作数据集的一些。事例，就是说你可以看到我们的数据集是以一个多视角去收集这个一个任务的数据集。完了，中间这幅图呢，主要是是这个展示了我们这个数据集的几大亮点吧。首先是我们有一个31万条的双臂操作数据集，完紧接着呢，我们把数据集中所用的这个仿真的资产呢，对应的在能用在直接用在 i-texsim 上的资产，仿真资产呢开源出来了。完了，我们的31万条的数据集呢，也还包含了这个1.2万条触觉的数据。完了，最后呢，我们构建了一种这个快慢系统，完了来实行长城的这个移动操作随机。完了右右面这张图呢，主要是详细。介绍了一下我们数据集的分布情况，就我们数据集涵盖了这个6种的本体吧，就弗朗卡、 UR5、天翼、天宫、方舟以及松岭。把这个，一，那个右边的这张图的左上角呢，主要是说明了一个每个本体的数据集呢，它含的数数据量。完下面是它的工作时长，以及右面就是我们含有丰富的一些这个任务上的技巧。紧接着呢，我们对数据进行了一个详细的评测。我们采用了常见的四种的模仿学习，以及四种 vla 模型进行训练，就大家可以看到有。 A C T DAS Policy D B C I Y U V A 啊以及派零、派零点五、 Hyper V L A 以及 S 二、 S 杠五二。那么我们首先会接下来会将，会讲解这四点主要创新是我们具体怎么做的。那首先呢，我们就是开源了这个。长城双臂移动操作数据集呢，它是有31万条。完了它包含6种本体，759个任务以及1139个操作物体。啊紧接着我们包含了12条这个长城移动操，1.2万条这个长城移动操作的这个数据集。完，最后呢我们又支持了这个。大小脑系统来完成，机器人大小脑系统来完成这些我们所收集到的这些长城移动操作数据集。最后呢，我们开源了我们数据集中所用的这个 manipulation 资产中manipulation 物体中的仿真资产。完，方便于大家在仿真中去应用。完，接下来呢，就是我们的这个数据集的一个下载地址吧。完，我们现在目前那么来讲呢，数据集下载量已经超过了200万，完是行业内基本上是应该是下载量。排名的前几名吧。完了，最后呢，我们开始详细介绍这四点的这个创创新点。完了，紧接着我们针对第一点呢，去去先介绍，就是说哎， sorry 我们为什么要构建一个移动操，双双臂这个操作数据集？那么我们可以看到目前为止这个 Janus 哎， sorry 哎，好。就是说 Janus One 呢，它它呢就有一个非常好的结论，就是大家可以看到它的 demo 非常酷炫嘛，就有很多这种。喂，我可以把...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-13-bilibili-bv1di546yefr-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-embodied-dataset-landscape-deep-dive-2026-08-14|具身数据集视频深研]]
