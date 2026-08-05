---
title: ORB-SLAM3
type: entity
date_created: 2026-06-02
last_updated: 2026-08-05
aliases:
  - ORB-SLAM3
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-338-orb-slam3-full-paper.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-339-orb-slam3-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-340-orb-slam3-github-repository-and-maintenance-audit.md
tags:
  - entity/tool
  - industry/robotics-embodied-ai
  - umi
  - slam
  - visual-inertial
status: active
---

# ORB-SLAM3

## 初学者解释

ORB-SLAM3 是萨拉戈萨大学团队发布的稀疏特征视觉/视觉惯性 SLAM 库。它支持单目、双目、RGB-D、单目惯性、双目惯性，以及针孔和鱼眼相机；Atlas 能在跟踪丢失时保留多个地图，并在未来重访旧区域时重定位或合并地图。

UMI 使用了 ORB-SLAM3 的分支来处理 GoPro 数据。

业务意义：如果要产品化，不能只说“用了 ORB-SLAM3”，还要能报告成功率、失败原因、轨迹质量和重采建议。

## 能力边界

| 能力 | 判断 |
|---|---|
| 核心输出 | 相机/IMU 轨迹、稀疏地图点、关键帧和地图关系 |
| 强项 | CPU 实时、回环、重定位、多地图/多会话复用、几何可解释 |
| 主要失败 | 论文明确指出低纹理环境；运动模糊、动态场景、遮挡、重复纹理和标定/同步误差也需实测 |
| 不等于 | 稠密/语义地图、Nav2 占据栅格、路径规划、避障、功能安全定位产品 |
| 工程状态 | 官方 `v1.0` 为 2021-12-22；2026-08-05 审计时默认分支最后提交为 2022-02-10，官方示例为 ROS Melodic-era，无官方 ROS 2 包 |
| 许可证 | GPLv3；官方 README 给出闭源商业许可的联系路径 |

论文作者在其设置中报告 EuRoC 双目惯性平均 RMS ATE 约 3.5 cm、TUM-VI room 双目惯性 9 mm。该数字受数据集、对齐方式、标定和运行条件限制，不能直接当作现场 SLA。完整证据与选型见 [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]。

## 补充说明

补充：在 UMI-like 数据采集业务中，ORB-SLAM3 只是 trajectory estimator。相机/IMU 轨迹还必须与夹爪状态、TCP 外参、动作表示和 episode 时间轴对齐，并通过跳变、尺度、丢失和重定位质检，才能成为可训练数据。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。
- 不要把论文 ATE 当成产品成功率；还要报告 failed sequence、lost frame、重定位、延迟、内存、地图版本和下游任务结果。
- 不要忽略 GPLv3；闭源商业集成必须在 PoC 前完成许可路径选择。

## 关联连接

- [[SLAM]]
- [[VisualInertialSLAM]]
- [[GoPro]]
- [[_sources/orb-slam3-paper-code-benchmark-source-set|ORB-SLAM3 来源集]]
- [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
