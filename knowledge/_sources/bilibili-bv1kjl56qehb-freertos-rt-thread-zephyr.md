---
title: "FreeRTOS · RT-Thread · Zephyr——差距到底在哪？"
type: source
date_created: 2026-09-11
last_updated: 2026-09-11
source_urls:
  - https://www.bilibili.com/video/BV1kjL56QEhb
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-11-bilibili-bv1kjl56qehb-freertos-rt-thread-zephyr.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# FreeRTOS · RT-Thread · Zephyr——差距到底在哪？

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1kjL56QEhb |
| BV / video id | `BV1kjL56QEhb` |
| Author | 兆鸣嵌入式 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-11-bilibili-bv1kjl56qehb-freertos-rt-thread-zephyr.json` |

## Transcript Excerpt

FreeRTOS、 RT-Thread Zephyr 很多人以为这是三个同类产品，其实它们根本不在一个层级上。大家好，我是赵明，三家世界500强，11年一线嵌入式。这两年我自己项目里跑的阿涛斯越来越多换成 zefir 今天讲透为什么换，也讲透它什么时候不该用。这一期我想讲的长一点，因为这事三分钟讲不透，讲透了你能省好几年弯路。先说 FreeRTOS FreeRTOS是行业标配。啊，这话先放在前面，没有任何贬义。地球上跑的 MCU 里，跑 FreeRTOS 的数量谁都超不过。主仓库名字就叫 FreeRTOS kernel 注意这个名字，kernel。Readme 第一行写的很清楚，只放内核源码和移植层，别的不管。任务调度、信号量、消息队列，5套 heap 实现可选，静态分配也支持，动态分配也支持。这些核心在主仓库里都有，而且 FreeRTOS 这些年没停下。2023年底，多核 SMP 支持合入主线，一份代码可以跑单核，也可以跑多核。 MPU 内存保护、 ARM 安全区集成都在。2017年亚马逊云收购了 FreeRTOS，现在整个项目是亚马逊在维护。围绕着 FreeRTOS 一圈，亚马逊又拉起了一整套物联网库。 MQTT HTTP OTA 升级、设备影子全部在官方仓库。常支持版本今年4月刚出了一版，包了15个库，支持到2028年。所以你说 FreeRTOS 是什么？它是一个 RTOS 配上一整套亚马逊云物联网生态。但有一件事得讲清楚，绝大多数用 FreeRTOS 的人，真的就只用它的调度盒。任务、信号量、队列，啊，三板斧。为什么？因为它的设计是解耦的。内核是内核，网络栈是另一个独立仓库，文件系统又是另一个仓库，命令行解析也是另一个仓库。你想用哪一块，自己拼到工程里去。这种解耦好处是灵活，什么都能塞进， ST 恩智浦、瑞萨、 TI 任何一家厂商的 SDK 里按需取舍。代价是，它没有统一的一套跨厂商的设备模型。GPIO 怎么写？串口怎么读？I²C 怎么挂？FreeRTOS 自己不管，这部分全靠你或者你芯片厂商的库。你换厂商库要换，驱动要重写，应用层难免也得动。这是它的设计选择，不是缺陷，但你心里要有数。好，再看 RT-Thread 这个名字大家都熟啊，最新发布版本是 V5.2.2。去年十月发的，下个版本 V5.3还在开发周期里。RT-Thread 比 FreeRTOS 走得更靠近完整 OS 除了调度器，它主线自带一套文件系统、网络协议栈、设备驱动框架、 USB 传感器框架，这些都在主仓库里。 RT-Thread 还有一个 nano 版本啊，只剩调度器其内核，跟 FreeRTOS 是一个量级的。今天说 RT-Thread 主要说它的完整版。国产 MCU 常委小厂支持的风度，RT-Thread 第一。雅特力 AT 32、华大 HC 32、 N 32、和宙 APM 32、 HT 32。这一票小厂的 MCU，RT-Thread 主仓库里都有 BSP。 加起来五十来块板子。Zefir 主线对这一票几乎是0。中文文档一流，中文社区活跃，ENV 工具链对国内同学比较友好。这些我都得替他说一句公道话。有几件事也得说清楚，一查 Gitlog 就知道。第一件，头部国产芯片，Zephyr 主线已经反超，最典型的是乐鑫 ESP32，RT-Thread 主线，ESP32六块。 Zephyr 主线87块，差了14倍。而且 Zephyr 这87块，清一色乐鑫自家员工在维护。啊，博流 BL602，BL808那一家。RT-Thread 的主线0块，Zephyr 主线12块。新唐，RT Thread零块，Zephyr14块。瑞萨，RA系列，啊，瑞萨总部在日本，但 RA 这条线主要在国内卖。RT Thread零块，Zephyr33块。啊，瑞萨是 Zephyr 白金会员派人维护的。GD 32，RT 3 thread 24块，Zephyr 16块，差不多，两边都是社区在维护，都没有厂商自家员工的 commit。国产 MCU 总账，RT-Thread 主线81块，Zephyr 主线同口径146块，Zephyr 主线已经反超。第二件，厂商把 RT-Thread 当亲儿子在维护的，一查贡献者就知道。真正活跃在官方维护的 MCU 厂商只有先楫、 HPM Microchip 一家。邮箱后缀就是...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-11-bilibili-bv1kjl56qehb-freertos-rt-thread-zephyr.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
