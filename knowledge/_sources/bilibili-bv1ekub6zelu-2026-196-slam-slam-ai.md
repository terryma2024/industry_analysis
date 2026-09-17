---
title: "【2026优化版】清华大佬196小时讲完的机器人SLAM技术，原理+实战带你从零到一快速掌握SLAM理论，速通具身智能机器人入门知识点！AI/机器人/无人驾驶"
type: source
date_created: 2026-09-17
last_updated: 2026-09-17
source_urls:
  - https://www.bilibili.com/video/BV1Ekub6zELu
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-17-bilibili-bv1ekub6zelu-2026-196-slam-slam-ai.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 【2026优化版】清华大佬196小时讲完的机器人SLAM技术，原理+实战带你从零到一快速掌握SLAM理论，速通具身智能机器人入门知识点！AI/机器人/无人驾驶

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1Ekub6zELu |
| BV / video id | `BV1Ekub6zELu` |
| Author | 深度学习项目实战 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-17-bilibili-bv1ekub6zelu-2026-196-slam-slam-ai.json` |

## Transcript Excerpt

然后本节课程那个大概安排呢，我大概这样啊。为什么要写这个书？然后为什么要讲这个课程？其实自动驾驶这个行业呢，其实挺大的啊，它里面做各种行，做各种东西的人都有。然后 SLAM 这块，特别是定位建图这块的整个方向呢，也挺多的。一般来说，一个团队里面会有做那个，做有做惯导的，啊，也有有做传感器标定的，然后有做那个轮式里程计的，然后有做有用激光 SLAM 的啊，激光 SLAM 的话呢，也还有分那个单线和多线的。然后也可能有做 VSLAM 的，可能做感知的，然后还有做那个什么 BEV 的。啊，这些人都有，然后他们多多少少都会接触一些这方面的一些东西啊，除了那些纯数学学历的人，可能可能对 SLAM 来说比较远的话，其他人多多少少都会跟 SLAM 有些关系。然后然后这里面因为牵扯到的人比较多，他其实互相之间沟通起来还是有那么一些障碍的，就是如果你作为一个纯惯导的人，他去学这个激光 SLAM 他就很费劲。特别是一些纯惯导的人，他们可能写的那个程序也就是偏那个裸 C 或者说 MATLAB 啊，或者说他们其实不不那么擅长去写 Linux 下面 C 加加啊。然后做 SLAM 这边这帮人呢，他也不太愿意去推那个大骨头的灌导，因为灌导很多书他写的方式，一个是成书时间也比较早啊。一个是它很多写作方式是一个跟你拆碎了讲的一个东西，就是一个从从从那个东西怎怎怎么做开始开始开始讲那个东西。但是其实大部分时候我们用的 mu 不太会涉及到它里面到底是怎么回事，我们更多的时候是说它输出的什么数据，然后我们怎么用，这样这样的一个关系。所以很多材料都特别大不同，这些学起来也比较费劲，所以整体上我们希望说把这个这里面的一些人的，大概一些共有的知识啊，给给他给他做一些梳理，然后我们想要去说那个 回顾一下说，或者说我们把很多的经典算法重新来实现一遍，看看我们现在能做到的什么程度啊。因为有很多历史原因啊，会导致特别是激光 SLAM 这一块啊，然后它很多的历史算法都是用一些比较繁琐的方式去推导的。包括以前我们说的一些，或者说一些那个咱们，或者说他们原始的论文啊，都是相对来说比较繁琐的一种这种这种方式，就是整个公式。公式推起来也比较长，然后解释起来也比较费劲。所以这我们写书的一个很大的一个动力在于我们想要把那个一些经典算法重新做一遍，其实就是造轮子啊，造轮子。然后这个轮子呢，我们能用一些比较现代的方法去造一些，或者说我们能不能把这个推导和那个实现再更加的简化一下，然后然后让那个让很多这个领域你不太熟悉的人啊，一看就能看明白这是怎么回事。然后惯导那块也是一样，就是说惯导这块东西其实你真真把它拿开来讲，你你不讲那个里面拆碎的一些东西来来看的，就是你光讲那个 MU 陀螺仪和加速器。那个东西也不是那么的麻烦啊，然后然后你这个东西对应的卡尔曼滤波器，你要把它从头到尾推一遍。你你会发现这东西其实也不是很长啊，也不是没有那么麻烦。所以我们想就是说能不能说从理论和实践方面都做一个大幅度的一个简化，然后让人家一一下子就能看明白里面是怎么回事。包括激光 SLAM 包包括那个主要惯导啊，这些东西都是都是这样子的。啊激光 SLAM 这块呢，主要是这个这个功能细节特别多啊，如果你从开源代码开始入手啊，就就功能细节特别多。那么我我可能我为了去讲一个激光 SLAM 我先跟你讲那个 ROS 是怎么回事，然后 ROS 怎么 ROS 里面怎么通信的，然后 ROS 的那个 launch 文件怎么回事，然后它里面 node 是怎么回事。它里面的各个节点之间这个这个技能调用怎么回事？lost message 怎么回事？啊，给你讲半天这个，讲半天这个东西，然后再再再跟你讲这个这个啊，这里面还有配置文件啊，这个是用 YAML 的，那个是用 Lua 的，这个是用 XML 的，这个东西是用 Message，那个东西是用 Protocol 的。啊这东西啰里吧嗦，讲一讲一大堆，然后讲完之后开始讲什么线程池啊线程池，然后这个这个线程怎怎么怎么怎么分配，我怎么搞一个线程池出来，能往里随随便便就能就能往里塞东西，然后多个线程之间的通信。啊，然后完了之后，可能还有我要突出作业拓展，啊我搞成模板源，搞成那个，这个这个模模板函数，我能我能我能推广啊，我能推广，我能我能利用各种模板源，模板源的东西给给给搞出来。然后你发现要讲讲明白这个激光 SLAM 这个事...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-17-bilibili-bv1ekub6zelu-2026-196-slam-slam-ai.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
