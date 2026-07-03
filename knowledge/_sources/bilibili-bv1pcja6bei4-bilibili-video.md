---
title: "还写什么单片机代码啊？直接微信聊天就行！"
type: source
date_created: 2026-07-03
last_updated: 2026-07-03
source_urls:
  - https://www.bilibili.com/video/BV1PCjA6bEi4
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-03-bilibili-bv1pcja6bei4-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# 还写什么单片机代码啊？直接微信聊天就行！

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1PCjA6bEi4 |
| BV / video id | `BV1PCjA6bEi4` |
| Author | 工科男孙老师 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-03-bilibili-bv1pcja6bei4-bilibili-video.json` |

## Transcript Excerpt

最近 ESP32官方发布了一个针对爱好者的开源项目 ESP Club 那你可以通过用微信聊天的方式，让 ESP32去完成一些任务。比如说让它控制一个舵机转动。再比如说让它在屏幕上显示一段滚动的文字。那官方甚至给出了通过聊天实时生成小游戏的 demo 那这感觉以后使用单片机都不用自己亲自写代码，直接提需求就可以了。那所以呢，在看到这个项目之后，我连夜画了一块专门用来体验 ESP Cloud 的开发板。主控是 ESP 32杠 S3，另外的话还有一颗六轴的陀螺仪芯片、一块彩屏以及一些方便扩展的 IO 接口。那资料的话都上传到了立创开源广场，有需要的直接去嘉立创打板就可以了。接下去我们就一起来看一下这块开发板加上 ESPCloud 到底有哪些玩法，以及要如何在 ESP32里面部署 ESPCloud 最简单的就是控制一些外设，只需要把它们插在外设接口上，然后在微信中告诉 ESPCloud 你接了哪个接口，需要它干嘛就可以了。那对于这种难度 的应用完全没有任何的问题。然后让它试试生成一个 Chrome 的小恐龙游戏。生成是生成了，就是有一些小问题。我没有摁下按键，它也在跳，所以反馈一下这个问题。那他很快就发现了问题所在，原来是我没有跟他说清楚到底是高电平代表按键摁一下，还是低电平代表按键摁一下。那根据我的反馈，它还是尝试修复了这个问题。那现在的话就可以通过按键来玩这个游戏了。然后试试让它生成一个转动的3D方块。那这次的话出了点小问题，那不知道你能不能看得清楚，其实有一些粒子，但是太小了，反馈一下。仔细看一下，其实有那么点意思了，但是呢它没有线条。那再次反馈之后，他自己也意识到这个问题，就给改好了。那其实很多时候我们跟 AI 的交互就是这样，并不能指望它一次就生成你想要的效果。一方面大模型的能力是有限的，当然你使用更好的大模型，就可以拿到更好的效果。那另外的话呢，大部分人也很难一次就给出很详细并且精准的提示词。就像刚才那个小恐龙游戏，ESP32 并不知道低电平代表了按键按下还是松开。所以我们可以把一些特定的需求整理成 skill 说白了就是给 AI 一些经验指导和示例代码。让他尽可能的少犯错误。那 ESP Cloud 提供了一个 Skill Lab，上面有很多总结好的经验。比如说这个 Skill 就是告诉 ESP Cloud 要如何去网上获取 UP 主的粉丝数。我们只需要把这句话通过微信发送给 ESP cloud 就完成了这个 skill 的安装。然后你就可以去问它我当前的粉丝数了。那基于这个 skill 如果你想做一个粉丝计数器，也完全没有问题。只需要让它把我的粉丝数实时的显示在屏幕上就可以了。这是一个 IMU 的 skill 安装好之后呢，就可以启动一个平衡球的游戏。你要是对这个游戏觉得有哪些不满意的地方，也可以要求它进行修改。比如说要求它把球改为红色，并且放大3倍。那这就是我觉得 ESB Cloud 有意思的地方。对于任何一个应用，在你不满意或者有新的需求的时候，你都可以实时的去修改。所以 ESB Cloud 又是如何生成或者修改代码，并且又是如何实时的运行代码的呢？那过去我们写单片机代码，基本上都是用的 C 语言。C 语言是一种编译语言，所以我们需要使用电脑上的编译器，把 C 语言文件转换成二进制的文件之后，才能烧录到单片机中进行运行。除了 C 语言这种编译语言之外，还有一种脚本语言，比如说 Python JS Lua 那它们的特点就是代码写完之后不需要编译，直接就可以一行一行的执行。当然脚本语言能够这么运行，是因为预先在系统里安装了一段叫做解释器的程序。那这个解释器会一行一行地读取脚本语言的代码，并且去执行。所以我们平时所谓的安装 Python 其中主要就是在安装 Python 的解释器。那在 ESPCloud 程序的内部就集成了一个 Lua 的解释器，它可以实时地执行 Lua 脚本。那么 ESP Cloud 又是如何实时的生成 Lua 脚本的呢？这就需要借助于云端的大语言模型了。你可以通过微信发送指令给 ESP Cloud，那 ESP Cloud 收到信息之后呢，会根据它的记忆以及预设的提示词，对你的需求进行整理。然后发送给大模型，最终大模型就会生成一段 Lua 脚本返回给 ESP32 运行。那看到这里，如果你也想玩一下 ESP32 简...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-03-bilibili-bv1pcja6bei4-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
