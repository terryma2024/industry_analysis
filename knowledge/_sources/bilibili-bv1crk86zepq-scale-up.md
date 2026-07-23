---
title: "和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥"
type: source
date_created: 2026-07-23
last_updated: 2026-07-23
source_urls:
  - https://www.bilibili.com/video/BV1cRK86zEpQ
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-23-bilibili-bv1crk86zepq-scale-up.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1cRK86zEpQ |
| BV / video id | `BV1cRK86zEpQ` |
| Author | 张小珺商业访谈录 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-23-bilibili-bv1crk86zepq-scale-up.json` |

## Transcript Excerpt

哈喽，大家好！我是小俊。今天我们的嘉宾是蚂蚁凌波的首席科学家沈宇军。这是一家由蚂蚁集团孵化的机器人公司。作为一家科技服务公司，蚂蚁为什么要涉足机器人业务？与此同时，他们探索的这条只做巨声原生模型的道路，这其中的赌注与思考是怎样的？那接下来就是我对沈宇军的访谈。我还是很坚信巨声一定会有自己的模型。嗯。这个观点如果不变的情况下，那它的数据必须要支撑。他可以做自己的模型。如何把数据很好的 scale up 是一个至关重要的点。对。不及预期的有吗？不及预期数据。我觉得从现在行业来看。大脑可能是目前是落后于本体的。如果机器人有性格的话，你希望它是什么性格？啊，我希望它是个 J 人。它好干活。对。我觉得它核心还是要实用。哈喽，宇军，先给观众朋友们打个招呼。大家好，我是沈宇军，现在是在蚂蚁灵波科技担任首席科学家。之前在清华，然后后来到了港中文。对。讲讲你在人工智能上的一系列探索。也是阴差阳错吧，然后当时我在清华读书的时候。刚好赶上大三，然后那个时候是商汤刚成立的时候，2014年底商汤成立嘛，然后我们大三要求是必须要有一个这个暑期的实习。嗯，然后当时商汤就正好在清华的东门门口。然后当时反正就去了跟 AI 相关的这个领域吧。嗯。在那个商汤一直干到大学毕业，然后就刚好去那个港中文汤老师那边去读了个书。然后去的时候其实也比较迷茫，因为当时 AI 虽然说比较火，但是也不知道自己到底喜欢做什么。然后就哎，尝试了很多方向吧，然后像其实其实本来那个港中文吧，港中文比较擅长的其实像这种检测分割啊、分类啊，这个他们当时也是拿了比较多的冠军。但其实我个人对这个，就是打榜啊这个事情，最后就看一个 number 这个事情，我坦白讲，我自己不是非常感兴趣。对，然后呢，那个时候刚好有一个技术火起来了，当时就要对抗生成网络，就是 GAN。对，哦，对对对，然后那个技术火起来之后呢，其实就有很多人在这方面做探索嘛。然后那个时候我对这个事情就感觉比较有意思，因为它是能真的能生成一张图，然后让大家去看，然后甚至于你可以去做一些简单的编辑什么。然后那个时候我就从，就是算是选择了说我可能接下来要再做这个，可能是想要往这个生成模型这个方向去做。对，然后当时做的也是比较早，从17年开始就就是做生成模型然后可能做着做着然后那个时候也是有一系列比较火的工作出现嘛尤其是像 StyleGAN 那个系列的时候然后做着做着。因为我刚开始做生成，然后做做生成，那个时候比较火的可能就是一些图像编辑相关的东西，就是你怎么把它按照你想要的方式去调整一下呀，比如说把你变得更漂亮一点啊之类的。然后但做着做着就会发现好像做的太下游了，然后就想把这个东西看看能不能再往前做一做，就是从编辑再往前做，那就是现在可能大家会讲的更多，就是叫预训练嘛。嗯。对，那个时候其实还没有这个概念，说白了就是想训这个生成模型。对，然后但是再训一训就会发现，好像这个东西完全有点不太不太能受自己的控制。就是你除了，因为那个时候还没有说什么堆参数量啊，这些还没有这个相关的说法。然后就是感觉做着做着也不知道怎么能让这个模型变得更好了。然后就开始想说，那我再往前一步，就是从生成之前，那就是做表征嘛。然后可能就是这么一步一步的从最开始对数字不感兴趣，然后对生成内容感兴趣，然后再从编辑，然后再做到底层的训练，然后再从底层训练再往前做，做到表征学习，可能基本上一路就是这么过来的吧。今年年初的时候还在尝试做最后一次尝试，然后。还没死心。对，就是哪怕是在 Diffusion 火了之后嘛，然后后面又大家又又开始用自回归也去做一些这个生成。然后哪怕是这样的时候，我还是，就是我们团队还是坚持做了一段时间干的，skill up。嗯。然后怎么说呢？其实是取得了一定的效果吧。就是我们前一阵子做的一个干的模型，会 release 出来啊。然后那个时候会发现，跟 Diffusion 比确实是在某一些方面没那么好，但是也比之前的前几年的技术其实还是要进步不少的。对，就是说它还是有它的价值，但是它最大的问题还是计算量的利用效率太少了。就是因为 Diffusion 毕竟它可以不断的，就是它可以迭代好多次，然后生成一张图。然后我们就觉得，那对于生成特别复杂内容，尤其是你想要做这种视频的生成的时候，因为它就是里面的内容实在是太多了，然后可能干确实不一定是一个最好的。选择了。然后所以可能，我...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-23-bilibili-bv1crk86zepq-scale-up.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## 已完成综合

- [[_syntheses/bilibili-robbyant-native-embodied-model-strategy-deep-dive-2026-07-23|蚂蚁灵波具身原生模型战略访谈深度调研]]（R03 主分类，R04/R07 次分类）。

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
