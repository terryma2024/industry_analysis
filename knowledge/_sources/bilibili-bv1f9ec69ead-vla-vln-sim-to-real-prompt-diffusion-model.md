---
title: "【VLA+VLN】具身智能必备技术原理解析+模型拆解！Sim-to-Real/Prompt/Diffusion Model/长期路径规划算法"
type: source
date_created: 2026-09-17
last_updated: 2026-09-17
source_urls:
  - https://www.bilibili.com/video/BV1f9ec69EAD
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-17-bilibili-bv1f9ec69ead-vla-vln-sim-to-real-prompt-diffusion-model.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 【VLA+VLN】具身智能必备技术原理解析+模型拆解！Sim-to-Real/Prompt/Diffusion Model/长期路径规划算法

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1f9ec69EAD |
| BV / video id | `BV1f9ec69EAD` |
| Author | CV前沿与深度学习 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-17-bilibili-bv1f9ec69ead-vla-vln-sim-to-real-prompt-diffusion-model.json` |

## Transcript Excerpt

啊，大家好，这一节我们开始讲第四章节的第一小节。第四章的话是生成式控制与 VLA 架构，就是 Vision Language Action。 然后第一小节是 Volley 架构原理解析。过去机器人让动起来需要一套复杂的这个动力学公式和控制模块。但是随着这个 ChatGPT 等这个大语言模型爆发。就开始出现一个思路。既然大模型能看图预测下个词，那能不能就是直接预测机器人下个动作？这就是 V L A 就是 Vision Language Action 这个架构的起源。但是在实现这个 VRA 之前，我们面临一个核心的矛盾。就大模型的这个输入是离散的文本 token 每个词都是字典里确定的这个编号。真实世界的这个物理动作，它是连续的这个浮点数。要让大模型控制机器人的话，必须在这个数字世界的这个语言。和物理世界这个运动之间架一个这个类似于翻译的桥梁。这种桥的话就可以叫做动作词表化，就 Action tokenization 它的核心思想话就是，既然这个大模型只能输出单词。那就把机械臂的这个动作定义成字典里的这个一批新单词。只要大模型输出了这个特定的词，底层就知道这个机器人该往哪走。然后控制机器人就变成了一个类似于选择题了。我们以这个谷歌 RTE 为例啊，第一步就是先做规划，把这个机器臂的活动范围，不管是上下左右的这个极限速度。还是夹爪这个开合程度全部这个等比例压缩到0~1的区间内。这步的话非常关键，就它就抹平了这个物理单位的差异，让大模型不用再去这个纠结毫米和度的这个换算。第二步的话就是分箱，我们把这个0~1这个线段切分成256份，机械臂此时的话，这个状态落在哪个格子里。就给它贴上一个整数标标签，就是这二二百五十六个这个数字就成了一个大模型专属一个动作词汇表。比如只要告诉这个大模型输出第191号词，它就在这个指指挥机械臂执行某个特定的这个速度。这个当模型思考完毕，输出了一串这个整数 token 比如191， 102时，系统就会这个执行反向操作，就是动作解码。它会把这个它会查表，把这些数字反向这个映射回这个1~0，0~1的这个小数。然后再按比例放大回这个真实的物理坐标。最后发送给底层这个电电机驱动器，大模型就就能实现这个物理控制了。分箱技术它虽然好，但是如果机器人长得它不一样的话，比如说 Glaciar 这个 G0.5模型，它提出一种这个 ActionCordic 技术就是按部件分组，把双臂、夹爪移动底盘等这个映射到一个共享的二十七维动作空间。控制哪种机器人的话，只只需要激活对应部部位的这个动作 token 就能够控制不同的机型。最后如何解决这个256分相精度不够，还有这个动作抖动的问题呢？这就引出了这个残差向量量化量化这个。RVQ 这是一种这个先大调后这个微调的一个机制。就第一轮的话生成的 token 就是先决定一个粗略的这个动作框架，后续生成的这个 token 再对微小的误差进行一个补充修正。就因此的话，就就能这个细腻流畅地输出这个控制动作。好，这也到这，好，谢谢大家。

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-17-bilibili-bv1f9ec69ead-vla-vln-sim-to-real-prompt-diffusion-model.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
