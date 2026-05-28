---
title: UMI-like v0 采集 SOP、Schema 对照与客户数据包模板
date: 2026-05-28
tags:
  - industry/robotics-embodied-ai
  - research-note
  - umi
  - data-package
  - sop
aliases:
  - UMI v0 SOP Schema 数据包模板
  - UMI-like 数据包交付模板
---

# UMI-like v0 采集 SOP、Schema 对照与客户数据包模板

> [!summary]
> 本 note 补齐 [[08-umi-gripper-research-and-business-plan#下一步任务清单|UMI business plan 下一步任务清单]] 中尚未落地的三项：v0 任务 SOP/QC、UMI/Zarr 与 LeRobot schema 对照、客户版数据包目录。这里不填未经实测的数据指标；凡涉及成功率、成本、baseline 结果的位置都保留为 `待实测` 或交付时填写。

## 关联文件

- UMI 路线总表：[umi_related_implementations.csv](../../../raw/robotics-embodied-ai/data/umi_related_implementations.csv)
- 硬件/BOM 深表：[umi_hardware_bom_and_localization.csv](../../../raw/robotics-embodied-ai/data/umi_hardware_bom_and_localization.csv)
- UMI/Zarr - LeRobot 对照：[umi_zarr_lerobot_schema_crosswalk.csv](../../../raw/robotics-embodied-ai/data/umi_zarr_lerobot_schema_crosswalk.csv)
- v0 SOP/QC 模板：[umi_v0_cup_transfer_sop_qc_template.csv](../../../raw/robotics-embodied-ai/data/umi_v0_cup_transfer_sop_qc_template.csv)
- 上游研究：[[umi-hardware-localization-2026-05-27]]、[[dataset-schema-comparison-2026-05-27]]、[[training-data-company-verification-2026-05-27]]

## 本轮复核结论

| 原任务 | 当前状态 | 证据/产出 |
|---|---|---|
| 给 `umi_related_implementations.csv` 增加 BOM、采购、许可证、关键传感器可得性、国内替代件 | 已补到原表；Dobb-E 和 Data Scaling Laws with UMI 未做硬件 BOM 核验，保留待验证 | [umi_related_implementations.csv](../../../raw/robotics-embodied-ai/data/umi_related_implementations.csv)、[umi_hardware_bom_and_localization.csv](../../../raw/robotics-embodied-ai/data/umi_hardware_bom_and_localization.csv) |
| 选一个 v0 任务，建立 100 条演示采集 SOP 和质检表 | 已建立模板；尚未实采，因此不填写有效率/成功率 | [umi_v0_cup_transfer_sop_qc_template.csv](../../../raw/robotics-embodied-ai/data/umi_v0_cup_transfer_sop_qc_template.csv) |
| 做 UMI/Zarr 与 LeRobot schema 对照表 | 已建立字段级 crosswalk | [umi_zarr_lerobot_schema_crosswalk.csv](../../../raw/robotics-embodied-ai/data/umi_zarr_lerobot_schema_crosswalk.csv) |
| 对 IO-AI、Robotin、FirstMove、国内机器人整机厂的数据服务能力做二次交叉验证 | 已完成一轮；Robotin、FirstMove、GenRobot、灵初、禹纲仍需工商/JD/客户案例补证 | [[training-data-company-verification-2026-05-27]] |
| 做一页给潜在客户看的数据包样例目录 | 已补模板；baseline 结果字段只作为占位，必须等实际训练后填写 | 本 note 的“客户版数据包样例目录” |

## v0 任务选择

**建议 v0 任务：单臂桌面杯子转移。**

选择理由是它足够窄，能同时暴露 UMI-like 设备的关键工程问题：腕部视角是否看得清、pose source 是否连续、gripper width 是否可识别、episode 边界是否一致、导出的数据是否能被训练脚本读取。它不代表商业最优场景，只是 v0 验证任务。

已知事实边界：

- UMI community 认为一个简单单任务数据集即使只有 50 demonstrations 也有分享价值。证据：[`SRC-robotics-068`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-068-umi-robot-dataset-community.md)
- 本计划的“100 条”是 v0 验收目标，不等于已采集，也不等于有效数据量。
- 有效率、每小时 episode、baseline 成功率必须实采和训练后填写，当前全部记为 `待实测`。

## v0 SOP 摘要

| 阶段 | 必做动作 | 记录物 |
|---|---|---|
| 任务定义 | 固定杯子、起点区、目标区、桌面布局和任务文本 | `task_id`、`scene_id`、`object_manifest`、任务 instruction |
| 设备检查 | 确认 RGB、pose source、gripper width、时间戳均正常 | `camera_ok`、`pose_ok`、`width_ok`、`time_sync_ok` |
| 标定 | 写入相机内参/外参、tracker-to-TCP、夹爪宽度标定版本 | `calibration_version`、标定文件路径 |
| 采集 | 采集 100 次 attempt，保留失败、重采和拒收原因 | `attempt_id`、`episode_id`、`attempt_outcome`、`re_record_reason` |
| 质检 | 审核视频、pose 连续性、width 信号、episode 边界和任务 outcome | `episode_quality.csv` |
| 导出 | 从同一 manifest 导出 UMI/Zarr 和 LeRobot | `manifest_hash`、`zarr_path`、`lerobot_path`、`exporter_version` |
| 交付 | 提供 raw、processed、annotations、qc、exports、training、failures | `README.md`、`data_schema.md`、`qc_report.md`、`train_commands.md` |

完整字段见 [umi_v0_cup_transfer_sop_qc_template.csv](../../../raw/robotics-embodied-ai/data/umi_v0_cup_transfer_sop_qc_template.csv)。

## UMI/Zarr 与 LeRobot Schema 对照

| UMI/Zarr | LeRobot v3 | 转换建议 |
|---|---|---|
| `dataset.zarr.zip` | `data/` Parquet + `videos/` MP4 + `meta/` metadata | UMI/Zarr 保留为训练导出，LeRobot 作为工程互通导出。 |
| `/meta/episode_ends` | `meta/episodes` episode length/offset/task records | 转为 `episode_index`、`start_offset`、`end_offset`、`length`。 |
| `/data/camera0_rgb` | `observation.images.wrist` 或 `observation.images.gripper` | 保留原始 MP4；训练视图按 LeRobot feature schema 暴露。 |
| `/data/robot0_eef_pos` | `observation.state` slice | 写明单位、坐标系和 state index。 |
| `/data/robot0_eef_rot_axis_angle` | `observation.state` slice | 明确是 axis-angle，不要静默转 representation。 |
| `/data/robot0_gripper_width` | `observation.state` slice；若有命令则进入 `action` | observation 和 commanded action 分开，避免把观测当控制命令。 |
| task label 缺省 | `meta/tasks.jsonl` / `task_index` | v0 每条 episode 必填任务文本。 |
| QC 缺省 | sidecar `episode_quality.csv` 或 custom metadata | ToB 交付必须补 QC，不依赖原始 UMI 示例。 |

完整 crosswalk 见 [umi_zarr_lerobot_schema_crosswalk.csv](../../../raw/robotics-embodied-ai/data/umi_zarr_lerobot_schema_crosswalk.csv)。证据来自 UMI dataset format 与 LeRobot v3 文档：[`SRC-robotics-068`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-068-umi-robot-dataset-community.md)、[`SRC-robotics-053`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md)。

## 客户版数据包样例目录

```text
project_<customer>_<task>_<date>/
  README.md
  manifest.csv
  data_schema.md
  license_and_consent/
    data_license.md
    site_permission.md
    privacy_redaction_log.md
  raw/
    videos/
    sensors/
    calibration/
  processed/
    episodes/
    dataset.zarr/
    lerobot/
  annotations/
    task_instructions.csv
    object_manifest.csv
    failure_labels.csv
  qc/
    episode_quality.csv
    tracking_drift_report.md
    frame_drop_report.md
    rejected_episodes.csv
    sample_replay.mp4
  exports/
    dataset.zarr.zip
    lerobot_dataset/
    hdf5_or_mcap_if_requested/
  training/
    configs/
    train_commands.md
    evaluation_report.md
    checkpoints/
  failures/
    failure_samples.csv
    recovery_or_retake_notes.md
  deliverables/
    customer_summary.md
    acceptance_checklist.md
```

> [!warning]
> `evaluation_report.md` 和 `checkpoints/` 只能在实际 baseline 训练后交付；当前模板不能预填成功率、loss、训练时长或 GPU 成本。

## 仍待验证

- 用真实 100 条 attempt 填充 `episode_quality.csv`，计算有效 episode、重采率、pose 失败率和导出失败率。
- 实际跑通 UMI/Zarr -> LeRobot 的转换脚本，记录 exporter 版本和字段损失。
- 选择一组 baseline（ACT、Diffusion Policy 或 LeRobot 示例策略）做小任务过拟合验证，再把训练结果写入客户样例。
- 对 Robotin、FirstMove、GenRobot、灵初、禹纲补工商、招聘 JD、样例数据和客户案例证据，避免只依据官网口径。
