---
title: "深度拆解 NVIDIA DLI 课程《从感知到预测：使用 Cosmos 3 开发物理 AI》"
type: source
date_created: 2026-09-12
last_updated: 2026-09-12
source_urls:
  - https://www.bilibili.com/video/BV1H1YL6YEZh
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-12-bilibili-bv1h1yl6yezh-nvidia-dli-cosmos-3-ai.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# 深度拆解 NVIDIA DLI 课程《从感知到预测：使用 Cosmos 3 开发物理 AI》

> [!summary]
> 已综合为 [[_syntheses/bilibili-nvidia-cosmos-3-physical-ai-course-selection-deep-dive-2026-09-12|NVIDIA Cosmos 3 物理 AI 课程与平台选型深研]]；视频中的成本、课程状态和安全/性能承诺保持 B 级。

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1H1YL6YEZh |
| BV / video id | `BV1H1YL6YEZh` |
| Author | GPUS开发者 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-12-bilibili-bv1h1yl6yezh-nvidia-dli-cosmos-3-ai.json` |

## Transcript Excerpt

好，我们现在开始今天的分享。我是 GPU s 开发者社区，Hock 陈。今天要跟各位分享的呢，是 NVIDIA DLI。 所提供的一个从感知到预测，使用 Cosmos 3开发物理 AI 的一个课程。如果对于 Cosmos 3不知道是做什么用的话，我们待会在内容里面都会讲清楚。 Cosmos 13，它是一个世界模型，World Model。这个模型呢，它具备了几种功能。第一个，它可以透过视觉的材料，包含是图像也好，包含视频也好。去进行推理，告诉我们说这个视频里面它到底有什么东西，然后在做什么。第二个呢，我们也可以透过这一个模型进行数据合成。因为很多时候我们要做一些物理 AI 的一些实验，或者是模型的生成。训练的时候呢，其实最痛苦的问题就是数据不够，质量不够。那 Cosmos 在这边呢，它提供了一个数据生成，就是我们给它一段视频。然后呢再根据我们提供的这个 prompt 它可以帮我们去生成各式各样符合这样要求的一个数据。这样的话，在我们未来在做物理 AI 的时候呢，我们要训练。各种不同场景的模型就会非常方便。第三个呢，它对于我们所要求的这个动作，它可以用顺向的运动学或者是逆向的运动学来帮我们生成说，比如说我们要让这个这个物体接下去要做哪些动作。它可以帮我们去生成说执行的这个策略。啊，所以 Cosmos 3非常非常的强大。主要我们今天的任务就是围绕在这三件事情上面。那这个课程我们要怎么找呢？首先一样，我们到 nvidia 点 cn 斜杠 training 里面呢，在线自主培训。在这个在线自主培训下面呢，我们找到这个物，仿真与物理 AI。啊，就会看到这边第一个就是我们今天所要分享的课程。好，点这个开始学习，就会出现到我们刚刚的这一个页面。这是一个收费的课程，所以我们如果要报名的时候呢，就到这边。购买此刻这个地方进去。啊，那因为这个过程呢，我们在先前的直播里面已经有提到过了，所以这边就不再赘述。等到你都弄完之后呢。像我这边已经是购买完了，所以我最后就进去这个 continue the learning 就可以开始这个课程。现在进到主页面，第一页给了我们一个实验室。但是不要一开始就先进去，我们先看一下它这个里面，下面有几个所谓的功能介绍，我们先把这些功能都了解之后呢，我们再进去。会比较好一点，不浪费时间。那首先我们来看一下 Cosmos 3的一个简介。它事实上最重要的三个主要功能就是我刚刚讲的推理。它是一个所谓的视觉跟语言的模型，VLM，Visual Language 的一个 model。 所以呢，我们可以导入视频或图像，它会帮我们去理解说目前这个视频里面有哪些东西。我们甚至于可以跟它去做 prompt 的一些交互动作，它会告诉我们更多的一些内涵。这个是第一个部分，叫推理。第二个呢，世界建模，这就是一个数据的生成。第三个部分就是在 action 建模，还有包含预测等等。它可以让我们把感知跟推理的结果转化成机器人或者自动驾驶汽车的真正具身决策。 Policy 还有控制的一个指令。所以这三件事情呢，是整个 Cosmos 最重要的功能。那这边呢，我们看一下 Cosmos 三架构。它是属于一个叫全模态的一个模型。单个模型它能够处理生成的本文，text 图像、视频、音频，还有动作。那在这里面呢，它最重要它有两个模块。第一个叫做推理的模块，是一种叫做自回归的，叫视觉语言模型。第二个模块呢，它是一个属于生成的模块，它一样是属于一种 diffusion 的一个 Transformer 方式，可以去帮我们生成更多的一个需求。我们在这边的输入可以是文字，可以是图像，可以是视频、声音，甚至于于是行为。根据我们所需要的要求去生成对应的内容。目前 Cosmos 呢，它提供三种不同大小的这个所谓的版本。对于我们正常的使用来说的话，一般我们大概是用到 NANO 会比较多。那接下来呢我们来看一下它的第一个功能叫做推理，就是在观察场景并且理解其中正在发生什么的能力。啊，它并不局限于说基本的场景的标注，就是你以前没有对这个东西做标注，没有关系。它它能够去理解了。好，这就是我们待会在 Notebook 的那个练习里面。会去用到的几个案例。啊，这边进去之后呢，就是选择一个，我们待会进去之后再说。好，要点跳过。那接下来一部分呢，我们就要来去做一个所谓的生成，generation。好，它会...

## Synthesis

- 深研页：[[_syntheses/bilibili-nvidia-cosmos-3-physical-ai-course-selection-deep-dive-2026-09-12|NVIDIA Cosmos 3 物理 AI 课程与平台选型深研]]。
- 一级交叉来源：`SRC-robotics-561`、`SRC-robotics-562`。

## Related Links

- [[ai/00-index|AI]]
