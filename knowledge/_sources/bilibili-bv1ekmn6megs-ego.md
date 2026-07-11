---
title: "具身智能真正基建：Ego无机器人数据采集平台拆解"
type: source
date_created: 2026-07-11
last_updated: 2026-07-11
source_urls:
  - https://www.bilibili.com/video/BV1eKMn6MEgS
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-11-bilibili-bv1ekmn6megs-ego.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 具身智能真正基建：Ego无机器人数据采集平台拆解

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1eKMn6MEgS |
| BV / video id | `BV1eKMn6MEgS` |
| Author | 失控的PM |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-11-bilibili-bv1ekmn6megs-ego.json` |

## Transcript Excerpt

哈喽，大家好啊，国内的一家公司奥比中光啊，发布了一个无机器人数据采集硬件平台。这是它的一些标准型无机器人硬件的这个采集套件。我们来看看是个啥？它已经完整的发布了。有双目的，有四目的，有外部相机，有5米，这就是它的一个整套方案。它还可以做一些定制啊。 OK，我们回到这个，Ego 吧。这整个呢就是他们的一整套方案啊。有不同的 ego 的采集啊，包括umi 的设备啊，包括它的连接方式。那这个产品呢？这个 ego 呢，不是一台 gopro 啊，而是一台这个数据采集设备。很多人第一次看到这样的一个 ego 啊，都会觉得，哎，这不就是两颗摄像头吗？如果只是录像，它和 GoPro 手机、运动相机呢，确实很像。但是如果把它接到机器人训练流程里面啊，它们就是完全两种不同的产品。那普通的运动相机呢，只负责拍一段 MP 四啊，视频拍完呢，这件事情就结束了。但对于机器人来说，一段 MP 四啊，是根本不够的。啊，机器人不仅要知道我看到了什么，还要知道每一帧是什么时间，相机当时在哪里，设备有没有换动，左右相机是不是完全同步，imu 在这一刻踩到了什么。所以呢，这个，Ego 真正卖的并不是一段视频，而是一套可计算、可训练、可复现的原始数据。啊，raw data。 GoPro 呢是一个记录视频，Ego 呢是记录一个可计算的世界。那很多人会问啊，这样的一个 Ego 设备，录一次视频为什么会保存这么多文件呢？啊，十几类原始数据。啊，其实啊，这些文件呢，没有一个是多余的。啊，例如这个元数据啊，它会记录设备啊，任务场景和版本。左右相机的视频啊，记录机器人真正看到的世界。左右的时间戳呢，保证每一帧都知道是在什么时间拍的。那音频呢，可以记录一些环境的一些声音。相机的标定文件呢，就是告诉算法相机到底是长什么样。IMU 的数据呢，就是记录设备这一刻是怎么运动的。 Camera IMU 的标定呢，就是告诉算法 IMU 在相机的什么位置。所以这不是十几个文件，而是一段 episode 的完整的数字化描述。你拿着这些高质量的原始数据，未来无论是重新计算深度啊，重新跑 VIO 重新生成点云，都可以重新去计算。这也是为什么我一直在强调，Ego 采集的不是视频，而是训练数据。Ego 这个产品真正难的不是做硬件啊，而是让所有的数据呢。完全的对齐。其实呢，做一个双目相机啊，我相信现在很多的公司都会，啊，甚至找一个 odm 厂商呢，几个月就能做出来。我看到社交网络平台呢，也有很多设计很好看的一些设备。但真正难的是让所有的传感器描述的是同一个世界，同一个时间。比如左相机拍的是上午10.01秒，001毫秒。那右相机呢也必须是这一刻，imu 采样也必须对应这一刻，音频也必须对应这一刻。否则算法会认为相机看到的是 A imu 感受到的是 B。那整个 V I O 呢都会飘。所以啊，Ego 最核心的能力不是镜头，而是工程能力。这就包括了高精度的标定。啊，Camera 与 IMU 的标定，硬件的同步。啊，统一的时间戳，硬件长期的稳定性，还有规模化的制造。啊，真正的门槛呢，从来不是硬件，而是工程化的一致性。那为什么这些参数都和数据的质量会有关系呢？我们看过很多的产品介绍啊，喜欢一上来呢把所有的参数啪摆一遍。但是在机器人行业呢，我觉得这个参数啊要特殊的去解释一下。每一个参数为什么会存在？比如说为什么要全局快门？因为机器人一直在运动嘛，人带着这个 ego 呢也是在运动。如果还是卷帘的快门呢，画面可能会发生变形、模糊啊，特征点呢都会飘。为什么 mcu 要做到400赫兹呢？因为相机只有30或60帧，两帧之间发生了什么？只能靠 IMU 去补。为什么要小于一毫秒的同步呢？因为 camera 跟 IMU 的描述啊，必须是同一个动作。如果差了几毫秒，机器人看到的世界就已经不是刚才的那个世界了。所以这些参数呢，并不是说为了堆配置，而是在保证最终输出高质量的 raw data。只有高质量的原始数据呢，才适合 VLA 世界模型的一个训练。奥比中光主要卖这个 e 狗呢，加这个 SDK 啊，其实是巨神智能的基础设施。硬件加 SDK 呢，输出的是原始数据。红色虚线框起来的部分呢，就是机器人本体公司啊、数据采集公司呀、 VLA 或者世界模型公司啊，他们根据自己的需求去做数据的质检啊、清洗啊、标志啊、语义啊等这样的一些工具链。通过 SDK 呢去做...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-11-bilibili-bv1ekmn6megs-ego.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
