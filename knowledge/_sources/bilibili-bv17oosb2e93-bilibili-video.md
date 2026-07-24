---
title: "人形机器人运控算法概览"
type: source
date_created: 2026-07-24
last_updated: 2026-07-24
source_urls:
  - https://www.bilibili.com/video/BV17ooSB2E93
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-24-bilibili-bv17oosb2e93-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 人形机器人运控算法概览

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV17ooSB2E93 |
| BV / video id | `BV17ooSB2E93` |
| Author | Cristina绛 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-24-bilibili-bv17oosb2e93-bilibili-video.json` |

## Transcript Excerpt

哈喽，大家好，欢迎继续收看从零手搓人形机器人。这一期呢，给大家录一期人形机器人的运动算法板块。我们都知道人形机器人从大的分类上来讲可以分为硬件本体，小脑运控算法以及大脑大模型。那在前面的很多视频中，我们主要介绍了人形机器人的硬件本体板块。那么这里呢，我们就再录一期人形机器人的人工算法。然后这一期呢是做一个人工算法的一个概览。这一期的主要内容有，第一是介绍一下这个人工算法的背景知识。第二是人工算法的发展历程，第三是人工算法的这个论文推荐，第四是做这个前景的预期。好话不多说，那我们直接开始。首先是基础背景知识板块，这里我总结了一张金字塔的图哈，上面是人形机器人的云控算法，然后它下面这个需要的这些基础知识都放这里。我们先看最底层的这些，最底层就是数学和控制理论。数学呢，就是这个矩阵理论啊，微积分啊，数值分析啊，复变函数与积分变换呀，概率论啊，几乎涵盖了我们这个数学的哎呀，本科或者研究生阶段的大部分的这些课程。然后控制理论也是比较关键的。经典的控制理论，现代控制理论只能控制，比如说经典控制理论，这里面的这个 pid 控制，然后现代控制理论里面的自由控制啊。二次规划呀，还有 MPC 呀，这些都是比较重要的。然后再往上的话就是这个机器人学跟运动学、动力学这一块，这块我们之前也都介绍，花了比较多的篇幅也已经介绍过了。然后感兴趣的同学可以再回过去看一下。然后另外就是嵌入式板块的，比如说关节电机控制啊、传感器啊、还有一些编程，还有一些这个仿真的软件的使用，你就说 SCSIM 等等。啊，还有运动规划、 SLAM 就是整整个运嵌入式板块有一个需要一个初步的一个了解。然后再往上呢，就是深度学习跟强化学习，还有大模型板块的。因为算法也很多，也会涉及到这些，所以这是一个金字塔的这样一个基础。所以说它的这个底层呢就是数学跟控制理论，中层呢就是机器人学跟嵌入式，然后上层呢就是强化学习大模型。从这里可以看出它的特点呢，就是需求的知识面是非常的广。从我目前了解下来，人形机器人应该是整个这个人形机器人的应用算法，应该是整个机器人里面相对要求知识全面性比较高的一个一个板块了。另外它对知识的深度要求还是比较高的，像数学啊，还有这个这个控制理控制理论这两块呢，要求其实都是比较深的。像在课本上常规学的，可能还还不够，还要再深入再去自学一下，深入学一下。第三呢就是这个强数学能力和控制控制能力，其实是是一个意思了。行，这个就是它的基础的。然后，然后感兴趣的话，大家可以去浏览一下这些。啊，当然这些并不一定说每一个板块都要去精通啊，这肯定这这肯定非常难的，因为它它是基础。只要有有些只需要大概了解，会一些基础的概念，知道去哪里查哪里学就可以。然后有的呢，像数学跟控制控制理论这两块，那肯定是要求比较相对来说比较熟一些的，就是这样一个状态。行，那我们看第二板块，运控算法的发展历程。然后整个运控算法呢，从分类上来讲可以分分为这个四个阶段。第一个阶段就是1970年到2010年这个阶段，它是这个简单模型，就是比较早期的，能能走起来就不错了。就简单利用这个简单模型，主要是 ZMP 跟这个新的里边。这种方式去控制的。然后第二个就是这个基于模型的方式，然后第第第三个是基于学习的方式，是当前已经最热的。然后再往后呢，就是可能会越来越多会搞这个大模型融合的这种算法。然后整个大的分类上就是四四种算法，简单模型，然后基于模型的，基于基于这个学习的，还有基于大模型，对大模型融合。然后从里面的这个具体的涉及到的内容呢？简单模型呢，这个大家比较熟悉，就是 ZMP 跟现金到600。这两个以这两个为主，然后这个包括这些 PID 啊。这个应用学这，你这个你动力学啊这些等等。然后它这个用到这个机器人本体呢，就是以这个本田的阿西莫机器人为典型。当时在2000年的时候，其实已经能实现了，相对来说比较流畅的行走啊。甚至奔跑啊，上楼梯啊这样一个操作。很多小伙伴也都也都见过，也也都在网上看过这样的。但是这个呢，其实它因为模型比较简单嘛，就是这个 v v m p 就零，这个零利率一点，然后先行到600，其实是比较偏向于规则，就是生硬编程去实现的。然后这个呢它其实，因为纯编程的嘛，它的这个泛化性、拓展性是非常差的，所以说当时根本搞不下去的。所以说当时很快也就就销声匿迹了。去去，也是受限于这个技术。然后再往后呢，就是到了这个10年到2020年...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-24-bilibili-bv17oosb2e93-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-humanoid-motion-control-algorithms-deep-dive-2026-07-24|人形机器人运控算法概览视频深度调研]]（R04 主分类，R07 次分类）。
