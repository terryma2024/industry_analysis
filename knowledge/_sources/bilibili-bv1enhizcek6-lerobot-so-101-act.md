---
title: "LeRobot训练SO-101机械臂ACT模型全流程解析"
type: source
date_created: 2026-09-10
last_updated: 2026-09-10
source_urls:
  - https://www.bilibili.com/video/BV1enHizcEk6
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-10-bilibili-bv1enhizcek6-lerobot-so-101-act.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# LeRobot训练SO-101机械臂ACT模型全流程解析

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1enHizcEk6 |
| BV / video id | `BV1enHizcEk6` |
| Author | GPUS开发者 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-10-bilibili-bv1enhizcek6-lerobot-so-101-act.json` |

## Transcript Excerpt

好，再次确定一下声音没有问题，那我们就正式开始我们的直播了。今天呢，给大家带来的这个直播的话，就是之前一直都是在赛赛仿真里，那我们今天我们来看一看如何在真实的乐 robod。这个框架下的 SOAR 101这个机械臂是如何采集数据以及训练的？那这个是我们今天比较关注的重点。顺带呢，今天一开始先跟大家看一下乐 robot 的最新的一个动态。那我们可以看到哈克费斯乐 robot 现在最新的这个仓库的话，它在三天前又有了更新。所以说这个框架还在不断的更新和迭代。那么对于我们的教程来说的话，它就有时效性，但是没有关系。那么我们今天所有的代码的历程基于什么版本呢？那么我们基于 Release V0.3.3的这个版本。也就是说，我们今天用到的乐 robot 这个代码的话，是从这个里面下载的，下载的 source code。 那么如果大家想跟我们完全的一比一复现的话，那么大家可以将自己的 robot 更新到 V0.3.3的版本。这样我们的环境就是保持一致和同步的。那么期间就会遇到较少的问题，即便遇到了问题，我们也可以更好的去解决。那么回到我们的 SO 101的经典教程。那这个教程的页面呢，我们今天其实不太会涉及。它的话就是大家在购买了我们的乐 rob 的机械臂，或者是大家自己 diy 了一个乐 rob 的机械臂，S O101的话，那么可以根据这个页面中的这个教程，将散件进行安装，以及环境进行安装。大家看它先是装环境，然后再一步一步的。告诉你每一个关节的舵机叫什么名字。然后的话它有视频的安装教程，然后这个都不是我们今天关注的重点。我们可以看到这有一个配置电机。大家会发现新版的配置电机的命令跟我们以前直播旧版的已经不太一样了。那么我们从今天之后的直播呢，都会更新到最新版本的命令的模式。我们可以继续看，配置好舵机之后呢，我们对它再做一次，你看，校准，然后校准完之后，这也有视频的校准视频。那么到这，接下来就要进入到我们的重点了。当我们完成整个机械臂的一个初始化任务之后呢，那么我们就可以搭建一个场景来尝试采集数据，并且训练一个模型。最终呢，让我们的机械臂自己执行某些任务。大家在这块可以看到一个，Getting Started with Real World Robots，就是在真实世界中。去使用我们的机器人，那么也就是这个链接了，我们今天主要来讲解讲解这个东西。那么我们今天所要用到的场景长什么样子呢？大家可以看到。这就是我们的这个桌面，我们桌面上有一个小红色的小盒子，里面有一堆方块。这个呢是我们的 Follower 币。这个是我们的 leader 币，我们 leader 是黑的，然后从币是白色的。然后的话，我们今天的环境中呢，它拥有两个摄像头。我们可以看到，这是我第一个俯视的摄像头。然后同时呢，我们还有另外一个侧视，前视的一个摄像头。大家看前面这个摄像头。还可以看到我们的这样的一个画面。也就是说我们会用两个摄像头来作为数据的输入。我们把这个摄像头切回俯视。 ok，这个是我们都要提前准备好的。那么这个摄像头的选型呢？没有关系，之后我们都可以在群里，大家一起相互交流。它普通的摄像头其实就是可以的。你像俯视的话就尽可能视野大一些，视角比较大更合适。好，那我们来看我们今天要完成的任务的话。它这个官方给的任务，是拾起乐高的块块。但是我们今天要做的呢，也非常的简单，就是我们这个块块会放在这些这个传送带上。然后传送带会带着我们的块不断的移动，那我们可以有请小助手简单的示意一下。对，就是我们会将一个能量块，放到了机械臂上，哎，放到传送带上，对，不好意思。然后我们的机械臂会追着这个能量块，然后把它推到这个小方格里。这个就是今天我们主要要来实现的。这也是模拟生产线上，比如说机器人识别到有异常的水果，你看这是正常水果，我们就让它通过，然后如果有异常的能量块混入的话，我就把它推走。啊，大概是实现这么样的一个状态。这是我们买了一些道具水果啊，非常的 q 弹，比较可爱。我们到今天视频结束的时候，我们来尝试一下。在昨天晚上的时候，我们训练了21万步的一个模型，基于 ACT 我们来看一下它的效果如何。到时候就拉出来溜溜，看看它的情况了。好，那么我们要如何实现呢？我们今天就来一步一步的。大家看，我们的机械臂校准完之后，我们开头的第一步就是要遥控我们的机器人。来确定我们所有的，包括串口、端口号和...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-10-bilibili-bv1enhizcek6-lerobot-so-101-act.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
