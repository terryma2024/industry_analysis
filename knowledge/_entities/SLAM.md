---
title: SLAM 同时定位与建图
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - SLAM
  - Simultaneous Localization and Mapping
  - 同时定位与建图
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/method
  - industry/robotics-embodied-ai
  - umi
status: active
---

# SLAM 同时定位与建图

## 初学者解释

SLAM 是 Simultaneous Localization and Mapping，同时定位与建图。

它要解决的问题是：设备一边观察环境，一边估计自己在哪里，并构建环境地图。

在 UMI 中，SLAM 用来从相机和 IMU 数据恢复手持夹爪的空间运动轨迹。

#### SLAM 成功率是什么

SLAM 成功率是衡量“采集到的演示里，有多少条能成功恢复出可用空间轨迹”的指标。

在 UMI 场景里，SLAM 成功不只是程序没有报错，而是至少满足这些条件：

- 能从 episode 开始到结束输出连续的 6DoF pose。
- 轨迹没有明显跳变、飞走、尺度错误或方向翻转。
- 输出轨迹长度和视频/IMU 时间轴基本对齐。
- 轨迹通过后续质量检查，能进入训练数据集或只需轻微修正。

一个最基础的计算方式：

```text
SLAM 成功率 = 成功恢复可用轨迹的 episode 数 / 尝试跑 SLAM 的 episode 总数
```

例子：

```text
今天采了 100 条演示；
其中 90 条进入 SLAM 流水线；
70 条输出了可用轨迹；

按“进入 SLAM 的样本”计算：SLAM 成功率 = 70 / 90 = 77.8%
按“当天总采集样本”计算：端到端轨迹可用率 = 70 / 100 = 70%
```

这两个口径都要记录，不能混用：

| 指标 | 分母 | 用途 |
|---|---:|---|
| SLAM 成功率 | 实际尝试跑 SLAM 的 episode | 衡量 SLAM 算法和传感器设置是否稳定。 |
| 端到端轨迹可用率 | 当天采集的全部 episode | 衡量采集 SOP、环境、操作者和算法整体是否稳定。 |

更严格的产品化口径会把“成功”分级：

| 等级 | 含义 | 是否进入训练 |
|---|---|---|
| A | 轨迹连续、平滑、时间对齐，人工抽检通过 | 可以直接进入训练集 |
| B | 轻微抖动或短时丢失，但可修正或可截断 | 可进入低权重数据或人工复核 |
| C | 轨迹跳变、尺度错误、长时间丢失、任务关键段失败 | 不进入训练集，标记重采 |

UMI 数据服务里，建议同时记录这些字段：

```yaml
episode_id:
slam_status: success | partial | failed
slam_quality_grade: A | B | C
tracking_lost_frames:
tracking_lost_ratio:
trajectory_jump_count:
max_pose_jump:
time_alignment_error_ms:
failure_reason:
reviewer:
```

业务意义：SLAM 成功率直接影响采集成本。如果 100 条演示里只有 40 条能恢复轨迹，客户实际买到的不是 100 条数据，而是 40 条可训练数据。ToB 报价和交付应该按“有效 episode + 质量等级”核算，而不是按原始录制时长核算。

容易误解：SLAM 不是总能成功。弱纹理、强反光、快速运动、遮挡、动态人群都会让它失败。

## 补充说明

补充：在 UMI 数据产线里，SLAM 应被当作数据质检和成本指标，而不只是算法模块；成功率、失败原因和轨迹质量等级会直接决定有效 episode 成本。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[VisualInertialSLAM]]
- [[ORBSLAM3]]
- [[ThreeDSLAM]]
- [[LiDAR]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
