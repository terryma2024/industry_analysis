---
title: 遥操训练数据每小时成本与训练数据占比快速调研
type: synthesis
date_created: 2026-07-09
last_updated: 2026-07-09
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-054-open-x-embodiment-robotic-learning-datasets-and-rt-x-models.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-057-robomind-benchmark-on-multi-embodiment-intelligence-normative-data-for-robot-man.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-077-mobile-aloha-learning-bimanual-mobile-manipulation-with-low-cost-whole-body-tele.md
  - https://www.washingtonpost.com/technology/interactive/2026/robot-chores-video-data/
  - https://www.theverge.com/2024/8/19/24223626/tesla-optimus-humanoid-robot-motion-capture-training
  - https://www.businessinsider.com/ai-startups-robotics-pay-film-chores-encord-micro1-scale-2025-10
  - https://www.businessinsider.com/robotics-ai-training-data-transforming-instawork-gig-work-platform-instacore-2026-4
  - https://arxiv.org/abs/1911.04052
  - https://arxiv.org/abs/2605.19138
  - https://arxiv.org/abs/2607.06403
  - https://arxiv.org/abs/2602.00919
  - https://arxiv.org/abs/2605.24934
  - https://arxiv.org/abs/2606.17200
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - robot-training-data
  - teleoperation
  - data-cost
status: active
aliases:
  - 遥操训练数据成本
  - Teleoperation Data Cost
  - Robot Teleoperation Data Share
---

# 遥操训练数据每小时成本与训练数据占比快速调研

> [!summary]
> 这里把用户提到的“摇操”按“遥操/teleoperation”理解。结论先讲明：公开资料没有形成统一市场报价，**最稳妥的口径是按“有效可训练数据小时”核算**。普通人类第一视角视频的直接人工价约为 `10-50 美元/小时`，高技能视频可到 `150 美元/小时`；机器人原生遥操数据因为占用机器人、场地、工程和质检，完全成本通常是人工单价的数倍到十几倍。训练占比则要分母：在“机器人 action 轨迹数据”里，遥操/人工示教常是 `80-100%`；在包含互联网图文、第一视角视频、仿真和合成数据的 foundation model 总训练混合里，遥操数据是少量但高权重的“金数据”。

## 口径

本文区分三种“小时”：

| 口径 | 含义 | 是否适合报价 |
|---|---|---|
| 操作者工时 | 人坐在工位、穿戴设备或拍摄视频的付费小时 | 只能反映人工成本 |
| 原始采集小时 | 录下来的 raw video/state/action 总时长 | 会混入等待、失败、重采、无效片段 |
| 有效可训练小时 | 通过时间同步、标定、动作连续性、任务标签和 QC 后进入训练集的 episode 时长 | 最适合做成本与采购口径 |

本文所有成本判断默认指“有效可训练小时”，除非特别注明。

## 公开锚点

| 证据 | 能说明什么 | 对成本/占比的含义 |
|---|---|---|
| Washington Post 2026 报道 DoorDash 等用家务视频训练机器人，普通 gig worker 可做到 `25 美元/小时`；同时明确机器人遥操数据质量高但最贵。 | 人类第一视角视频是低成本补充，遥操是高质量高成本数据。 | 人类视频直接人工价可作为低端锚点，不等于机器人原生 action 数据成本。 |
| Business Insider 2025 报道 Micro1 等普通家务视频 `25-50 美元/小时`，技术任务可到 `150 美元/小时`，并称 Scale AI 机器人训练 footage 已超过 `100,000 小时`。 | 机器人/家务视频数据已有外包市场，但多是 video，不一定带 robot action。 | 第一视角视频成本低，适合预训练或观察性数据；不能直接替代遥操 action 数据。 |
| The Verge 2024 报道 Tesla Optimus Data Collection Operator 最高 `48 美元/小时`，且可能需要海量数据。 | 人形机器人动捕/数据采集人工单价的公开上界样本。 | 只覆盖人工，不覆盖机器人、设备、场地、工程和 QC。 |
| DROID: `76k` demonstrations、`350h` interaction data、`50` collectors、`12` 个月。 | 大规模真实机器人数据采集仍然重工程、慢、昂贵。 | 平均每小时约 `217` 条 demo，但这是有效 interaction data，不是付费工时。 |
| RoboTurk: `111h` robot manipulation data、`54` users、`1` 周、remote teleoperation。 | 云端/远程遥操能提高吞吐。 | 平台化能降低固定成本，但仍需机器人资源和 QC。 |
| COBALT: 智能手机遥操，支持并发用户，试点 `7,500+` demos / `50+ h`，5 天跨 9 国采集。 | 低门槛遥操硬件和并发系统正在压低采集成本。 | 未来成本下降主要来自更便宜控制器、并发、自动 QC 和众包。 |
| RoboMIND: `107k` trajectories，明确由 human teleoperation 采集，含 `5k` failure demos。 | 中国多本体真实操作数据集里，遥操是主数据来源。 | 在该类真实机器人轨迹数据中，遥操占比接近 `100%`。 |
| AgiBot World: `1M+` trajectories、`217` tasks、5 个场景，standardized pipeline + human-in-the-loop verification。 | 企业级数据工厂重视人工验证和标准化。 | 摘要未披露遥操占比；可确认人工在采集/验证链路中占关键位置。 |
| Open X-Embodiment: 22 robots、21 institutions、527 skills。 | VLA 预训练常用跨本体混合数据。 | 子数据集来源不一，不能直接给出统一遥操占比。 |
| pi0: 使用预训练 VLM + 7 个机器人配置、68 个任务的跨本体机器人数据。 | 现代 VLA 同时吃互联网知识和机器人 action 数据。 | 若按全部 VLM 预训练 token 算，遥操占比很低；若按 action-supervised robot data 算，占比很高。 |
| LingBot-VLA 2.0: `60,000h` 预训练数据，其中 `50,000h` robot trajectories、`10,000h` 第一视角人类视频。 | 前沿 VLA 已公开进入数万小时级混合数据。 | 这是 2026-07-07 新近 arXiv claim，需等待复现和后续版本验证。 |
| ACE-Ego-0: `4.53k h` robot/sim 数据 + `1.48k h` pseudo-action 第一视角人类视频。 | 人类视频正在被转成伪 action 数据进入 VLA 预训练。 | 仍需要 robot/sim action 数据对齐，不能只靠视频。 |
| Instawork / Business Insider 2026: 报道行业从 `100k h`、`1M h` 向更大规模 robotics training data 需求演进。 | 运维人员、现场工人和机器人维护角色可能成为数据采集网络。 | 这是媒体/公司估计，适合作为需求方向，不应当作已验证市场规模。 |

## 成本区间

以下是基于公开锚点和中国项目落地的估算，需在真实采购或自建数据工厂中用 `qc_pass_rate`、`有效 episode 数`、`机器人占用小时` 校准。

| 数据类型 | 有效可训练小时成本 | 适合用途 | 依据与假设 |
|---|---:|---|---|
| 人类第一视角/家务视频 | 中国约 `50-200 RMB/h`；美国约 `20-100 USD/h` | 预训练、动作先验、物体/场景覆盖 | 公开美国报价 `10-50 USD/h` 普通任务；中国按更低人力成本、平台抽成和 QC 折损估算。 |
| 低成本 UMI/手持夹爪示教 | 中国约 `80-300 RMB/h`；美国约 `30-150 USD/h` | 低成本 manipulation demo、机器人可迁移示教 | 不占用高价机器人；主要成本是人工、设备折旧、标定和 retargeting/QC。 |
| 单臂/桌面真实机器人遥操 | 中国约 `300-1,200 RMB/h`；美国约 `150-800 USD/h` | 机器人原生 action fine-tune、客户任务包 | 人工只是小头；需摊销机械臂、相机、场地、重采、数据工程和训练验证。 |
| 双臂/移动操作/人形/灵巧手遥操 | 中国约 `1,000-5,000+ RMB/h`；美国约 `500-3,000+ USD/h` | 长时程、双臂、接触丰富、真实部署任务 | 机器人更贵、控制更慢、失败率和安全成本更高，且 often 需要专家/工程师在场。 |
| 医疗、精密装配等高技能遥操/视频 | 中国待验证；美国可超过 `150 USD/h` 人工 | 高技能小样本、专家示教 | BI 报道技术任务视频可到 `150 USD/h`；机器人原生数据还要叠加设备和合规成本。 |

### 经验公式

```text
有效数据小时成本 =
  (操作者 + 机器人/传感器折旧 + 场地 + 工程支持 + 标定 + 存储计算
   + 标注/QC + 重采 + baseline 训练验证 + 合规)
  / 有效可训练小时
```

如果只想快速估算：

```text
机器人原生遥操有效小时成本
≈ 操作者小时工资 x 3-20
```

倍率取决于机器人价格、有效采集率和 QC 通过率。桌面单臂可接近 `3-8x`；双臂、人形、灵巧手、客户现场部署通常接近 `8-20x+`。

## 训练数据需求量：需要多少小时

具身智能训练数据需求不是一个统一数字，而是随目标层级跳变。这里仍用“有效可训练小时”口径，不用 raw footage 或操作者工时。

| 目标 | 建议有效数据量 | 典型数据形态 | 判断 |
|---|---:|---|---|
| 可演示 demo / proof-of-concept | `0.5-5h` | 少量高质量示教、人类第一视角视频、小范围微调 | 适合证明路线可行，不代表可部署。HumanEgo 报告每任务 `15-30` 分钟人类第一视角视频可显著提升受限任务表现。 |
| 单任务、有限泛化 | `5-50h` | 数百到数千条 episode，覆盖物体、姿态、场景、操作者变化 | Data Scaling Laws 的关键结论是多样性比同质 demo 数量更重要；达到每个环境/物体的阈值后，继续加同分布 demo 边际收益很小。 |
| 单客户/单场景产品化 | `50-500h` | 现场遥操、失败恢复、人工接管、自主 rollout、holdout 验证 | 这是工厂工位、仓储单元、零售后场、家庭某类任务包更现实的第一阶段预算。pi0 报告简单任务 post-training 可约 `5h`，复杂任务可用 `100h+`。 |
| 跨任务/跨本体策略模型 | `500-5,000h+` | 多机器人、多任务、多场景数据集，叠加开源数据和仿真 | DROID 为 `350h`/`76k` demos；Octo 使用 `800k` Open X-Embodiment trajectories；AgiBot World 进入 `1M+` trajectories。 |
| 前沿 VLA / robot foundation model | `10,000-60,000h+` | robot action、egocentric human video、sim、synthetic、互联网 VLM 预训练混合 | pi0 报告 `10,000h+` robot data；LingBot-VLA 2.0 报告约 `60,000h` 预训练数据。 |

### 从多样性单元反推小时

```text
需要有效小时 =
  任务数 x 物体/状态数 x 场景数 x 操作者/机器人配置数 x 每格 demo 数 x 平均 episode 秒数
  / 3600

需要采集小时 = 需要有效小时 / qc_pass_rate
```

例如：`1` 个任务、`20` 类物体/状态、`10` 个场景、`3` 个操作者、每格 `5` 条 demo、每条 `20s`，约为 `16.7` 有效小时。若 QC 通过率只有 `50%`，实际需要约 `33` 小时采集；再加入失败恢复、holdout rollout 和长尾扰动，预算很容易上升到 `50-100h`。

### 从轨迹数粗换算小时

DROID 的公开数字是 `76k` demonstrations / `350h`，约 `217` 条 demo/小时。若用这个短 episode 口径粗算：

```text
100,000 条短轨迹 ~= 460 小时
1,000,000 条短轨迹 ~= 4,600 小时
```

但这个换算只适合短时桌面操作。移动操作、双臂、人形、家务长任务的 episode 可能从几十秒到十几分钟，不能直接套 DROID 的 demo/hour。

## 占比判断

### 1. 在机器人 action 轨迹数据中

| 场景 | 遥操/人工示教占比 | 判断 |
|---|---:|---|
| 早期 imitation learning / 单任务 ACT / Diffusion Policy | `90-100%` | 训练集基本就是人类示教轨迹，例如 ALOHA/Mobile ALOHA、UMI-like、RoboMIND。 |
| 大规模真实机器人数据集 | `80-100%` | DROID、RoboMIND 这类数据的核心是人类示教/遥操；差异在是否保留失败、接管、恢复和自动化段。 |
| 部署后的 HIL/DAgger/接管闭环 | `20-80%` | 分母开始包含机器人自主 rollout；人的贡献从完整示教转向接管、纠错、恢复。 |
| 仿真/合成扩增后的训练集 | `1-30%` 按小时，但质量权重更高 | 少量真实遥操作为 seed/校准/验证，仿真生成大量轨迹。 |

### 2. 在 VLA / robot foundation model 总训练混合中

| 分母 | 遥操占比 | 正确理解 |
|---|---:|---|
| 包含 VLM 互联网图文预训练的全部 token/样本 | 极低，通常不可直接比较 | VLM 预训练数据量巨大，机器人遥操数据在数量上被淹没。 |
| 仅 action-supervised robot trajectory 数据 | 很高，常是 `50-100%` | 只有机器人轨迹/动作数据能直接教 action head 输出。 |
| 加入第一视角人类视频、仿真、合成轨迹后的机器人相关数据混合 | `5-50%` | 取决于阶段。预训练阶段低，后训练/客户 fine-tune 阶段高。 |

我的当前判断：**遥操数据不是靠数量取胜，而是靠“动作监督密度”和“可直接部署校准”取胜。**更像 RLHF/专家示范里的高权重数据：数量小，但决定 action head、接触行为、失败恢复和客户现场细节。

## 面向数据工厂的建议配比

| 阶段 | 建议配比 | 原因 |
|---|---|---|
| 冷启动通用 manipulation 模型 | `人类视频/开源数据/仿真 70-90%` + `遥操 10-30%` | 先用便宜数据铺场景和动作先验，再用遥操对齐 robot action。 |
| 单客户/单场景 fine-tune | `遥操/现场接管/失败恢复 50-90%` | 客户验收看目标机器人在目标场景能不能做，通用视频价值下降。 |
| 数据工厂长期飞轮 | `自主 rollout 30-70%` + `人工接管/纠错 10-40%` + `新示教 10-30%` | 成熟后不应一直采完整示教，应让模型暴露失败，再补高价值纠错数据。 |
| 世界模型/仿真生成 | `真实遥操 seed 1-10%` + `仿真/生成 90%+` | 真实数据主要用于校准分布、物理边界和评测，而不是机械堆量。 |

## 运维场景采集 80% 长尾遥操数据的市场价值

这里讨论一个额外商业假设：如果具身智能运维平台能在真实部署中采集 `80%` 的遥操长尾数据，包括异常、卡住、人工接管、失败恢复、客户现场扰动和低频任务，那么这部分数据的市场价值可能有多大？

### 价值来源

| 价值层 | 如何变现 | 判断 |
|---|---|---|
| 替代采集成本 | 客户不再为同类长尾场景重复购买遥操采集 | 这是价值下限，可按本文的有效小时成本估算。 |
| 模型迭代收益 | 用真实失败/恢复数据提升部署成功率，降低人工值守和售后成本 | 通常比普通成功示教更值钱，因为长尾决定客户验收和复购。 |
| 数据网络效应 | 同一场景多客户、多机器人持续沉淀，形成跨客户可迁移的 failure library | 需要清晰授权、脱敏、场景抽象和数据权益设计。 |
| 运维入口控制 | 平台掌握接管、诊断、补采、回放、评测和再训练闭环 | 更像“机器人 MLOps + 数据飞轮”收入，而不是一次性卖数据集。 |

### 测算公式

```text
年度长尾有效小时 =
  部署机器人数量 x 年活跃天数 x 每台每天长尾/接管小时 x 80% x QC通过率

年度数据资产价值 =
  年度长尾有效小时 x 单位有效小时价值
```

单位有效小时价值可以先用替代采集成本做底线：

- 单臂/桌面真实机器人遥操：`300-1,200 RMB/h`
- 双臂/移动操作/人形/灵巧手遥操：`1,000-5,000+ RMB/h`
- 真实部署长尾数据若有排他性、失败恢复标签和可复用授权，可给 `1.5-5x` 稀缺性溢价；若授权受限或只能服务单客户，溢价应大幅下调。

### 三档市场价值预期

| 场景 | 假设 | 年长尾有效小时 | 数据资产价值下限 | 可收入化空间 |
|---|---|---:|---:|---:|
| 保守试点 | `1,000` 台机器人，`250` 天/年，每台每天 `3` 分钟长尾接管，`80%` 捕获，QC `80%` | 约 `8,000h` | `800万-4,000万 RMB/年` | 若按 `10-30%` 变现，约 `80万-1,200万 RMB/年` |
| 基准规模化 | `10,000` 台机器人，`300` 天/年，每台每天 `6` 分钟长尾接管，`80%` 捕获，QC `80%` | 约 `192,000h` | `1.9亿-9.6亿 RMB/年` | 若按 `10-30%` 变现，约 `1,900万-2.9亿 RMB/年` |
| 激进平台化 | `100,000` 台机器人，`330` 天/年，每台每天 `12` 分钟长尾接管，`80%` 捕获，QC `80%` | 约 `4.22M h` | `42亿-211亿 RMB/年` | 若按 `5-20%` 变现，约 `2.1亿-42亿 RMB/年` |

这里的“数据资产价值”不是会计口径收入，而是按重新采集同等有效长尾数据的替代成本估算。真正可收入化部分取决于三件事：客户是否允许跨客户训练，平台是否能证明成功率/人工值守成本改善，以及数据是否能抽象成跨本体、跨场景可迁移的 episode/failure library。

### 当前判断

如果一个具身智能运维平台真的能稳定捕获 `80%` 长尾遥操数据，它的早期商业价值不在“卖多少小时数据”，而在**把部署越多、失败越多、模型越强、人工越少**做成闭环。短期更像 `千万元级` 数据/运维增值业务；达到万台级机器人活跃部署后，才可能变成 `亿元级` 年度收入机会；十万台级且授权清晰时，才有 `十亿元级` 数据飞轮想象空间。

但要谨慎：这个机会的前提是已有真实部署。没有机器人活跃在客户现场，“80% 长尾数据”只是采集口号；有部署、有接管、有闭环评测，才会变成高价值数据资产。

## 1 亿小时 AGI 级具身基座模型数据 TAM

这里加入一个更激进的 top-down 假设：**如果业界训练出 AGI 级具身智能基座模型需要 `1 亿小时` 具身数据**，那么围绕数据采集、清洗、遥操、运维接管、标注、QC、回放评测和再训练闭环的 TAM 可以粗分为三层。

### 简化计算逻辑

这部分测算只做四步：

1. 先定总量：假设 AGI 级具身基座模型需要 `1 亿小时` 数据。
2. 再拆结构：把 `1 亿小时` 拆成人类第一视角视频、标准 robot action / 遥操、高 DoF 长尾遥操/运维接管、仿真/合成数据。
3. 给每类数据一个“有效小时单价”：人类视频约 `50-200 RMB/h`，标准 robot action 约 `300-1,200 RMB/h`，长尾遥操约 `1,000-5,000 RMB/h`，仿真/合成约 `10-100 RMB/h`。
4. 最后乘可收入化比例：数据资产价值不等于平台收入，平台只能通过采集、清洗、授权、运维、模型迭代等环节拿走其中一部分。

核心公式：

```text
数据资产 TAM = 数据小时数 x 单位有效小时价值
平台收入 TAM = 数据资产 TAM x 可收入化比例
```

基准情景的计算就是：

```text
60M h 人类视频 x 50-200 RMB/h
+ 25M h 标准 robot action x 300-1,200 RMB/h
+ 10M h 长尾遥操 x 1,000-5,000 RMB/h
+ 5M h 仿真/合成 x 10-100 RMB/h
= 205.5亿-925亿 RMB 数据资产 TAM
```

如果只看“运维能采集 80% 长尾遥操数据”：

```text
1亿小时 x 10% 长尾遥操占比 x 80% 运维捕获 = 800万小时
800万小时 x 1,000-5,000 RMB/h = 80亿-400亿 RMB 数据资产价值
80亿-400亿 RMB x 10-30% 可收入化比例 = 8亿-120亿 RMB 平台收入 TAM
```

### 1. 全量数据替代成本 TAM

若把 `1 亿小时` 全部按单一数据类型定价，得到的是理论上限/下限，不代表真实采购结构：

| 数据定价口径 | 单位有效小时价值 | `1 亿小时` 对应 TAM | 含义 |
|---|---:|---:|---|
| 人类第一视角/家务视频 | `50-200 RMB/h` | `50亿-200亿 RMB` | 低成本、低动作监督密度，适合铺场景和动作先验。 |
| 低成本 UMI/手持示教 | `80-300 RMB/h` | `80亿-300亿 RMB` | 比视频更接近机器人动作，但仍需要 retargeting/QC。 |
| 单臂/桌面 robot action | `300-1,200 RMB/h` | `300亿-1,200亿 RMB` | 可直接训练 action head，是更接近模型训练价值的中枢口径。 |
| 双臂/移动操作/人形/灵巧手长尾遥操 | `1,000-5,000+ RMB/h` | `1,000亿-5,000亿+ RMB` | 高价值、低频、难采，适合衡量长尾部署数据的稀缺价值。 |

因此，如果只问“1 亿小时数据的替代采集成本 TAM”，区间非常宽：**`50亿-5,000亿+ RMB`**。这个大区间本身说明，TAM 不能脱离数据结构谈。

### 2. 更现实的混合数据 TAM

一个更合理的 AGI 级具身基座模型数据 mix 可能不是 `100%` 遥操，而是：

| 数据类型 | 占比假设 | 小时数 | 单价假设 | 价值 |
|---|---:|---:|---:|---:|
| 人类第一视角/场景视频 | `60%` | `60M h` | `50-200 RMB/h` | `30亿-120亿 RMB` |
| 标准 robot action / 遥操数据 | `25%` | `25M h` | `300-1,200 RMB/h` | `75亿-300亿 RMB` |
| 高 DoF 长尾遥操/运维接管 | `10%` | `10M h` | `1,000-5,000 RMB/h` | `100亿-500亿 RMB` |
| 仿真/合成/自动 rollout 质检数据 | `5%` | `5M h` | `10-100 RMB/h` | `0.5亿-5亿 RMB` |

在这个混合假设下，`1 亿小时` 的**数据资产替代成本 TAM 约为 `205.5亿-925亿 RMB`**。如果按 `10-30%` 的平台可收入化比例估算，数据采集/处理/授权/运维平台的年度或周期性收入 TAM 约为 **`20亿-278亿 RMB`**。

### 3. 运维场景捕获 80% 长尾遥操数据的 TAM

如果进一步采用前一节假设：运维场景能捕获 `80%` 的遥操长尾数据，那么有两种算法。

**算法 A：把 1 亿小时视为总具身数据需求。**若其中长尾遥操占比为 `10%`，则长尾遥操总需求为 `10M h`，运维可捕获 `8M h`：

```text
8M h x 1,000-5,000 RMB/h = 80亿-400亿 RMB 数据资产价值
```

按 `10-30%` 可收入化比例，运维数据平台可收入 TAM 约为：

```text
8亿-120亿 RMB
```

**算法 B：把 1 亿小时直接视为遥操/长尾 action 数据需求。**这是更激进的口径，运维可捕获 `80M h`：

```text
80M h x 1,000-5,000 RMB/h = 800亿-4,000亿 RMB 数据资产价值
```

按 `5-20%` 可收入化比例，运维数据平台可收入 TAM 约为：

```text
40亿-800亿 RMB
```

### 当前 TAM 判断

| 口径 | 我会采用的 TAM 结论 |
|---|---|
| 最保守 | 若 1 亿小时主要是低成本视频，数据层 TAM 约 `50亿-200亿 RMB`。 |
| 基准 | 若按具身基座模型混合数据结构，数据资产 TAM 约 `205亿-925亿 RMB`，平台可收入 TAM 约 `20亿-278亿 RMB`。 |
| 运维长尾重点 | 若长尾遥操占总数据 `10%` 且运维捕获 `80%`，数据资产 TAM 约 `80亿-400亿 RMB`，平台可收入 TAM 约 `8亿-120亿 RMB`。 |
| 激进 | 若 1 亿小时本身就是长尾遥操/action 数据需求，数据资产 TAM 约 `800亿-4,000亿 RMB`，平台可收入 TAM 约 `40亿-800亿 RMB`。 |

我的判断：对“具身智能运维 + 长尾遥操数据”公司，最值得采用的投资叙事不是 `1 亿小时 x 最高单价 = 5,000亿 RMB`，这个太容易高估；更可信的是**先讲 `80亿-400亿 RMB` 的长尾数据资产 TAM，再讲随着真实机器人部署扩大，平台收入可从 `亿元级` 走向 `十亿-百亿级` 的可能性**。真正的拐点不是数据小时口号，而是活跃机器人数量、每日接管分钟数、QC 通过率、跨客户授权和模型成功率提升。

## 对采购/报价的问法

不要问“遥操数据多少钱一小时”，要问：

1. `有效可训练小时` 如何定义？是否包含失败、等待、重采和静止段？
2. 每小时包含多少 `episode`，平均 episode 时长、任务数量、物体数量、场景数量是多少？
3. 是否提供 `robot-native action`、`canonical action`、状态、相机标定、时间戳和 QC 报告？
4. `qc_pass_rate`、重采率、成功/失败比例、接管比例是多少？
5. 是否能导出 LeRobot/RLDS/HDF5/Zarr/MCAP，并提供 baseline 训练和 holdout rollout？
6. 授权是否覆盖商用训练、客户现场数据、隐私和二次分发？

## 待验证

- 中国国内遥操员/机器人训练师的真实薪资、外包报价和数据工厂收费仍缺少公开一手报价，需要通过招聘 JD、供应商报价单和访谈补证。
- AgiBot World、RoboMIND 2.0、Galaxea、Figure/1X/Tesla 等公司的真实训练混合比例未公开；本文只依据论文摘要、公开报道和数据集属性推断。
- 真实成本对 `有效采集率` 极敏感：同样 `100 RMB/h` 的人工，若有效数据率从 `50%` 掉到 `10%`，有效数据小时人工成本会从 `200 RMB/h` 升到 `1,000 RMB/h`。

## 来源 URL

- Washington Post: https://www.washingtonpost.com/technology/interactive/2026/robot-chores-video-data/
- The Verge / Tesla Optimus data collection operator: https://www.theverge.com/2024/8/19/24223626/tesla-optimus-humanoid-robot-motion-capture-training
- Business Insider / robotics chore footage pay: https://www.businessinsider.com/ai-startups-robotics-pay-film-chores-encord-micro1-scale-2025-10
- Business Insider / Instawork robotics training data: https://www.businessinsider.com/robotics-ai-training-data-transforming-instawork-gig-work-platform-instacore-2026-4
- DROID: https://arxiv.org/abs/2403.12945
- RoboTurk: https://arxiv.org/abs/1911.04052
- COBALT: https://arxiv.org/abs/2605.19138
- RoboMIND: https://arxiv.org/abs/2412.13877
- AgiBot World: https://arxiv.org/abs/2503.06669
- Open X-Embodiment: https://arxiv.org/abs/2310.08864
- pi0: https://www.physicalintelligence.company/download/pi0.pdf
- LingBot-VLA 2.0: https://arxiv.org/abs/2607.06403
- Green-VLA: https://arxiv.org/abs/2602.00919
- HumanEgo: https://arxiv.org/abs/2605.24934
- ACE-Ego-0: https://arxiv.org/abs/2606.17200

## 关联连接

- [[../09-training-data-deep-dive|机器人训练数据深度调研]]
- [[robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]
- [[open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
- [[vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]]
