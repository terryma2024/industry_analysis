---
title: "【机器人ROS2】1小时跟着大佬搞懂激光雷达工具和相机使用进阶，菜鸟学完即学即用！雷达过滤器/点云数据/雷达融合/具身智能机器人"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1LfTF6EEsG
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1lftf6eesg-ros2-1.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 【机器人ROS2】1小时跟着大佬搞懂激光雷达工具和相机使用进阶，菜鸟学完即学即用！雷达过滤器/点云数据/雷达融合/具身智能机器人

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1LfTF6EEsG |
| BV / video id | `BV1LfTF6EEsG` |
| Author | 具身智能机器人入门 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1lftf6eesg-ros2-1.json` |

## Transcript Excerpt

接下来进入我们的第二大节，激光雷达工具。那么在这啊，需要大家注意的是，这节介绍的知识点是极其重要的。以后啊，你工作当中呢，经常性的会使用到相关内容。好，首先呢，我们先看一下引言部分。在 ROS two 当中呢，我们可以使用各种强大的功能包。来处理激光雷达数据。当然这些功能包啊，一般都是工具性质的啊。紧接着他给我们介绍了三个应用场景啊，首先是第一种。其次呢是第二个应用场景。此外是第三个应用场景。逐一说明一下啊。先看场景一，我们可以进行雷达数据的过滤。通过去除异常点和噪声来提高数据的质量和准确性。在这也解释一下啊，大家看，当前我们这个无人车上，现在呢安装了一个激光雷达，而车体上啊，本身呢它是有一些附属物的。比如说，在这呢有四个支架，然后呢还有凸起的线束。另外呢，我还可能会安装一些其他的设备。这些附属物啊可能会对我们的激光雷达呢造成一定程度的遮挡。我们知道啊，激光雷达呢本身就是用来采集车周边的一个这个障碍物信息的。而在采采集过程当中啊，这些遮挡啊，可能呢也会被当成障碍物来给采集到了。那么很显然啊，这些数据呢其实是无效数据。在使用过程当中呢，我们需要将这些数据呢给过滤掉，给剔除掉。那么怎么过滤呢？怎么剔除呢？这时候呢，就可以使用 ROUND 里面。提供的现成的过滤相关的功能包了好，这场景一。嗯，接下来再看场景二啊。我们可以将多个雷达数据啊进行融合以获得更多的信息和更好的感知结果。还是啊，接着我们上一，上面这个介绍的啊。当前啊，由于车它本身啊对雷达造成一些遮挡，因此呢，会产生一些探测的盲区。那么有了盲区之后啊，我的有一些障碍物呢可能就感知不到了。这时候怎么解决呢？我们可以啊给车辆呢安装多个激光雷达。比如说我后面安一个。前面安一个，更有甚者呢，我还可以呢在上面也安一个。那么这多个激光雷达，它的盲区是不一样的，它采集的数据啊啊，这个呢可以做一个互补，然后把它们采集的数据融合在一起。融合在一起之后呢，就可以得到一个完整的周边环境数据了。这时候呢，就需要用到雷达的一个融合了。然后图里面相关的功能包也已经给我们提供好了。最后再看场景三，我们还可以啊将激光雷达数据。转换为点云数据反过来呢也可以将点云数据啊转换成激光雷达数据。点云数据呢，在这啊就是多线激光雷达呀，或者是这个深度相机采集的。那么这二者之间的互相转换有什么意义呢？首先说啊，前者激光雷达数据转点云，转面之后呢，我们就可以利用点云处理库。算法了那么这些处理库啊和算法呢，是有这期现实的应用场景的。像我在扫描过程当中啊，我想识别周边的一个环境的特征信息，比如说我想把这个圆柱形的物体呢。给它识别出来。这时候呢，在点云处理库里面就已经封装了相关的算法了，我们直接拿过来用就行了，就不需要你再自自自己去编写这个。去编写相关的这个功能实现了。由此呢就提高了我们的一个工作效率了。另外啊，对于路径规划和导航等任务，这是我们后面第四章要介绍的机人导航。机器人导航的时候呢，它只能够输入单线激光雷达数据，它不能使用点云数据。这时候呢，我们就可以将这个多线激光雷达呀，或者深度相机呀采集的点云数据转换成这个激光雷达扫描了。然后进一步呢就能够实现这个导航相关的功能了。好，等等啊。嗯，扫有这些功能啊，在 Notom 当中呢，都得到了支持，使得激光雷达的应用呢，更加灵活和强大，能够广泛地应用于进行导航、感知和建图。荣耀 WIN 手机 OK，这是工具的一个应用场景啊。接下来呢，我们再看一下这一大节下面我们要具体学学习的内容。这一大节下面呢有六小节，这六小节啊其实就是对应刚刚我们介绍的三个场景，对不对？第一二小节呢，是关于雷达过滤的。在这我们会分别有这个雷达过滤器的简介和应用啊两部分组成。然后三四小节呢，是关于这个雷达融合的，也是啊，有简介和应用两部分。五六小节呢，是关于这个点云数据。与激光扫描互转的。那么在这也是包含这个简介和应用啊两部分。好，OK。这是我们关于激光雷达工具的一个简介。这部分呢我就先介绍到这，视频暂停一下。

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1lftf6eesg-ros2-1.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
