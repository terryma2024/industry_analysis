---
title: UMI 硬件 BOM、国产化与数据包交付研究
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-note
  - umi
  - hardware
  - data-collection
aliases:
  - UMI hardware localization
  - UMI BOM 国产化
---

# UMI 硬件 BOM、国产化与数据包交付研究

> [!summary]
> 本 note 只作为 subagent 5 的中间调研结果，不改动主知识笔记。结论是：国内切入具身智能数据采集，第一阶段不应押注单一 UMI 论文复刻，而应做“可替换追踪源 + 可训练数据包 + 质检报告”的产品。UMI-3D 的 BOM 最适合中国本土化，FastUMI 的工程方向最接近产品，UMI-FT/TacUMI 适合作为高价值接触任务的二期路线。

## 输出文件

- 数据表：[umi_hardware_bom_and_localization.csv](../../raw/robotics-embodied-ai/data/umi_hardware_bom_and_localization.csv)
- 本研究 note：[[umi-hardware-localization-2026-05-27]]

## 一页结论

| 路线 | 当前可产品化程度 | 关键风险 | 中国落地建议 |
|---|---:|---|---|
| UMI original | 中 | GoPro/ORB-SLAM3 复现和弱纹理失败；原始 Google 硬件文档需人工复核 | 用作 v0 数据接口和 SOP，不把原版硬件当最终产品 |
| FastUMI | 中高 | T265 停产；RoboBaton Mini 替代需实测 | 抽象 pose tracker，优先验证国产 VIO 模块 |
| UMI-3D | 高 | LiDAR-camera 标定、同步和 ROS 工程复杂 | 作为国内 v1 主线，Livox/Hikrobot/ZLKC 供应链友好 |
| TacUMI | 低到中 | 无公开 BOM/license；触觉/力传感器供应不明 | 作为接触任务的高端方案研究，不做首发 SKU |
| UMI-FT | 中 | CoinFT 非商用许可；传感器漂移和供电敏感 | 不直接商用 CoinFT，改做可替换力觉模块 |
| MV-UMI | 中 | 代码/硬件仓库 still coming soon | 作为多视角数据服务插件，等待公开实现 |
| Actuated UMI | 高 | 不是完整数据流水线；伺服替代要验证 | 做 robot-side gripper 参考件 |
| GELLO/ALOHA | 高但重 | 需要目标机器人，成本高 | ToB 服务对照路线：客户有机器人时用 GELLO/ALOHA，客户没机器人或需外场覆盖时用 UMI-like |

## 官方证据摘录

- UMI original：官方 repo 是 MIT，README 直接链接 Hardware Guide、Data Collection Instruction、SLAM repo，并说明 GoPro SLAM pipeline、GoPro Labs 和硬件设置。项目页说明手持平行夹爪 + GoPro + IMU + 夹爪宽度追踪 + 机器人运动学过滤。
- FastUMI：官方 repo 是 MIT，README 推荐 Ubuntu 20.04、ROS Noetic、librealsense v2.53.1，原因是 T265 不被后续版本支持；数据输出支持 HDF5，并提供 TCP 到 Diffusion Policy/Zarr 转换。项目页称 FastUMI Pro 为解决 T265 停产引入 RoboBaton Mini。
- UMI-3D：官方硬件 repo 是 Apache-2.0，BOM 明确列出 Livox MID-360/MID-360S、Hikrobot MV-CB013-A0UC-S、ZLKC MTV185IR12MP、同步板和 12V 电池，目标成本约 RMB 5000。
- TacUMI：项目页说明 ViTac tactile sensors、6D force-torque sensor、Vive tracker 和连续自锁机构，但未找到公开 BOM/代码/license。
- UMI-FT：官方 repo 是 MIT；硬件指南列出 CoinFT、Teensy 4.0、iPhone 15 Pro/ARKit、PLA/TPU、连接器和螺丝等；CoinFT 官方页明确为 CC BY-NC-SA 4.0，商业用途需要 Stanford 单独许可。
- Actuated UMI：官方 README 给出完整 BoM，核心件为 Dynamixel XL430-W250-T、U2D2、U2D2 Power Hub、恒力弹簧、MGN7C 导轨、平皮带和紧固件；repo 为 MIT。
- GELLO：software 和 mechanical repo 均 MIT，项目页称零件成本低于 300 美元，但每种目标机器人需要对应 kinematic replica。
- ALOHA/Mobile ALOHA：官方 repos 为 MIT；ALOHA 项目页称约 20k 美元预算，Mobile ALOHA 是整机式双臂移动数据采集对照路线。

## 国内替代件优先级

### v0 必须国产化或可本地采购

| 模块 | 原方案 | 国内替代思路 | 验证方式 |
|---|---|---|---|
| 结构件 | PLA/TPU 3D 打印 | 本地 3D 打印服务、Bambu/拓竹、PA-CF 或小批量 CNC | 1000 次开合耐久、跌落、螺母热嵌强度 |
| 导轨/弹簧/紧固件 | MGN rails、compression/constant-force springs、M2/M3 | 淘宝/1688 标准件，多供应商备选 | 夹爪间隙、回弹一致性、异响/卡滞率 |
| 视觉 | GoPro HERO9 + Max Lens Mod | GoPro 新款、Insta360、DJI Osmo Action、Hikrobot/Daheng/MindVision 工业鱼眼 | 时间戳稳定性、IMU 可读性、畸变标定、低光/运动模糊 |
| 位姿追踪 | ORB-SLAM3 / T265 | RoboBaton Mini、ARKit、Vive Tracker、UMI-3D LiDAR-SLAM、外部 MoCap | 10 条标准轨迹 ATE/RPE，对遮挡/弱纹理/动态背景打分 |
| 机器人侧夹爪 | WSG-50 / Dynamixel | DH/因时/Robotiq/遨博/节卡/越疆/ARX/Piper 生态夹爪或自研伺服夹爪 | width 标定、延迟、力限位、急停和电气安全 |
| 数据格式 | UMI Zarr / FastUMI HDF5 | 同时导出 Zarr、LeRobot、HDF5、CSV manifest | 小数据集训练 DP/ACT/LeRobot baseline |

### 不建议 v0 首发的模块

- CoinFT：研究价值高，但非商用许可明确；先用采购可商用的 F/T 或自研低精度力觉模块替代。
- ViTac/TacUMI：公开 BOM 不完整，适合作为接触丰富任务的二期方案。
- Mobile ALOHA 完整整机：适合做高端数据工厂，不适合低成本切入。

## v0 样机建议

### 样机目标

做一个能卖试点的“UMI-like 数据采集 starter kit”，而不是论文复刻玩具。

最小交付能力：

- 采集 100 条单臂桌面任务 episode；
- 自动生成 raw、processed、qc、exports 四类目录；
- 至少导出 UMI/Zarr 和 LeRobot/HDF5 之一，最好双导出；
- 交付 baseline 训练命令和一个可复现小模型；
- 给客户一份质量报告，说明有效轨迹率、丢帧、追踪漂移、重采原因和失败标签。

### 推荐硬件路线

| 版本 | 配置 | 适用场景 | 成本判断 |
|---|---|---|---|
| v0-A 被动 UMI-like | 3D 打印夹爪 + GoPro/国产运动相机 + marker width + ORB-SLAM3/ARKit/RoboBaton 任选一条 | 快速理解数据接口和采集 SOP | 最低，但 SLAM/追踪质量波动大 |
| v0-B FastUMI-like | 被动夹爪 + 独立 pose tracker + RGB camera + ROS/HDF5/Zarr | 客户试点、实验室数据采集 | 最适合第一笔 ToB 试点 |
| v1 UMI-3D | Livox MID-360 + Hikrobot camera + sync board + LiDAR-SLAM | 弱纹理、遮挡、工业/仓储/零售 | 成本高一些，但中国供应链更稳定 |
| v2 Contact | v1 + commercial F/T/tactile fingertip | 插接、擦拭、线缆、抛光 | 高价服务包，需专项客户需求 |

## 数据包交付目录

建议每个客户项目交付以下目录结构：

```text
project_<customer>_<task>_<date>/
  README.md
  manifest.csv
  license_and_consent/
    data_license.md
    site_permission.md
    privacy_redaction_log.md
  raw/
    videos/
      episode_0001_camera_wrist.mp4
      episode_0001_camera_third_person.mp4
    sensors/
      episode_0001_pose.csv
      episode_0001_gripper_width.csv
      episode_0001_imu.csv
      episode_0001_wrench.csv
    calibration/
      camera_intrinsics.yaml
      hand_eye.yaml
      tracker_to_tcp.yaml
      time_sync_report.md
  processed/
    episodes/
      episode_0001.parquet
      episode_0001.json
    dataset.zarr/
    dataset.hdf5
    lerobot/
      meta/
      data/
      videos/
  annotations/
    task_instructions.csv
    step_labels.csv
    failure_labels.csv
    object_manifest.csv
  qc/
    episode_quality.csv
    tracking_drift_report.csv
    frame_drop_report.csv
    rejected_episodes.csv
    sample_replay.mp4
  training/
    configs/
      diffusion_policy.yaml
      act.yaml
      lerobot.yaml
    checkpoints/
    train_commands.md
    evaluation_report.md
  deliverables/
    customer_summary.pdf
    data_schema.md
    baseline_results.md
```

## ToB 产品化落地步骤

### 0-2 周：采购和复现

- 采购两条硬件路线：被动 UMI-like 和 UMI-3D-like。
- GoPro/国产运动相机/工业鱼眼相机至少各试一种，避免早期被单一相机绑定。
- 位姿追踪至少同时验证 ORB-SLAM3、RoboBaton Mini/类似国产 VIO、ARKit。
- 输出：BOM v0、装配 SOP、标定 SOP、失败清单。

### 3-6 周：可训练数据包

- 任务选择：杯子移动、抽屉开合、物体分拣三选一。
- 每个任务采 100 条，必须保留失败和重采标签。
- 跑通 HDF5/Zarr/LeRobot schema 至少两个。
- 输出：第一版数据包目录、QC 报告、baseline 训练脚本。

### 7-10 周：试点客户

- 客户优先级：具身模型公司、高校实验室、机器人整机厂、末端执行器/力控公司。
- 报价不要按“夹爪硬件”报价，按“有效 episode + QC + baseline”报价。
- 试点指标：有效轨迹率、每小时有效 episode、追踪失败率、baseline 成功率、客户复采时间。

### 11-16 周：小批量工程化

- 将追踪模块抽象成 `pose_source`，支持 `orb_slam3`、`vio_module`、`arkit`、`lidar_slam`。
- 将 gripper width 抽象成 `width_source`，支持 marker、编码器、霍尔、电机反馈。
- 将数据导出抽象成 `export_target`，支持 UMI/Zarr、LeRobot、ACT/HDF5、CSV。
- 做 5 套内部设备和 2 套客户借测设备。

### 4-8 个月：场景化数据服务

- 选择一个付费场景，不做泛家庭全能。
- 推荐优先：仓储/零售货架、实验室耗材整理、轻工业桌面装配、线缆/插接的简化任务。
- 建立任务库、物体库、场景随机化、采集员培训和质检员复核机制。

## 待验证项

- UMI original Google Hardware Guide 的完整 BOM 链接、CAD license、GoPro 具体型号可替代性。
- FastUMI hardware purchase/3D printing artifacts 的可下载性、per-file license、FastUMI Pro 的 RoboBaton Mini 接口细节。
- RoboBaton Mini 的 SDK license、商业供货价格、ROS/ROS2 支持和 occlusion 下精度。
- UMI-3D 的同步板 Taobao 链接可持续性，是否需要自研同步 PCB。
- TacUMI 的 ViTac sensor 型号、F/T sensor 型号、Vive tracker 版本、代码/BOM 发布计划。
- UMI-FT 若商业使用，CoinFT 是否能通过 Stanford OTL 获得授权；否则需要国产 F/T/tactile 替代方案。
- MV-UMI code/hardware repo 何时公开，三爪 gripper 和 linear motor 的 BOM。
- GELLO/ALOHA Google Doc hardware tutorials 的完整 BOM 是否可转换为国内采购清单。

## 来源 URL

- UMI project: https://umi-gripper.github.io/
- UMI paper: https://arxiv.org/abs/2402.10329
- UMI repo: https://github.com/real-stanford/universal_manipulation_interface
- UMI hardware guide: https://docs.google.com/document/d/1TPYwV9sNVPAi0ZlAupDMkXZ4CA1hsZx7YDMSmcEy6EU/edit
- FastUMI project: https://www.fastumi.com/FastUMI/
- FastUMI repo: https://github.com/zxzm-zak/FastUMI_Data
- Intel RealSense T265 EOL notice: https://www.realsenseai.com/tracking-camera-t265/
- Hessian Matrix RoboBaton: https://en.hessian-matrix.com/
- UMI-3D project: https://umi-3d.github.io/
- UMI-3D hardware repo: https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware
- TacUMI project: https://tac-umi.github.io/TacUMI/
- TacUMI paper: https://arxiv.org/abs/2601.14550
- UMI-FT project: https://umi-ft.github.io/
- UMI-FT repo: https://github.com/real-stanford/UMI-FT
- UMI-FT hardware guide: https://docs.google.com/document/d/e/2PACX-1vRrfSfjj3ct5u4bdyJYX92zH3QwZahU1D0nfb9wjb6GqDXqEZYVsaxwcCh1gwJgjRlq1fbgLJECGoPf/pub
- CoinFT: https://coin-ft.github.io/
- MV-UMI project: https://mv-umi.github.io/
- MV-UMI paper: https://arxiv.org/abs/2509.18757
- Actuated UMI repo: https://github.com/actuated-umi/actuated-umi-gripper
- GELLO project: https://wuphilipp.github.io/gello_site/
- GELLO software repo: https://github.com/wuphilipp/gello_software
- GELLO mechanical repo: https://github.com/wuphilipp/gello_mechanical
- ALOHA project: https://tonyzhaozh.github.io/aloha/
- ALOHA repo: https://github.com/tonyzhaozh/aloha
- Mobile ALOHA project: https://mobile-aloha.github.io/
- Mobile ALOHA repo: https://github.com/MarkFzp/mobile-aloha
