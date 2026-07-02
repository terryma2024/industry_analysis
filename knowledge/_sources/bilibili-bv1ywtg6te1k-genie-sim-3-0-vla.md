---
title: "深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（下）"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1YwTg6TE1K
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1ywtg6te1k-genie-sim-3-0-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（下）

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1YwTg6TE1K |
| BV / video id | `BV1YwTg6TE1K` |
| Author | 寒墨阁 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ywtg6te1k-genie-sim-3-0-vla.json` |

## Transcript Excerpt

哈喽，观众朋友们大家好，欢迎来到韩默阁的频道。今天呢，我们继续来看我的这个仓库，就是关于支援机器人的。巨神智能仿真平台的一个，或者是说试用也好，评测也好，是这样的一个项目，也这样的一个工程。上一期呢，我们看到了 Stage One 和 Stage Two 的做。然后我们现在来看 stage three 这个呢就是说我们这支援机器人的 GenSim V3，已经给我们提供了一套工具链。让我们可以把在现实当中拍摄的视频，可以把它转化成在 Isaac Sim 当中可以使用的巨人智能仿真场景。这样的话在jenny sim 当中也可以进行使用。然后我就是做了一些手机的拍摄，啊，非常简单。啊，就是做了这样的一个静态场景。啊，就是左下角这个静态场景，然后另外三个呢，是希望作为动态物体来进行 机器人的操作，然后这个左下角就是机器人的一个操作台。但是呢，就是首先就是来到了我们的第一个局限，在它的文档当中其实是推荐使用它。一种比较独有的传感器来进行现场的采集。这是一种带雷达信息的这样的一种带深度像信息的相机。但是我呢是直接使用的是手机来进行拍摄，所以说并没有鲜艳的带有深度的信息，这样在重建和后期的对齐当中都会产生各种各样的问题。然后我们首先来看呢，就是一个可能是题外话，就是在就是这个支支援机器人的 jenny sim 当中，它本身就带有了一批啊，可以给我们作为示例的，它从三维世界当中实际提取出来的信息。转化出来的。具身智能的仿真场景。比如说我文字当中所说的这个所谓的 House D 杠二，这个就是在它的 jenny sim 当中，一个压缩包中已经存好了的，这个从实际当中提取出来的，我们可以看一下视频啊。它是大概是一个什么样子。我们把这样的一个场景放在Isaac Sim 当中，啊，就可以看到它具体的一个场景了。当然是人家是把这个文件组织好了的。它这是让是一个室内封闭环境啊，就是它的，我的意思是说它并没有一些漏洞啊、空洞啊等等，然后整体环境也会比较的规整。这就已经是一个 sim ready 的一个这样一个场景。然后它还，除此之外呢，除了这个这几个 house 之外呢，剩下还有一些动态物体，比如说这个冰红茶。啊，这个冰红茶物体。这个也已经变成了一个在 SAX sim 当中可以加载的数字资产。然后运行起来之后，它就因为重力，它就掉在地上了。好，因此呢，就是我们的目标就是把现实当中。啊，这是一个纸巾啊，这是一盒一一包纸抽。我们的目的就是把我们现实当中给重建出，给拍摄下来的场场景，重建出来，然后放到 ISIS 当中。是什么效果呢？我们按它的这个工具链呢，只是使用了比较就是比较原本的3D高审的一个重建，然后进行了一个 mesh 的提取，然后同时呢进行了一些 uv 贴片的烘焙。啊，这样的话就组织成了他这样他需要的一些资产的形式。啊，我们首先来看三 d gaussian 的重建的效果啊，这个因为我没有对拍摄的视频进行任何处理，比如说进行一些这个明暗的调整啊。甚至我拍摄的时候也并没有很注意空间的封闭性，啊，以至于这这一片是有，啊，在在在视频的这一片是有。大量空间是一个非封闭的，啊，它是与另外一个房间了。只只有中间的这个桌子，看上去还算是相对的完整。啊。另外可能会有物体在动啊，这个周围也也许会有。然后另外呢，在这个自动化的流程当中，我都是使用 Cloud Code 进行推进。这样的一个自动化的过程当中，生成出的这样的一个3D高深的产物，点云。啊，也并没有进行后续的一些处理，其实。比如说像这些杂乱的点云，你应该进行一些这个修修剪。啊，没有进行这些处理啊。所以说我们直接看一下它直接提取出来的 mesh。啊，麦氏呢，也就是比较一般了，这个地面啊，都是鼓鼓起来的，凸起来的，啊，中间的桌子还算完整。然后另外动态物体就效果可能就会更差一点，因为一开始做图像采集之后，我也并没有使用一些模型来。对它进行物体的剪切，啊就没有用一些 mask 把它给挑出来，啊直接是这样来进行重建和生成的，你想而易显而易见它是不会成功的。好，我们就最终看一下，把我的这个场景放到Isaac Sim 当中是个什么样子吧？啊，首先它是翻转的，它它还需要人工的进行调整，进行进行翻转，你才能把它正过来，看到大概是这样的一个桌子啊。而且呢这个桌子隐，就是隐去了很多细节。就是在智源的这个工具链当中，在最后 uv 烘焙的时候，如果...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ywtg6te1k-genie-sim-3-0-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
