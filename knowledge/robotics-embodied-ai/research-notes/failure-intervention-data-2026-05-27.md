---
title: 失败轨迹与人工接管数据是否会成为具身智能稀缺资产
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-note
  - data
  - intervention-learning
  - failure-recovery
aliases:
  - 失败轨迹数据
  - 人工接管数据
  - robot failure data
  - human intervention data
source_table: ../../raw/robotics-embodied-ai/data/failure_intervention_data_sources.csv
status: draft
---

# 失败轨迹与人工接管数据是否会成为具身智能稀缺资产

> [!summary]
> 初步判断：会，但不是以“失败视频”本身成为资产，而是以**带上下文、带原因、带恢复/接管动作、可训练、可评测、可追责**的闭环数据成为稀缺资产。具身智能正从成功示教驱动的行为克隆，走向部署后从失败、接管和恢复中学习；这类数据天然稀缺，因为它需要真实任务、真实策略、真实风险边界和合规授权。

来源明细见：[failure_intervention_data_sources.csv](../../raw/robotics-embodied-ai/data/failure_intervention_data_sources.csv)。

## 结论

- **事实**：RoboMIND 已明确把失败示教作为数据集组成部分，披露 107k 轨迹中包含 5k real-world failure demonstrations，并带 detailed causes，用于 failure reflection and correction。证据：`FID-001`
- **事实**：Oopsie Data 是专门面向机器人操作失败的多实验室数据项目，强调常规评测中失败轨迹经常被丢弃，但这些轨迹可用于 offline RL、policy steering、failure prediction、bottleneck recognition 和 human intervention request。证据：`FID-002` `FID-003` `FID-004`
- **事实**：LeRobot 已把 Human-in-the-Loop / DAgger 数据采集写成工具链能力，记录 autonomous segments、recovery/correction movements，并支持反复 deploy-collect-fine-tune。证据：`FID-005` `FID-006`
- **事实**：HIL-SERL、RaC、Fleet-DAgger、Learning while Deploying、pi*0.6 等工作显示，人工接管/纠错不只是安全兜底，也是在策略分布上采集高价值训练样本。证据：`FID-007` 到 `FID-014`
- **判断**：DROID、ALOHA、Mobile ALOHA、UMI 仍主要公开表达为成功示教或演示数据集，失败/接管是否保留、如何标注、是否可训练并不透明。它们是对照组：证明大规模成功数据重要，但也暴露下一阶段数据缺口。证据：`FID-020` 到 `FID-023`
- **判断**：自动驾驶的 takeover/disengagement 体系给机器人行业一个清晰类比：人工接管日志会从工程调试副产物，逐步变成安全、评测、监管和训练闭环的一部分。证据：`FID-024` `FID-025`

## 为什么会稀缺

| 稀缺原因 | 解释 | 对数据公司意味着什么 |
|---|---|---|
| 真实失败不能随便制造 | 真实物理失败可能损坏设备、工件、环境，甚至产生人身风险 | 需要安全边界、软硬件保护、风险分级和保险/责任设计 |
| 失败分布跟策略强绑定 | 同一任务下，不同模型、不同控制频率、不同末端执行器的失败模式不同 | 数据服务要记录 policy_id、checkpoint、控制参数和机器人配置 |
| 接管点最有信息密度 | 人在“将要失败但还没彻底失败”的时刻接管，常对应策略盲点 | 需要低延迟远程接管、接管触发记录、接管前后窗口切片 |
| 标注成本高 | 成功/失败二值标签不够，真正有用的是失败原因、严重度、恢复动作和可否复现 | 需要 failure taxonomy、双人复核、质量评分、样例库 |
| 合规和客户授权难 | 部署日志可能包含客户现场、工艺、人员、设备参数 | 需要租户隔离、脱敏、边缘处理、授权模板和数据用途约束 |
| 可训练格式稀缺 | 失败数据如果只有视频，没有状态/动作/时间同步，训练价值会大幅下降 | 需要导出 LeRobot/RLDS/HDF5/Zarr，并保留元数据 |

## 如何采集

### 1. 评测式失败采集

适合实验室、整机厂、模型公司做系统 benchmark。

- 对每个 task family 定义目标状态、成功标准、禁止动作、安全边界。
- 让当前策略自主执行，记录全量轨迹，而不是只保存成功 episode。
- 每个 episode 至少保存：多视角视频、机器人状态、动作、任务 instruction、policy_id、checkpoint、环境配置、对象配置、操作者/监督者、时间戳。
- 失败 episode 额外保存：失败发生时间、失败类别、严重度、是否可恢复、是否需要人工接管。
- Oopsie 的 HDF5 episode schema 可作为第一版参考：`episode_annotations` 下保留 `success`、`failure_description`、`taxonomy`、`severity`，并保存 observations、robot_states 和 actions。证据：`FID-004`

### 2. 人工接管式采集

适合真实部署或半真实试点。

- 模型先自主执行；人类监督员通过 teach pendant、spacemouse、VR/手柄、主从臂或网页遥操作接管。
- 记录三个窗口：接管前 `pre_intervention_window`、接管期间 `intervention_segment`、释放后 `post_intervention_window`。
- 记录接管触发类型：人工主动、规则触发、模型置信度低、安全边界触发、客户/现场人员触发。
- 记录接管动作来源：人类直接控制、恢复到安全状态、重试任务、终止任务。
- LeRobot HIL 和 HIL-SERL 都体现了这种路线：用小量 demos 启动，再在在线训练中不断加入 correction/intervention。证据：`FID-005` `FID-009` `FID-010`

### 3. 恢复/纠错式采集

适合长程任务和高价值工业任务。

- 当失败将要发生时，人类先把机器人带回熟悉状态，再提供正确操作片段。
- 将 episode 切成 `mistake_state -> recovery_action -> corrected_subtask -> success/failure_outcome`。
- RaC 的思路是把 recovery/correction 扩展成专门的数据配方，而不是把失败 episode 整段丢进模仿学习。证据：`FID-011`

### 4. 合成失败采集

适合稀有风险、长尾错误和语言化失败解释。

- 从成功示教出发，在仿真中扰动关键帧、对象位姿、动作顺序、抓取姿态、接触状态，生成 counterfactual failures。
- 对生成的失败做物理可行性、视觉一致性和任务语义过滤。
- AHA/FailGen、RoboFAC、Dream2Fix 说明 failure trajectory 可以被程序化合成或从成功示教反事实生成，但真实可执行性仍需验证。证据：`FID-016` `FID-017` `FID-018`

## 如何标注

建议把标签拆成四层，避免只做“成功/失败”。

| 层级 | 字段 | 示例 |
|---|---|---|
| outcome | success、failure、partial_success、aborted、unsafe_stop | 失败但未损坏；部分完成；人工终止 |
| failure cause | perception、planning、control、grasp、contact、object_shift、occlusion、instruction、environment | 没识别透明物体；抓取偏移；线缆缠绕 |
| intervention | no_intervention、human_takeover、human_hint、reset、rewind、remote_stop | 人工接管 8 秒；重置物体；远程急停 |
| recovery | unrecoverable、self_recovered、human_recovered、retry_success、retry_failed | 人类恢复后模型继续完成 |

最小可用 schema：

```yaml
episode_id:
task_id:
robot_id:
policy_id:
checkpoint_id:
environment_id:
operator_id:
instruction:
outcome:
failure_start_ts:
failure_end_ts:
failure_category:
severity:
intervention_required:
intervention_start_ts:
intervention_end_ts:
intervention_actor:
recovery_action:
final_outcome:
data_quality_score:
license_scope:
privacy_level:
```

标注流程：

1. 机器预切片：按接管按钮、速度异常、力/电流异常、停止事件、规则 violation 自动生成候选 failure windows。
2. 人工一标：标 success/failure、失败原因、严重度、接管动作。
3. 人工二审：只抽查高价值/高风险/标签分歧样本。
4. 自动一致性检查：时间戳、视频/动作长度、action/state 对齐、episode 完整性、taxonomy 合法性。
5. 训练反馈闭环：记录哪些失败样本被训练使用，是否降低相同失败模式。

## 如何使用

| 用法 | 训练/评测位置 | 数据要求 | 代表证据 |
|---|---|---|---|
| Failure prediction | 执行前/执行中判断“是否将要失败” | 成功和失败对照、失败发生前窗口 | Oopsie、RoboMD |
| Intervention request | 模型不确定或危险时请求人类接管 | 接管触发点、风险标签、监督员响应时间 | Oopsie、Fleet-DAgger |
| Recovery policy | 训练从坏状态回到可继续状态 | 失败状态、恢复动作、恢复后结果 | RaC、Dream2Fix、Failure-Aware RL |
| Offline RL / RLHF-style ranking | 从成功/失败/纠错轨迹中学习偏好或奖励 | outcome、严重度、任务完成度、负样本 | HIL-SERL、SSDF |
| VLA failure reasoning | 用语言解释失败原因并指导下一步 | 视频、任务文本、失败类别、自然语言解释 | AHA、RoboFAC |
| Data curation | 找训练集里导致部署失败的模式 | rollout 失败日志、训练样本影响分析 | Deployment-Time Reliability |
| Benchmark | 衡量模型在长尾失败和恢复上的能力 | 固定 failure taxonomy、held-out scenes/tasks | RoboMIND failure demos、Oopsie |

关键提醒：失败轨迹不能直接等价为“负样本越多越好”。对行为克隆来说，整段模仿失败动作可能会污染策略；更可行的是切出失败前状态、失败检测标签、人类恢复片段、成功对照和可学习的纠错动作。

## 数据集/工具对照

| 项目 | 是否明确保留失败 | 是否明确有人类接管/纠错 | 格式/工具 | 备注 |
|---|---:|---:|---|---|
| RoboMIND | 是 | 不完全明确 | dataset | 明确 5k real-world failure demonstrations with detailed causes |
| Oopsie Data | 是 | 可支持 | HDF5，计划导出 RLDS/LeRobot | 专门为失败轨迹采集/标注设计 |
| LeRobot HIL | 是，作为 HIL episode | 是 | LeRobotDataset / HIL workflow | 适合国内工具链适配 |
| HIL-SERL | 有正/负样本 | 是 | RL training system | 强调 sparse reward + intervention |
| DROID | 未明确 | 未明确 | large robot dataset | 成功示教为主，失败保留待验证 |
| UMI | 未明确 | 部署可人工 stop/control | Zarr | 公开 pipeline 更强调 SLAM/可用数据，不是失败标签 |
| ALOHA / Mobile ALOHA | 未明确 | 主要是遥操作示教 | ACT data | 低成本成功示教代表 |
| AHA / RoboFAC | 是 | 偏失败解释/纠错 | VLM QA / synthetic + real | 适合训练 failure reasoning |
| 自动驾驶 takeover | 是 | 是 | disengagement/takeover logs | 可做监管和商业闭环类比 |

## 对国内 ToB 业务的商业价值

### 可能的产品形态

1. **失败数据采集套件**：机器人端 recorder、接管按钮、事件触发器、多相机同步、状态/动作日志、edge NAS。
2. **远程接管平台**：低延迟视频流、权限管理、接管回放、接管质量评分、操作员排班。
3. **Failure taxonomy + annotation service**：按行业定义失败原因、严重度、恢复动作和安全等级。
4. **可训练数据包交付**：LeRobot/RLDS/HDF5/Zarr 导出，带 train/val/test split、dataset card、loader、质量报告。
5. **部署数据闭环服务**：从客户机器人 fleet 日志中挖失败，做模型微调前的数据筛选、标注和评测。
6. **工业异常/恢复 task pack**：面向 CNC、仓储拣选、零售补货、酒店/医院服务、实验室自动化等场景，交付带 exception coverage 的任务包。

### 谁会先买

- 具身模型公司：需要 post-training 和 failure recovery 数据。
- 整机厂：需要交付前评测、客户试点数据闭环、远程运维降本。
- 工业集成商：需要把客户现场异常、工艺状态和机器人动作对齐。
- 高校/实验室：需要 failure-aware benchmark 和可复现实验工具。
- 地方公共平台：可能建设具身智能数据工厂、评测中心、训练场。

### 定价逻辑

| 计价单位 | 适合场景 | 备注 |
|---|---|---|
| 每 episode | 标准实验室任务、短任务 | 要按有效 episode 而不是原始录制时长计价 |
| 每 task pack | 工业客户/模型公司 | 包含任务定义、异常覆盖、schema、loader、QA |
| 每接管小时 | 远程运维/在线部署 | 需区分值守、主动接管、标注回放 |
| 每失败类别 | 长尾异常补齐 | 适合稀有失败模式的专项采集 |
| 数据闭环订阅 | 已部署 fleet | 按机器人数量、日志量、标注量、模型迭代频率计费 |

## 风险

- **训练污染风险**：把失败动作当成正向模仿，会降低策略；必须区分 detection、avoidance、recovery、correction。
- **数据权属风险**：客户现场数据可能含工艺秘密、人员影像、设备参数；需要合同明确数据用途、再训练权、模型权属和删除权。
- **安全责任风险**：诱发失败或接管不及时可能造成损失；采集服务必须有安全边界和现场责任分工。
- **泛化不足风险**：失败模式高度依赖任务、本体、policy checkpoint；通用失败数据不一定迁移。
- **标注一致性风险**：失败原因常有多因一果，需要 taxonomy、二审和 inter-rater agreement。
- **商业时点风险**：如果客户仍处于 demo 阶段，没有足够部署/评测频率，接管数据服务会缺少稳定需求。

## 待验证项

- DROID 原始数据是否保留 unsuccessful attempts、reset、intervention 或 success flags；公开论文摘要只证明 demonstration 规模，不证明失败标签。
- ALOHA/Mobile ALOHA 开源数据中是否存在失败 episode 或 only-success filtering 规则。
- UMI 社区数据是否记录 task-level failure、human stop、retry，而不仅是 SLAM/数据可用性。
- RoboMIND 5k 失败示教的下载字段、失败 taxonomy、许可和商业可用性。
- LeRobot HIL 的当前稳定 API、数据字段和与标准 LeRobotDataset v3 的兼容细节。
- 国内智元、宇树、IO-AI、星海图等是否已经在产品中记录接管、失败原因、恢复动作，并是否向 ToB 客户开放。
- TalosHub 等商业公司是否有真实客户、样例数据和可训练 loader；目前只能作为市场信号。

## 下一步建议

1. 做一张 `failure_intervention_schema_comparison.csv`：对比 Oopsie、LeRobot HIL、RoboMIND、DROID、UMI、RLDS、Zarr。
2. 用 LeRobot 做一个 v0 schema demo：模拟 `success/failure/intervention_start/intervention_end/failure_category/recovery_action` 字段。
3. 抽样下载 RoboMIND/Oopsie/LeRobot HIL 示例数据，确认字段真实存在，而不是只存在于文档。
4. 访谈 3 类潜在买家：具身模型团队、整机厂算法负责人、工业集成商交付负责人，验证他们是否愿意为“失败/接管数据包”付费。
5. 对国内目标行业选一个低风险场景试点，例如桌面整理、仓储 tote 拣选、机床上下料的非危险离线采集，先验证采集-标注-导出-训练闭环。

## 来源 URL

- RoboMIND: https://arxiv.org/abs/2412.13877
- Oopsie Data: https://oopsie-data.com/
- Oopsie Quickstart: https://oopsie-data.com/quickstart/
- Oopsie Format: https://oopsie-data.com/format/
- LeRobot HIL: https://github.com/huggingface/lerobot/blob/main/docs/source/hil_data_collection.mdx
- LeRobot: https://github.com/huggingface/lerobot
- DAgger: https://arxiv.org/abs/1011.0686
- HG-DAgger: https://arxiv.org/abs/1810.02890
- HIL-SERL: https://arxiv.org/abs/2410.21845
- HIL-SERL project: https://hil-serl.github.io/
- RaC: https://arxiv.org/abs/2509.07953
- pi*0.6 / RECAP: https://arxiv.org/abs/2511.14759
- Learning while Deploying: https://arxiv.org/abs/2605.00416
- Fleet-DAgger: https://arxiv.org/abs/2206.14349
- Learning from Imperfect Demonstrations with Self-Supervision: https://arxiv.org/abs/2401.08957
- AHA: https://aha-vlm.github.io/
- RoboFAC: https://arxiv.org/abs/2505.12224
- Dream2Fix: https://arxiv.org/abs/2603.13528
- Failure-Aware RL: https://failure-aware-rl.github.io/
- Deployment-Time Reliability: https://arxiv.org/abs/2603.11400
- RoboMD: https://arxiv.org/abs/2412.02818
- DROID: https://arxiv.org/abs/2403.12945
- UMI GitHub: https://github.com/real-stanford/universal_manipulation_interface
- Mobile ALOHA: https://arxiv.org/abs/2401.02117
- ALOHA/ACT: https://arxiv.org/abs/2304.13705
- ADAS-TO: https://arxiv.org/abs/2603.06986
- California DMV Disengagement Reports: https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/disengagement-reports/
- TalosHub: https://taloshub.io/
