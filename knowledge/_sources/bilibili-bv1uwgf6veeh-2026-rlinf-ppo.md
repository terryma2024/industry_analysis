---
title: "2026智源大会丨清华于超主讲：具身智能为什么需要强化学习？面向具身智能的高灵活大规模强化学习框架RLinf！—具身智能机器人/PPO算法"
type: source
date_created: 2026-07-28
last_updated: 2026-07-28
source_urls:
  - https://www.bilibili.com/video/BV1uwgf6VEeh
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-28-bilibili-bv1uwgf6veeh-2026-rlinf-ppo.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 2026智源大会丨清华于超主讲：具身智能为什么需要强化学习？面向具身智能的高灵活大规模强化学习框架RLinf！—具身智能机器人/PPO算法

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1uwgf6VEeh |
| BV / video id | `BV1uwgf6VEeh` |
| Author | 具身智能机器人入门 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-28-bilibili-bv1uwgf6veeh-2026-rlinf-ppo.json` |

## Transcript Excerpt

那第一场报告是我来分享我们团队近期做的面向具身智能的高灵活大规模的强化学习框架 RLinf 那我今天其实也主要想就是对我自己来说也是一个回顾，给大家讲一下 RLinf 在整个研发，我们大概9个月。的一个成长的故事线。首先呢，我其实只准备了第一页背景，就是想因为今天有两个关键词，一个是居身智能，一个是强化学习。所以其实在这一页只准备了一个背景，叫做我们为什么居身智能需要强化学习。那因为参会的主要是中国人，所以我就用了一句诗来表达，叫做纸上得来终觉浅，觉知此事要躬行。那么这句诗前半句其实讲的是我们从离线的 offline 的数据当中去学习，那么结论呢就是终觉浅，因为我们训练好的策略，这个模型。它从你离线学好，然后部署到它真实应该去运行的环境，不可避免地存在数据分布的偏差，从而其实就展现出大家所认为的这种泛化性差等等一些问题。那么应该怎么做呢？其实古人已经给出了答案，叫做觉知此事要躬行。那他这句话讲的是说我们应该从真实的、在线的交互数据当中去学习，通过这种学习方式，从而能够获得一个这种成功率更高的一个模型。那这个其实跟人类智能的增长过程也是非常相似的。比如说我们家小孩在学习搭积木，那最开始可能父母去教他怎么去搭这个积木，到后来他会自己先去尝试，这个过程他一开始会出错。几天之后，你可能某一天早晨起来发现，哦，他已经能够把这个积木成功的垒起来了。这个其实就是典型一个，他要通过在不断的这种真实的在线交互当中，才能够把这个智能给学给学习起来。其实从 cv 角度去理解，在今年拆，China3DV 上，孙浩老师其实也在传达这样的观点，叫做无交互不理解。只有通过跟这个物理世界真实的交互，才能够更好地理解这个物理世界当中的规律。其实这一点跟强化学习我们这一脉所一直讲的一个观点其实是类似的。那我们团队在强化学习和居身智能结合方面，其实从25年2月份开始就做了系列工作。为什么这个点这么深刻呢？是因为25年2月份是过年，然后我们课题组有个传统，大家要在过年前，然后聚个餐。表达对这一年努力的一个认可。那当时是 Deepseek RONE出来，所以当时在这种聚餐完之后，跟课题组同学们讲一件事情，说Deepseek RONE其实已经证明了在强化学习加大模型这件事情上，强化学习本身所能够展现出来的潜力。那么在强化学习加巨深大模型这一块，到底有什么样的作用？所以我当时想问同学一个问题，叫做相比较于数，纯这种我们可以称之为离线数据驱动的 SFT。强化学习，它训练后的这种具身大模型到底有哪些方面的优势？其实也就是说，我们需要明白它的机理是否是正确的，才能够在这个方向持续做一些投入。而在当时，其实业内至少具身智能这个领域，强化学习如何应用仍然是一个就是一个开放性的问题。然后当时这个同学其实做了一个事情，叫做把 PPO 跟这种巨神大模型去做了结合。其实当时他做这工作也非常不容易，但是回过头来看，方法已经不重要了，而是这个文章传达出来的结论是我到今天还是记忆比较深刻的。那这个地方我们其实做了 ood 测试，就是这种分布外泛化。我们因为它是 VRA 模型，所以我们从视觉泛化、语义泛化以及执行泛化三个层面，我们对强化学习训练后的模型和监督学习训练后的模型去做了这样的测试。结论是比较有意思的。相比较于 SFT，强化学习训练后的这个模型的这个 VRE 模型，它在语义和执行层面的泛化性提升是非常显著的。这个显著代表着说它的 performs job 会更加小。而对于世界泛化层面，强化学习训练后的模型和这种SFT 训练后的模型其实差别并没有那并没有那么明显。这个事情告诉我们，如果你想提升这个模型在视觉层面的泛化，那这个事情其实你并不需要强化学习去做，你把这个事情留给 SFT 做就好了。那如果你想提升它在语义和执行层面的一些泛化性，那这个事情强化学习还是比 SFP 更加擅长。那有了这一步，其实我们得到一个事情是，机理是可行的，但是同时我们也认识到另一个事情叫做系统是很拉胯的。那这个系统拉胯体现在哪呢？当时的认知是这个系统太慢了，因为我们组一般，比如说我们 weekly sync 对吧？我们要跟同学们每个周同步一下进展，但这个同学比较特殊，他要两个周才能跟我进，这种 sync 一次。原因就是一个周，它的模型还训不出来。它要两个周，一大概是一周半才能训出来。然后呢，再这种测评一下，然后给一点数据，所...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-28-bilibili-bv1uwgf6veeh-2026-rlinf-ppo.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.
- Completed synthesis: [[_syntheses/bilibili-rlinf-embodied-reinforcement-learning-infrastructure-deep-dive-2026-07-28|RLinf 具身强化学习基础设施视频深度调研]].

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
