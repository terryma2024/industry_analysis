---
title: 机器人仿真器的物理解算引擎与 Sim2Real 技术调研
type: synthesis
date_created: 2026-10-26
last_updated: 2026-10-26
sources:
  - knowledge/_sources/robot-physics-engines-sim2real-source-set-2026-10-26.md
  - knowledge/robotics-embodied-ai/sources.csv
tags:
  - industry/robotics-embodied-ai
  - physics-simulation
  - sim2real
  - contact-dynamics
  - research/R04
status: active
aliases:
  - 机器人物理引擎技术地图
  - 物理解算器与现实差距
---

# 机器人仿真器的物理解算引擎与 Sim2Real 技术调研

> [!summary] 结论与置信度
> **高置信度**：没有一种引擎在接触真实性、运行速度、可微性、多物理耦合和易用性上全面占优。Sim2Real 的主要困难是：接触/摩擦的模型近似、碰撞几何误差、未知且随工况变化的物性、执行器与控制时序偏差，以及数值计算和优化梯度的误差。
>
> **技术判断，中高置信度**：实用路线是“任务相关建模 → 真机参数辨识 → 针对性随机化 → 力/触觉等反馈 → 必要时残差模型或在线适应 → 真机留出测试”。更精细的求解器是其中一环，不能替代整条验证链。
>
> **选型判断**：刚体控制基线优先比较 MuJoCo；GPU 大规模训练比较 MuJoCo Warp、PhysX、Newton 的具体后端及 Genesis；接触面受力/准静态操作重点研究 Drake；布料、线缆、软体和颗粒应按材料与接触需求单独比较 SOFA、Chrono、IPC、Genesis/Newton 专用后端。以上是验证起点，不是未经实测的准确率或速度排名。

## 1. 分类、边界与证据状态

- **主分类 R04**：技术原理、论文与前沿方向；**次分类 R05、R06**：工具比较及候选池扫描。
- **分类理由**：回答“有哪些物理引擎、物理解算到底在算什么、为何迁移到真机会失败、哪些技术与论文可解决哪些误差”。
- **研究截止日**：2026-10-26；官方动态文档以当日抓取快照为准。并不宣称覆盖所有厂商或当天全部新论文。
- **范围**：三维机器人刚体/关节、摩擦接触、柔性体与多物理、可微仿真、系统辨识、迁移评测；以全球技术底座为比较对象，讨论中国团队的工程适用性。
- **排除**：渲染质量排名、市场规模、股票、采购报价和创业商业计划。商业相关两节按用户要求压缩为适用性说明。
- **完成状态**：完成文献与官方资料综合、22 行候选矩阵和22篇论文阅读地图；**没有安装/运行候选引擎、复现作者成绩、训练策略或完成真机迁移实验**。
- **证据标记**：`事实`指官方实现/许可或论文中可核对的陈述；`作者报告`不代表独立复现；`判断/建议`是本报告推断；`待验证`表示仍需实验。来源 S 级表示一级材料，不代表论文结论已经普适成立；厂商产品页为 A 级能力自述。

资料入口：[[_sources/robot-physics-engines-sim2real-source-set-2026-10-26|59条来源、版本与抓取限制]]；[机器可读引擎比较 CSV](../../../raw/robotics-embodied-ai/data/robot-physics-engine-matrix-2026-10-26.csv)。

## 2. 先把三层对象分开

| 层级 | 做什么 | 例子 | 比较时需要固定什么 |
|---|---|---|---|
| 仿真平台/学习环境 | 场景、资产、传感器、ROS、任务、奖励、训练接口 | Isaac Sim / Isaac Lab、Gazebo、CoppeliaSim、ManiSkill | 平台版本、插件、控制器、环境及实际后端 |
| 物理引擎/动力学框架 | 碰撞、动力学、约束、积分及状态管理 | MuJoCo、PhysX、Bullet、Drake、Chrono；Newton/Genesis 还包含多后端组织 | 模型表示、接触定律、后端与功能支持 |
| 求解算法/具体 solver | 数值求解接触力/冲量、约束、非线性优化或材料方程 | PGS、TGS、Newton 迭代、ADMM、SAP、XPBD、VBD | 步长、迭代数、容差、稳定化、精度及缓冲容量 |

**重要消歧**：MuJoCo 中的 `Newton` 是优化算法；`newton-physics/newton` 是较新的开源机器人仿真框架；`Newton Dynamics / Newton Game Dynamics` 是另一套历史引擎，不能混为一谈。[SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) [SRC-robotics-622](../../../raw/robotics-embodied-ai/documents/SRC-robotics-622-newton-official-repository-and-license.md) [SRC-robotics-639](../../../raw/robotics-embodied-ai/documents/SRC-robotics-639-newton-dynamics-legacy-engine-license.md)

平台映射只作理解入口：

- **Gazebo** 通过 Physics 插件加载后端；不能把 Gazebo Classic 的后端清单直接视为任一 Gazebo Sim 发行版的现成支持。[SRC-robotics-648](../../../raw/robotics-embodied-ai/documents/SRC-robotics-648-gazebo-physics-plugin-and-backend-feature-interface.md)
- **CoppeliaSim** 官方列出 Bullet、ODE、MuJoCo、Vortex、Newton Dynamics 五种；这里的 Newton Dynamics 不是新 Newton。[SRC-robotics-647](../../../raw/robotics-embodied-ai/documents/SRC-robotics-647-coppeliasim-physics-engine-backend-list.md)
- **Isaac Lab** 新版官方文档区分 IsaacSim PhysX、Newton、OvPhysX；后两者有不依赖 Omniverse Kit 的运行路径。锁定具体发行版和 task preset，不能将 develop/main 文档的能力全算到旧稳定版。[SRC-robotics-673](../../../raw/robotics-embodied-ai/documents/SRC-robotics-673-isaac-lab-version-3-physics-backends-and-runtime-boundaries.md)

## 3. 物理解算器实际在算什么

对关节刚体系统，连续时间动力学可示意为：

$$
M(q)\dot v+b(q,v)=S^\top\tau+J(q)^\top f_c,
\qquad \dot q=N(q)v.
$$

$q,v$ 是位形与广义速度，$M$ 是质量矩阵，$b$ 包含重力与科氏等项，$\tau$ 是执行器输出，$J$ 将接触空间与关节空间联系起来。四元数位形和速度维数可能不同，所以不能总把 $\dot q=v$。对于常见的时间步进，可简写：

$$
M(v_{k+1}-v_k)=h(S^\top\tau-b)+J^\top\lambda,
$$

其中 $h$ 是物理步长，$\lambda$ 是该步接触冲量，不要与瞬时接触力混用。示意式省略了具体积分、约束稳定化与位形评估细节。[SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md)

对理想无黏附刚性静态法向接触，常见表述是：

$$
g_n\ge0,\quad f_n\ge0,\quad g_nf_n=0,\qquad
\|f_t\|\le\mu f_n.
$$

它表达不穿透、不能隔空拉住物体、非接触时无接触力以及摩擦锥约束；**摩擦锥本身还不足以定义滑动方向和耗散，需补充 Coulomb/最大耗散规律**。撞击则需要冲量/速度层的接触与恢复定律。真实物体存在压缩、黏弹性和表面粗糙度，因此“更严格满足理想硬接触”也不自动等于“更接近该真实材料”。[SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md)

一条完整计算链是：碰撞候选筛选 → 几何距离/法向/接触点或接触面 → 无约束动力学 → 接触及关节约束求解 → 积分 → 传感器与控制更新。碰撞几何错了，后面的求解器即使完全收敛，也只是在准确计算错误模型。

### 3.1 主要技术路线

| 路线 | 原理和代表实现 | 主要优点 | 技术代价与失败边界 |
|---|---|---|---|
| 刚性非光滑接触 | 互补问题 LCP/NCP，Coulomb 摩擦及冲量时间步进；DART、ODE、Dojo 等不同变体 | 对宏观刚体、静摩擦及碰撞有清晰表述 | 非凸/非光滑、解可能不唯一；近似摩擦锥和有限迭代会改变行为 |
| 柔顺/正则化接触 | 力与侵入/速度有关，或将接触写成正则化约束优化；MuJoCo、Drake SAP 等 | 数值鲁棒，便于控制、优化和并行 | 存在受控侵入及模型偏差；刚度、阻尼、步长和摩擦近似共同影响结果 |
| 面接触/压力场 | Drake hydroelastic 在接触面上积分分布压力及摩擦 | 更适合讨论接触斑、支撑力矩和面接触 | 要建压力场/网格；不等同于完整材料变形 FEM，不能自然覆盖全部剪切历史效应 |
| 位置/能量投影 | PBD/XPBD/VBD 等，对约束或能量迭代处理 | 适合交互式布料、软体与混合系统 | XPBD 改善柔顺度对步长/迭代的依赖，不代表所有力与摩擦都精确；不可把此类方法全部等同 |
| 连续体/多物理 | FEM、MPM、SPH、离散弹性杆等 | 适合软体、绳索、颗粒、流体及大变形 | 本构、材料标定、自碰撞和刚柔耦合代价高；不是选一个“软体开关”就解决 |
| 屏障式接触 | IPC 以接触屏障、连续碰撞检测及隐式优化避免相交 | 适合复杂变形和严格几何接触研究 | 非线性优化、网格和容差成本；数值不相交不保证现实材料与摩擦完全准确 |

来源分别见 MuJoCo 计算文档、接触综述、Drake 用户指南、IPC 及 XPBD 原始材料。[SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) [SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) [SRC-robotics-630](../../../raw/robotics-embodied-ai/documents/SRC-robotics-630-drake-hydroelastic-contact-user-guide-and-limitations.md) [SRC-robotics-652](../../../raw/robotics-embodied-ai/documents/SRC-robotics-652-incremental-potential-contact-original-project.md) [SRC-robotics-669](../../../raw/robotics-embodied-ai/documents/SRC-robotics-669-xpbd-position-based-simulation-of-compliant-constrained-dynamics.pdf)

### 3.2 坐标表示、积分器与接触求解算法也要分开

- **广义/约化坐标**用关节自由度描述机构；ABA（Articulated Body Algorithm）等递推算法能高效计算树状多体的无接触动力学。闭环需要额外约束；“树状自由动力学可线性复杂度计算”不意味着任意多接触问题都能线性时间解决。
- **极大坐标**为每个刚体保留位姿，再用约束维持关节；机构拓扑灵活，但多了约束和稳定化工作。两种坐标表示都可以用于机器人，不能仅凭坐标形式判断精度。
- **积分器**负责如何从速度/加速度推进时间；**接触 solver**负责该步的力/冲量或约束优化。增加 solver 迭代与减小物理步长解决的问题不同，不能随意互换。

| 算法族 | 计算特点 | 适用性与注意事项 |
|---|---|---|
| PGS / sequential impulses | 反复遍历接触或约束，并投影到允许域，计算预算容易控制 | 小预算实用；强耦合、大质量比、接触顺序及 warm start 会影响有限迭代结果 |
| TGS | PhysX 的时间式 Gauss-Seidel，在位置迭代中推进/更新相关状态与误差估计 | 有助于部分关节/接触稳定性；仍是近似离散算法，不等同于精确连续接触 |
| Newton / CG | 对给定优化目标利用曲率或搜索方向，全局处理多约束耦合 | 可提高收敛；矩阵形成/分解、稀疏结构和GPU批量形状影响性能；不是在求所有引擎共享的同一个目标 |
| Proximal / ADMM | 将约束问题分裂，用近端/增广项协调求解 | 利于处理全局耦合；惩罚参数、残差和所用接触松弛仍影响解 |
| 直接/枢轴方法 | 对离散约束和活跃集合进行矩阵分解或枢轴求解；AGX 有直接与混合路线 | 某些高质量比和静摩擦场景值得验证；直接求解不消除模型近似和条件数问题 |
| 隐式/变分能量优化 | 将下一步状态写成能量/增量势的优化，再处理材料和接触约束 | 适合刚性材料和变形耦合，但非线性搜索、网格与接触检测成本可能成为瓶颈 |

上述区分由当前官方计算/求解文档及P02支持；表中适用性是工程解释，不是统一实测排名。Coulomb系数的混合方式、关节drive是否隐式、接触margin和迭代截断都属于模型合同；跨引擎照抄同名参数不保证物理等价。[SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) [SRC-robotics-623](../../../raw/robotics-embodied-ai/documents/SRC-robotics-623-newton-solver-backend-comparison.md) [SRC-robotics-625](../../../raw/robotics-embodied-ai/documents/SRC-robotics-625-physx-pgs-and-tgs-simulation-solvers.md) [SRC-robotics-643](../../../raw/robotics-embodied-ai/documents/SRC-robotics-643-agx-dynamics-solver-technology.md) [SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md)

## 4. 开源引擎与研究框架候选池

“开源”与“能否商业使用”不是互斥分类：宽松开源引擎也可以用于商业产品。下面列核心代码许可；插件、资产、渲染器和二进制依赖需要单独核查。**CPU/GPU 标记表示路径存在，不表示功能完全对等或经过本文实测。**

| 候选 | 核心许可/状态 | 求解与运行特点 | 技术上最值得考察的场景 | 主要限制/核验项 |
|---|---|---|---|---|
| **MuJoCo** | Apache-2.0 | 广义坐标、凸正则化接触；CPU；PGS/CG/Newton 优化与多种积分 | 刚体控制、系统辨识、RL 基线 | 软接触和摩擦参数需校准；不能简化为普通显式弹簧模型 [SRC-robotics-618](../../../raw/robotics-embodied-ai/documents/SRC-robotics-618-mujoco-official-repository-and-license.md) [SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) |
| **MJX-JAX / MuJoCo Warp** | MuJoCo 生态，Apache-2.0 | 前者 JAX/XLA、后者 NVIDIA Warp/CUDA，批量多环境 | 高吞吐训练；MJX-JAX 可微研究 | **Warp 目前不支持自动微分**；后端功能、接触容量和数值结果不完全相同 [SRC-robotics-620](../../../raw/robotics-embodied-ai/documents/SRC-robotics-620-mujoco-xla-backend-comparison-and-differentiability.md) [SRC-robotics-621](../../../raw/robotics-embodied-ai/documents/SRC-robotics-621-mujoco-warp-features-limitations-and-determinism.md) |
| **Newton Physics** | Apache-2.0；多求解器框架 | MuJoCo Warp 为主要刚体后端；另有 Kamino、XPBD、VBD、MPM 等 | GPU 刚体学习、闭环机构与刚柔耦合研究 | 逐后端核验；Kamino/VBD 等仍有 experimental 标记；不能宣传为所有功能同时成熟 [SRC-robotics-622](../../../raw/robotics-embodied-ai/documents/SRC-robotics-622-newton-official-repository-and-license.md) [SRC-robotics-623](../../../raw/robotics-embodied-ai/documents/SRC-robotics-623-newton-solver-backend-comparison.md) |
| **PhysX** | BSD-3；GPU 源码亦开放 | PGS/TGS、关节 articulation；CPU/GPU 路径 | Isaac/SAPIEN 类工作流、GPU 刚体批量训练 | GPU 接触/约束缓冲、碰撞形状、力与 drive 语义；平台许可另算 [SRC-robotics-624](../../../raw/robotics-embodied-ai/documents/SRC-robotics-624-physx-gpu-source-code-bsd-release-announcement.md) [SRC-robotics-625](../../../raw/robotics-embodied-ai/documents/SRC-robotics-625-physx-pgs-and-tgs-simulation-solvers.md) |
| **Bullet / PyBullet** | zlib，个别目录例外 | 刚体、多关节、软体与多 solver；常见机器人工作流在 CPU | 轻量原型、既有 RL/机器人项目 | 不把仓库实验性 GPU 功能等同于现成 GPU 向量化训练；需锁 solver/多刚体配置 [SRC-robotics-626](../../../raw/robotics-embodied-ai/documents/SRC-robotics-626-bullet-physics-official-repository-and-license.md) |
| **DART** | BSD-2 | 广义坐标 ABA；LCP 接触，Dantzig/PGS 等；CPU | 机器人动力学、Gazebo 后端、控制研究 | 碰撞检测插件不同于动力学求解器；摩擦近似/容差需验证 [SRC-robotics-627](../../../raw/robotics-embodied-ai/documents/SRC-robotics-627-dart-official-repository-and-license.md) |
| **ODE** | LGPL 或 BSD 双许可 | 刚体、关节、碰撞；CPU | 历史机器人/系统仿真、兼容既有模型 | 不因历史悠久推断不适用；大质量比、多接触及步长需压测 [SRC-robotics-628](../../../raw/robotics-embodied-ai/documents/SRC-robotics-628-open-dynamics-engine-overview-and-license.md) |
| **Simbody** | Apache-2.0 | 科学/工程多体动力学，广义坐标、约束；CPU | 生物力学、机构与连续力动力学 | 接触模型和批量训练工具链需按任务搭建 [SRC-robotics-629](../../../raw/robotics-embodied-ai/documents/SRC-robotics-629-simbody-official-repository-and-license.md) |
| **Drake** | BSD-3 | 多体系统、点接触/面接触，SAP 等；以 CPU 系统仿真为主 | 操作、接触优化、受力验证 | hydroelastic 非完整 FEM；刚体-刚体 hydroelastic 不生成对应压力面，可能报错或 fallback [SRC-robotics-630](../../../raw/robotics-embodied-ai/documents/SRC-robotics-630-drake-hydroelastic-contact-user-guide-and-limitations.md) [SRC-robotics-675](../../../raw/robotics-embodied-ai/documents/SRC-robotics-675-drake-official-repository-and-bsd-license.md) |
| **Project Chrono** | BSD-3 | 刚柔多体、非光滑/柔顺接触；按模块有 CPU/GPU/分布式能力 | 车辆、轮地、颗粒、刚柔耦合 | GPU 能力是模块相关，不能认为所有系统可无损转为 GPU [SRC-robotics-631](../../../raw/robotics-embodied-ai/documents/SRC-robotics-631-project-chrono-official-repository-and-license.md) |
| **SOFA** | 核心 LGPL；应用/插件可能 GPL 或其他 | FEM 为核心，碰撞/约束/多物理插件化 | 软体机器人、医疗与组织交互 | 材料与网格、求解器和插件集成成本高 [SRC-robotics-632](../../../raw/robotics-embodied-ai/documents/SRC-robotics-632-sofa-official-repository-fem-and-license.md) |
| **Genesis World** | Apache-2.0 | Rigid/FEM/MPM/PBD/SPH/uipc 等，当前使用 Quadrants 编译后端 | 多材料、异构并行环境及刚柔交互 | 当前编译器已非旧宣传中的纯 Taichi 路线；自动微分和耦合必须按 solver pair 核验 [SRC-robotics-633](../../../raw/robotics-embodied-ai/documents/SRC-robotics-633-genesis-world-official-repository-and-license.md) [SRC-robotics-634](../../../raw/robotics-embodied-ai/documents/SRC-robotics-634-genesis-toolsolver-and-rigid-solver-differentiation-limit.md) [SRC-robotics-676](../../../raw/robotics-embodied-ai/documents/SRC-robotics-676-genesis-latest-coupling-legacy-sap-and-ipc-models.md) |
| **Dojo** | MIT | 极大坐标、变分积分、非线性摩擦锥与内点求解、隐式微分；Julia | 接触轨迹优化、系统辨识及梯度研究 | 不应默认是超大规模 GPU RL 的即插即用替代 [SRC-robotics-635](../../../raw/robotics-embodied-ai/documents/SRC-robotics-635-dojo-documentation-contact-and-mit-license.md) [SRC-robotics-651](../../../raw/robotics-embodied-ai/documents/SRC-robotics-651-dojo-a-differentiable-physics-engine-for-robotics.md) |
| **IPC Toolkit/研究生态** | MIT（toolkit） | 接触距离、屏障、CCD 等算法工具 | 变形体与稳健接触算法研究 | **toolkit 不是完整机器人环境**；需搭配动力学和材料求解框架 [SRC-robotics-636](../../../raw/robotics-embodied-ai/documents/SRC-robotics-636-ipc-toolkit-official-repository-and-license.md) [SRC-robotics-652](../../../raw/robotics-embodied-ai/documents/SRC-robotics-652-incremental-potential-contact-original-project.md) |
| **Rapier** | Apache-2.0 | Rust 实时物理、多语言接口 | Rust/嵌入式软件生态的定制仿真 | 关节、接触与机器人模型导入需自行验收；无本文真机迁移基准 [SRC-robotics-638](../../../raw/robotics-embodied-ai/documents/SRC-robotics-638-rapier-physics-official-overview-and-license.md) |
| **Jolt** | MIT | 多核友好的通用实时刚体/碰撞引擎 | 场景/交互仿真、定制系统 | 不能将游戏场景的稳定和速度直接外推为机器人受力精度 [SRC-robotics-637](../../../raw/robotics-embodied-ai/documents/SRC-robotics-637-jolt-physics-official-repository-and-license.md) |
| **Newton Dynamics** | zlib | 与新 Newton 独立的刚体引擎 | CoppeliaSim 等历史兼容需求 | 需要独立核查维护、模型导入和目标插件版本 [SRC-robotics-639](../../../raw/robotics-embodied-ai/documents/SRC-robotics-639-newton-dynamics-legacy-engine-license.md) [SRC-robotics-647](../../../raw/robotics-embodied-ai/documents/SRC-robotics-647-coppeliasim-physics-engine-backend-list.md) |
| **Brax（历史物理路线）** | Apache-2.0 | JAX 物理与 RL 工具生态 | 理解可微并行仿真发展脉络 | 官方说明仅 `brax/training` 活跃维护，物理新项目转向 MJX/MuJoCo Warp；不作为独立新物理底座优先项 [SRC-robotics-640](../../../raw/robotics-embodied-ai/documents/SRC-robotics-640-brax-maintenance-scope-and-migration-notice.md) |

### 4.1 新框架最容易被混淆的两个边界

**Newton 的“可扩展/可微”不能覆盖式外推。**官方功能矩阵逐 solver 列出刚体、关节、柔性体和微分支持，部分仅为 basic/experimental。MuJoCo Warp 被集成进来后，也不会因此自动获得 Warp 自动微分。[SRC-robotics-623](../../../raw/robotics-embodied-ai/documents/SRC-robotics-623-newton-solver-backend-comparison.md) [SRC-robotics-621](../../../raw/robotics-embodied-ai/documents/SRC-robotics-621-mujoco-warp-features-limitations-and-determinism.md)

**Genesis 的“统一多物理”不等于所有双向耦合都已支持。**当前 ToolSolver 文档仍将它描述为可微刚柔交互的临时、单向工具路径，并等待 RigidSolver 直接支持；要区别编译器有 autodiff、某 solver 可微、两 solver 耦合可微、碰撞拓扑变化时梯度可用这四件事。旧版本 coupling 表仅作历史快照，当前能力以 latest 和固定代码版本验证。[SRC-robotics-634](../../../raw/robotics-embodied-ai/documents/SRC-robotics-634-genesis-toolsolver-and-rigid-solver-differentiation-limit.md) [SRC-robotics-666](../../../raw/robotics-embodied-ai/documents/SRC-robotics-666-genesis-non-rigid-solver-coupling-matrix.md) [SRC-robotics-676](../../../raw/robotics-embodied-ai/documents/SRC-robotics-676-genesis-latest-coupling-legacy-sap-and-ipc-models.md)

## 5. 商用/专有物理解算方案

| 方案 | 许可/交付边界 | 技术重点 | Sim2Real 需要验证什么 |
|---|---|---|---|
| **RaiSim** | 核心二进制需激活授权；学术免费不等于核心开源；公开 wrapper/examples 与核心分开 | 机器人多体与摩擦接触，腿足/RL 工作流 | 目标机器人接触与执行器标定；公开速度宣传需相同误差标准复测 [SRC-robotics-641](../../../raw/robotics-embodied-ai/documents/SRC-robotics-641-raisim-licensing-academic-and-commercial.md) [SRC-robotics-642](../../../raw/robotics-embodied-ai/documents/SRC-robotics-642-raisim-installation-binary-and-wrapper-boundary.md) |
| **Algoryx AGX Dynamics** | 专有商业 SDK | 直接/迭代/混合求解，摩擦接触、多体、线缆与工程系统 | 直接求解对高质量比/静摩擦可能有利，但物性、摩擦模型和容差仍需校准；“直接”不表示无近似 [SRC-robotics-643](../../../raw/robotics-embodied-ai/documents/SRC-robotics-643-agx-dynamics-solver-technology.md) [SRC-robotics-644](../../../raw/robotics-embodied-ai/documents/SRC-robotics-644-agx-dynamics-contact-friction-models-and-solve-types.md) |
| **CM Labs Vortex Studio** | 专有物理核心与平台；集成/插件许可分开 | 实时机械、车辆/履带、线缆、土壤等模块，支持 ROS 2 集成 | 核对所购模块与控制接口，用真实受力/轮地数据验证；产品能力说明不等于迁移成功证据 [SRC-robotics-645](../../../raw/robotics-embodied-ai/documents/SRC-robotics-645-vortex-studio-mechanical-simulation-and-ros2.md) [SRC-robotics-647](../../../raw/robotics-embodied-ai/documents/SRC-robotics-647-coppeliasim-physics-engine-backend-list.md) |
| **Havok Physics** | 专有商业 C++ SDK | 通用实时刚体、约束、查询与跨平台确定性 | 更偏通用交互/游戏底座；机器人力控/灵巧操作需专门证据，不列为本文短名单首选 [SRC-robotics-646](../../../raw/robotics-embodied-ai/documents/SRC-robotics-646-havok-physics-official-product-sheet.pdf) |

工程 CAE、多体设计软件、游戏整引擎及工业机器人离线编程软件属于相邻类别；本次不把它们全部混入“可嵌入机器人接触动力学内核”候选池。开源/专有的区分也不构成物理精度排序。

## 6. Sim2Real 的九类问题与对应解法

以下按误差机制分类，**不是互不相关或可简单相加的误差预算**。例如错误执行器扭矩会改变法向力，再改变摩擦和滑移，看起来像“摩擦参数错了”。

| 问题 | 为什么会出错、常见症状 | 可行解法 | 仍然存在的边界 | 主要证据 |
|---|---|---|---|---|
| **1 接触/摩擦模型结构偏差** | 摩擦锥多面体近似引入方向偏差；部分凸松弛可能带来非物理法向运动；Coulomb 单系数忽略速度、载荷及历史 | 任务匹配的硬/柔顺接触；椭圆锥；合适恢复定律；对面接触考虑压力斑；测滑动/滚动/扭转 | 更低数值残差不能消除模型偏差；精确理想摩擦也不是所有真实表面 | P02/P03，[SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) [SRC-robotics-650](../../../raw/robotics-embodied-ai/documents/SRC-robotics-650-an-unconstrained-convex-formulation-of-compliant-contact.md) |
| **2 碰撞几何与接触拓扑错误** | 凸包填平孔洞、指尖厚度错、倒角缺失、法向/尺度错，导致接触发生位置和先后顺序错误 | 单独构造 collider；测量关键公差；拟合任务相关局部几何与接触事件；自适应提高局部分辨率 | 不能靠摩擦随机化补回不存在的孔洞/接触模式；高面数也不必然更准 | P16/P17，[SRC-robotics-670](../../../raw/robotics-embodied-ai/documents/SRC-robotics-670-validating-robotics-simulators-on-real-world-impacts.md) [SRC-robotics-661](../../../raw/robotics-embodied-ai/documents/SRC-robotics-661-concent-contact-centric-real-to-sim-to-real-learning-from-one-demonstration.md) |
| **3 刚度与离散化矛盾** | 接触很硬但步长过大，抖动/穿透/能量注入；过软又会改变夹持/插入力 | 步长收敛实验、子步、稳定积分、误差控制、自适应步长；按需求选择柔顺度 | 提高稳定性不等于提升真实性；RK4 的光滑高阶精度不能直接套到撞击切换 | P01/P13，[SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) [SRC-robotics-659](../../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md) |
| **4 执行器和控制时序遗漏** | 理想位置驱动替代真实电机；限矩/扭矩速度曲线、齿隙、摩擦、柔性、延迟或采样保持缺失 | 电流-扭矩标定、阶跃/扫频辨识；显式饱和/迟滞/延迟模型；actuator network / residual | 不能让残差吞掉接触初始化/时间对齐错误；新温度/负载仍可能 OOD | P08/P18/P21，[SRC-robotics-654](../../../raw/robotics-embodied-ai/documents/SRC-robotics-654-learning-agile-and-dynamic-motor-skills-for-legged-robots.md) [SRC-robotics-662](../../../raw/robotics-embodied-ai/documents/SRC-robotics-662-closing-the-reality-gap-zero-shot-sim-to-real-dexterous-force-based-grasping.md) [SRC-robotics-671](../../../raw/robotics-embodied-ai/documents/SRC-robotics-671-contact-uan-unsupervised-actuator-networks-as-a-residual-world-model-for-humanoi.md) |
| **5 物性不可辨识/工况变化** | 多组质量、摩擦、drive 参数可拟合同一轨迹；只看位置可能隐藏力错误 | 多激励、多载荷、多模态辨识，约束参数物理可行域；保留后验分布与 holdout | 一个最优参数不一定是真物性，尤其缺少力传感或充分激励时 | P09/P16，[SRC-robotics-655](../../../raw/robotics-embodied-ai/documents/SRC-robotics-655-closing-the-sim-to-real-loop-adapting-simulation-randomization-with-real-world-e.md) [SRC-robotics-670](../../../raw/robotics-embodied-ai/documents/SRC-robotics-670-validating-robotics-simulators-on-real-world-impacts.md) |
| **6 多材料/软体与耦合不足** | 布料弯曲、线缆扭转、软体滞回、颗粒沉陷、流固交互用粗略刚体替代 | FEM/MPM/杆模型/IPC 等任务适配；标定本构；验证跨 solver 动量/能量与双向作用 | 资产、本构、网格、摩擦和计算代价相互制约；面接触不是完整软体动力学 | P05/P14/P15，[SRC-robotics-652](../../../raw/robotics-embodied-ai/documents/SRC-robotics-652-incremental-potential-contact-original-project.md) [SRC-robotics-660](../../../raw/robotics-embodied-ai/documents/SRC-robotics-660-benchmarking-the-sim-to-real-gap-in-cloth-manipulation.md) [SRC-robotics-668](../../../raw/robotics-embodied-ai/documents/SRC-robotics-668-diffcloth-differentiable-cloth-simulation-with-dry-frictional-contact.md) |
| **7 可微性与梯度失真** | 穿越碰撞时间、接触点/法向切换的导数缺失；无接触时梯度为零；长时梯度爆炸/消失 | 事件/法向导数修正；隐式微分；自适应积分；平滑/替代梯度与采样联合 | AD 可精确求导某个程序，但程序导数未必等于真实系统导数；替代梯度有偏 | P04/P12/P13，[SRC-robotics-651](../../../raw/robotics-embodied-ai/documents/SRC-robotics-651-dojo-a-differentiable-physics-engine-for-robotics.md) [SRC-robotics-658](../../../raw/robotics-embodied-ai/documents/SRC-robotics-658-differentiable-physics-simulations-with-contacts-do-they-have-correct-gradients.md) [SRC-robotics-659](../../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md) |
| **8 策略利用仿真漏洞** | 通过穿透、接触抖动、无限 drive 力或不合理摩擦获得高 reward | 物理量约束与违规记录、真实数据校准、针对性随机化、跨引擎压力测试、接触事件约束 | Sim2Sim 通过仍不能证明 Sim2Real；多个引擎可能共享几何/参数错误 | P07/P11/P17，[SRC-robotics-653](../../../raw/robotics-embodied-ai/documents/SRC-robotics-653-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization.md) [SRC-robotics-657](../../../raw/robotics-embodied-ai/documents/SRC-robotics-657-dynamics-randomization-revisited-a-case-study-for-quadrupedal-locomotion.md) [SRC-robotics-661](../../../raw/robotics-embodied-ai/documents/SRC-robotics-661-concent-contact-centric-real-to-sim-to-real-learning-from-one-demonstration.md) |
| **9 速度、容量和可复现性冲突** | 为速度减少迭代/接触点；GPU buffer 溢出；异步、原子规约或碰撞排序导致差异 | 同时报告物理误差和吞吐；监控容量/溢出；固定模型/版本/种子；多次重复和统计 | 固定种子不保证跨设备逐位相同；吞吐和单步延迟是两种指标 | 官方后端文档，[SRC-robotics-620](../../../raw/robotics-embodied-ai/documents/SRC-robotics-620-mujoco-xla-backend-comparison-and-differentiability.md) [SRC-robotics-621](../../../raw/robotics-embodied-ai/documents/SRC-robotics-621-mujoco-warp-features-limitations-and-determinism.md) [SRC-robotics-625](../../../raw/robotics-embodied-ai/documents/SRC-robotics-625-physx-pgs-and-tgs-simulation-solvers.md) |

### 6.1 接触：需要同时处理“算什么”与“怎样算”

可以把问题分成三层：**接触定律**规定目标物理；**几何/离散化**决定约束怎样进入离散系统；**数值迭代**决定在预算内离目标解多近。改变任意一层都会改变结果。

例如 PGS 迭代次数不足可能出现关节漂移或接触误差；增加迭代能减少此类残差。但如果约束本身采用了不适合任务的摩擦松弛，迭代充分后仍有系统性偏差。另一方面，真实软指尖确有柔顺性，不能把所有可见侵入都视为错误。应以力-位移曲线、滑移阈值、扭转力矩与接触事件一致性决定模型选择。[SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) [SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) [SRC-robotics-630](../../../raw/robotics-embodied-ai/documents/SRC-robotics-630-drake-hydroelastic-contact-user-guide-and-limitations.md)

### 6.2 参数：先辨识，再随机化，并验证真实分布是否被覆盖

建议目标函数写成多物理观测损失，而不只拟合 reward：

$$
\hat\theta=\arg\min_{\theta\in\Theta_{\rm physical}}
\sum_{i,t}\bigl[
 w_q\|q^{sim}_{it}-q^{real}_{it}\|^2+
 w_v\|v^{sim}_{it}-v^{real}_{it}\|^2+
 w_f\|f^{sim}_{it}-f^{real}_{it}\|^2
\bigr]+\lambda R(\theta).
$$

这是**方法建议，不是某篇论文的原样公式**。各项要按量纲/噪声归一化；没有可靠力测量时不能假装有 $f^{real}$。应另外检查接触时刻/模式、初态和传感器对齐，并在不同动作/材料/载荷上留出测试。

DR 主要处理已被参数族表达的不确定性；它无法系统修复缺失的机械结构或材料状态。范围过窄覆盖不了真机，过宽可能学出保守低效策略。P11 给出了无需动力学随机化亦可迁移的特定四足案例，因此“所有任务必须大幅随机化”不是通用定理。[SRC-robotics-653](../../../raw/robotics-embodied-ai/documents/SRC-robotics-653-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization.md) [SRC-robotics-655](../../../raw/robotics-embodied-ai/documents/SRC-robotics-655-closing-the-sim-to-real-loop-adapting-simulation-randomization-with-real-world-e.md) [SRC-robotics-657](../../../raw/robotics-embodied-ai/documents/SRC-robotics-657-dynamics-randomization-revisited-a-case-study-for-quadrupedal-locomotion.md)

### 6.3 执行器：力迁移往往比“动作看起来像”更难

位置轨迹相似，可能同时存在完全不同的关节扭矩和接触载荷。执行器网络应学习从指令/历史状态到实际扭矩的关系，并明确饱和、延迟及训练覆盖范围。2026 年 Contact-UAN 特别强调**接触一致的 replay 初始化**，否则模型可能学习补偿重置伪影。不能把它的效果归因于“换了更准的接触 solver”。[SRC-robotics-654](../../../raw/robotics-embodied-ai/documents/SRC-robotics-654-learning-agile-and-dynamic-motor-skills-for-legged-robots.md) [SRC-robotics-671](../../../raw/robotics-embodied-ai/documents/SRC-robotics-671-contact-uan-unsupervised-actuator-networks-as-a-residual-world-model-for-humanoi.md)

残差模型可写为 $F_{hybrid}=F_{physics}+r_\phi$，但残差加在力、扭矩、状态转移还是接触定律上，其可解释性和约束完全不同。建议优先采用有结构的修正，并检查功率/能量、饱和和分布外行为。P22 是针对高速球运动、台面和球拍接触使用解析物理与残差结合的实例；不能将专用模型外推为通用世界模型。[SRC-robotics-672](../../../raw/robotics-embodied-ai/documents/SRC-robotics-672-physics-models-for-sim-to-real-transfer-in-professional-level-robot-table-tennis.md)

### 6.4 可微：区分数学正确的梯度与优化有用的梯度

平滑接触容易提供梯度，但可能改变正向物理；硬接触的事件切换又可能造成导数不连续、缺失或数值不稳定。Dojo 对松弛接触问题使用隐式微分；DiffMJX 对刚性接触采用自适应积分，并用 CFD 在**反向计算**中提供远距离接触信号。CFD 是优化用替代梯度，不是在正向仿真中增加真实远程接触力。[SRC-robotics-651](../../../raw/robotics-embodied-ai/documents/SRC-robotics-651-dojo-a-differentiable-physics-engine-for-robotics.md) [SRC-robotics-659](../../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md)

推荐同时验证：解析简单系统的导数、固定接触模式下的有限差分、多扰动尺度下的方向导数、接触创建/消失附近的优化效果，以及优化后动作的真机结果。在真正不连续处，不应要求普通中心有限差分给出唯一“真导数”。可微方法与采样/MPC/模型无关 RL 是互补关系，不是必须替代关系。[SRC-robotics-658](../../../raw/robotics-embodied-ai/documents/SRC-robotics-658-differentiable-physics-simulations-with-contacts-do-they-have-correct-gradients.md) [SRC-robotics-659](../../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md)

## 7. 论文阅读地图：22 篇及其证据边界

阅读深度：P02/P13 已核阅 HTML 全文中的原理与限制；大多数其余论文核对作者原始摘要、项目页或官方论文元数据，作为路线地图，**未对全部实验表、代码依赖及消融逐项复核**。P01/P06 的官方 PDF 已保留；没有把下载成功等同于全文精读。年代区分首次预印本与后续发表/修订；未知会议信息不补写。

### 7.1 建模、求解与可微的基础论文

| 编号 / 论文 | 年代与路线 | 应读的问题 | 实验/复现边界与材料 |
|---|---|---|---|
| **P01** Todorov, Erez, Tassa — *MuJoCo: A physics engine for model-based control* | IROS 2012；多关节与接触动力学 | 为什么面向控制的物理计算与游戏交互不同 | 原始设计不是当前所有功能规范；结合当前计算文档。[SRC-robotics-667](../../../raw/robotics-embodied-ai/documents/SRC-robotics-667-mujoco-a-physics-engine-for-model-based-control-original-paper.pdf) [SRC-robotics-619](../../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) |
| **P02，最优先** Le Lidec et al. — *Contact Models in Robotics: a Comparative Analysis* | 2023 预印本，2024 v3 | LCP/CCP/NCP、摩擦近似、求解器收敛及物理残差 | 有 ContactBench C++ 实现；其历史结果不直接排名2026所有引擎。[SRC-robotics-649](../../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) [SRC-robotics-665](../../../raw/robotics-embodied-ai/documents/SRC-robotics-665-contactbench-solver-benchmark-official-implementation.md) |
| **P03** Castro, Permenter, Han — *An Unconstrained Convex Formulation of Compliant Contact* | 2021 预印本/2022 T-RO；SAP | 如何将柔顺接触转成稳健凸优化 | 有 Drake 实现；证明的是所建离散模型的性质，不是任意材料的真机等价。[SRC-robotics-650](../../../raw/robotics-embodied-ai/documents/SRC-robotics-650-an-unconstrained-convex-formulation-of-compliant-contact.md) |
| **P04** Howell et al. — *Dojo: A Differentiable Physics Engine for Robotics* | 2022 预印本；硬接触与隐式微分 | 极大坐标、变分积分、摩擦锥与有用梯度 | Julia/MIT 开源；需要实际任务规模验证，不只看小例子。[SRC-robotics-651](../../../raw/robotics-embodied-ai/documents/SRC-robotics-651-dojo-a-differentiable-physics-engine-for-robotics.md) [SRC-robotics-635](../../../raw/robotics-embodied-ai/documents/SRC-robotics-635-dojo-documentation-contact-and-mit-license.md) |
| **P05** Li et al. — *Incremental Potential Contact: Intersection- and Inversion-free, Large-Deformation Dynamics* | SIGGRAPH/TOG 2020；屏障接触 | 复杂软体如何处理不相交和单元翻转 | 项目和 toolkit 可追溯；数值性质与真机材料误差分开评估。[SRC-robotics-652](../../../raw/robotics-embodied-ai/documents/SRC-robotics-652-incremental-potential-contact-original-project.md) [SRC-robotics-636](../../../raw/robotics-embodied-ai/documents/SRC-robotics-636-ipc-toolkit-official-repository-and-license.md) |
| **P06** Macklin, Müller, Chentanez — *XPBD: Position-Based Simulation of Compliant Constrained Dynamics* | 2016；位置约束柔顺度 | 为什么普通 PBD 的刚度受步长和迭代影响，XPBD 如何改善 | 原始算法研究；不能由此推断完整机器人力控已经验证。[SRC-robotics-669](../../../raw/robotics-embodied-ai/documents/SRC-robotics-669-xpbd-position-based-simulation-of-compliant-constrained-dynamics.pdf) |
| **P12** Zhong, Han, Brikis — *Differentiable Physics Simulations with Contacts: Do They Have Correct Gradients w.r.t. Position, Velocity and Control?* | 2022 预印本；梯度诊断 | LCP/凸优化/柔顺/PBD 四类的梯度为何可能错误 | 有公开实验代码链接；主要为解析/受控系统，需补机器人长时任务。[SRC-robotics-658](../../../raw/robotics-embodied-ai/documents/SRC-robotics-658-differentiable-physics-simulations-with-contacts-do-they-have-correct-gradients.md) |
| **P13，前沿重点** Paulus et al. — *Differentiable Simulation of Hard Contacts with Soft Gradients for Learning and Control* | 2025 首版；2026-03 v2，ICLR 2026；原题 *Hard Contacts with Soft Gradients* | DiffMJX、自适应积分、Contacts From Distance | 全文有实物方块辨识及 MPC 研究；容差过紧、额外接触及 checkpoint 带来成本，仍有非凸问题。[SRC-robotics-659](../../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md) |

### 7.2 辨识、随机化、执行器及真实数据验证

| 编号 / 论文 | 年代与方法 | 与物理解算的关系 | 应怎样使用证据 |
|---|---|---|---|
| **P07** Peng et al. — *Sim-to-Real Transfer of Robotic Control with Dynamics Randomization* | 2017 预印本/ICRA 2018 | 动力学参数随机化与策略适应 | 真机推物案例支持该任务路线，不证明接触模型精度无关。[SRC-robotics-653](../../../raw/robotics-embodied-ai/documents/SRC-robotics-653-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization.md) |
| **P08** Hwangbo et al. — *Learning agile and dynamic motor skills for legged robots* | Science Robotics 2019 | 学习执行器动态，改善关节层迁移 | 腿足真机证据；执行器网络需重新对目标硬件采样。[SRC-robotics-654](../../../raw/robotics-embodied-ai/documents/SRC-robotics-654-learning-agile-and-dynamic-motor-skills-for-legged-robots.md) |
| **P09** Chebotar et al. — *Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience* | 2018 预印本/ICRA 2019；SimOpt | 用少量真实试验迭代仿真参数分布 | 需要真实回放/实验闭环，无法零数据自动恢复全部物性。[SRC-robotics-655](../../../raw/robotics-embodied-ai/documents/SRC-robotics-655-closing-the-sim-to-real-loop-adapting-simulation-randomization-with-real-world-e.md) |
| **P10** Kumar et al. — *RMA: Rapid Motor Adaptation for Legged Robots* | RSS 2021 | 从近期观测适应环境/系统隐变量 | 修策略的适应性，未直接修接触定律；局部观测不可辨识时仍有限制。[SRC-robotics-656](../../../raw/robotics-embodied-ai/documents/SRC-robotics-656-rma-rapid-motor-adaptation-for-legged-robots.md) |
| **P11，反方必读** Xie et al. — *Dynamics Randomization Revisited: A Case Study for Quadrupedal Locomotion* | 2020 预印本/2021 修订 | 分离 DR 与其他控制设计因素 | 特定四足可不依赖 DR 迁移；不能反推所有任务都无需 DR。[SRC-robotics-657](../../../raw/robotics-embodied-ai/documents/SRC-robotics-657-dynamics-randomization-revisited-a-case-study-for-quadrupedal-locomotion.md) |
| **P16，评测必读** Acosta, Yang, Posa — *Validating Robotics Simulators on Real-World Impacts* | 2021 预印本/RA-L 2022 | 对 Drake/MuJoCo/Bullet 做真实撞击数据辨识与对照 | 方块和 Cassie 落地显示整体运动相似仍有接触误差；是历史版本结果。[SRC-robotics-670](../../../raw/robotics-embodied-ai/documents/SRC-robotics-670-validating-robotics-simulators-on-real-world-impacts.md) |
| **P14** Blanco-Mulero et al. — *Benchmarking the Sim-to-Real Gap in Cloth Manipulation* | 2023 预印本 | 真实布料静/动态操控与四种模拟器比较 | 有公开数据/代码入口；材料和硬件设置决定可比性。[SRC-robotics-660](../../../raw/robotics-embodied-ai/documents/SRC-robotics-660-benchmarking-the-sim-to-real-gap-in-cloth-manipulation.md) |
| **P15** Li et al. — *DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact* | 2021 预印本/TOG 2022 | 可微布料、干摩擦、系统辨识和控制 | 专门的布料方法，不是通用刚体求解器替代。[SRC-robotics-668](../../../raw/robotics-embodied-ai/documents/SRC-robotics-668-diffcloth-differentiable-cloth-simulation-with-dry-frictional-contact.md) |

### 7.3 截至2026年10月的近作与新方向

以下均按**作者报告/预印本证据**理解；未独立复现，不因时间新就排在成熟方法之前。

| 编号 / 论文 | 日期 | 贡献与本报告关注点 | 下一步需要核验 |
|---|---|---|---|
| **P17 ConCent** — *Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration* | 2026-06-29 | 将接触事件序列、局部几何和动力学一致性用于 Real2Sim2Real；限制策略利用不现实接触 | 原语几何对复杂凹物体是否足够、示范覆盖和新接触模式泛化。[SRC-robotics-661](../../../raw/robotics-embodied-ai/documents/SRC-robotics-661-concent-contact-centric-real-to-sim-to-real-learning-from-one-demonstration.md) |
| **P18** Dong et al. — *Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation* | 2026-01-06 | 触觉/扭矩观测、电流-扭矩标定、齿隙与扭矩速度饱和建模 | 虚拟触觉距离信号与真实触觉的语义、传感器标定和不同物体分布。[SRC-robotics-662](../../../raw/robotics-embodied-ai/documents/SRC-robotics-662-closing-the-reality-gap-zero-shot-sim-to-real-dexterous-force-based-grasping.md) |
| **P19 PACE** — *Proprioception-Anchored Cross-Modal Pretraining for Zero-Shot Sim-to-Real Contact-Rich Assembly* | 2026-09-07；09-16 v3 | 用本体状态转移约束视觉与力表征；作者报告四项装配任务平均真机成功率93.3% | 该数字是指定任务均值；需核样本量/区间/扰动及真实数据协议，不能归因于 solver 单项提升。[SRC-robotics-663](../../../raw/robotics-embodied-ai/documents/SRC-robotics-663-pace-zero-shot-sim-to-real-contact-rich-assembly.md) |
| **P20 ContactBench 1.0** — *A Benchmark for Everyday Contact-Rich Robotic Manipulation* | 2026-10-17；10-23 v2 | 8类技能、36任务、40余对象的物理/仿真资产路线；选取6任务评测视觉与视触觉策略 | **v2 摘要写“will be open-sourced”**，不能沿用首版“已全部开源”的说法；资产/代码完整性待实际验收。[SRC-robotics-664](../../../raw/robotics-embodied-ai/documents/SRC-robotics-664-contactbench-1-0-everyday-contact-rich-robotic-manipulation.md) |
| **P21 Contact-UAN** — *Unsupervised Actuator Networks as a Residual World Model for Humanoid Control* | 2026-10-13 | 保留物理先验，修正执行器；强调接触一致 replay；作者使用6.5分钟真实行走数据 | 数据量不含所有前置工作；受力、扭矩收益需在目标人形和工况复核。[SRC-robotics-671](../../../raw/robotics-embodied-ai/documents/SRC-robotics-671-contact-uan-unsupervised-actuator-networks-as-a-residual-world-model-for-humanoi.md) |
| **P22** Conti et al. — *Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis* | 2026-06-27；07-01 v2 | 飞行、台面和球拍接触的专用物理+残差模型，覆盖高速/旋转 | 专用数据与材料覆盖、接触模型的外推；不是现成通用机器人仿真后端。[SRC-robotics-672](../../../raw/robotics-embodied-ai/documents/SRC-robotics-672-physics-models-for-sim-to-real-transfer-in-professional-level-robot-table-tennis.md) |

> [!warning] 两个 ContactBench 是不同项目
> P02 配套的 **Simple-Robotics/ContactBench** 用来比较接触模型与求解器；P20 的 **ContactBench 1.0** 是日常接触操作任务/资产基准。名字相近，作者、范围和用途都不同。[SRC-robotics-665](../../../raw/robotics-embodied-ai/documents/SRC-robotics-665-contactbench-solver-benchmark-official-implementation.md) [SRC-robotics-664](../../../raw/robotics-embodied-ai/documents/SRC-robotics-664-contactbench-1-0-everyday-contact-rich-robotic-manipulation.md)

**建议阅读顺序**：P02（模型地图）→ P16（真实撞击对照）→ P08/P09（执行器与辨识）→ P03/P04（求解路线）→ P12/P13（梯度）→ 按腿足/灵巧手/柔性物选择 P10、P14/P15、P17–P22。

## 8. 怎么选：按任务建立短名单

以下是**工程判断**，需要用下一节实验推翻或确认，不是通用产品榜单。

| 任务 | 第一轮候选 | 最先验证的量 | 不宜采用的选型捷径 |
|---|---|---|---|
| 机械臂刚体抓放/推物 | MuJoCo 与 PhysX；有明确许可条件可加入 RaiSim | 夹持滑移、接触时刻、力/扭矩、执行器响应 | 按视觉逼真度选接触 solver |
| 腿足/人形大规模 RL | MuJoCo Warp、PhysX、Newton 的 MJWarp/Kamino 等任务适配后端；Genesis；RaiSim | 地面冲量、脚滑、关节功率、延迟、吞吐和容量 | 用最快 demo 的 steps/s 代替迁移成功率 |
| 接触面受力、准静态重定位、抓持力矩 | Drake hydroelastic/SAP；以 MuJoCo/其他引擎作独立对照 | 压力/法向总力、支撑力矩、滑动/扭转阈值 | 认为面接触模型就是完整弹性体 |
| 精密插接/装配 | MuJoCo/Drake 起步，按实际材料比较 AGX 等 | 间隙/倒角、楔紧、插入力、过载峰值、控制带宽 | 用调大摩擦补偿错误碰撞孔洞 |
| 布料/软体/线缆 | SOFA、Chrono、IPC/专用方法、Genesis 或 Newton 的对应 solver | 拉伸/弯曲/扭转、迟滞、自接触、刚柔双向作用 | 用刚体训练吞吐比较软体精度 |
| 土壤/颗粒/轮地 | Chrono、AGX/Vortex、适用的 MPM/颗粒后端 | 沉陷、牵引力、滑移率、材料含水/密实状态 | 把摩擦平面当成松软地面 |
| 非 NVIDIA 硬件 | CPU MuJoCo/DART/Drake/Chrono；按已支持设备验证 MJX-JAX/Genesis 路径 | 实际编译、正确性、驱动、内存与长期稳定性 | 将“AMD/Metal 可用”推断为任意国产 GPU 可用 |

## 9. 最小技术验证方案：从组件到真机任务

### 9.1 三层验证，分别回答不同问题

1. **解析/受控模型测试**：单摆、滑块、弹性球、静摩擦斜面、堆叠和闭环机构。验证动量/能量趋势、关节约束、摩擦方向及步长收敛。守恒检查要扣除驱动做功、重力势能和模型定义的耗散，不能要求有摩擦的系统总机械能不变。
2. **真实回放对齐**：采集同一硬件的指令、编码器、时间戳、电流/扭矩、接触力/视觉轨迹；分辨识集和留出集。先对齐动作/传感器延迟，再拟合参数；评价自由空间、接触切换和持续接触三种工况。
3. **闭环策略迁移**：相同模型/训练预算下比较固定物理、辨识物理、辨识+DR、辨识+DR+反馈/残差/适应。跨引擎测试用于诊断，最终仍以真机留出任务验证。

### 9.2 必须冻结和记录的实验条件

| 类别 | 至少记录 |
|---|---|
| 版本 | 引擎/solver/插件 commit 或 tag，GPU/CPU、驱动、浮点精度，训练和评估设备 |
| 资产 | 单位、坐标、重力、惯量、质心、关节轴/limits、collider、网格和摩擦组合规则 |
| 时间 | 物理步长、子步、控制周期、动作保持方式、传感器频率、滤波、总延迟 |
| 求解 | 迭代/容差、warm start、接触 margin、摩擦锥、刚度/阻尼、恢复参数、接触缓冲容量 |
| 控制 | 力/位置/速度 drive 类型、显式或隐式 PD、限矩/限速、策略 observation 与动作定义 |
| 随机化 | 参数分布及相关性、种子、episode 内/间变化、训练是否覆盖真机工况 |
| 评测 | 样本与失败定义、留出对象/轨迹/工况、重复次数、置信区间、所有异常和安全停机 |

### 9.3 指标与验收逻辑

| 维度 | 建议指标 | 怎样解释 |
|---|---|---|
| 几何/接触 | 接触位置/时刻误差、穿透深度、漏接触/伪接触率 | 先排除模型拓扑错误，避免用参数拟合掩盖 |
| 动力学 | 位姿/速度误差、接触冲量、力/扭矩偏差、滑移、功率及能量误差 | 力峰值依赖采样和过滤；撞击应同时比较积分冲量 |
| 数值 | 步长减半、迭代增加后的敏感性；残差；buffer overflow | 数值收敛只验证给定模型，不直接证明真实 |
| 任务 | 真机成功率、过载/损伤、失败恢复、轨迹时间 | 预注册失败标准；报告样本量与区间 |
| 计算 | 单环境步进 p50/p95、总 steps/s、显存、编译/初始化、渲染与 I/O 成本 | 分开吞吐和延迟，比较同一误差容忍度 |
| 梯度 | 解析/有限差分方向一致性、接触切换稳健性、优化改善量 | 程序导数、平滑目标导数与替代梯度分开报告 |

**不设脱离任务的统一阈值。**应从真实任务公差、力限和控制带宽倒推。对于精密装配，接触位置误差若已接近物理间隙，就应先修几何；对于低带宽抓放，优先看抓取滑移与执行器响应，不必追求每个瞬时接触力峰值逐点相同。

## 10. 中国团队的技术适用性与研究优先级

本次不展开政策或市场分析。以下是依据上述技术约束给出的**研究判断**，不是对全国实验能力的统计结论：

- 值得优先积累的是**真实执行器、指尖/足底材料、接触几何、同步受力和失败回放数据**，以及可重放的标定流程；单靠集成开源 viewer 难以回答迁移误差从哪里来。
- 国产硬件适配应区分“策略推理可用”“CPU 物理可用”“GPU solver 编译并正确运行”“同口径性能达标”。CUDA/Warp、JAX/XLA、Quadrants 的设备路径各有边界，不能由计算卡算力规格推导仿真兼容性。[SRC-robotics-620](../../../raw/robotics-embodied-ai/documents/SRC-robotics-620-mujoco-xla-backend-comparison-and-differentiability.md) [SRC-robotics-622](../../../raw/robotics-embodied-ai/documents/SRC-robotics-622-newton-official-repository-and-license.md) [SRC-robotics-633](../../../raw/robotics-embodied-ai/documents/SRC-robotics-633-genesis-world-official-repository-and-license.md)
- 对技术研究更有价值的题目包括：接触/执行器参数联合可辨识性；力与接触事件联合辨识；几何公差与 collider 自动校准；可信接触梯度；刚柔双向耦合；跨引擎等价建模与真实数据 benchmark。
- 研究成果应交付完整环境、版本、数据协议、对照实验和失败案例；不能将“仿真 reward 提升”“某视频动作流畅”或“能完成一次真机演示”视为普适 Sim2Real 解决方案。

## 11. 知识冲突、反方证据与证伪条件

| 常见判断 | 反方/限定证据 | 下一步怎样验证 |
|---|---|---|
| “更高精度仿真一定更好迁移” | 参数、执行器或观测错时，数值精度无法修结构错误；P07/P11 说明策略与控制设计也重要 | 固定策略/数据，逐项替换 solver、参数、drive、反馈，比较真机收益 |
| “DR 是必要且充分条件” | P11 的特定四足可无 DR 迁移；DR 也不补缺失接触模式 | 分开做系统辨识、DR、历史观测、网络及控制带宽消融 |
| “可微物理天然更准确” | P12 分析错误梯度；P13 需要额外积分和反向处理 | 解析/扰动梯度、优化后真机复核，报告反向近似 |
| “加触觉就能解决接触操作” | P20 在选取的6项任务上未发现视触觉策略有显著性能改善 | 固定传感器质量，检查表征、时延、融合与训练覆盖，而非只加传感器 |
| “跨两个引擎都成功就能上真机” | 两者可能共享错误资产、理想驱动与同类摩擦近似 | 用实际物理量与真实留出数据验证，不仅看任务 reward |
| “平台所有功能均可商用且开源” | PhysX 核心开源不替代整个平台/资产许可；RaiSim wrapper 与核心分开 | 固定分发包、依赖和具体许可版本核验 |

**与既有知识库的关系**：[[isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|7月平台选型]]侧重平台层；其场景适配评分属于当时工程判断，不能直接用来认定某引擎在接触受力上最准确。本篇补充求解器层与新版后端事实，不覆盖旧文的版本快照。[[3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D仿真资产管线专题]]说明外观与 collider/物性分离，和本篇“先核对接触几何”的结论一致。

若未来在同一真实数据集、相同资产/执行器和误差容忍度下，某方法对多材料、多机器人和留出任务均显示稳定优势，可据此收窄本报告的多候选建议。目前缺少本文独立跑出的这类统一证据。

## 12. 商业应用可能性

按本次技术研究边界，仅保留适用性结论：可用于策略训练、虚拟调试、接触参数辨识和回归测试。**软件可运行的成熟度高于通用迁移精度已验证的成熟度**；实际可用性取决于上一节的任务验收。未调研客户采购、收入、ROI 或订单，本报告不据此作商业前景排序。

## 13. 中小型创业者的机会

不作创业机会研究或推荐，仅记录技术进入门槛：真实标定数据、接触模型验证和长期引擎维护均有成本。若以后另做商业研究，`可立即验证`可限定为某硬件的一套标定/回归原型；`需要条件成熟`包括获得真实数据与合作硬件后的专用刚柔仿真；`不建议据本报告直接进入`的是宣称一套内核解决全部机器人 Sim2Real。付费需求、团队、资金和收益均为**本次范围外/待验证**。

## 14. 待验证事项与下一步

- [x] 核查主要开源/专有候选、平台/引擎/solver 边界及当前许可说明。
- [x] 建立问题—方法—论文地图，并区分作者报告与本报告判断。
- [x] 保存官方资料、来源集、候选 CSV，并连接行业与全局索引。
- [ ] 对22篇论文的全部实验表、数据许可、代码版本、缺失依赖及发表状态做逐项复现审计；新预印本尤其需要。
- [ ] 在目标硬件上跑统一刚体接触/执行器回放实验；按需求再添加软体/轮地模块。
- [ ] 复核 Newton 各 solver、Genesis 各 pair 的实际 feature/gradient coverage，避免沿用旧版本矩阵。
- [ ] 对 ContactBench 1.0 的资产与代码公开完整性做后续验收；不把2026-10-23 v2 的未来时描述写成既成事实。
- [ ] 取得真实滑移、受力、撞击和多负载数据，检验参数可辨识性；本文不声称拥有这些数据。

## 关联连接

- [[robotics-embodied-ai/00-index|机器人行业导航]]
- [[robotics-embodied-ai/02-technology-and-products|技术与产品]]
- [[_sources/robot-physics-engines-sim2real-source-set-2026-10-26|本次来源与原始材料]]
- [[_concepts/robot-contact-model-solver-and-sim2real-gap|接触模型、求解误差与现实差距]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|平台层选型]]
- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|物理资产建模]]
- [[robotics-embodied-ai/research-notes/tactile-end-effectors-hands-grippers-selection-2026-10-20|触觉末端与传感器]]
