---
title: "AI自己做科研了，那么人干嘛？#AI #AI科研 #英伟达 #人工智能 #科技改变生活"
type: source
date_created: 2026-07-15
last_updated: 2026-07-15
source_urls:
  - https://www.bilibili.com/video/BV1WLja6gEwq
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-15-bilibili-bv1wlja6gewq-ai-ai-ai.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# AI自己做科研了，那么人干嘛？#AI #AI科研 #英伟达 #人工智能 #科技改变生活

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. The ASR term “Empower/Empire” is corrected to ENPIRE in the linked deep research after primary-source verification.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1WLja6gEwq |
| BV / video id | `BV1WLja6gEwq` |
| Author | 新达同学 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-15-bilibili-bv1wlja6gewq-ai-ai-ai.json` |

## Transcript Excerpt

就在这几天，英伟达 GE AI 实验室联合 CMU 和 UC Berkeley 干了一件事。他们给 AI 分配了8个机器人，一堆 GPU 和一笔 token 预算，然后对 AI 说，学会插针脚。说完人就走了。接下来的时间，AI 自己去查论文、改代码，自己在真实世界里操控机器人跑实验，失败了还会自己分析改进再跑。几天后，他们回来看报告，99%的成功率。而这过程从头到尾没有任何人插手。为此，他们发布了这套名叫 Empower 的框架，全称是 Autonomous Robot Policy Self-Improvement in the Real World。 翻译成人话就是让 AI 变成 agent 在真实的物理世界里自己管自己，持续优化机器人操作策略。他们把这个方向叫 Auto Research 也就是 AI 自己做科研。那么具体是怎么做的呢？有四个模块，分别是 E N P I R 和 E。 E N 也就是 Environment 负责大环境，自动重置场景，自动打分。 Policy improvement 负责查论文、改算法、迭代策略。而 Rollout 负责在真实机器人上跑实验、录数据。Evolution 则负责把成功经验留下来，失败的砍掉。跨 agent 互相借鉴。他们测了一些任务，说实话都挺刁钻的。像是把细小的针脚精确插入盒子、用剪刀剪扎带、把 GPU 插到主板，全是高精度灵巧操作。最终策略成功率干到了99%。他们还同时测了三家的编程 Agent。分别是 Codex Claude Code 月之暗面的 kimi Code 三家都能跑通流程，但说到这里，它也只是一个很牛的科技新闻。下面我想聊点更深的东西。我们再来仔细看 Empower 这个循环，重置、执行、验证、改进。它本质是什么？是一个给定目标函数之后的最优化搜索，也就是给定标准，然后找最优解。结构上没什么区别，区别只在四个字，物理世界。之前 AI 的自主循环都在数字世界里跑，仿真力做到100%，但搬到真实世界可能就会直接掉到30%。这叫模拟与现实之间的差距。而 Empire 是第一次搬进物理世界，用真实数据闭环，这很厉害，但结构没变。所以我想问的是，AI 跑完这一整套科研流水线，它做的事和我们说的科研是同一个东西吗？形式上几乎一样，一个 Empire 的 agent 和一个博士生放在同一个任务上，查论文、做消融、记结果、调方法，80%重合，但还是有很大的区别，区别在 agent 跑到99%成功率之后就不动了。它满意了，它不会在某个瞬间停下来想等等，做到了99%。但这真的是正确的问题吗？他不会怀疑自己的问题，因为怀疑不在最优化循环里。爱因斯坦发现相对论不是因为比谁算得快，而是因为他问了一个没人问的问题，如果我追上一束光会看到什么？这个问题不是从数据里优化出来的，它是一个人对已有框架的不满，是一种觉得哪里不对劲的直觉，而这东西目前量化不了。所以，AI PR 真正证明的不是 AI 可以做科研了，它证明的是科研这件事正在裂成两层。下层叫施工，实验设计，代码实现，数据收集。上层叫选题，问什么问题，用什么标准，什么算成功。施工层正在被高速自动化，选题层则暂时还空着。而 AutoResearch 自动的是，也只是 research 这个动作，不是发现这件事。所以科研自动化之后，人不是没事干，而是人终于可以专心干那件只有人能干的活了。也就是我们常说的问一个好的问题。这里是辛达同学，如果你想及时了解最新科技、 AI 动态，关注我获取更多内容吧！

## Research Outcome

- 已完成单视频综合：[[_syntheses/bilibili-enpire-physical-autoresearch-deep-dive-2026-07-15|ENPIRE 真实世界机器人自我改进视频深度调研]]。
- 一级核验：[`SRC-ai-080`](../../raw/ai/documents/SRC-ai-080-enpire-agentic-robot-policy-self-improvement-in-the-real-world.md) 确认框架为 ENPIRE、四模块结构、任务范围与 `pass@8` 边界。
- 仍不可把本视频作为公司财务、政策、市场规模或通用机器人能力的一级证据。

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_syntheses/bilibili-enpire-physical-autoresearch-deep-dive-2026-07-15|ENPIRE 真实世界机器人自我改进视频深度调研]]
