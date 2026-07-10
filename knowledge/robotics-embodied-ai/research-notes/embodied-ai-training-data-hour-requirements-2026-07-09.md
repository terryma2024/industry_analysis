---
title: 具身智能训练数据需求量与小时数分层估算
type: synthesis
date_created: 2026-07-09
last_updated: 2026-07-09
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-056-octo-an-open-source-generalist-robot-policy.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-078-data-scaling-laws-in-imitation-learning-for-robotic-manipulation.md
  - https://arxiv.org/abs/2405.12213
  - https://arxiv.org/abs/2607.06403
  - https://arxiv.org/abs/2602.00919
  - https://arxiv.org/abs/2605.24934
  - https://arxiv.org/abs/2606.17200
  - https://www.businessinsider.com/ai-startups-robotics-pay-film-chores-encord-micro1-scale-2025-10
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - robot-training-data
  - data-scaling
  - vla
status: active
aliases:
  - 具身智能训练数据小时数
  - Embodied AI Data Hour Requirements
---

# 具身智能训练数据需求量与小时数分层估算

> [!summary]
> 具身智能训练数据不能用一个统一小时数回答。**demo 级可以是 `0.5-5` 小时；可泛化单任务通常要 `5-50` 有效小时；客户场景产品化通常要 `50-500` 有效小时；跨任务/跨本体模型进入 `500-5,000+` 小时；前沿 VLA/robot foundation model 已公开到 `10,000-60,000+` 小时混合数据量级。**这里的关键口径是“有效可训练小时”，不是原始录制小时、操作者工时或互联网视频小时。

## 口径

本文把“需要多少小时”拆成四个口径：

| 口径 | 含义 | 备注 |
|---|---|---|
| 原始录制小时 | 摄像头、传感器或机器人系统实际录下来的全部时长 | 会混入等待、失败、静止、标定错误和重采片段 |
| 有效可训练小时 | 通过同步、标定、任务切分、动作连续性和 QC 后能进入训练集的 episode 时长 | 最适合做数据需求和成本测算 |
| robot action hours | 带机器人状态和动作监督的数据小时 | 对 action head 最稀缺、最有价值 |
| human video hours | 人类第一视角或第三视角视频小时 | 适合学场景、物体、动作先验，但不能直接等同 robot action |

经验上，采购或自建数据工厂应按“有效可训练小时 + 多样性单元”管理，而不是只堆 raw hours。

## 分层结论

| 目标 | 建议有效数据量 | 典型数据形态 | 判断 |
|---|---:|---|---|
| 可演示 demo / proof-of-concept | `0.5-5h` | 少量高质量示教、人类第一视角视频、小范围微调 | 适合证明路线可行，不代表可部署。HumanEgo 报告每任务 `15-30` 分钟人类第一视角视频就能显著提升若干任务表现，但这是受限任务设定。 |
| 单任务、有限泛化 | `5-50h` | 数百到数千条 episode，覆盖物体、姿态、场景、操作者变化 | 数据多样性比单纯小时数更关键。Data Scaling Laws 的结论是达到每个环境/物体足够 demo 后，继续加同质 demo 边际收益很小。 |
| 单客户/单场景产品化 | `50-500h` | 现场遥操、失败恢复、人工接管、自主 rollout、holdout 验证 | 这是工厂工位、仓储单元、零售后场、家庭某类任务包更现实的第一阶段预算。pi0 报告 post-training 简单任务约 `5h`，复杂任务可用 `100h+`。 |
| 跨任务/跨本体策略模型 | `500-5,000+h` | 多机器人、多任务、多场景数据集，叠加开源数据和仿真 | DROID 为 `350h`/`76k` demos；Octo 用 `800k` Open X-Embodiment trajectories；AgiBot World 进入 `1M+` trajectories。 |
| 前沿 robot foundation model / VLA | `10,000-60,000+h+` | robot action、egocentric human video、sim、synthetic、互联网 VLM 预训练混合 | pi0 报告使用 `10,000h+` robot data；LingBot-VLA 2.0 报告约 `60,000h` 预训练数据，其中 `50,000h` 机器人轨迹和 `10,000h` 第一视角人类视频。 |

## 公开锚点

| 来源 | 数据规模锚点 | 对“小时数”的含义 |
|---|---:|---|
| DROID | `76k` demonstrations，`350h` interaction data，`564` scenes，`84` tasks | 一个高质量 in-the-wild 真实机器人数据集已经是数百有效小时，而不是几万小时。 |
| Octo | `800k` Open X-Embodiment trajectories | 通用策略模型更常以 trajectory/step 计量；若没有 episode 时长，不能机械换算成小时。 |
| AgiBot World | `1M+` trajectories，`217` tasks，5 类场景 | 中国头部数据工厂公开数据规模已到百万轨迹，但论文摘要未给出统一有效小时。 |
| Data Scaling Laws in IL | `40,000+` demonstrations 和 `15,000+` real-world rollouts | 单任务泛化的瓶颈是覆盖环境/物体/操作者组合，而不是无限重复同一分布。 |
| pi0 | `10,000h+` robot data；复杂任务 post-training 可到 `100h+` | 前沿 VLA 已进入万小时机器人数据；但下游任务仍可以用几十到百小时完成适配。 |
| Green-VLA | `3,000h` demonstrations pipeline | 说明中大型 VLA 数据处理已用千小时级示教作为工程规模。 |
| ACE-Ego-0 | `4.53k h` robot/sim + `1.48k h` pseudo-action egocentric human data | 人类第一视角视频正在被动作伪标注后纳入训练，但仍需 robot/sim action 数据对齐。 |
| LingBot-VLA 2.0 | `60,000h` pretraining data，其中 `50,000h` robot trajectories | 截至 2026-07-09 可见的最新公开前沿锚点之一，显示 foundation model 阶段进入数万小时。 |
| Business Insider / Scale AI | 超过 `100,000h` robotics training footage | 这是媒体报道的 footage 口径，可能混有人类视频、机器人视频和其他训练素材，不能等同有效 robot action hours。 |

## 计算方法

### 1. 从多样性单元反推小时

```text
需要有效小时 =
  任务数 x 物体/状态数 x 场景数 x 操作者/机器人配置数 x 每格 demo 数 x 平均 episode 秒数
  / 3600
```

如果要估算采集小时，还要除以 QC 通过率：

```text
需要采集小时 = 需要有效小时 / qc_pass_rate
```

例如：`1` 个任务、`20` 类物体/状态、`10` 个场景、`3` 个操作者、每格 `5` 条 demo、每条 `20s`：

```text
1 x 20 x 10 x 3 x 5 x 20 / 3600 = 16.7 有效小时
```

若 QC 通过率只有 `50%`，实际需要约 `33` 小时采集；若还要加入失败恢复、holdout rollout 和长尾扰动，预算很容易上升到 `50-100h`。

### 2. 从轨迹数粗换算小时

DROID 的公开数字是 `76k` demonstrations / `350h`，约 `217` 条 demo/小时。若用这个短 episode 口径粗算：

```text
100,000 条短轨迹 ~= 460 小时
1,000,000 条短轨迹 ~= 4,600 小时
```

但这个换算只适合短时桌面操作。移动操作、双臂、人形、家务长任务的 episode 可能从几十秒到十几分钟，不能直接套 DROID 的 demo/hour。

## 数据工厂与商业判断

1. 初创公司不应一开始追 `10,000h+`。更务实的第一里程碑是 `50-200h` 高质量垂直场景数据，并证明 holdout 场景成功率提升。
2. 对中国公共训练场、地方数据基地或机器人数据工厂，`1,000-10,000h` 有效 robot action data 才有资格谈跨任务数据资产；否则更像项目制采集。
3. 前沿 foundation model 需要数万小时，但它不是纯遥操堆量。更合理的 mix 是真实 robot action、第一视角人类视频、仿真、合成、失败/接管数据和 VLM 互联网预训练共同组成。
4. 对客户部署，最值钱的数据通常不是“成功示教”，而是失败、卡住、接管、恢复和现场长尾扰动。`10h` 高质量失败恢复数据可能比 `100h` 同质成功数据更有边际价值。

## 当前判断

- **如果问“做一个能看的 demo 要多少小时”：`0.5-5h` 可起步。**
- **如果问“做一个单任务可泛化策略要多少小时”：`5-50h` 是常见工程预算。**
- **如果问“做一个客户现场可验收的数据包要多少小时”：优先按 `50-500h` 规划。**
- **如果问“训练一个跨任务 VLA / 具身基础模型要多少小时”：至少 `500-5,000h` 起步，前沿公开锚点已经是 `10,000-60,000h+`。**

## 待验证

- LingBot-VLA 2.0 是 2026-07-07 新近 arXiv 来源，数据量 claim 需等待同行复现、技术报告细节和后续版本验证。
- Business Insider/Scale AI 的 `100,000h` 是媒体 footage 口径，不能当作 action-labeled robot data 直接使用。
- 国内头部公司真实训练 mix、有效小时、QC 通过率和采集成本仍未公开；后续应通过供应商报价、JD、访谈和数据包样例补证。

## 来源 URL

- DROID: https://arxiv.org/abs/2403.12945
- Octo: https://arxiv.org/abs/2405.12213
- AgiBot World: https://arxiv.org/abs/2503.06669
- Data Scaling Laws in Imitation Learning: https://arxiv.org/abs/2410.18647
- pi0: https://www.physicalintelligence.company/download/pi0.pdf
- Green-VLA: https://arxiv.org/abs/2602.00919
- HumanEgo: https://arxiv.org/abs/2605.24934
- ACE-Ego-0: https://arxiv.org/abs/2606.17200
- LingBot-VLA 2.0: https://arxiv.org/abs/2607.06403
- Business Insider / robotics footage: https://www.businessinsider.com/ai-startups-robotics-pay-film-chores-encord-micro1-scale-2025-10

## 关联连接

- [[teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]]
- [[robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]
- [[open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
- [[vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]]
- [[../09-training-data-deep-dive|机器人训练数据深度调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
