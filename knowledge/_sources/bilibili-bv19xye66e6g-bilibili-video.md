---
title: "【十字路口】当具身智能走到十字路口｜和苏度、蚂蚁灵波、自变量、破壳：四种一线判断【视频播客】"
type: source
date_created: 2026-09-15
last_updated: 2026-09-15
source_urls:
  - https://www.bilibili.com/video/BV19XYe66E6G
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-15-bilibili-bv19xye66e6g-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【十字路口】当具身智能走到十字路口｜和苏度、蚂蚁灵波、自变量、破壳：四种一线判断【视频播客】

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Its standalone synthesis is [[_syntheses/bilibili-embodied-ai-crossroads-data-model-scenario-deep-dive-2026-09-15|具身智能十字路口：数据、模型与场景商业化验证]]; this card remains the traceable B-grade source record.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV19XYe66E6G |
| BV / video id | `BV19XYe66E6G` |
| Author | Koji杨远骋at十字路口 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-15-bilibili-bv19xye66e6g-bilibili-video.json` |

## Transcript Excerpt

那我们今天直奔主题。然后我们今天呢会聊这个三个话题，一个是数据之争，一个是智能之争，一个是场景之争。为什么都是各种之争呢？就是因为感觉在2026年，我们正处在一个十字路口啊，有非常多的没有收敛的路径在等着大家去探索。所以我们第一个问题呢，想这个请教韩峥总。因为我们今天这个在数据这方面，有人会认为要 BET 仿真，然后也有这个公司或者也有研究员在坚定的要 BET 真机。从您的角度，看你们在坚定的这个压铸仿真啊，就是当初的这个压铸是因为看到了哪些信号？然后到今天，你们有没有看到一些新的增强的信号？我首先讲一下，就是我们是这个坚信要使用仿真，但是同时呢，还有后面一句话，就是我们也坚信这个真实世界的数据的话，也是非常有用的。嗯，啊，并不是说纯粹用仿真。但我们其实出发点的话也比较朴素，从最早可能在15年16年开始做这个机器人的仿真器，合成数据的这条路，直到这个我们自己开始成立公司搞商业化版本的时候，其实是经历过两轮。啊，那么仿真包括基于模型的强化学习的这条路，在仿真器里边能够去进行大规模的强化学习。这条路本身呢，我觉得科研和这个啊，真正商业化的话是不太一样的。啊，科研的话，其实你可以用一些，比如说我们放出来的，开源的项目和数据算法当中的话，去做一些实验。但大家通常呢，就会试一下之后的话，不知道接下来再怎么去大规模的去修改到一个基础模型。所以大家一般就会停到那个位置上，或者是大家使用仿真的时候，会在，比如说这个偏传统的一些的控制方法里边的话，在。换成一些这个机器学习方法的时候，会用仿真器去做一些数据的补充，等等。但真正大规模做这个大规模预训练，基于模型的强化学习去做大规模的预训练的数据生成和训练的话。实际上现在市面上不管是我们之前的这些开源的仿真器，CPM、ManSGO，还是英伟达的 Isaac，在我们自己内部看的话，还是有一定的局限性。所以我们在24年之后，就是坚定地做了一个大规模的、完全重构的必然的数据，包括这个数据管线，然后包括仿真器管线。啊，到去年年底呢，我们大概在11月份、12月份的时候，也是在今年4月份放出来的一个结果。啊，就是让大家看到对于这个物体和环境包括光线等等当中的话，组合在一起的强化化。下的，比如说某些技能的操作，比如说像抓，包括后面我们放出来的一些这个，比如说像放置，包括一些组装类的任务的话，的确是可以在这个。物体和环境几乎没有限制的情况之下的话，几乎能达到100%的成功率。但是我们也坚信，就是说包括其他的这个路线的探索方式，最终大家呢还是会有一些这个上下分层，然后包括一些配合的方法。啊，我觉得各自都在探索这个不一样的路径。啊，但数据方面的话，我们还是坚持这个观点，就是光靠真实世界的数据收集呢，主要是效率。比较慢，质量呢有的时候的话也比较受限，所以仿真是绕不过去的。我觉得这也是最近一段时间，比如说在美国的我们的一些的这个同行，他们自己也开始加强。这个仿真器的能力啊，我们苏老师的一个学生，啊，其实也还是没有毕业啊，这个最近也加入了这个美国的一家公司，然后担任他仿真器的这个核心的负责人。我觉得这也是这个给业内有一些信号吧，虽然各自使用的方法不太一样。对。好的，谢谢。啊，那接下来有请这个沈雨君沈总啊。就宁波在数据路线上是非常明确的选了真实的数据。对，就在您的角度来看，就真实数据哪些方面是不可替代的？就是仿真是怎么都做不到的。那相比仿真的数据，它提供的这个就是最大的价值是什么？其实也不能说是不是坚决的选择了这个真实数据啊，就是数据这个事情，我们是这么看，在凌波内部啊，我们从来不觉得说哪一种数据是一定要选或者一定不要选的。就是可能不同的数据在不同的阶段能起到不同的作用。我们会认为在预训练阶段，就是可能比如说从互联网的数据啊，以及真实的物理世界采集的数据，可能就是作用更大一点。然后，但是如果你说，像刚刚韩老师也说，如果我们说回归到做一个某一个具体任务，就尤尤其是仿真其实在自动驾驶意义就比较大嘛。对，如果我们回归到具体的某一个任务本身的时候，仿真数据还是有价值的。这一点我们没有说仿真坚决不行啊，对，这这是先澄清一个事情。对，但是同时为什么我们会比较坚持的说从，就是预训练阶段的部分的数据更多从这个真实场景来呢？因为是是这样啊，就是我觉得机器人它处在，就是我们设想一下，机器人如果有一天真的能够在这个现实世界中干活，它可能跟现在数字世界很多模...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-15-bilibili-bv19xye66e6g-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-embodied-ai-crossroads-data-model-scenario-deep-dive-2026-09-15|具身智能十字路口：数据、模型与场景商业化验证]]
