---
title: 机器人物理解算引擎与 Sim2Real 来源集
type: source
date_created: 2026-10-26
last_updated: 2026-10-26
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/documents/source_capture_manifest.csv
tags:
  - sources
  - physics-simulation
  - sim2real
status: active
---

# 机器人物理解算引擎与 Sim2Real 来源集

> [!summary] 范围与结果
> 本轮登记59条一级论文/官方仓库/文档及厂商产品资料（SRC-robotics-618–676），编译为 [[robotics-embodied-ai/research-notes/robot-physics-engines-sim2real-2026-10-26|技术报告]]，附22行候选矩阵和22篇论文地图。抓取状态：{'ok': 57, 'fallback_html': 1, 'failed': 1}。能力来源与物理准确性证据分开；没有执行引擎 benchmark 或真机复现。

## 证据使用与限制

- 618–648：主要引擎、许可与平台后端。官网能力是事实陈述来源，不构成跨引擎速度/迁移精度排名。
- 649–669：接触建模、辨识、随机化、可微、布料等论文与配套文档；670–672补充真实撞击、最新执行器残差和高速接触模型。
- 673是Isaac Lab版本化后端文档；675是Drake许可；676是Genesis当前coupling文档，替代674的迁移失效路径。
- P02/649与P13/659核阅了HTML全文中的原理、实验和限制段落；其他论文以作者摘要/项目页/元数据为主，未逐项核验全部实验表与代码。PDF 646/667/669已保存，下载成功不等同于全文精读。
- 623为纯文本RST，Defuddle拒绝后以`fallback_html`保留；`.html`扩展文件实际为原始RST全文，可读且供报告核验，`.md`为抓取说明，未伪称干净Markdown。
- 674旧latest路径404失败，manifest保留失败原因；676新路径单独登记和抓取，未覆写失败证据。
- 657初始抓取的frontmatter误登记publisher为Vandesompele；正文作者是**Xie et al.**，`sources.csv`及报告已用正确作者；保留raw不重写。663标题以2026-09-16 v3的*Proprioception-Anchored Cross-Modal Pretraining...*为准，初始raw标题是阅读简称。
- P20/664当前v2摘要为“will be open-sourced”，不同于初版搜索摘要，故资产与代码完整性仍待验收。它与665的同名接触solver benchmark是不同项目。
- source_date未知的官方动态页面保留“待验证”；访问/抓取时间明确为2026-10-26，不把访问日冒充发布日期。

## Claim 到来源的路线

| Claim/问题 | 来源与证据边界 |
|---|---|
| MuJoCo软接触、求解与积分；MJX/Warp区别 | 619–621；Warp目前不支持自动微分，GPU不保证逐位确定性 |
| Newton多solver与experimental边界 | 622–623；不能把项目级宣传外推所有后端 |
| PhysX GPU已开源 | 624为2025-03-25官方公告，625为PGS/TGS文档；平台和资产另有许可 |
| RaiSim公开仓库不等于核心开源 | 641–642区分激活、商业授权、二进制和wrapper |
| 面接触不等于完整变形体 | 630的限制章节；650为SAP论文 |
| 接触模型偏差与数值残差不同 | 649全文Sec.III、IV-A、IV-B、V；665实现 |
| 自动微分不保证物理梯度正确 | 658；659正文Sec.3–5与Appendix D |
| 执行器、初态与时间对齐也是迁移核心 | 654、662、671；论文结果不可泛化到任意硬件 |
| DR并非所有任务必要 | 657特定四足的反方案例，不外推为全领域结论 |
| 真实数据验证的重要性 | 670撞击、660布料、664任务基准，分别覆盖不同问题 |

## 原始资料清单

| 来源 | 标题/原网址 | 抓取状态与证据 |
|---|---|---|
| [SRC-robotics-618](../../raw/robotics-embodied-ai/documents/SRC-robotics-618-mujoco-official-repository-and-license.md) | [MuJoCo official repository and license](https://github.com/google-deepmind/mujoco) | ok；S |
| [SRC-robotics-619](../../raw/robotics-embodied-ai/documents/SRC-robotics-619-mujoco-computation-contact-models-and-solvers.md) | [MuJoCo computation contact models and solvers](https://mujoco.readthedocs.io/en/stable/computation/index.html) | ok；S |
| [SRC-robotics-620](../../raw/robotics-embodied-ai/documents/SRC-robotics-620-mujoco-xla-backend-comparison-and-differentiability.md) | [MuJoCo XLA backend comparison and differentiability](https://mujoco.readthedocs.io/en/stable/mjx.html) | ok；S |
| [SRC-robotics-621](../../raw/robotics-embodied-ai/documents/SRC-robotics-621-mujoco-warp-features-limitations-and-determinism.md) | [MuJoCo Warp features limitations and determinism](https://mujoco.readthedocs.io/en/stable/mjwarp/) | ok；S |
| [SRC-robotics-622](../../raw/robotics-embodied-ai/documents/SRC-robotics-622-newton-official-repository-and-license.md) | [Newton official repository and license](https://github.com/newton-physics/newton) | ok；S |
| [SRC-robotics-623](../../raw/robotics-embodied-ai/documents/SRC-robotics-623-newton-solver-backend-comparison.md) | [Newton solver backend comparison](https://raw.githubusercontent.com/newton-physics/newton/main/docs/solvers/index.rst) | fallback_html；S |
| [SRC-robotics-624](../../raw/robotics-embodied-ai/documents/SRC-robotics-624-physx-gpu-source-code-bsd-release-announcement.md) | [PhysX GPU source code BSD release announcement](https://github.com/NVIDIA-Omniverse/PhysX/discussions/384) | ok；S |
| [SRC-robotics-625](../../raw/robotics-embodied-ai/documents/SRC-robotics-625-physx-pgs-and-tgs-simulation-solvers.md) | [PhysX PGS and TGS simulation solvers](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/Simulation.html) | ok；S |
| [SRC-robotics-626](../../raw/robotics-embodied-ai/documents/SRC-robotics-626-bullet-physics-official-repository-and-license.md) | [Bullet Physics official repository and license](https://github.com/bulletphysics/bullet3) | ok；S |
| [SRC-robotics-627](../../raw/robotics-embodied-ai/documents/SRC-robotics-627-dart-official-repository-and-license.md) | [DART official repository and license](https://github.com/dartsim/dart) | ok；S |
| [SRC-robotics-628](../../raw/robotics-embodied-ai/documents/SRC-robotics-628-open-dynamics-engine-overview-and-license.md) | [Open Dynamics Engine overview and license](https://ode.org/) | ok；S |
| [SRC-robotics-629](../../raw/robotics-embodied-ai/documents/SRC-robotics-629-simbody-official-repository-and-license.md) | [Simbody official repository and license](https://github.com/simbody/simbody) | ok；S |
| [SRC-robotics-630](../../raw/robotics-embodied-ai/documents/SRC-robotics-630-drake-hydroelastic-contact-user-guide-and-limitations.md) | [Drake hydroelastic contact user guide and limitations](https://drake.mit.edu/doxygen_cxx/group__hydroelastic__user__guide.html) | ok；S |
| [SRC-robotics-631](../../raw/robotics-embodied-ai/documents/SRC-robotics-631-project-chrono-official-repository-and-license.md) | [Project Chrono official repository and license](https://github.com/projectchrono/chrono) | ok；S |
| [SRC-robotics-632](../../raw/robotics-embodied-ai/documents/SRC-robotics-632-sofa-official-repository-fem-and-license.md) | [SOFA official repository FEM and license](https://github.com/sofa-framework/sofa) | ok；S |
| [SRC-robotics-633](../../raw/robotics-embodied-ai/documents/SRC-robotics-633-genesis-world-official-repository-and-license.md) | [Genesis World official repository and license](https://github.com/Genesis-Embodied-AI/genesis-world) | ok；S |
| [SRC-robotics-634](../../raw/robotics-embodied-ai/documents/SRC-robotics-634-genesis-toolsolver-and-rigid-solver-differentiation-limit.md) | [Genesis ToolSolver and rigid solver differentiation limit](https://genesis-world.readthedocs.io/en/latest/api_reference/engine/solvers/tool_solver.html) | ok；S |
| [SRC-robotics-635](../../raw/robotics-embodied-ai/documents/SRC-robotics-635-dojo-documentation-contact-and-mit-license.md) | [Dojo documentation contact and MIT license](https://dojo-sim.github.io/Dojo.jl/dev/) | ok；S |
| [SRC-robotics-636](../../raw/robotics-embodied-ai/documents/SRC-robotics-636-ipc-toolkit-official-repository-and-license.md) | [IPC Toolkit official repository and license](https://github.com/ipc-sim/ipc-toolkit) | ok；S |
| [SRC-robotics-637](../../raw/robotics-embodied-ai/documents/SRC-robotics-637-jolt-physics-official-repository-and-license.md) | [Jolt Physics official repository and license](https://github.com/jrouwe/JoltPhysics) | ok；S |
| [SRC-robotics-638](../../raw/robotics-embodied-ai/documents/SRC-robotics-638-rapier-physics-official-overview-and-license.md) | [Rapier physics official overview and license](https://rapier.rs/docs/) | ok；S |
| [SRC-robotics-639](../../raw/robotics-embodied-ai/documents/SRC-robotics-639-newton-dynamics-legacy-engine-license.md) | [Newton Dynamics legacy engine license](https://github.com/MADEAPPS/newton-dynamics/blob/master/LICENSE) | ok；S |
| [SRC-robotics-640](../../raw/robotics-embodied-ai/documents/SRC-robotics-640-brax-maintenance-scope-and-migration-notice.md) | [Brax maintenance scope and migration notice](https://github.com/google/brax) | ok；S |
| [SRC-robotics-641](../../raw/robotics-embodied-ai/documents/SRC-robotics-641-raisim-licensing-academic-and-commercial.md) | [RaiSim licensing academic and commercial](https://raisim.com/sections/License.html) | ok；S |
| [SRC-robotics-642](../../raw/robotics-embodied-ai/documents/SRC-robotics-642-raisim-installation-binary-and-wrapper-boundary.md) | [RaiSim installation binary and wrapper boundary](https://raisim.com/sections/Installation.html) | ok；S |
| [SRC-robotics-643](../../raw/robotics-embodied-ai/documents/SRC-robotics-643-agx-dynamics-solver-technology.md) | [AGX Dynamics solver technology](https://www.algoryx.se/technology/) | ok；S |
| [SRC-robotics-644](../../raw/robotics-embodied-ai/documents/SRC-robotics-644-agx-dynamics-contact-friction-models-and-solve-types.md) | [AGX Dynamics contact friction models and solve types](https://www.algoryx.se/documentation/complete/agx/tags/latest/doc/UserManual/source/creating_objects.html) | ok；S |
| [SRC-robotics-645](../../raw/robotics-embodied-ai/documents/SRC-robotics-645-vortex-studio-mechanical-simulation-and-ros2.md) | [Vortex Studio mechanical simulation and ROS2](https://cm-labs.com/en/vortex-studio/) | ok；A |
| [SRC-robotics-646](../../raw/robotics-embodied-ai/documents/SRC-robotics-646-havok-physics-official-product-sheet.pdf) | [Havok Physics official product sheet](https://www.havok.com/wp-content/uploads/2025/03/havokphysics-productsheet.pdf) | ok；A |
| [SRC-robotics-647](../../raw/robotics-embodied-ai/documents/SRC-robotics-647-coppeliasim-physics-engine-backend-list.md) | [CoppeliaSim physics engine backend list](https://manual.coppeliarobotics.com/en/dynamicsModule.htm) | ok；S |
| [SRC-robotics-648](../../raw/robotics-embodied-ai/documents/SRC-robotics-648-gazebo-physics-plugin-and-backend-feature-interface.md) | [Gazebo Physics plugin and backend feature interface](https://gazebosim.org/api/physics/8/physicsplugin.html) | ok；S |
| [SRC-robotics-649](../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) | [Contact Models in Robotics a Comparative Analysis](https://arxiv.org/html/2304.06372v3) | ok；S |
| [SRC-robotics-650](../../raw/robotics-embodied-ai/documents/SRC-robotics-650-an-unconstrained-convex-formulation-of-compliant-contact.md) | [An Unconstrained Convex Formulation of Compliant Contact](https://arxiv.org/abs/2110.10107) | ok；S |
| [SRC-robotics-651](../../raw/robotics-embodied-ai/documents/SRC-robotics-651-dojo-a-differentiable-physics-engine-for-robotics.md) | [Dojo A Differentiable Physics Engine for Robotics](https://arxiv.org/abs/2203.00806) | ok；S |
| [SRC-robotics-652](../../raw/robotics-embodied-ai/documents/SRC-robotics-652-incremental-potential-contact-original-project.md) | [Incremental Potential Contact original project](https://ipc-sim.github.io/) | ok；S |
| [SRC-robotics-653](../../raw/robotics-embodied-ai/documents/SRC-robotics-653-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization.md) | [Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](https://arxiv.org/abs/1710.06537) | ok；S |
| [SRC-robotics-654](../../raw/robotics-embodied-ai/documents/SRC-robotics-654-learning-agile-and-dynamic-motor-skills-for-legged-robots.md) | [Learning agile and dynamic motor skills for legged robots](https://arxiv.org/abs/1901.08652) | ok；S |
| [SRC-robotics-655](../../raw/robotics-embodied-ai/documents/SRC-robotics-655-closing-the-sim-to-real-loop-adapting-simulation-randomization-with-real-world-e.md) | [Closing the Sim-to-Real Loop Adapting Simulation Randomization with Real World Experience](https://arxiv.org/abs/1810.05687) | ok；S |
| [SRC-robotics-656](../../raw/robotics-embodied-ai/documents/SRC-robotics-656-rma-rapid-motor-adaptation-for-legged-robots.md) | [RMA Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034) | ok；S |
| [SRC-robotics-657](../../raw/robotics-embodied-ai/documents/SRC-robotics-657-dynamics-randomization-revisited-a-case-study-for-quadrupedal-locomotion.md) | [Dynamics Randomization Revisited A Case Study for Quadrupedal Locomotion](https://arxiv.org/abs/2011.02404) | ok；S |
| [SRC-robotics-658](../../raw/robotics-embodied-ai/documents/SRC-robotics-658-differentiable-physics-simulations-with-contacts-do-they-have-correct-gradients.md) | [Differentiable Physics Simulations with Contacts Do They Have Correct Gradients](https://arxiv.org/abs/2207.05060) | ok；S |
| [SRC-robotics-659](../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md) | [Differentiable Simulation of Hard Contacts with Soft Gradients for Learning and Control](https://arxiv.org/html/2506.14186v2) | ok；S |
| [SRC-robotics-660](../../raw/robotics-embodied-ai/documents/SRC-robotics-660-benchmarking-the-sim-to-real-gap-in-cloth-manipulation.md) | [Benchmarking the Sim-to-Real Gap in Cloth Manipulation](https://arxiv.org/abs/2310.09543) | ok；S |
| [SRC-robotics-661](../../raw/robotics-embodied-ai/documents/SRC-robotics-661-concent-contact-centric-real-to-sim-to-real-learning-from-one-demonstration.md) | [ConCent Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration](https://arxiv.org/abs/2606.30268) | ok；S |
| [SRC-robotics-662](../../raw/robotics-embodied-ai/documents/SRC-robotics-662-closing-the-reality-gap-zero-shot-sim-to-real-dexterous-force-based-grasping.md) | [Closing the Reality Gap Zero-Shot Sim-to-Real Dexterous Force-Based Grasping](https://arxiv.org/abs/2601.02778) | ok；S |
| [SRC-robotics-663](../../raw/robotics-embodied-ai/documents/SRC-robotics-663-pace-zero-shot-sim-to-real-contact-rich-assembly.md) | [Proprioception-Anchored Cross-Modal Pretraining for Zero-Shot Sim-to-Real Contact-Rich Assembly](https://arxiv.org/abs/2609.07534) | ok；S |
| [SRC-robotics-664](../../raw/robotics-embodied-ai/documents/SRC-robotics-664-contactbench-1-0-everyday-contact-rich-robotic-manipulation.md) | [ContactBench 1.0 Everyday Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2610.24512) | ok；S |
| [SRC-robotics-665](../../raw/robotics-embodied-ai/documents/SRC-robotics-665-contactbench-solver-benchmark-official-implementation.md) | [ContactBench solver benchmark official implementation](https://github.com/Simple-Robotics/ContactBench) | ok；S |
| [SRC-robotics-666](../../raw/robotics-embodied-ai/documents/SRC-robotics-666-genesis-non-rigid-solver-coupling-matrix.md) | [Genesis non-rigid solver coupling matrix](https://genesis-world.readthedocs.io/en/v1.0.0/user_guide/advanced_topics/solvers_and_coupling.html) | ok；S |
| [SRC-robotics-667](../../raw/robotics-embodied-ai/documents/SRC-robotics-667-mujoco-a-physics-engine-for-model-based-control-original-paper.pdf) | [MuJoCo A physics engine for model-based control original paper](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf) | ok；S |
| [SRC-robotics-668](../../raw/robotics-embodied-ai/documents/SRC-robotics-668-diffcloth-differentiable-cloth-simulation-with-dry-frictional-contact.md) | [DiffCloth Differentiable Cloth Simulation with Dry Frictional Contact](https://people.csail.mit.edu/liyifei/publication/diffcloth/) | ok；S |
| [SRC-robotics-669](../../raw/robotics-embodied-ai/documents/SRC-robotics-669-xpbd-position-based-simulation-of-compliant-constrained-dynamics.pdf) | [XPBD Position-Based Simulation of Compliant Constrained Dynamics](https://matthias-research.github.io/pages/publications/XPBD.pdf) | ok；S |
| [SRC-robotics-670](../../raw/robotics-embodied-ai/documents/SRC-robotics-670-validating-robotics-simulators-on-real-world-impacts.md) | [Validating Robotics Simulators on Real-World Impacts](https://arxiv.org/abs/2110.00541) | ok；S |
| [SRC-robotics-671](../../raw/robotics-embodied-ai/documents/SRC-robotics-671-contact-uan-unsupervised-actuator-networks-as-a-residual-world-model-for-humanoi.md) | [Contact-UAN Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](https://arxiv.org/abs/2610.18991) | ok；S |
| [SRC-robotics-672](../../raw/robotics-embodied-ai/documents/SRC-robotics-672-physics-models-for-sim-to-real-transfer-in-professional-level-robot-table-tennis.md) | [Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis](https://arxiv.org/abs/2606.28805) | ok；S |
| [SRC-robotics-673](../../raw/robotics-embodied-ai/documents/SRC-robotics-673-isaac-lab-version-3-physics-backends-and-runtime-boundaries.md) | [Isaac Lab version 3 physics backends and runtime boundaries](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics_backends.html) | ok；S |
| [SRC-robotics-674 manifest](../robotics-embodied-ai/00-source-capture-index.md) | [Genesis latest non-rigid coupling documentation](https://genesis-world.readthedocs.io/en/latest/user_guide/advanced_topics/solvers_and_coupling.html) | failed；S |
| [SRC-robotics-675](../../raw/robotics-embodied-ai/documents/SRC-robotics-675-drake-official-repository-and-bsd-license.md) | [Drake official repository and BSD license](https://github.com/RobotLocomotion/drake) | ok；S |
| [SRC-robotics-676](../../raw/robotics-embodied-ai/documents/SRC-robotics-676-genesis-latest-coupling-legacy-sap-and-ipc-models.md) | [Genesis latest coupling legacy SAP and IPC models](https://genesis-world.readthedocs.io/en/latest/user_guide/theory/coupling/index.html) | ok；S |

## 关联连接

- [[robotics-embodied-ai/research-notes/robot-physics-engines-sim2real-2026-10-26|技术报告]]
- [[_concepts/robot-contact-model-solver-and-sim2real-gap|接触、数值与现实差距概念]]
- [[robotics-embodied-ai/00-source-capture-index|行业来源索引]]
- [[robotics-embodied-ai/00-index|机器人导航]]
