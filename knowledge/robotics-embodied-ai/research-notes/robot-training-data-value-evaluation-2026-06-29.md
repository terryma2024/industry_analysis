---
title: 具身智能训练数据价值评估框架
type: synthesis
date_created: 2026-06-29
last_updated: 2026-06-29
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-054-open-x-embodiment-robotic-learning-datasets-and-rt-x-models.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-057-robomind-benchmark-on-multi-embodiment-intelligence-normative-data-for-robot-man.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-078-data-scaling-laws-in-imitation-learning-for-robotic-manipulation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-095-oopsie-data-manipulation-failure-dataset-project.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-097-lerobot-human-in-the-loop-data-collection-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md
  - https://arxiv.org/abs/2410.18647
  - https://arxiv.org/abs/2403.12945
  - https://arxiv.org/abs/2503.06669
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - robot-training-data
  - data-collection
  - data-quality
  - data-valuation
status: active
aliases:
  - 机器人训练数据价值评估
  - 具身智能数据价值
  - Robot Data Valuation
---

# 具身智能训练数据价值评估框架

> [!summary]
> 截至 2026-06-29，具身智能训练数据的价值不应按“采了多少小时/多少条 episode”估，而应按**它对目标机器人策略的边际能力提升、可复用性、可审计性和采集成本风险比**来估。采集前先问“它补哪个能力缺口”，采集中看“它是否可训练、可复现、可追责”，采后用 holdout rollout 或离线代理指标验证“新增数据是否真的改变模型”。

## 一句话结论

推荐把训练数据价值写成一个经营公式：

```text
Data Value = Expected Capability Lift x Reuse Multiplier x Trust Multiplier
             / Fully Loaded Cost and Risk
```

其中：

- `Expected Capability Lift`：这批数据能否提升目标任务、未见物体、未见场景、长尾失败或安全边界上的成功率。
- `Reuse Multiplier`：同一批数据能否被多个模型、多个本体、多个客户或多个训练阶段复用。
- `Trust Multiplier`：时间同步、标定、schema、许可、隐私、质检、baseline 和版本记录是否足够完整。
- `Fully Loaded Cost and Risk`：不仅是采集人工成本，还包括硬件、场地、标定、重采、清洗、标注、合规、训练适配和客户现场风险。

这个公式的含义很直接：**一条昂贵但能覆盖真实部署长尾、带失败/接管标签、能让模型在未见场景成功率提升的数据，价值可能高于一百条重复成功示教。**

## 为什么数量不是第一指标

机器人数据与互联网文本/图像数据不同，物理采集有三层约束：

1. **采集成本高**：DROID 用固定硬件和分布式采集，公开数据仍只有 76k demonstrations、350 hours、564 scenes、84 tasks、50 collectors 这一量级，说明真实世界多样化采集本身就是重工程。证据：[`SRC-robotics-055`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md)。
2. **边际收益递减**：Data Scaling Laws in Imitation Learning 指出，环境和物体多样性通常比单个环境/物体下重复 demonstration 数更重要；当每个环境/物体的示教达到一定阈值后，继续堆重复示教收益变小。证据：[`SRC-robotics-078`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-078-data-scaling-laws-in-imitation-learning-for-robotic-manipulation.md)。
3. **可训练性不等于可记录性**：LeRobot、AIRSPEED 等工具链强调标准格式、同步视频/状态/动作、元数据、转换和 streaming；这说明“采到视频”只是 raw material，必须变成能被训练代码稳定加载的 episode 才是训练资产。证据：[`SRC-robotics-052`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md)、[`SRC-robotics-188`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md)。

## 五层评估框架

### 1. 任务价值：这批数据补哪个能力缺口

| 维度 | 高价值信号 | 低价值信号 | 采集决策 |
|---|---|---|---|
| 场景缺口 | 目标客户真实场景中频繁出现，现有模型明显失败 | 展示性任务，部署中很少出现 | 优先采真实部署任务，而不是 demo 好看的任务 |
| 泛化缺口 | 覆盖未见物体、未见布局、未见光照、未见人流/遮挡 | 与已有数据同质，只有背景轻微变化 | 优先增加环境/物体多样性 |
| 长尾缺口 | 覆盖危险、难恢复、高损失失败模式 | 只采容易成功的标准动作 | 给失败/接管/恢复单独预算 |
| 商业缺口 | 能直接服务一个客户验收指标或公共训练场任务包 | 没有明确买方或评测协议 | 先定义验收指标再采 |
| 战略缺口 | 能积累公司独有 know-how，如装配、仓储、零售后场、工业复合作业 | 公开数据集中已大量存在且无差异化 | 只采有专有场景优势的数据 |

判断规则：采集需求必须能写成一句话：`为了把模型在 X 场景 / Y 物体 / Z 失败模式上的成功率从 A 提到 B，需要采 N 条覆盖 C 分布的 episode`。如果写不出来，先不要大规模采。

### 2. 学习价值：模型能否从中学到东西

| 维度 | 要看什么 | 典型风险 |
|---|---|---|
| 因果可见性 | 关键状态是否在 observation 里可见；是否需要 depth、LiDAR、力觉、触觉、第三视角 | 视频看得见人类动作，但机器人 policy 看不到关键接触状态 |
| 动作可执行性 | action 是否是目标机器人可执行的控制空间；是否有 robot-native action 和 canonical action | 人类第一视角数据难以 retarget 到机器人 |
| 时间结构 | fps、控制频率、延迟、timestamp 是否稳定 | 视觉帧和动作错位，训练学到错误对应关系 |
| 成功边界 | 是否记录 success/failure/partial success、终止原因、重试次数 | 只有“成功视频”，无法训练避错或恢复 |
| 任务语言 | 指令是否粒度适中；是否有 subtask / instruction segment | 任务文本太泛，模型无法对应动作阶段 |

AgiBot World 的价值信号不仅是 1M+ trajectories，更在于标准化采集、human-in-the-loop verification、长时程任务和多场景；RoboMIND 的价值信号也包括失败示教。证据：[`SRC-robotics-058`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md)、[`SRC-robotics-057`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-057-robomind-benchmark-on-multi-embodiment-intelligence-normative-data-for-robot-man.md)。

### 3. 工程价值：能否变成可交付数据包

一批数据进入采集计划前，应要求至少能交付以下资产：

| 交付物 | 最低要求 | 高价值加分 |
|---|---|---|
| raw layer | 原始视频、传感器日志、机器人状态、控制命令、标定文件保留 | 支持回放、重处理、重新导出 |
| processed layer | episode 边界、timestamp 对齐、observation/action/state/task 字段完整 | 支持 LeRobot/RLDS/HDF5/Zarr/MCAP 多格式导出 |
| metadata | robot_id、operator_id、scene_id、object_id、task_id、calibration_id、policy_id | 可追溯到操作者、设备、场景、策略版本 |
| QC report | 丢帧、漂移、时间同步、异常动作、成功率、重采率 | 有自动质检阈值和人工复核记录 |
| baseline | 至少跑一个 ACT/Diffusion Policy/VLA fine-tune 或小样本 ablation | 有 holdout task/env/object 和 rollout 视频 |
| license/security | 采集授权、客户数据边界、隐私脱敏、商业使用限制 | 能进入客户私有化或数据产品目录 |

LeRobot 的 Parquet + MP4/images + metadata 方向适合作为工程互通默认出口；AIRSPEED 的 HDF5 episode + 多格式转换思路则提醒：工业交付不要只保留一个压缩训练格式。证据：[`SRC-robotics-052`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md)、[`SRC-robotics-188`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md)。

### 4. 经济价值：边际收益是否超过全成本

采集项目应按“有效 episode 成本”而不是“录制成本”核算：

```text
Cost per Useful Episode =
  (硬件折旧 + 场地 + 操作者 + 机器人占用 + 标定 + 数据工程 + 标注/QC + 重采 + 训练验证 + 合规)
  / 通过 QC 且能提升目标指标的 episode 数
```

建议每个采集任务维护四个数：

| 指标 | 说明 | 用途 |
|---|---|---|
| `raw_episode_cost` | 采一条原始 episode 的表面成本 | 观察采集效率 |
| `qc_pass_rate` | 通过同步、标定、字段、成功/失败标签检查的比例 | 识别采集 SOP 或硬件问题 |
| `useful_episode_cost` | 通过 QC 并进入训练集的成本 | 做供应商/任务横向比较 |
| `marginal_lift_per_100_episodes` | 每新增 100 条对 holdout 成功率/失败率的影响 | 决定继续采还是换分布 |

边际收益低时，不要机械追加同类数据；应切换到新物体、新布局、新操作者、新传感器、新失败模式，或转向仿真/合成数据扩增。

### 5. 战略价值：是否形成可复用壁垒

| 数据类型 | 短期价值 | 长期壁垒 |
|---|---|---|
| 通用桌面成功示教 | 快速启动训练 | 容易被开源数据和低成本采集追平 |
| 客户现场复合作业 | 直接服务商业验收 | 场景 know-how、客户流程和安全边界难复制 |
| 失败/接管/恢复 | 提升部署稳定性 | 需要真实部署和持续运营，不易一次性外包获得 |
| 多本体对齐数据 | 支持平台型模型 | schema、action 表示、标定和适配器是壁垒 |
| 触觉/力觉/接触数据 | 支撑精细操作 | 传感器、标定、标签和控制策略门槛更高 |
| 数据治理/QC 记录 | 降低客户信任成本 | 可形成标准、审计和数据产品化能力 |

对中国具身智能公司而言，短期最值得积累的不是“全球最大泛化数据集”口号，而是某些垂直场景的**高密度任务包 + 失败闭环 + 可复现 baseline + 客户验收指标**。

## 采集前打分表

建议用 100 分制，不追求伪精确，目的是让团队在采集前把隐含判断摊开。

| 模块 | 分值 | 打分问题 |
|---|---:|---|
| 任务/客户相关性 | 15 | 是否对应真实部署、客户验收或训练场评测任务 |
| 分布新增性 | 15 | 是否补足现有数据缺口，而非重复同质数据 |
| 学习可见性 | 15 | 关键状态、动作、接触、时间结构是否能被模型观察和学习 |
| 长尾/失败价值 | 10 | 是否覆盖失败、接管、恢复或安全边界 |
| 工程可训练性 | 15 | 是否能稳定导出 LeRobot/RLDS/HDF5/Zarr 等训练格式 |
| 质检和可追溯 | 10 | 是否有 metadata、QC、标定、版本和许可记录 |
| 经济性 | 10 | 有效 episode 成本是否可接受，重采率是否可控 |
| 复用性 | 10 | 是否能服务多个模型、本体、客户或训练阶段 |

解释：

- `80-100`：优先采集，适合进入正式任务包。
- `60-79`：小批试采，先做 50-200 条 episode 和 ablation。
- `40-59`：只做探索，不宜规模化。
- `<40`：暂停，先补任务定义、传感器、schema 或客户需求。

## 采集中实时质检

采集现场不要等到训练失败才发现数据坏了。最低实时看板应包括：

| 类别 | 现场指标 | 触发动作 |
|---|---|---|
| 传感器 | 相机掉帧、曝光过暗/过曝、深度空洞、力觉饱和 | 暂停采集，修参数或换位 |
| 时间同步 | video/state/action timestamp drift、控制延迟 | 重新标定时钟或降低频率 |
| 轨迹 | 突跳、异常速度、夹爪状态缺失、episode 边界错误 | 标记重采或剔除 |
| 任务分布 | 物体/场景/操作者覆盖是否达标 | 动态调整采集清单 |
| 成败分布 | 全成功或全失败是否异常 | 调整任务难度，补失败/恢复标签 |
| 标签一致性 | instruction、subtask、failure cause 是否混乱 | 现场统一标注口径 |

采集中最重要的管理动作是“stop-loss”：如果前 30-50 条 episode 的 QC pass rate 低于阈值，应先修 SOP/标定/硬件，而不是继续堆坏数据。

## 采后验证：数据是否真的有用

采后至少做三种验证：

1. **分布体检**：episode 数、任务分布、物体分布、场景分布、操作者分布、成功/失败比例、动作频谱、静止段比例、传感器缺失率。
2. **离线代理指标**：训练 loss 不是充分证据，但可看 action prediction、nearest-neighbor novelty、coverage、embedding cluster、异常轨迹。
3. **真实或仿真 rollout**：必须设置 holdout object / holdout environment / holdout task；如果新增数据只提升训练场景，不提升 holdout，就不应继续采同分布。

最小实验设计：

| 版本 | 数据 | 验证问题 |
|---|---|---|
| baseline | 现有数据 | 当前模型瓶颈在哪里 |
| +same-more | 加同分布 100-300 条 | 重复数据是否还有边际收益 |
| +diverse | 加新物体/新场景/新操作者 | 多样性是否提升泛化 |
| +failure | 加失败/接管/恢复 | 是否降低部署失败率或恢复时间 |
| +sensor | 加 depth/LiDAR/force/tactile | 新传感器是否真的改善接触/遮挡任务 |

如果 `+same-more` 不提升而 `+diverse` 提升，说明采集预算应转向多样性；如果 `+failure` 只降低失败率但不提升成功率，它仍可能有很高商业价值，因为客户关心安全和稳定。

## 一票否决项

以下情况即使数据看起来稀缺，也不应进入正式训练资产：

- 无法确认采集许可、客户授权或隐私边界。
- 缺少机器人动作、状态或时间戳，只能作为观察视频使用。
- 关键传感器与目标部署机器人不一致，且没有 retargeting/adapter 方案。
- 失败标签、成功标签或 episode 边界无法复核。
- 标定文件缺失，坐标系/单位/控制模式不清楚。
- 数据无法被主训练栈加载，或转换依赖个人脚本且不可复现。
- 只在训练集提升，holdout rollout 没有改善，且无法解释原因。

## 对采购/外包数据的尽调问题

如果从第三方数据服务商采购或委托采集，至少问：

| 类别 | 问题 |
|---|---|
| 数据定义 | episode、task、success、failure、intervention 的口径是什么 |
| 本体和控制 | 用什么机器人、控制频率、action space、坐标系、单位 |
| 传感器 | 相机/深度/力觉/触觉/IMU/LiDAR 配置、标定和同步方式 |
| 场景分布 | 多少场景、多少物体、多少操作者、是否有长尾扰动 |
| 质量 | QC pass rate、重采率、丢帧率、timestamp drift、标注一致性 |
| 格式 | 是否支持 LeRobot/RLDS/HDF5/Zarr/MCAP，是否保留 raw |
| 验证 | 是否提供 baseline 训练、holdout 评测和失败样例 |
| 合规 | 数据权属、商业使用、客户隐私、跨境、删除和审计 |
| 复购 | 新任务复采周期、成本下降曲线、adapter 是否可复用 |

## 适用于不同路线的权重差异

| 路线 | 价值权重最高的维度 |
|---|---|
| VLA 预训练 | 跨任务/跨本体/跨场景多样性、语言标签、格式可混训 |
| 单任务模仿学习 | 同任务下物体/环境多样性、动作质量、holdout 成功率 |
| 工业部署 | 客户真实流程、失败/恢复、安全边界、现场可复现 |
| 人形/双臂 | 长时程 subtask、全身/双臂同步、接触状态、多视角 |
| 灵巧手/精细操作 | 触觉/力觉、接触可见性、失败原因、微小动作精度 |
| 数据平台公司 | 多格式导出、QC、元数据、权限、私有化和客户验收 |
| 公共训练场/测评中心 | 标准任务包、统一 schema、可审计数据、评测协议 |

## 当前判断

- **事实**：开源和产业数据集已经从“只公布数据规模”转向强调多样性、标准化采集、human-in-the-loop verification、metadata、格式互通和 baseline 复现。证据：DROID、AgiBot World、LeRobot、AIRSPEED。
- **判断**：对商业公司来说，最有价值的数据不是最容易采的数据，而是能解释和减少真实部署失败的数据。
- **判断**：未来数据采购/外包的验收单位会从“小时数/条数”迁移到“有效 episode、QC 通过率、holdout 提升、失败率下降、可复用 adapter 和可审计数据包”。
- **假设**：如果中国地方训练场、数据券和数据产品目录继续推进，具身数据服务会逐步形成类似“任务包 + 数据包 + 测评报告 + 复采服务”的标准商业形态。

## 后续可做

- 建一个 `robot-dataset-inspector` 工具，对 LeRobot/HDF5/Zarr/RLDS 输出自动价值体检表。
- 为一个具体场景做试采预算：例如零售后场补货、仓储拣选、轻装配或实验室耗材整理。
- 把本页打分表做成 CSV 模板，用于数据采集项目立项和供应商尽调。
- 对 AgiBot World、RoboMIND、DROID、LeRobot 样例做实际字段级核验，验证失败/接管/metadata 的可用性。

## 关联连接

- [[../09-training-data-deep-dive|机器人训练数据深度调研]]
- [[open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
- [[dataset-schema-comparison-2026-05-27|具身智能数据集 Schema 横向比较]]
- [[failure-intervention-data-2026-05-27|失败轨迹和人工接管数据]]
- [[airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]
- [[../../_concepts/robot-training-data|Robot Training Data]]
- [[../../_entities/QualityControl|Quality Control 数据质检]]
