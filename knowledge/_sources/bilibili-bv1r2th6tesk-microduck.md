---
title: "Microduck硬件架构拆解"
type: source
date_created: 2026-09-02
last_updated: 2026-09-02
source_urls:
  - https://www.bilibili.com/video/BV1R2tH6tEsK
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-02-bilibili-bv1r2th6tesk-microduck.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# Microduck硬件架构拆解

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1R2tH6tEsK |
| BV / video id | `BV1R2tH6tEsK` |
| Author | Z-Rob |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-02-bilibili-bv1r2th6tesk-microduck.json` |

## Transcript Excerpt

最近机器人圈有一只小鸭子特别火，它叫 Micro Duck，看起来不大，身高大约25厘米，重量不到一公斤，外形甚至有一点像桌面玩具。但就是这么一台小机器人，上线之后很快就卖爆了。短时间内就做出了千万级人民币的订单额，而它的售价只有399美元。为什么一台看起来这么简单的小机器人会突然爆火？我觉得真正值得关注的其实并不是它长得可爱，而是它把过去看起来非常复杂的一整套机器人技术。压缩进了一台不到800克的小机器里。它有15个智能舵机，有 RK 3566 Linux 主控，有 IMU 有相机，有8×8 TOF 深度传感器。可以通过 WiFi 和蓝牙通信。更重要的是，它不是靠预设动作一帧一帧播放来走路，而是真的在运行强化学习训练出来的运动策略。它可以站立，可以走路，可以跌倒恢复，甚至还可以继续训练更多动作。但当我真正把 Micro Duck 的硬件架构一点一点拆开以后，发现了一件很有意思的事情。它其实一点都不豪华，没有 jetson，没有 RK3588，没有 EtherCAT，没有昂贵的无框力矩电机，甚至没有我们做人形机器人时经常看到的 STM32小脑。它真正的核心就这么几样东西，一颗 RK 三五六六，15个智能舵机，一条 Dynamic XO 总线，一颗主运动 IMU 然后在这套硬件上以50赫兹跑强化学习策略。所以今天这一期，我们就把这只最近特别火的小鸭子彻底拆开，看看它的 RK3566到底是哪块板？15个舵机到底是什么型号？一根串口线为什么就能控制整台机器人？IMU 为什么也要挂在舵机总线上？所谓的激光雷达到底是什么？50赫兹的强化学习控制到底怎么运行？以及最后一个最现实的问题。如果我们今天自己做一台国产版 Micro Duck 到底要多少钱？下面开始拆。第一张，Micro Duck 整机硬件架构，先不看细节。先看整机，Micro Duck 的整个硬件架构其实非常简单。最上层是一颗 RK3566，这颗芯片负责 Linux 系统、运动控制。强化学习策略推理、视觉、通信和系统服务。RK3566往下主要有三条链路。第一条 MIPI CSI。 连接前置广角相机。第二条 I2C，连接一颗8×8的 TOF 深度传感器。第三条，也是整台机器人最关键的一条，就是 UART。 URT 下去以后是一条 Dyna Mixer 智能舵机总线。这条总线上挂了15个舵机，同时还挂了一颗 I M U。所以，如果把 MicroDock 简化成一句话。 RK 3566是大脑，Dynamixel 总线是神经，15个智能舵机是肌肉，IMU 是平衡感官，相机和 TOF 则负责看外面的世界。它没有我们想象中的复杂控制网络，反而非常简洁。这也是 Micro Duck 最值得研究的地方。第二章，RK3566到底是哪块板？接下来第一个问题，Micro Duck 里面的 RK 3566到底是不是一块 CED 自己做的板子？目前从官方软件、设备配置和开发文档来看。可以确认的一点是，Micro Duck 在开发和 bring up 阶段使用的是 REX A03W。这块板非常小，尺寸大约只有65×30毫米。核心芯片就是 Rockchip RK3566，4核 Cortex A55，带 WiFi 带蓝牙，支持 MIPI CCSI 也有 GPIO 和 eMMC。但这里有一个细节，Microdot 官方参数写的是1GB 内存加32GB 存储，而 Reddit 的 ZERO3W 常规版本并没有非常标准的1GB 加32GB 组合。同时在 Microsoft 官方代码里，Red Sazero 三还被标成 provisional，也就是暂定目标。所以比较合理的推断是，前期开发大概率使用 Red Sazero 三 W。 到了真正 seed 批量生产以后，不排除使用定制 RK3566板卡或者定制内存 eMMC 组合。所以如果我们自己要参考 Microdot 没必要执着于 Redmi 3W。真正值得记住的是，一颗 RK3566级别的芯片就已经足够完成这台机器的全部核心任务。第三章，15个舵机到底是什么型号？Micro Duck 一共有15个电机。这里不是普通 PWM 舵机，而是 Robo Otis 的 Dynamixel 智能舵机。从官方强化学习项目以及执行器模型来看，使用的是 XL330系列。结合机械参数和第三方逆...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-02-bilibili-bv1r2th6tesk-microduck.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
