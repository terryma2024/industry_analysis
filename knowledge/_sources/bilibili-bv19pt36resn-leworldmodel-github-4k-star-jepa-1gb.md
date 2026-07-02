---
title: "世界模型入门：LeWorldModel算法讲解 -- github 4k star的JEPA框架世界动作模型，1GB显存可运行"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV19pT36rEsN
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# 世界模型入门：LeWorldModel算法讲解 -- github 4k star的JEPA框架世界动作模型，1GB显存可运行

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV19pT36rEsN |
| BV / video id | `BV19pT36rEsN` |
| Author | 尤里卡AI |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb.json` |

## Transcript Excerpt

我们今天讲的是 Word Model，一个低显存、高推理速度的世界模型。我会分为四个部分来讲。近期世界模型非常火。一开始是火在视频生成，像 Sora Citations 这些模型，它也被用在空间重建上。比如李飞飞她做的世界模型，就可以用于3D 场景重建。最近一段时间，世界模型它在巨型智能领域也变得非常火爆。但遗憾的是，世界模型它的显存占用非常高，训练成本也非常高，加上它的推理延迟也大。所以实时性要求很高的场景，像是机器人，它就很难用得上。为什么之前的世界模型会出问题呢？因为之前的世界模型它都是偏向于像素级的预测的。像素级的预测就是它要预测出图像中的所有细节。像 Cities Sora 它都是像素级的预测。像素级的预测，它是可以直接输出图像数据的。所以像素级的世界模型，它可以用来生成图片。生成视频。这种世界模型，它的输出虽然细节很丰富，但是消耗的资源也很多，用于生成视频、图像都很好。但是如果用在极限的领域，就会增加它的训练成本，尤其是在显存占用上。那本文的那个 word model 它的输出并不是像素级的，虽然它可以使用原始的像素素材来完成端到端的稳定学习。但是它在预测的是浅状态。我们可以看这张图，它输入的是一张图片，这张图片输入到一个编码器之后，输出的是当前状态。这个当前状态是作为世界模型的的输入。当前状态和这个动作一起输入给世界模型，可以输出下一个时态的状态。下一个时刻的潜状态。就是模型的输出，意味着模型它有对环境的预测能力。但是它预测的并不是直接可以看到的像素，而是整体的潜状态。潜状态它更加的高维，虽然它没有大量的可以直观看到的视觉信息，但是它大幅度地提高了模型的推理速度。这种思路其实就很像回忆的画面，通常来说是比较模糊的，只能想个大概。比如我回忆我家的猫，我只能想出我猫大概轮廓。当我在回忆我的猫的时候，我的脑海中出现的这种很模糊的图像，它和这种浅状态就很类似。所以说人在回忆的时候，虽然也用到了画面，但是人思考的画面，它也是模糊的，并不会像现在的 C 语言或者 Sora 那样子有大量的细节。这或许就是为什么人的思考速度可以这么快。好在往下讲之前，我想给大家看下效果。我们先看官方放出的演示，看完之后我们再往下说。官方一共做出了四组实验。现在打开我的笔记，这四组实验我都已经跑完了。我们先看一下这四组实验是什么东西。第一个是推方块，在这个任务里面有一个二维的平面。 Agent 也就是这个蓝色的小圆圈，它推动这个方块。这个方块和这个方块要重合在一起。我们看一下这个实验具体跑出来的效果。这个是实验的示意图。他要把这个方块推到和它接近的位置，这就算他成功了。他的第二个实验是穿越房间。在它的第二个实验里面有两个点，一个是绿色点，一个红色点。它的任务要求是模型要控制这个绿色的点从起点到达目标的位置。目标的位置一定是在这个房间的右侧。我们看一下它的实际效果。这张图里面分为左半部分和右半部分。左半部分是模型要控制的点和它的环境，右半部分是给出的最终的状态。这个最终的状态是给模型进行参考的，就相当于是告诉模型最终它达到怎么样的效果。当它执行成功的时候，我们可以看到这个红色的球可以到右侧这个最终状态的。位置附近，啊表示它成功了。第三个任务是控制二维机械臂，它要让这个二维机械臂的关节到达某个角度。我们看它的运行效果，和刚才一样，它的右侧这两组，上，这边和这边都表示给的。目标状态，它以这个为目标。好，这边左侧是实际控制它的效果，可以看到它已经到达目标状态了。这个也到达目标状态。好，它最后一个是抓方块，它把这个方块移动到目标地点。实际上这个是实际可以用在机器人里面的。它的右侧这张图也是给的目标的状态，左侧是实际执行的效果。这四个就是它实际要做的任务。这里我做个总结，这个世界模型它的功能就是给定一个目标的状态，比如说这个目标状态是右侧的小红点的最终位置。这个目标的状态是它的机械臂的角度。这个的目标状态是这个小红的方块所在的最终位置。还有这些 b 所在的最终位置。这个的最终状态我没有画出来，但实际上给出的就是最终的这个 t 字它所在的位置。这个模型它可以通过最终位置来推断出要到这个最终位置。所需要的动作轨迹。好，现在我们已经知道这个模型是来干什么的，我们去往下说。往下说之前，我来介绍我的课程。啊，这门课程是事件模型的入门课。在这门课里面，我们会着重地讲雷沃德 mo...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
