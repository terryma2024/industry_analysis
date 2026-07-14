---
title: Monte Carlo Tree Search
type: entity
date_created: 2026-07-14
last_updated: 2026-07-14
aliases:
  - MCTS
  - 蒙特卡洛树搜索
  - Monte-Carlo Tree Search
sources:
  - https://doi.org/10.1007/11871842_29
  - https://doi.org/10.1109/TCIAIG.2012.2186810
  - https://arxiv.org/abs/2410.10762
  - knowledge/news/2026-07-14-harness-engineering-self-improvement-deep-dive.md
  - raw/_inbox/articles/2026-07-04-lilian-weng-harness-engineering-for-self-improvement.md
tags:
  - entity/algorithm
  - industry/ai
  - search
  - planning
  - reinforcement-learning
  - agent
status: active
---

# Monte Carlo Tree Search

> [!summary]
> Monte Carlo Tree Search（MCTS，蒙特卡洛树搜索）是一类用反复采样来指导树搜索的规划算法。它不穷举整棵决策树，而是在“继续搜索已知高分分支”和“尝试尚未充分探索的分支”之间动态平衡，把有限计算预算逐渐集中到更有希望的区域。

## 实体信息

| 字段 | 内容 |
|---|---|
| 中文名 | 蒙特卡洛树搜索 |
| 英文名 | Monte Carlo Tree Search |
| 缩写 | MCTS |
| 类型 | 搜索与规划算法 |
| 核心思想 | 树搜索 + 随机/策略采样 + 结果回传 |
| 典型选择规则 | UCT（Upper Confidence Bounds applied to Trees） |
| 典型应用 | 棋类、序列决策、规划、强化学习、程序与 Agent 工作流搜索 |
| 关键矛盾 | 探索（exploration）与利用（exploitation）的平衡 |

## 一句话理解

面对大到无法穷举的决策树，MCTS 会一边试走不同路线，一边把结果沿路径反馈回来，逐渐学会“哪些方向值得继续投入计算”。

它不是纯随机搜索：**随机或策略化模拟负责提供样本，树上积累的访问次数和奖励统计负责指导下一次试哪里。**

## 它解决什么问题

MCTS 适合以下情形：

- 决策需要连续进行多步，天然形成树结构；
- 分支多、深度大，完整穷举不可行；
- 很难为每个中间状态手写精确评价函数；
- 可以通过模拟、执行或 rollout 得到结果分数；
- 计算预算可以逐步增加，希望“算得越久，通常判断越好”。

> [!warning] 适用边界
> MCTS 不是所有搜索问题的默认最优解。如果分支极多、一次 rollout 很贵、奖励噪声很大，或无法快速评价候选，MCTS 也可能成本过高或收敛缓慢。

## 核心循环

```mermaid
flowchart LR
    A["Selection\n选择"] --> B["Expansion\n扩展"]
    B --> C["Simulation / Evaluation\n模拟或执行评估"]
    C --> D["Backpropagation\n结果回传"]
    D --> A
```

### 1. Selection：选择

从根节点向下，根据树上已有统计，反复选择一个既有潜力、又值得继续了解的子节点。

### 2. Expansion：扩展

到达尚未充分探索的节点后，添加一个或多个新子节点。子节点代表新的动作、方案或工作流版本。

### 3. Simulation / Evaluation：模拟或评估

从新节点继续运行，直到获得可评分结果。传统游戏可以随机落子到终局；Agent 系统可能直接执行候选工作流，再按正确率、单元测试、成本或延迟评分。

### 4. Backpropagation：回传

把本轮奖励沿访问路径向上传递。路径上的每个节点都会更新访问次数、累计奖励或平均奖励，使后续选择更有依据。

## 核心公式：UCT

常见 UCT 选择规则可写为：

$$
\operatorname{UCT}_i
=
\frac{Q_i}{N_i}
+
c\sqrt{\frac{\ln N_p}{N_i}}
$$

| 符号 | 含义 |
|---|---|
| $Q_i$ | 子节点 $i$ 的累计奖励 |
| $N_i$ | 子节点 $i$ 的访问次数 |
| $N_p$ | 父节点的访问次数 |
| $c$ | 探索系数，控制探索强度 |

UCT 由两项组成：

$$
\underbrace{\frac{Q_i}{N_i}}_{\text{利用：平均成绩}}
+
\underbrace{c\sqrt{\frac{\ln N_p}{N_i}}}_{\text{探索：访问不足的奖励}}
$$

- 第一项高：这条路线过去表现好，值得继续利用；
- 第二项高：这条路线尝试得少，当前结论不可靠，值得探索；
- 随着 $N_i$ 增加，探索奖金下降，算法会逐渐根据真实平均表现作选择；
- 未访问节点通常被优先试一次，具体实现可把其 UCT 视为正无穷或单独处理。

### 探索系数 $c$

- $c$ 较小：更偏向当前高分分支，搜索更“贪心”；
- $c$ 较大：更愿意探索陌生分支；
- 不存在跨任务统一最优的 $c$，需要根据预算、奖励噪声和漏掉新路线的代价调整。

## 小例子

假设父节点已访问 100 次，取 $c=1$：

- A 分支访问 50 次，平均奖励为 $0.8$；
- B 分支访问 2 次，平均奖励为 $0.5$。

则：

$$
\operatorname{UCT}_A
=0.8+\sqrt{\frac{\ln 100}{50}}
\approx 1.10
$$

$$
\operatorname{UCT}_B
=0.5+\sqrt{\frac{\ln 100}{2}}
\approx 2.02
$$

虽然 A 的已知平均成绩更好，但 B 几乎没被探索，探索奖金使 B 暂时获得更高优先级。如果继续尝试后 B 仍然很差，它的探索奖金会下降，搜索资源会重新回到 A。

## 与相邻搜索方法的区别

| 方法 | 核心做法 | 相对特点 |
|---|---|---|
| 随机搜索 | 随机抽取候选并评价 | 简单，但不系统复用树上经验 |
| 贪心搜索 | 每轮只扩展当前最高分候选 | 便宜，但容易过早陷入局部最优 |
| Beam Search | 每层保留固定数量高分候选 | 适合分层生成，但探索规则通常更固定 |
| Minimax / Alpha-Beta | 按对抗性最优策略搜索 | 需要较明确的博弈结构和叶节点评价 |
| MCTS | 采样、树统计和探索—利用平衡 | 能把预算聚焦到有希望分支，适合难以穷举的序列决策 |

## 在 Agent 与 Harness 搜索中的映射

[[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering 深度研读]]提到的 AFlow 把 Agent 工作流表示为图和代码，再使用 MCTS 搜索候选工作流。

| MCTS 概念 | Agent 工作流搜索中的含义 |
|---|---|
| 根节点 | 初始工作流 $W_0$ |
| 树节点 | 一个完整的 Agent 工作流版本 |
| 子节点 | 在父工作流上修改得到的新版本 |
| 扩展 | 让 LLM 修改 prompt、控制流、工具或角色组合 |
| 模拟/评估 | 实际执行工作流处理 benchmark 任务 |
| 奖励 | 正确率、测试通过率、成本、延迟等指标 |
| 回传 | 把候选表现更新到该节点和祖先节点 |

这使系统能够保留多条改进路线。某个修改短期得分一般，但其后续组合可能很强；MCTS 比只沿当前冠军继续修改的贪心方法更有机会保留这种路径。[AFlow 论文](https://arxiv.org/abs/2410.10762)将工作流优化明确表述为代码表示空间中的搜索问题。

## 工程实现中的关键设计

### 状态和动作定义

必须先明确一个节点保存什么，以及从节点可以执行哪些动作。若动作空间允许 LLM 任意重写全部系统，分支数会迅速失控，也难以归因哪项修改有效。

### Rollout 与评价器

评价器决定搜索方向。只优化单一 benchmark，可能产生过拟合、测试投机或 reward hacking。Agent 场景宜同时记录质量、成本、延迟、安全与可维护性。

### 预算与停止条件

常见预算包括最大扩展次数、总 rollout 数、token、时间或费用。AFlow 一类系统也可以在 top-$k$ 候选平均分长期不再上升时停止。

### 随机性与重复评估

LLM 调用和环境执行可能具有随机性。单次高分不一定可靠，重要候选应重复运行，记录均值、方差和失败分布。

### 树之外的状态

经典 MCTS 通常假设节点价值可以由稳定分布估计。如果模型、数据、工具或 evaluator 在搜索过程中持续变化，旧统计可能失效，需要版本隔离、衰减或重新评估。

## 易错边界

- “Monte Carlo”不等于完全随机；现代实现可以使用策略模型、价值模型或启发式规则指导 rollout。
- UCT 是 MCTS 的常见树策略，不等于 MCTS 的唯一实现。
- MCTS 没有保证在有限预算下找到全局最优解。
- 更多 rollout 通常改善估计，但前提是模拟与奖励能代表真实目标。
- 在 Agent 搜索中，一个“节点”应是可复现、可版本化的工作流，而不是只存在于聊天上下文中的临时描述。
- 树搜索得到的高 benchmark 分数不自动等价于更安全、更便宜或更易维护的系统。

## 来源

- Kocsis, Levente; Szepesvári, Csaba. [Bandit Based Monte-Carlo Planning](https://doi.org/10.1007/11871842_29), ECML 2006。UCT 的原始论文来源。
- Browne et al. [A Survey of Monte Carlo Tree Search Methods](https://doi.org/10.1109/TCIAIG.2012.2186810), IEEE Transactions on Computational Intelligence and AI in Games, 2012。MCTS 核心循环、变体与应用综述。
- Zhang et al. [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762), ICLR 2025。MCTS 用于 Agent 工作流代码搜索的实例。
- [[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering for Self-Improvement 深度研读与公式通俗解释]]。
- [Lilian Weng 原文抽取](../../raw/_inbox/articles/2026-07-04-lilian-weng-harness-engineering-for-self-improvement.md)。

## 关联连接

- [[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering 深度研读]]
- [[ai/00-index|AI 研究入口]]
- [[Rollout|Rollout 执行评测]]
- [[PolicyModel|Policy 策略模型]]
- [[Baseline|Baseline 基线]]
- [[_entities/README|Entities Layer]]

