---
title: "【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能"
type: source
date_created: 2026-07-03
last_updated: 2026-07-03
source_urls:
  - https://www.bilibili.com/video/BV1UR7H6dEy5
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-03-bilibili-bv1ur7h6dey5-2026-slam-ai-slam-ai.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1UR7H6dEy5 |
| BV / video id | `BV1UR7H6dEy5` |
| Author | AI学习百宝箱 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-03-bilibili-bv1ur7h6dey5-2026-slam-ai-slam-ai.json` |

## Transcript Excerpt

Plan 是主要是因为在于它对于机器人来说非常之重要，因为从上个世纪，其实从80年代的时候，做那个地面车，其实主要是依赖于地面的那种小型的那种，叫 mobile robot mobile robot 就移动平台。用无云端平台，它主要是有一些编码器、超声这种简单的 sensor 在这种情况下呢，无，因为对于机器人来说，机器人是非常需要这种定位的技术去支持它做导航，因为这就不能不提到一个问题，就是在机器人领域中，有个很重要的概念叫导航的概念。导航是在机器人中 非常重要，而 SLAM 给出了一个什么样的东西呢？我们往下看。我们先看到，对于机器人来说，有个很重要的东西。机，我们从下往上看，大家可以看到啊，最底层是执行器层以及数学模型。这东西说什么意思啊？执行器层，比如说大家都知道各种电机，伺服电机，舵机，对吧？然后那个步进电机，还有什么，然后电机里面还有什么直直流的电机，直流电机分有刷无刷，当然这东西大家可以回去自己查一查到底是什么东西，但对每个电机，它是有个电机模型。因为你要不然你没法做控制。但你基于电机电机模型之后呢，那你上层的话，你做更高层的控制，比如说你怎么样让电机稳定到一个稳定转速，对吧？这就是一个 esc 模块，对吧？electric speed controller 这个模块。然后每个模块里面呢，它的控制器有什么？PID 的呀，PID 的控制器啊，然后还有 AQG 的控制器啊，等等，就是这么一些控制器。从控制控制层呢，我们再往上走，因为你在对于电机的控制，执行器的控制之后呢？哎，立马你就回归到一个更更高的一个一个层的上面去看。哎，我们有了控制层对于电机的控制，也就是说我假如说我是一个像左方的这样一个波士顿动态的一个大狗。波士顿动态大家应该都知道波士顿 dynamic。那么我现在腿是关节是能，是有关节的单独的控制。但是有个问题，我现在让他从 A 点走到 B 点，我让他怎么走呢？因为人是知道，人是通过这种类似于，就像那种偏差控制，我想要到达一个点，我是慢慢的，不停的校正自己。但是问题是我人从 A 点走到 B 点，我一开始是有规划的，我比如说从一一楼走到五楼，我知道是怎么走。那么在这个地方就提出了一个很大的一个问题，就是说你怎么样知道你在哪个环境中？对吧？因为你只有知道环境，然后你知道目标点，然后你才能去规划这么一条路，这就是在中间层做的一些事情。然后到中间层呢，因为你拿到了这个环境的信息，还有你位置的信息之后，然后你再通过上层的一个叫任务规划或者决策，因为比如说你要做导航。你要做避让，或者说你做服务机机器人，你要做一些什么抓取的动作，那么这是在更加的 high level 中间层，感知、定位、构图，这块就是说你要去感知环境，了解环境。那么我们 SLAM 就在这么一个层中。SLAM 主要是归功于在这么一个承上启下的一个感知定位及构图层。它主它的主要的核心问题是回答两个东西。第一个，我在当前环境中是是的什么位置？第二个，当前环境是什么样子？这就是我们人也去做的一件事情。所以我们学生现在目前做的事情就是在于做室内导航。就是因为它这个东西比较有意思，就在于你不管是做无人车，还是做室内导航，或者做无人机导航，你所做的第一件事情，首先是让它能飞起来，或者让它能动起来。那么你第二件事情就是让他能自主地动起来。这就是一个很连贯的动作。既然你说让他能自主地动起来的话，那么你就应该知道你的环境是什么。而且你要知道你当前在环境中的位置是什么，因为位从我们控制来说，有位置层，然后有速度层，还有角速度层，当然这东西是你不管或者是航向层，它都要是有一些这样的一些东西，有，就是这样的一个几个层次。但是呢，最高层就是说最外环的层是有位置层，因为你连自己的位置都没有，你是没有办法去做这种导航规划的。嗯，ok。然后呢，就是既然说死了去回答这样的一个问题，那他什么时候去提出呢？这里面就不得不提出，就是说说到一个很重要的继承林中一个会议。叫 ITC 叫 ITC Conference on Robotics and Automation 这就是我们机器人领域最顶级的会议，叫 ICRA 在这个 I- ICRA 这个会议在1986年的时候，有个叫 Peter 还有个叫 Chestman 还有 Jim Gurry。叫，还有个 Who Durant 那个 We 其中我把红色的定义，...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-03-bilibili-bv1ur7h6dey5-2026-slam-ai-slam-ai.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
