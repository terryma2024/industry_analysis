---
title: 高强度交流之后，聊聊 WRC 对具身大脑的看法
type: source
date_created: 2026-08-26
last_updated: 2026-08-26
source_urls:
  - https://mp.weixin.qq.com/s/rdg8LFwVjVedwVbr82EVMw
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-534-wrc.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-535-token-wrc-2026.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-536-waic-ceo-99.md
evidence_grade: C
tags:
  - source/wechat
  - industry/robotics-embodied-ai
  - wrc
  - reliability
  - vla
  - business-model
status: active
aliases:
  - 天南 WRC 具身大脑观点
  - WRC 可靠性模型规模与物理 Token 文章来源卡
---

# 高强度交流之后，聊聊 WRC 对具身大脑的看法

> [!summary]
> 这篇文章最值得保留的不是 `99%`、`80%`、`7B`、万卡或毛利数字本身，而是把具身智能商业化拆成三个相互制约的问题：原子技能能否组合成长程可靠任务、模型与数据是否存在尚未跨越的 scaling 区间、供应商能否从卖硬件转为按可验证结果收费。原文是从业者现场观察和二次转述，关键数字均不得直接作为行业事实。

## 来源元数据

| 字段 | 内容 |
|---|---|
| 标题 | 高强度的交流之后，冷静下来和大家聊聊 WRC 对大脑的看法。 |
| 平台 | 微信公众号 |
| 公众号 / 署名 | 天南具身公园 / 天南 |
| 发布日期 | 待验证；Defuddle 未返回可靠日期 |
| 入库日期 | 2026-08-26 |
| 提取方式 | Defuddle Markdown，正文成功捕获 |
| 证据等级 | C：从业者评论，混合现场观察、他人整理和作者判断 |
| 原文 | [微信链接](https://mp.weixin.qq.com/s/rdg8LFwVjVedwVbr82EVMw) |
| 原始抽取 | [`SRC-robotics-534`](../../raw/robotics-embodied-ai/documents/SRC-robotics-534-wrc.md) |

## 原文主张地图

### 可靠性与泛化

- 苏度的 `99%+` 被解释为限定问题范围内的原子技能稳定性；宇树的“两个 `80%`”被解释为陌生场景覆盖与完整任务成功率。
- 作者认为两者不是“先可靠还是先泛化”的冲突，而是技能成功率与任务覆盖率两个层级。
- 作者用独立串联系统近似说明长程任务的误差累积：若 100 步任务要达到 80% 完成率，则单步成功率约需 `99.78%`。

### 模型规模与算力

- 原文转述摩尔线程观点：VLA 多集中在 `7B` 左右，具身基础模型的能力跃迁可能需要千卡、万卡集群与更大参数量。
- 作者进一步提出“也许 `7B` 才是门槛”，并判断当前数据、基础设施、资金和人才尚不足以支撑万卡级具身训练。

### 商业模式

- 原文转述星海图的三阶段路径：整机销售 → 方案订阅 → “物理世界 Token”销售。
- 作者把毛利曲线解释成可靠性曲线的影子：只有机器人能稳定跑完整工作流，客户才可能从购买设备转向购买解决方案或结果。

## 事实、估计、判断与假设

| 类型 | 内容 | 入库处理 |
|---|---|---|
| 可复核计算 | 独立且同分布的 `n` 个步骤若单步成功率为 `p`，无恢复时任务成功率为 `p^n`；`0.8^(1/100) ≈ 99.777%` | 公式成立，但独立、同分布、无恢复是假设，不是现场任务事实 |
| 可核验技术事实 | π0 使用约 3.3B 参数；OpenVLA 主模型约 7B/7.5B | 说明 VLA 并非都固定在 7B，也不能由参数量单独推断能力 |
| 可归因主张 | 星海图提出“物理世界 Token”商业模式；苏度强调 `99%+` 可靠性 | B 级媒体整理支持“谁说过什么”，不支持审计后的性能、毛利或客户经济性 |
| 数字估计 | `40%–60%` 整机毛利、`20%` 方案阶段毛利、负毛利硬件、`99.9%` 成功率、10 小时后训练 | 口径、样本、合同和成本归集不明，全部保留为 `待验证` |
| 技术判断 | 具身能力跃迁需要更大模型和千卡/万卡训练 | 目前没有公开 scaling law 足以确认固定阈值 |
| 商业假设 | 当可靠性足够高时，价值会从硬件迁移到智能服务与按结果收费 | 需要合同、回款、复购、SLA、责任分配和单位经济性验证 |

## 补充来源与修正

- 雷峰网整理的 WRC 演讲 [`SRC-robotics-535`](../../raw/robotics-embodied-ai/documents/SRC-robotics-535-token-wrc-2026.md) 可支持“星海图提出过该商业路径”的归因，但其毛利、成功率、精度和训练时间仍是公司口径。
- 量子位/AITNT 访谈 [`SRC-robotics-536`](../../raw/robotics-embodied-ai/documents/SRC-robotics-536-waic-ceo-99.md) 可支持“苏度把 `99%+` 视为部署前提”的归因，但未给出完整 trial protocol、置信区间和客户验收报告。
- π0 论文 [`SRC-robotics-061`](../../raw/robotics-embodied-ai/documents/SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md) 明确为 3.3B 参数；OpenVLA 官方仓库 [`SRC-robotics-117`](../../raw/robotics-embodied-ai/documents/SRC-robotics-117-openvla-github-repository.md) 明确主模型约 7B/7.5B，并支持 1B–34B 训练代码。现有证据不支持“7B 是能力涌现门槛”。
- `SRC-robotics-316` 的政策原文要求按真实作业成功率、效率、安全可靠性和经济可行性验证，并鼓励按效用付费、经营性租赁；这支持“从卖设备向按效用收费探索”，但不验证“物理 Token”必然成为主导模式。

## 可取之处与校正

- **可取**：把原子技能、长程工作流、陌生分布覆盖和商业 SLA 分层，避免用单个 Demo 成功率代替部署可靠性。
- **校正**：真实失败通常相关，且系统会重试、恢复、绕行或人工接管；不能直接用 `p^n` 预测生产任务。
- **校正**：参数量、训练 GPU 数、数据量、动作表示、控制频率、推理时延和后训练方法共同决定系统能力；不存在已验证的单一 `7B` 或万卡门槛。
- **校正**：“物理 Token”当前更适合作为按效用付费的比喻。进入合同前必须定义计费单位、质量门、失败退款、停机责任、安全事件和审计日志。

## 下游编译

本文按 `R07 商业落地与需求真实性验证` 主分类、`R04 技术原理与前沿` 和 `R03 公司与商业模式` 次分类，编译为 [[robotics-embodied-ai/research-notes/embodied-ai-reliability-scaling-and-outcome-pricing-2026-08-26|具身智能可靠性、模型规模与按结果付费的商业化门槛]]。

## 商业应用可能性

近期最有可能采用按结果收费的不是开放家庭场景，而是任务边界、计量方式和责任边界都可冻结的工业上下料、仓储拣选/打包和巡检。当前公开证据多停留在演示、公司报告或合作叙事，重复采购、全成本毛利和跨站点复制仍待验证。

## 中小型创业者的机会

- **可立即验证**：任务级 benchmark、验收与回归工具；失败/接管/恢复日志；按任务计量和客户对账；现有本体的技能编排与售后运维。
- **需要条件成熟**：跨品牌技能市场、按结果结算平台、机器人保险与责任数据服务。
- **不建议进入**：用自有资本训练通用超大具身基座模型、无客户任务就补贴整机铺量、把“物理 Token”包装成脱离实际交付的金融化概念。

## 知识冲突

- 原文倾向把更大参数与万卡训练视为下一次能力跃迁的必要条件；现有一手资料只证明不同规模模型均可形成有效能力，尚无公开 scaling law 给出通用阈值。
- 原文用独立串联近似解释长程失败累积；真实机器人错误有相关性，也存在恢复与人工接管，必须用完整任务分布和连续运行验证替代公式外推。
- 星海图的毛利迁移是战略叙事，不是行业已发生的财务事实；应以收入分层、成本归集、回款和复购验证。

## 关联连接

- [[robotics-embodied-ai/00-index|机器人（具身智能）]]
- [[embodied-ai|Embodied AI]]
- [[robot-training-data|Robot Training Data]]
- [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品比较]]
- [[robotics-embodied-ai/research-notes/embodied-model-physical-understanding-evaluation-2026-07-03|具身智能大模型物理理解能力评估框架]]
- [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地候选池]]
