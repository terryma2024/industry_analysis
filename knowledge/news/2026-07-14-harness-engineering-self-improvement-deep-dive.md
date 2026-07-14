---
title: Harness Engineering for Self-Improvement 深度研读与公式通俗解释
type: news-summary
date_created: 2026-07-14
last_updated: 2026-07-14
sources:
  - raw/_inbox/articles/2026-07-04-lilian-weng-harness-engineering-for-self-improvement.md
  - https://lilianweng.github.io/posts/2026-07-04-harness/
  - https://arxiv.org/abs/2601.21557
  - https://arxiv.org/abs/2310.02304
tags:
  - industry/ai
  - agent
  - harness-engineering
  - context-engineering
  - recursive-self-improvement
  - math-explainer
status: active
aliases:
  - Harness Engineering 深度研读
  - AI Harness 公式通俗解释
---

# Harness Engineering for Self-Improvement 深度研读与公式通俗解释

> [!summary]
> 文章最重要的判断不是“AI 已经能自己改写大脑”，而是：**短期内更现实的自我改进对象，是包围模型的运行系统（harness），而非模型权重本身。** Harness 决定模型看见什么、如何循环、能用什么工具、怎样保存记忆、如何验收、何时回滚。文章中的数学公式都在描述同一件事：把“上下文、工作流、改进器”从人写死的规则，变成可被搜索、评分和迭代的软件对象。

## 来源与研究边界

| 项目 | 内容 |
|---|---|
| 原文 | [Lilian Weng, Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) |
| 发布信息 | Lil’Log，2026-07-04，作者 Lilian Weng |
| 原始快照 | [Defuddle Markdown 抽取](../../raw/_inbox/articles/2026-07-04-lilian-weng-harness-engineering-for-self-improvement.md) |
| 抽取方式 | `defuddle parse <url> --md`；正文和 LaTeX 公式完整保留，网页图片仍使用远程 URL |
| 交叉核验 | [MCE](https://arxiv.org/abs/2601.21557)、[STOP](https://arxiv.org/abs/2310.02304)、[Meta-Harness](https://arxiv.org/abs/2603.28052)、[ADAS](https://arxiv.org/abs/2408.08435)、[AFlow](https://arxiv.org/abs/2410.10762)、[Self-Harness](https://arxiv.org/abs/2606.09498)、[DGM](https://arxiv.org/abs/2505.22954)、[SIA](https://arxiv.org/abs/2605.27276) |
| 证据边界 | 原文是高质量技术综述，但不是系统综述；多篇 2026 工作仍是预印本，任务、模型、预算和 benchmark 不同，不能把各论文提升幅度直接横比 |

## 一句话理解 Harness

如果基础模型是一台发动机，那么 harness 不是一句“如何开车”的提示词，而是整辆车：方向盘、仪表盘、变速箱、导航、行车记录仪、刹车、交通规则和维修流程。

一个实用 harness 通常至少包括：

- **上下文**：这次该把哪些资料交给模型，哪些不交；
- **工具与权限**：能读什么、能改什么、哪些动作需要审批；
- **控制流**：计划、执行、观察、测试、修复、再执行；
- **持久状态**：文件、日志、代码 diff、实验记录和失败轨迹；
- **评估器**：什么叫完成，怎样防止“模型自称成功”；
- **并行执行**：子智能体和后台任务如何启动、监控、取消与合并；
- **安全边界**：可编辑面、沙箱、预算、回滚和人工检查点。

这比早期的“Agent = LLM + Memory + Tools + Planning + Action”多了一层软件工程含义：**不仅给模型能力，还要治理模型怎样使用这些能力。**

## 全文主线：优化对象不断上移

```mermaid
flowchart LR
    A["提示词：怎么回答"] --> B["结构化上下文：该看什么"]
    B --> C["工作流：按什么步骤做"]
    C --> D["Harness 代码：系统怎样运行"]
    D --> E["优化器代码：怎样改进 Harness"]
    E --> F["模型权重 + Harness 联合优化"]
```

文章把相关研究串成了五级台阶：

1. **上下文工程**：不把全部历史塞进 prompt，而是检索、筛选、压缩、组织。
2. **工作流搜索**：不只手写“先规划再反思”，而是把工作流写成图或代码后搜索。
3. **Harness 搜索**：把提示、工具、控制流、记忆和权限组合成可执行候选，再用测试筛选。
4. **改进器自我改进**：让“负责改程序的程序”把自己也当作待优化对象。
5. **权重与 Harness 联合优化**：外部软件结构和模型内部参数一起更新；这是更接近完整 RSI 的方向，但证据仍早期。

> [!important] 三个概念不要混淆
> - **答案变好**：同一套系统多想一次，得到更好的单次输出。
> - **Harness 变好**：模型权重不变，但外围代码、上下文或工作流变好。
> - **模型变好**：训练或测试时学习改变了权重。
>
> STOP、Meta-Harness、Self-Harness 和 DGM 主要证明第二类，不等于基础模型已经能无限递归提升自身智能。

## 公式阅读预备：先认符号

| 符号 | 通俗含义 |
|---|---|
| $a \in A$ | $a$ 是集合 $A$ 里的一个成员 |
| $\{a_1,\dots,a_n\}$ | 一组东西；省略号表示中间还有成员 |
| $f(x;\theta)$ | 用参数/配置 $\theta$ 控制函数 $f$ 处理输入 $x$；分号只是强调“输入”和“配置”角色不同 |
| $\arg\max_z f(z)$ | 找到让 $f$ 最大的那个 $z$；结果是“最佳方案”，不是最大分数本身 |
| $z^*$ | 最优或当前最佳的 $z$ |
| $\mathbb{E}[X]$ | $X$ 的平均值/期望值 |
| $\triangleq$ | “定义为” |
| $\hat u$ | 对真实效用 $u$ 的样本估计；帽子表示“估出来的” |
| 下标 $t,k$ | 第 $t$ 轮、第 $k$ 个版本 |
| 上标 train/val | 训练集分数、验证集分数，不是乘方 |
| $\propto$ | 成正比；还需要再除以所有候选权重之和，才能变成概率 |

## 公式一：一个“上下文技能”到底是什么

原文写道：

$$
s \in \mathcal{S}, \qquad c_s=(\rho_s,F_s), \qquad c=F_s(x;\rho_s)
$$

逐项翻译：

- $\mathcal{S}$：所有候选“上下文工程方法”的集合；
- $s$：从中选出的一个技能，例如“先按关键词检索，再按相关度排序，最后压缩成 2,000 token”；
- $c_s$：技能 $s$ 所定义的完整上下文函数；
- $\rho_s$：静态材料；
- $F_s$：动态加工步骤；
- $x$：当前问题；
- $c$：最终实际交给模型的上下文。

其中：

$$
\rho_s=\{\rho_1,\dots,\rho_m\}, \qquad
F_s=\{F_1,\dots,F_k\}
$$

$\rho_s$ 可以包含系统提示、知识库、代码库和范例；$F_s$ 可以包含搜索、选择、过滤、排序和格式化。最通俗的读法是：

> **上下文 = 用一套动态流水线，针对当前问题，从静态仓库里加工出来的“临时资料包”。**

### 一个小例子

问题 $x$ 是“客户为什么无法退款？”；静态材料 $\rho_s$ 包含退款政策、订单数据库说明和客服范例；动态操作 $F_s$ 依次执行：识别订单号 → 查询订单状态 → 检索适用条款 → 删除无关条款 → 生成带来源的上下文。最后的 $c$ 不是整个客服知识库，而是本次回答真正需要的几段信息。

## 公式二：MCE 的双层优化

$$
\text{Inner: }c_s^*=\arg\max_{c_s}J_\text{train}(c_s;s)
$$

$$
\text{Outer: }s^*=\arg\max_{s\in\mathcal{S}}J_\text{val}(c_s^*)
$$

这是全文最重要、但也最容易被符号吓到的公式。

### 内层：在方法不变时，把资料包做得最好

先固定技能 $s$，只优化它产出的上下文 $c_s$。$J_\text{train}$ 是训练任务上的总评分，可以综合准确率、成本、延迟或格式合规。$\arg\max$ 的意思是“不断试，找到训练集分数最高的上下文方案”。

例如技能规定“关键词检索 + 摘要”，内层可以尝试：取 3 条还是 8 条、摘要 500 字还是 1,500 字、是否加入反例，最后选出训练集上最好的版本 $c_s^*$。

### 外层：比较“做资料包的方法”本身

外层不再只改资料，而是比较不同技能：关键词检索、向量检索、规则路由、动态写代码、分层记忆等。每个技能先在内层练到最好，再拿它的最佳结果去验证集考试，最终选择泛化最好的 $s^*$。

### 为什么必须区分 train 和 val

如果内外层都看同一批题，系统可能记住训练题的答案或堆入大量只对训练题有效的规则。验证集相当于闭卷新题，用来判断“方法真的会做同类问题”，还是只会背题。

可以把它类比为招聘：

- 内层：每位候选人用练习题把自己的答题资料打磨到最好；
- 外层：所有人再做一套没见过的题，决定哪种学习方法最有效。

> [!note] 这不是微积分求导
> 这里的 $\arg\max$ 通常由智能体试错、代码修改、检索和评估实现，是黑盒搜索。公式只规定“要找什么”，没有承诺可以通过梯度一步算出答案。

## 公式三：历史库、交叉生成和上下文更新

### 历史库

$$
\mathcal{H}_{k-1}=\{(s_i,c_i,J_i^\text{train},J_i^\text{val})\}_{i=1}^{k-1}
$$

意思是：在第 $k$ 轮之前，把过去每一轮的四件事都存下来——用过的技能 $s_i$、产出的上下文 $c_i$、训练分数、验证分数。

它不是抽象数学对象，在工程里通常就是一个目录、数据库或实验表。保留失败记录很重要：只存冠军会失去“哪些路已经试过而且为什么失败”的信息。

### 交叉生成新技能

$$
s_k=\operatorname{crossover}(\tau,\mathcal{H}_{k-1})
$$

$\tau$ 是任务说明。`crossover` 借用了进化算法术语，但这里不一定是机械地拼接两个父代。元智能体会阅读历史库，抽取成功设计、避开失败模式，再生成第 $k$ 个新技能。

通俗说：**让一位架构师看完历届方案、成绩和事故报告后，写出下一版工作方法。**

### 执行技能并更新上下文

$$
c_k=\operatorname{engineer}(\tau,s_k;c_{k-1}^*,\mathcal{R}_k)
$$

- $c_{k-1}^*$：上一轮最好的上下文，作为 warm start；
- $\mathcal{R}_k$：本轮执行轨迹和反馈；
- 分号：强调前面是任务与方法，后面是可供参考的旧版本与新反馈；
- $c_k$：综合这些信息做出的新上下文函数。

这就是“保留上一版可用系统 → 看本轮失败 → 做定向修改”，而不是每轮从零重写。

### 工具集合

$$
\mathcal{T}=\{\texttt{Read},\texttt{Write},\texttt{Edit},\texttt{Bash},\texttt{Glob},\texttt{Grep},\texttt{TodoWrite}\}
$$

这没有隐藏的数学运算，只是在列清单：智能体被允许使用的工具集合是 $\mathcal{T}$。它也揭示文章的工程观点：复杂的上下文优化并不一定需要专用神经网络，文件系统加一组通用编程工具已经能表达很大的搜索空间。

## 公式四：STOP——先定义“改进器”

$$
s'=I(u,s;M)
$$

- $s$：原始解法或程序；
- $u$：评分函数；
- $M$：不修改权重的黑盒语言模型；
- $I$：调用模型、产生候选、测试并挑选的“改进器程序”；
- $s'$：改进后的解法。

例如 $s$ 是一段排序代码，$u$ 同时检查正确性和运行速度，$I$ 让模型提出 10 个修改并实际跑测试，最后返回得分最高的 $s'$。

关键转折是：STOP 的最终目标不只是让 $s$ 变好，而是让 **$I$ 自己变成更会改程序的改进器**。

## 公式五：STOP 的元效用，以及原文中的一处疑似记号错误

博客给出的版本是：

$$
\hat{u}(I)\triangleq \frac{1}{|\mathcal D|}
\mathbb E_{(u,s)\sim\mathcal D}
\left[u\bigl(I(u,s;M)\bigr)\right]
$$

它想表达的是：把改进器 $I$ 放到一批下游任务上，取改进后得分的平均值。$\hat u(I)$ 越高，说明这个改进器越通用。

但按标准数学记号，这里很可能多除了一次 $|\mathcal D|$。STOP 原论文的有限样本平均是：

$$
\hat{u}(I)=\frac{1}{|\mathcal D|}
\sum_{(u,s)\in\mathcal D}
u\bigl(I(u,s;M)\bigr)
$$

它等价于：

$$
\hat{u}(I)=
\mathbb E_{(u,s)\sim\operatorname{Unif}(\mathcal D)}
\left[u\bigl(I(u,s;M)\bigr)\right]
$$

**“除以任务数后的求和”与“在任务集上取均匀期望”二选一即可，不能同时再除一次。**

### 数字例子

假设三个任务上的得分分别是 $0.8,0.6,0.9$，正确平均值为：

$$
\hat u(I)=\frac{0.8+0.6+0.9}{3}=0.7667
$$

若把博客中的 $\mathbb E$ 按标准“平均值”解释，再除以 3，就会变成 $0.2556$。当所有候选都使用同一个任务集时，额外常数通常不改变排名，却会让分数尺度错误，并影响跨任务集比较、阈值与预算决策。

> [!warning] 核验结论
> 这是对博客公式记号的技术校正，不影响作者想表达的概念。STOP 论文把 $\hat u$ 定义为训练任务上的样本平均；真实目标则是对任务分布的期望效用。样本平均只是对真实泛化能力的估计。

## 公式六：STOP 如何“改进改进器”

$$
I_t=I_{t-1}(\hat u,I_{t-1};M)
$$

把它按参数位置读一遍：

1. 当前改进器是 $I_{t-1}$；
2. 这次要被改的“原始解法”也是 $I_{t-1}$ 自己；
3. 评价它的新评分函数是元效用 $\hat u$；
4. 它仍然调用同一个黑盒模型 $M$；
5. 输出下一代改进器 $I_t$。

伪代码直觉如下：

```text
旧改进器 = I[t-1]
候选新改进器 = 旧改进器(
    评分函数 = 多任务平均表现,
    待改对象 = 旧改进器自己的源代码,
    语言模型 = M
)
I[t] = 候选新改进器
```

这里的“递归”来自同一角色既是工匠又是工件。它不是无限递归调用，也不是模型权重自己重写。原论文还显示：强模型能找到 beam search、遗传算法和模拟退火等改进策略，但较弱模型并不稳定改善。这说明**递归结构不是魔法，底层模型能力、评分器质量和计算预算仍是硬约束。**

## 文章里其他带符号的表述

### AFlow：$W_0$、$N$ 与 top-$k$

- $W_0$：搜索树的起始工作流；
- $N$：最多允许多少轮搜索，属于计算预算；
- top-$k$：当前排名最高的 $k$ 个候选；
- “top-$k$ 平均分不再上升”是停止条件，避免因单个偶然高分候选误判整体还在进步。

AFlow 用 [[_entities/MonteCarloTreeSearch|MCTS]] 在代码表示的工作流树上平衡两件事：多试没走过的分支（探索），以及继续改高分分支（利用）。[原论文](https://arxiv.org/abs/2410.10762)把工作流优化正式化为搜索问题，而不是证明某个固定工作流永远最好。

### Self-Harness：$h_t\rightarrow h_{t+1}$ 与 $D_\text{in}/D_\text{out}$

- $h_t$：第 $t$ 版 harness；
- $h_{t+1}$：合并通过验证的编辑后的下一版；
- $D_\text{in}$：专门检查已知弱点是否被修复；
- $D_\text{out}$：检查修改有没有破坏未针对优化的能力。

它对应软件工程里的“修复测试 + 回归测试”双门禁。只在 $D_\text{in}$ 上变好，可能只是对已知失败样例打补丁；只有 $D_\text{out}$ 也不退步，才更像可泛化改进。[Self-Harness 摘要](https://arxiv.org/abs/2606.09498)报告三种模型在 Terminal-Bench-2.0 held-out pass rate 上都有提升，但这是特定 benchmark 下的结果，不足以证明开放世界中的持续改进。

### DGM：“表现成正比、子代数成反比”

文章用文字描述父代采样规则。只为帮助理解，可把它示意写成：

$$
p_i\propto \frac{\text{performance}_i}{1+\text{children}_i}
$$

这不是对 DGM 实现细节的逐字复刻，只表达文章中的方向：高分候选更容易被选，但已经产生很多后代的候选会被降权。这样既利用强者，又给较少探索的分支机会，防止整个种群过早收缩到一条路线。[DGM 论文](https://arxiv.org/abs/2505.22954)强调维护开放式候选档案，并用实证 benchmark 而非形式证明来判断修改是否有益。

## 研究谱系：这些工作分别在优化什么

| 研究 | 主要优化对象 | 模型权重是否变化 | 核心反馈 | 关键局限 |
|---|---|---:|---|---|
| ACE | 条目化上下文 playbook | 否 | 成功/失败轨迹 | 工作流和数据结构仍由人预设 |
| MCE | 上下文技能 + 上下文文件/代码 | 否 | train/validation 指标 | 双层搜索成本、验证集过拟合 |
| ADAS / AFlow | Agent 工作流代码/图 | 否 | benchmark 分数 | 搜索空间大，结果依赖任务与预算 |
| Meta-Harness | 端到端 harness 代码 | 否 | 分数、源码、完整轨迹 | 起点和强 proposer 可能贡献很大 |
| STOP | “改进程序的程序” | 否 | 多任务元效用 | 强模型才可能稳定改善；评分器定义决定方向 |
| Self-Harness | 当前模型自己的 harness | 否 | 弱点聚类 + 双分割回归测试 | 仍需外部不可编辑的验证与权限边界 |
| DGM | 可编辑的 coding-agent 代码库 | 否 | SWE-bench / Polyglot 等适应度 | 开放式探索昂贵；benchmark ≠ 通用智能 |
| SIA | Harness 与模型权重 | 是 | 反馈智能体决定更新哪一侧 | 变量混杂，早期结果不易归因 |

## 我的判断：文章最有价值的三点

### 1. 把“模型能力”和“系统能力”拆开

同一个模型，在不同上下文、工具、循环、验证和权限下，可以表现得像不同产品。只比较裸模型 benchmark，会漏掉部署系统这个可快速迭代、可审计、可回滚的能力层。

### 2. 文件系统不是落后的记忆方案，而是可审计接口

文件能被搜索、diff、版本控制、回放和人工检查。对于长任务，可靠性往往来自“把重要状态写下来”，而不是赌模型在超长上下文里始终抓住重点。MCE 和 Meta-Harness 都把技能、上下文、历史和候选实现为文件/代码，这与文章主张相互印证。[MCE 原论文](https://arxiv.org/html/2601.21557)明确把文件与代码视为无固定 schema 的上下文表示。

### 3. 自我改进的瓶颈越来越像“评估工程”

当代码能表达任意工作流时，“能不能生成候选”不再是唯一难点。真正决定方向的是：评分是否可靠、测试是否 held-out、失败是否保存、权限边界是否在循环之外。没有强验证器，自我改进很容易变成自我说服。

## 我不同意或保留意见的地方

### 1. 现有证据更像“自动化搜索有效”，还不是强 RSI 证据

多数系统固定了基础模型、任务、工具和评估器，只在外部代码空间里搜索。它们证明 AI 能参与改进部署结构，但还没有证明跨领域、长期、无人工定义目标的递归智能增长。

### 2. 论文结果不能只看提升百分点

不同研究使用不同模型、起点 harness、token/rollout 预算、测试集和验证规则。Meta-Harness 从强基线初始化、DGM 用特定 coding benchmark、MCE 横跨分类任务；这些结果说明方向有潜力，不构成统一排行榜。

### 3. “代码是通用语言”同时扩大能力与攻击面

代码确实能表达 prompt、工具、循环、记忆和子智能体，但一旦允许系统修改执行自己的代码，普通应用配置就升级为安全边界问题。可编辑区、凭据、网络、评估器、审批和回滚必须由不可自改的外层控制。

### 4. 最大未解问题不是生成，而是慢、模糊、会被钻空子的评分

单元测试、运行时间和游戏胜负容易量化；研究品味、长期可维护性、商业价值和社会影响很难快速评分。优化器会忠实放大评分器的漏洞，这就是 Goodhart 定律和 reward hacking 在 harness 层的版本。

## 可落地的最小 Harness 改进闭环

对于真实团队，比“让 Agent 随意改自己”更稳妥的第一版是：

1. **版本化**：prompt、工具定义、权限、上下文逻辑和工作流全部进入代码仓库；
2. **记录轨迹**：保存输入、工具调用、输出、错误、成本、延迟和人工纠正；
3. **弱点聚类**：区分表面报错与根因，例如同为 timeout，可能是搜索无界、命令挂起或重试策略错误；
4. **限定可编辑面**：只允许提出小范围 patch，不允许修改 evaluator、凭据、审批器和沙箱；
5. **双门评测**：已知失败集检查修复，held-out 集检查回归；
6. **多目标验收**：质量、成本、延迟、安全和可维护性一起看，不只优化 pass rate；
7. **人工合并与可回滚**：高风险修改保持人在环，失败候选也归档；
8. **达到统计门槛再升级**：确认改进跨批次、跨模型调用随机性仍稳定，再扩大自动接受范围。

## 常见误解

| 误解 | 更准确的理解 |
|---|---|
| Harness 就是 system prompt | Prompt 只是上下文的一部分；harness 还包括工具、控制流、状态、评估、权限和运行时 |
| 长上下文会消灭上下文工程 | 窗口变长不等于注意力、成本和信息选择问题消失 |
| $\arg\max$ 表示已经知道怎样找到最优解 | 它只是定义目标；实际仍要靠昂贵且不完备的搜索 |
| 训练分数上涨就是系统变聪明 | 可能是过拟合、泄漏、重复采样或 reward hacking，必须看 held-out 结果和轨迹 |
| STOP 改了模型本身 | STOP 固定黑盒模型，改的是调用模型的 scaffolding/improver 代码 |
| 自我修改意味着不再需要人 | 人更需要定义目标、边界、验证器、升级门槛和停止条件 |

## 后续值得追踪的问题

- 同一模型、同一预算下，prompt、context、workflow、harness code 各自贡献多少增益？
- Harness 优化能否在跨仓库、跨领域和长时间跨度下稳定泛化？
- 怎样构造不可由候选 harness 访问或修改的 evaluator 与 held-out 数据？
- 如何把维护成本、技术债、权限风险和未来调试成本纳入目标函数？
- 候选数量增长后，怎样控制推理、评测和存储成本？
- 失败轨迹如何去隐私、去敏感信息后沉淀为长期资产？
- 权重更新与 harness 更新同时发生时，怎样做因果归因？

## 结论

Lilian Weng 的文章最适合作为一张研究地图，而不是“AI 已实现递归自我进化”的宣言。它把近年的上下文工程、工作流搜索、程序进化和自动研究统一到一个清晰问题上：

> **能否把产生答案的机器本身，变成可执行、可评估、可版本化、可搜索的优化对象？**

数学上，MCE 的双层优化说明“既优化资料，也优化做资料的方法”；STOP 的元效用说明“用跨任务平均表现评价改进器”；递归更新则说明“旧改进器可以把自己的代码当作待改对象”。工程上真正的护城河并不是公式本身，而是高质量 evaluator、可追溯轨迹、持久文件、严格权限和可靠回归测试。

## 关联连接

- [[ai/00-index|AI 研究入口]]
- [[ai/research-notes/README|AI Research Notes]]
- [[_concepts/knowledge-compilation|Knowledge Compilation]]
- [[_concepts/source-traceability|Source Traceability]]
- [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02|MATLAB/Simulink Agentic AI 工具链视频调研]]
- [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]]

## 来源

### 核心来源

- Weng, Lilian. [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/), 2026-07-04。原文观点与公式来源。
- Ye et al. [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/abs/2601.21557), 2026。MCE 公式与双层框架的一手来源。
- Zelikman et al. [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304), COLM 2024。STOP 样本平均、递归更新及实验边界的一手来源。

### 交叉核验来源

- Lee et al. [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052), 2026。
- Hu et al. [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435), ICLR 2025。
- Zhang et al. [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762), ICLR 2025。
- Zhang et al. [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498), 2026。
- Zhang et al. [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954), 2025。
- Hebbar et al. [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276), 2026。

## 知识冲突

- **STOP 元效用公式记号**：博客写成 $|\mathcal D|^{-1}\mathbb E_{(u,s)\sim\mathcal D}[\cdot]$；STOP 原论文的有限训练集定义是 $|\mathcal D|^{-1}\sum_{(u,s)\in\mathcal D}[\cdot]$。若 $\mathbb E$ 已表示均匀平均，博客版本会重复归一化。后续如作者修订原文，应重新核对。
- **跨论文“提升”不可直接比较**：各研究的模型、任务、预算、初始 harness 和评估器不同。当前笔记只比较优化对象和机制，不制作统一性能排名。
