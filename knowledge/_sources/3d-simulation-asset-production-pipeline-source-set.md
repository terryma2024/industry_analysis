---
title: 3D 仿真资产生产技术管线来源集
type: source
date_created: 2026-08-06
last_updated: 2026-08-06
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-407-openusd-introduction-and-composition-model.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-408-openusd-rigid-body-physics-schema.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-409-simready-foundation-specification-and-validation-framework.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-410-nvidia-isaac-sim-current-asset-ingestion-overview.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-413-unreal-engine-datasmith-cad-import-and-tessellation-workflow.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-414-colmap-structure-from-motion-and-multi-view-stereo-pipeline.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-416-nerfstudio-gaussian-splatting-implementation-and-export-limits.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-417-infinigen-sim-procedural-articulated-simulation-assets.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-418-hunyuan3d-2-1-image-to-3d-and-pbr-asset-generation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-419-trellis-structured-3d-latent-asset-generation.md
tags:
  - industry/robotics-embodied-ai
  - source-set
  - simulation
  - sim-ready
  - real2sim
status: active
aliases:
  - SimReady 资产来源集
---

# 3D 仿真资产生产技术管线来源集

> [!summary]
> 本来源集支撑 [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产生产技术管线综合调研]]。它优先采用规范、官方产品文档、官方代码和论文，分别限定“资产组织与物理合同、工程转换、现实重建、神经表示、程序化和生成式 3D”的能力边界。来源支持“能做什么”，不自动支持客户 ROI、统一精度或跨引擎等价。

## 来源矩阵

| SRC | 证据级 | 支撑内容 | 不能推出 |
|---|---:|---|---|
| [`SRC-robotics-407`](../../raw/robotics-embodied-ai/documents/SRC-robotics-407-openusd-introduction-and-composition-model.md) | S | OpenUSD prim/layer/reference/payload/variant、几何、材质和非破坏式组合 | USD 文件天然有正确物理 |
| [`SRC-robotics-408`](../../raw/robotics-embodied-ai/documents/SRC-robotics-408-openusd-rigid-body-physics-schema.md) | S | 刚体、质量分布、collider、physics material、joint 和单位 | 所有非刚体/传感器域已标准化；跨引擎数值一致 |
| [`SRC-robotics-409`](../../raw/robotics-embodied-ai/documents/SRC-robotics-409-simready-foundation-specification-and-validation-framework.md) | S | 以 capability/feature/profile/rule 检查仿真资产 | 规则通过即获得真实任务增益 |
| [`SRC-robotics-410`](../../raw/robotics-embodied-ai/documents/SRC-robotics-410-nvidia-isaac-sim-current-asset-ingestion-overview.md) | S | CAD、URDF、现实采集到 USD 的当前官方工作流 | 厂商性能宣传是独立 benchmark |
| [`SRC-robotics-411`](../../raw/robotics-embodied-ai/documents/SRC-robotics-411-nvidia-isaac-sim-urdf-importer-extension.md) | S | URDF 导入、asset structure、visual-to-collision 选项 | 自动 collider 对目标接触任务一定正确 |
| [`SRC-robotics-412`](../../raw/robotics-embodied-ai/documents/SRC-robotics-412-omniverse-replicator-synthetic-data-pipeline.md) | S | 程序化合成数据管线入口 | synthetic-only 一定提升 real KPI |
| [`SRC-robotics-413`](../../raw/robotics-embodied-ai/documents/SRC-robotics-413-unreal-engine-datasmith-cad-import-and-tessellation-workflow.md) | S | CAD tessellation 及误差—三角数权衡 | CAD 转换后已具有物理/语义 |
| [`SRC-robotics-414`](../../raw/robotics-embodied-ai/documents/SRC-robotics-414-colmap-structure-from-motion-and-multi-view-stereo-pipeline.md) | S | SfM、相机位姿、稀疏/稠密重建和 mesh | 无控制点时天然有绝对尺度；困难材质无失败 |
| [`SRC-robotics-415`](../../raw/robotics-embodied-ai/documents/SRC-robotics-415-autodesk-recap-local-scan-to-mesh-workflow.md) | S | 点云到分割网格、本地计算与存储约束 | 扫描 mesh 自动具有可动结构和物性 |
| [`SRC-robotics-416`](../../raw/robotics-embodied-ai/documents/SRC-robotics-416-nerfstudio-gaussian-splatting-implementation-and-export-limits.md) | S | 3DGS PLY 导出、mesh/point cloud 与相机模型限制 | 所有 3DGS 实现均永久相同；3DGS 不能参与视觉仿真 |
| [`SRC-robotics-417`](../../raw/robotics-embodied-ai/documents/SRC-robotics-417-infinigen-sim-procedural-articulated-simulation-assets.md) | S | 程序化 articulated asset、物性导出和作者实验 | 所有工业类别与真实物性已覆盖 |
| [`SRC-robotics-418`](../../raw/robotics-embodied-ai/documents/SRC-robotics-418-hunyuan3d-2-1-image-to-3d-and-pbr-asset-generation.md) | S | 图像到 mesh 与 PBR 的国内开源入口 | 尺寸、碰撞、惯量和商用权自动正确 |
| [`SRC-robotics-419`](../../raw/robotics-embodied-ai/documents/SRC-robotics-419-trellis-structured-3d-latent-asset-generation.md) | S | text/image 到 radiance field、Gaussian、mesh/GLB | 生成资产天然可用于机器人接触任务 |
| [`SRC-robotics-420`](../../raw/robotics-embodied-ai/documents/SRC-robotics-420-mujoco-model-asset-collision-and-inertia-documentation.md) | S | visual mesh、convex collision、inertia inference 的区别 | 网格推断惯量等于实测惯量 |
| [`SRC-robotics-421`](../../raw/robotics-embodied-ai/documents/SRC-robotics-421-ros-2-urdf-physical-and-collision-properties-tutorial.md) | S | URDF visual/collision/inertial/joint dynamics 分层 | Humble 教程代表所有当前发行实现细节 |
| [`SRC-robotics-422`](../../raw/robotics-embodied-ai/documents/SRC-robotics-422-houdini-solaris-procedural-usd-workflow.md) | S | 程序化 USD component、material、variant、payload、layer | Houdini 是所有团队的最低成本方案 |

## 证据缺口

- 没有统一资产、硬件、人员能力和精度目标下的跨工具生产成本 benchmark。
- 没有证据证明同一个 USD physics asset 在 Isaac、Gazebo、MuJoCo 和 Unreal 中数值等价。
- 生成式 3D 官方展示集中于视觉/几何质量，缺少统一的 metric、physics 和真机任务验收。
- 商业产品的报价、SLA、客户复购、数据权属和资产再分发条款需逐项目询价。

## 关联连接

- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产生产技术管线综合调研]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
- [[index|Knowledge Index]]
