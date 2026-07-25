---
title: "模型越强， Superpowers 和 MattPocock-Skills 应该删除谁？"
type: source
date_created: 2026-07-23
last_updated: 2026-07-23
source_urls:
  - https://www.bilibili.com/video/BV1KtKY6RExA
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-23-bilibili-bv1ktky6rexa-superpowers-mattpocock-skills.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# 模型越强， Superpowers 和 MattPocock-Skills 应该删除谁？

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1KtKY6RExA |
| BV / video id | `BV1KtKY6RExA` |
| Author | AI随风随风 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-23-bilibili-bv1ktky6rexa-superpowers-mattpocock-skills.json` |

## Transcript Excerpt

大家好，在 AI 编程的工作流里面，有两个非常流行的工作流啊。一个是 Superpulse，那么在 GitHub 上的 stars 已经有258K了。那么还有一个是最近冒起来非常火的 Marty Skills，那么在 GitHub 上也有180K了。而且这两个工作流呢，里面有些技能是非常相似的。那么这就会导致一个问题，那在使用过程中应该选择谁呢？模型越来越强之后，哪个工作流对模型的支持是最好的？哪个工作流对模型又起到反作用呢？那本期视频就来给大家详细的讲解一下这两个工作流该如何选择以及区别。首先我们来理解一下模型的发展到底是在发展什么，那对于我们跟 AI 进行对话，我们输入了我们的需求，然后模型会进行推理，然后最终会输出我们要的代码。那么模型在发展，在版本在迭代，在升级的时候，它就会把自己的这个推理能力和和支持更长的任务，也就是更长的推理。所以这块能力是在提升的。那这块能力的提升就会导致我们的输入有可能会产生变化。那比如说在模型比较差的情况下，那么我们的输入要更详细点，我们要告诉他怎么做，第一步怎么做，代码的接口什么样子的。那么他收到我们这个更加详细的需求之后，他的推理的这个难度就会减少，所以搜出来效果会更好。那等模型越来越强之后，也就是他推理能力越来越强之后，这就要求我们的输入，也就是我们的需求过程的细节要少，我们要更注重的是我们要它实现的目标是什么。验证这个实现目标的条件是什么？那整个实现过程全部靠模型的推理去完成，我们就不再需要去详细定义这个过程的细节了。这个就是模型增强之后，我们跟模型之间的提示词的变化。所以总的来说，不管是你工作流还是技能带来的问题都是一样的。比如说在模型越弱的时候，技能提供的是更加详细的过程，这种约束。那么模型变强之后，如如果你提供的还是很详细的这个过程约束的话，那么给模型带来的就是更臃肿的上下文，也限制了它的推理的效果。所以这个是一个模型变强之后技能的变化。那这两个工作流哪一个工作流违反了我们刚刚讲的模型变强之后提供了过多的细节呢？那接着往下看。首先我们来了解一下这两种工作流常用的这个技能啊。第一个呢就是 MATE 这个工作流，它是从 GreaseDOS 这个技能会跟你进行一个需求对齐沟通，然后呢会转换成文档，ToSpec，然后再把文档进行一个垂直拆分。然后再去执行，然后再去 code review，最后去提交发布。那么这是一个常用的工作流啊。那 super pose 工作流就是首先是头脑风暴，风暴完之后会生成一个文档，那么基于这个文档再去调用这个 writing plans 去写这个计划文档。那写了计划文档之后，就可以用这个 tdd 或者说其他的这种执行计划的这个技能啊去执行，然后再去 review 呢，再去发布。两者的流程是非常相似的，都是需求对齐，计划然后拆分，然后再执行，再验收。所以整个过程是非常相似的。那我们再详细的对比一下几个核心的技能啊。那第一个就是需求对齐，那 Matt 这边是 gray with doors。 那 Superforce 这边是头脑风暴。那我们首先来看一个动画的演示，来对比一下这两个技能在需求对齐这个维度上有什么区别。那我们可以看下 Match Skills 里面，首先会拆出四个分支。那么基于四个分支，比如主体是谁，然后去回答，去问答。然后如果说主体这个分支的问题都解决了，他又会回来，回到第二个分支，比如状态。你有订单有什么样的状态，然后如果这个解决完之后，他再回到这边，售后有什么问题，然后所有的分支的问题都解决了之后，他会形成一个共享的理解。一些领域的词汇，比如说一些奇异点啊，一些重大决策啊，都会记下来。所以你使用 Multi-Skills 里面去进行句子对齐的时候，那么它会对完之后会形成一些文档，在后续过程中会起到非常重要的作用。我们再看一下 Superpulse，那么它这边的话是使用苏格拉底式的提问，也就是说它会针对当前代码库或者说你的详细的需求文档啊，来进行问题的追问。比如第一个问题。问的是什么时候算下单成功？如果你回答支付完成算下单成功，那么他就会针对这个支付完成，又会更详细地往下追问。他是一层一层地往下追问的，所以说这叫苏格拉底式的提问。然后最后经过几轮的问答之后，他觉得 OK 没有问题了。那么会那生成一个这样总的一个文档。所以这两个技能其实在需求对齐这个维度上...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-23-bilibili-bv1ktky6rexa-superpowers-mattpocock-skills.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
