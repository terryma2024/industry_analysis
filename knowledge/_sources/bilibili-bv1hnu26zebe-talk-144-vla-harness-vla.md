---
title: "【青稞Talk 144期】从 端到端 VLA 到 Harness VLA：面向具身智能与机器人操作任务的记忆增强式执行框架"
type: source
date_created: 2026-08-13
last_updated: 2026-08-13
source_urls:
  - https://www.bilibili.com/video/BV1HNu26ZEbe
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-13-bilibili-bv1hnu26zebe-talk-144-vla-harness-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【青稞Talk 144期】从 端到端 VLA 到 Harness VLA：面向具身智能与机器人操作任务的记忆增强式执行框架

> [!summary]
> Bilibili video source packet; its claims are separated and cross-checked in the linked deep research.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1HNu26ZEbe |
| BV / video id | `BV1HNu26ZEbe` |
| Author | 青稞社区 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-13-bilibili-bv1hnu26zebe-talk-144-vla-harness-vla.json` |

## Transcript Excerpt

大家好，我是张义贤，然后我是清华大学深圳研研究生院的硕士研究生。那今天我给大家分享一下我们组的这个一篇最新的工作，Harness VR A，主要是如何将一个冻结的 VR A 用一个用积极指导的 Agent 来让他做很多可信以及可泛化的操作的一个探索，一个做出了一个小小的探索。希望大家批评指正。然后我的导师是余超和丁伟博老师。也非常欢迎大家关注我们 Honey SORA 的网站啊，可以实时关注我们的进展。我们，其实 Honey SORA 目前还会做更多的工作以及解决更多尚未解决的问题。行，那就，那我接下来就简单和大家，也不是说简单吧，详细和大家介绍一下我们的工作。那我们的工作是基于这样的一个背景来做的，就是我们发我们发现或者说大家也知道目前的VRA 他们越来越强，越来越强，有非常多的方法让 VRA 训得越来越好，包括扩大模型啊，或者说扩大数据啊，各种数据合成啊等等。那现在的 那现在的 VRA 我们知道虽然它非常非常强，但是它们毕竟是要基于数据，啊一步步地学出来，所以 VLA 它也只能完成它在数据学习内做的事情，也就是在作为in the data distribution。做的那些内容。就比如说在下面的这个例子中，我们给威尔 a 一个任务描述，他拿起海绵，然后拿起拿起锅，然后把它放到水槽里，然后打开水龙头。那只要VRA 的数据里包含了这么一个 distribution 那它就可以比较，精准稳定地完成这个任务。但是在实际部署的时候就可能没有办法像之前 in in diffusion 那样那么轻松，因为我们毕竟啊物理世界啊，即使是仿真啊，数据都都是，毕竟是有限，特别。那在实际部署的时候，我们认为会产生一一种 deploy deployment shifts 的一种偏移。在这里我们大概总结了两种情况。一种是空间目标的一个偏移，另一种是语义的一个校正，或者说重新定位。这两种我们觉得是在实际部署的时候可能会很大的影响 VRA 的一个性能。一方面，比如说语义重新校准，就比如说在我们的任务描述里，我们训练 VRA 的时候，是让它先拿锅，再拿海绵，最后打开水龙头。那我们换一个，换个语句描述，比如说先打开水龙头。再拿锅，再拿海绵。那这个时候因为 v r a 它肯定没有经过这样的训练，所以它肯定不会按照你语义指导它的来做。所以他还还是会做之前先来海绵，先来锅再来海绵这样的操作。那这方面语义的这个重定位，是目是目前 VR 比较缺乏，因为也没有办法，因为我们确实没有这样的数据来训练它，不可能每一种语义组合的训练，它语义是在对于 VRA 来说依然是比较狭窄的。另一方面就是一些空间的偏移，就比如说我们虽然大虽然训练的数据和部署的场景可能差不多，但是可能这个桌面的纹理啊，这个锅啊，这个海绵换一个位置。然后水槽，换一个不同的长相，那这个时候，VIA 也因为它的这些空间的偏移，也会变得很不稳定。那如果它一次执行失败之后可能就会到达一些比较极端的位置，导致它 VLA 就没有办法再恢复，没有办法再 restage 让整个 VLA 的这个整个的 end to end 的一个 reward 变得非常的不稳定。所以这也是目前VLA 的一个问题。那大家可能如果是基于纯 VLA 的路线，大家可能会做的就是继续扩大模型。继续产生更多的数据，然后然后继续合成更多数据。我，我们认为这样这样的方法也非常非常好。但是我们就在思考能不能在扩大 YLA 的数据和 model 的同时，我们还有一些别的路径可以相辅相成，继续提升。那最近随着这个 Codian 的的一个迅猛的发展，也也这个也越来越多产生了一另一条路，叫 Code Agent as Policy 这这条路就和和 VRA 的控制就不太一样。 Code Agent as Policy 他们会用一个已经有非常强大的泛化性的一个多模态的 LM 模型，把它放到一个 codition 里面。那这个那它就可以自，他那他就可以充分地理解我们的任务描述。那这样就没有语义的重定位啊各种的问题了。那你输给 coding agent 的什么样的语义描述，它基本都能理解。另一方面，因为 codition 的多模态能力，泛化性也比较广，比起普通的 VRA 模型来说，那它也它很多时候也能理解这个。空间物体的变化，比如说锅锅不一样了，或者说海绵不一样了，或者说水槽不一样，...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-13-bilibili-bv1hnu26zebe-talk-144-vla-harness-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-harness-vla-deep-dive-2026-08-14|Harness VLA 视频深研]]
