---
title: Do As I Do 灵巧操作视频数据深度调研
type: synthesis
date_created: 2026-07-07
last_updated: 2026-07-07
sources:
  - knowledge/_sources/bilibili-bv1wftk6eez8-do-as-i-do.md
  - raw/_inbox/transcripts/2026-07-07-bilibili-bv1wftk6eez8-do-as-i-do.json
  - knowledge/robotics-embodied-ai/sources.csv
tags:
  - bilibili
  - robotics
  - embodied-ai
  - robot-training-data
  - dexterous-manipulation
status: active
---

# Do As I Do 灵巧操作视频数据深度调研

> [!summary]
> 本页是对单个选中视频 `BV1WfTk6EEZ8` 的深研。视频解读 UC Berkeley `Do as I Do: Dexterous Manipulation Data from Everyday Human Videos`。视频中的关键数字和方法已用 arXiv HTML 交叉验证；Bilibili 仍只作为 B 级解释线索。

## Source Metadata

| Field | Value |
|---|---|
| Bilibili source | [[_sources/bilibili-bv1wftk6eez8-do-as-i-do|Do As I Do source card]] |
| BV | `BV1WfTk6EEZ8` |
| URL | https://www.bilibili.com/video/BV1WfTk6EEZ8 |
| Author | 失控的PM |
| Published | unknown |
| Plays captured by script | 397 |
| Extraction | Volcengine ASR via daily pipeline |
| Raw transcript | [2026-07-07 transcript](../../raw/_inbox/transcripts/2026-07-07-bilibili-bv1wftk6eez8-do-as-i-do.json) |
| Primary source | `SRC-robotics-241` / `SRC-ai-056`，arXiv `2606.19333` |

## Full-Video Thesis

视频认为 Do As I Do 的意义在于把日常人类视频转成机器人可用的灵巧操作数据，从而缓解遥操作数据贵、慢、难规模化的问题。论文确实提出了两阶段流程：先从 monocular RGB 视频重建手-物交互，再将估计出的交互重定向为真实机器人可执行动作。

仓库判断：这条线索对中国具身数据产业很重要，但不能理解为“互联网视频马上替代遥操作”。更准确的表述是：互联网/第一人称/生成视频可成为候选数据源，前提是经过严格筛选、4D 重建、动力学重定向、仿真验证和真机抽检。

## Facts

| Fact | Evidence |
|---|---|
| Do As I Do 论文由 UC Berkeley 作者提出，目标是从 everyday monocular RGB human videos 生成多指灵巧机器人手可执行数据。 | `SRC-robotics-241` / `SRC-ai-056`，arXiv `2606.19333`。 |
| 论文方法包括两步：reconstruction 和 retargeting；reconstruction 估计 3D hand/object/camera，retargeting 用 simulation 中的 sampling-based optimization 转为 robot action。 | arXiv HTML method section；视频转录与之相符。 |
| 论文使用 SAM 3/SAM 3D、MoGe、guided diffusion/object tracking 等组件处理手、物体和姿态。 | arXiv HTML lines around method; Bilibili transcript。 |
| Retargeting 表中 reconstruction 数据成功率从 Annealed Sampling baseline 的 0.25 提升到 +Transition Reward 的 0.71；OakInk2 从 0.72 提升到 0.81。 | arXiv HTML Table 3 / `SRC-robotics-241`。 |
| 论文称 real-world deployment 使用 bimanual setup with Sharpa Wave hands and UR3e arms, commanded at 50 Hz。 | arXiv HTML experimental setup / `SRC-robotics-241`。 |
| 论文 human data filtering playbook 对 100DOH 抽样 2000 个 10 秒 clips，最终只有 83 个（4%）通过 reconstruction pass。 | arXiv HTML Human Data Filtering Playbook / `SRC-robotics-241`。 |

## Estimates

| Estimate | Status |
|---|---|
| 视频说“全网几百万小时视频是机器人免费资料”是方向性类比。 | 论文实际强调需要筛选，100DOH 样本中仅约 4%-5% 直接相关。 |
| “中国工厂 ego 第一人称 + 双目 + 外部相机短期性价比高”是作者产业判断。 | 需用中国工厂数据采集项目成本、工人干扰、客户 ROI 验证。 |
| “从石器时代进入海量视频自我进化新纪元”是营销化表达。 | 本页不作为事实。 |

## Judgments

- **数据价值**: Do As I Do 证明“观察性视频 -> 机器人经验数据”有可行路径，但质量筛选和物理重定向是核心瓶颈。
- **产业判断**: 对创业公司，最有价值的不是简单爬视频，而是做视频筛选、重建、物理仿真、重定向、真机抽检和 dataset packaging。
- **中国启发**: 中国制造现场适合做低干扰的人类作业视频采集，但应优先采 task boundary 明确、手-物交互清晰、相机运动可控的片段。
- **风险判断**: 单目 RGB 的深度/接触歧义、刚体假设、环境约束缺失和物理模拟近似，会限制它直接进入高风险生产任务。

## Hypotheses

1. 未来具身数据平台会把“遥操作 episode”和“人类视频重建 episode”并列管理，前者质量高，后者规模大但需筛选。
2. 对灵巧操作，数据服务商会从按小时采集收费转向按“可训练、可复现、通过真机抽检的 trajectory”收费。
3. 中国工厂若能低干扰采集人类手部作业视频，可能在工序级灵巧操作数据上形成成本优势。

## Industry Implications

- **数据公司**: 需要建立 video filtering playbook，自动剔除无交互、边界不清、镜头剧烈运动、遮挡严重和模型无法重建的片段。
- **机器人公司**: 可把 Do As I Do 类方法用于生成候选轨迹，再用遥操作/真机数据校正。
- **工具链**: 需要把 SAM/3D reconstruction、MuJoCo/Isaac、retargeting、LeRobot/RLDS/HDF5 导出接成流水线。

## Investment View

- **可关注方向**: 人类视频到机器人数据转换、灵巧手数据平台、4D hand-object reconstruction、retargeting simulation、数据筛选/质检。
- **监控指标**: 视频通过率、trajectory 成功率、真机复现率、单位可用轨迹成本、下游策略提升。
- **风险**: 数据版权/隐私、单目深度误差、仿真与真机差距、只适用于刚体物体、无法处理全场景约束。

## Career View

- **角色方向**: 机器人数据工程、3D vision、手-物交互重建、MuJoCo/Isaac 仿真、灵巧手控制、dataset QA。
- **作品集建议**: 选 10 段简单手-物交互视频，做自动筛选、3D 重建、仿真重定向和失败原因报告；重点展示可复现性和质量判断。

## Risks And Follow-Up

- 需要将 `Do as I Do` 建成独立 source card，并补 raw artifact。
- 后续可与 [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|训练数据价值评估框架]] 对齐，新增“观察性视频数据”评分维度。

## 关联连接

- [[_concepts/robot-training-data|Robot Training Data]]
- [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]]
- [[_entities/DiffusionPolicy|Diffusion Policy]]
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]
- [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]
