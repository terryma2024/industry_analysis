---
title: 3DGS PLY 到 SimReady 仿真资产来源集
type: source
date_created: 2026-09-22
last_updated: 2026-09-22
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-571-3d-gaussian-splatting-for-real-time-radiance-field-rendering-official-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-572-gaussian-splats-particle-fields-in-omniverse.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-573-isaac-sim-6-neural-volume-rendering.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-574-simready-specification-and-physics-best-practices.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-575-sugar-surface-aligned-gaussian-splatting-official-implementation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-576-gaussian-opacity-fields-official-implementation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-577-mujoco-collision-detection-and-modeling-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-578-mujoco-openusd-importing-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-579-maniskill-loading-actors-and-articulations-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-581-omniverse-gsplat-converter-user-manual.md
tags:
  - industry/robotics-embodied-ai
  - 3dgs
  - simready
  - real2sim
status: active
---

# 3DGS PLY 到 SimReady 仿真资产来源集

> [!summary]
> 本来源集用于回答“3DGS 输出的 PLY 怎样成为 MuJoCo、Isaac Sim、ManiSkill 可用的 SimReady 资产”。一级资料共同支持一个结论：3DGS PLY 是外观/辐射场表示，不是完整表面和物理资产；Isaac Sim 6 可原生渲染 OpenUSD ParticleField，但三套仿真器都仍需要独立的碰撞、质量、惯量、摩擦、语义和任务验收层。

## 来源分组

| 分组 | 来源 | 支持的结论 | 边界 |
|---|---|---|---|
| 3DGS 表示 | [`SRC-robotics-571`](../../raw/robotics-embodied-ai/documents/SRC-robotics-571-3d-gaussian-splatting-for-real-time-radiance-field-rendering-official-repository.md)、[`581`](../../raw/robotics-embodied-ai/documents/SRC-robotics-581-omniverse-gsplat-converter-user-manual.md) | 标准 PLY 包含位置、尺度、旋转、不透明度和球谐系数；不是普通 XYZ/RGB 点云 | PLY 方言很多，必须先验 header |
| Isaac / Omniverse | [`SRC-robotics-572`](../../raw/robotics-embodied-ai/documents/SRC-robotics-572-gaussian-splats-particle-fields-in-omniverse.md)、[`573`](../../raw/robotics-embodied-ai/documents/SRC-robotics-573-isaac-sim-6-neural-volume-rendering.md) | PLY/SPZ 可转 OpenUSD ParticleField 并与 polygonal robot 同场渲染 | ParticleField 没有明确表面；不能替代 collider |
| SimReady 合同 | [`SRC-robotics-574`](../../raw/robotics-embodied-ai/documents/SRC-robotics-574-simready-specification-and-physics-best-practices.md) | 真实尺度、语义、碰撞、质量和物理材质是资产能力的一部分 | Profile 通过不证明任务级 sim-to-real |
| 3DGS 到 mesh | [`SRC-robotics-575`](../../raw/robotics-embodied-ai/documents/SRC-robotics-575-sugar-surface-aligned-gaussian-splatting-official-implementation.md)、[`576`](../../raw/robotics-embodied-ai/documents/SRC-robotics-576-gaussian-opacity-fields-official-implementation.md) | SuGaR/GOF 可在兼容训练流程中提取 mesh | 不是任意 PLY 的无损一键转换；仍需清理、标尺和物理编译 |
| MuJoCo | [`SRC-robotics-577`](../../raw/robotics-embodied-ai/documents/SRC-robotics-577-mujoco-collision-detection-and-modeling-documentation.md)、[`578`](../../raw/robotics-embodied-ai/documents/SRC-robotics-578-mujoco-openusd-importing-documentation.md) | 非凸 visual mesh 与凸 collision 逻辑分离；USD 导入仍属实验性 | 官方资料未证明 ParticleField 作为原生视觉/碰撞类型可用 |
| ManiSkill / SAPIEN | [`SRC-robotics-579`](../../raw/robotics-embodied-ai/documents/SRC-robotics-579-maniskill-loading-actors-and-articulations-documentation.md) | ActorBuilder/loader 分别管理 visual、collision、density、friction 等 | 自定义资产在 GPU 批量环境中仍须实测内存和吞吐 |

## 抓取状态

- `SRC-robotics-571`–`579`、`581` 已得到 `ok` 的 durable raw Markdown。
- `SRC-robotics-580`（SAPIEN actor 教程）Defuddle 与 fallback HTML 均因网络/SSL 超时失败；该页内容只作为检索线索，不作为报告独立关键证据。下一步可从 SAPIEN 新文档域或固定提交源码补抓。

## 关联连接

- [[robotics-embodied-ai/research-notes/3dgs-ply-to-simready-assets-for-robot-simulation-2026-09-22|3DGS PLY 到 SimReady 仿真资产技术调研]]
- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产生产技术管线综合调研]]
