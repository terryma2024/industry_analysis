---
title: Ego 视频到灵巧手训练数据：技术路线、系统设计与落地方案
type: synthesis
date_created: 2026-07-14
last_updated: 2026-07-14
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-275-hawor-world-space-hand-motion-reconstruction-from-egocentric-videos.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-276-dexumi-using-human-hand-as-the-universal-manipulation-interface-for-dexterous-ma.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-279-unidex-official-implementation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-280-egoscale-scaling-dexterous-manipulation-with-diverse-egocentric-human-data.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-281-spider-scalable-physics-informed-dexterous-retargeting.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-282-spider-official-implementation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-283-geometric-retargeting-a-principled-ultrafast-neural-hand-retargeting-algorithm.md
tags:
  - industry/robotics-embodied-ai
  - dexterous-manipulation
  - egocentric-video
  - robot-training-data
  - hand-retargeting
  - research-note
status: active
aliases:
  - Ego 视频灵巧手训练数据
  - 人类视频到灵巧手动作
---

# Ego 视频到灵巧手训练数据：技术路线、系统设计与落地方案

## 执行摘要

> [!summary]
> 如果目标是**控制灵巧手**或把第一人称视频变成**可训练、可执行、可审计的机器人数据**，MediaPipe 一类 21 点手骨架只能充当实时预览、粗筛和辅助标注，不能作为主数据链路。主链路必须联合恢复相机、手、物体和接触关系，再完成机器人本体约束下的运动学重定向、物理可行性优化、仿真与真机验收。

按使用场景，当前最合理的技术组合是：

1. **已有大量普通单目 Ego/互联网视频**：以 Do As I Do 为参考，使用 HaWoR 做世界坐标手部重建，联合物体分割、形状/6D 位姿、手物对齐，再用 SPIDER 一类物理重定向生成可执行轨迹。
2. **可以重新设计采集系统**：优先 RGB-D + 同步手姿/手套或便携动捕，参考 UniDex-Cap、DexCap；这是成本、可扩展性和数据质量之间最均衡的路线。
3. **追求高接触质量、在线遥操和生产数据**：优先 DexUMI/RealDexUMI 类可穿戴外骨骼或同构末端接口，保留触觉/力觉和机器人可达性约束；纯视觉不应承担力与接触真值。
4. **跨多种灵巧手训练**：用 UniDex 的功能—执行器对齐思路构造统一动作空间，以 GeoRT 做低延迟运动学映射，以 SPIDER 做离线动力学修正。
5. **训练大规模基础策略**：采用 EgoScale 式“海量人类 Ego 预训练 → 少量对齐的人—机器人数据中训练 → 目标本体真机后训练”，而不是把所有人类视频直接混入行为克隆。

一句话建议：**PoC 从 UniDex-Cap/DexCap 式受控 RGB-D 采集开始；存量视频接 Do As I Do；实时控制接 GeoRT；最终高质量离线数据用 SPIDER 与真机 rollout 验收。**

## 1. 课题边界：手姿识别不等于机器人动作数据

### 1.1 三个经常被混淆的问题

| 层级 | 目标 | 典型输出 | 能否直接训练/控制灵巧手 |
|---|---|---|---|
| 手势/骨架识别 | 找到手与关键点 | 2D/相机相对 3D 关键点、左右手、手势类别 | 否，只能做观测或弱标签 |
| 手—物交互重建 | 恢复世界中的手、相机、物体与接触过程 | MANO/手网格、相机轨迹、物体 mesh/6D pose、接触候选 | 仍不能直接执行 |
| 机器人动作生成 | 将人手意图变成目标本体可达、稳定、无碰撞的动作 | 关节位置/速度/力矩、腕部 SE(3)、接触/夹持状态、控制频率 | 是，但需仿真和真机验收 |

MediaPipe Hand Landmarker、RTMPose、WiLoR 等可以提升第一层的速度或精度，但第二、三层还需要时序世界坐标、物体状态、接触约束和机器人模型。尤其对旋盖、插拔、捏取、工具使用等高接触任务，仅有手指关节角不能解释物体是否被稳定夹持、所需摩擦力是否足够，以及动作能否在目标灵巧手上执行。

### 1.2 最低可用的数据闭环

一个可用于灵巧手学习的 episode 至少要回答：

- **看到了什么**：同步 RGB/RGB-D、相机内外参、时间戳和必要的触觉/力觉。
- **人做了什么**：世界坐标中的腕部与手指运动、可见度和估计置信度。
- **物体发生了什么**：物体身份/几何、6D 位姿、速度、遮挡和重新捕获状态。
- **机器人应该怎么做**：目标本体上的关节/腕部动作、控制频率和约束。
- **动作是否可信**：碰撞、穿透、滑移、接触一致性、仿真成功和真机 rollout 结果。
- **数据从哪里来**：原视频、模型和版本、标定、重定向配置、人工修改与许可证。

## 2. 路线选择矩阵

| 业务场景 | 推荐主方案 | 主要优点 | 主要缺口 | 适合阶段 |
|---|---|---|---|---|
| 已有海量普通单目视频 | HaWoR + 手物重建 + Do As I Do + SPIDER | 可利用历史/互联网资产；无须重新采集 | 通过率低；深度、接触、尺度和物体位姿不稳定 | 离线数据挖掘、预训练 |
| 可控室内 Ego 数据采集 | RGB-D + UniDex-Cap/DexCap 式手姿传感 | 时间同步、尺度和遮挡更可控；成本适中 | 仍需跨本体重定向；传感器要标定 | 首个 PoC、规模化采集 |
| 高接触/高精度数据生产 | DexUMI/RealDexUMI 类外骨骼或同构接口 | 采集时约束机器人可达性；可加入触觉反馈 | 硬件复杂、穿戴影响自然动作、本体绑定更强 | 生产级示教、真机策略 |
| 在线人手控制灵巧手 | 手套/外骨骼 + GeoRT + 安全控制器 | 低延迟；可把操作者实时意图映射到机器人 | 运动学映射不等于动力学稳定；必须有碰撞和力限幅 | 遥操、纠错、HIL |
| 多种灵巧手共享数据 | UniDex FAAS + 多本体 adapter + SPIDER | 减少 6–24 DoF 等不同本体的动作空间割裂 | 统一空间会损失个别硬件特性 | 基础模型、跨手迁移 |
| 大规模 VLA/基础策略 | EgoScale 式三阶段训练 | 用人类视频学习通用运动先验，再用少量机器人数据对齐 | 仍离不开对齐数据和目标本体后训练 | 中长期模型平台 |

## 3. 推荐系统架构

```mermaid
flowchart LR
    A["采集：Ego RGB/RGB-D、手姿、IMU、触觉/力觉"] --> B["同步与标定：时间戳、内外参、坐标系"]
    B --> C["Episode 切分与粗筛：任务、手物可见、镜头边界"]
    C --> D["4D 重建：相机、手网格、物体 mesh/6D pose"]
    D --> E["手物对齐与接触候选：尺度、距离、遮挡、置信度"]
    E --> F["运动学重定向：腕部 SE(3)、指尖、关节约束"]
    F --> G["物理重定向：碰撞、摩擦、力学、接触序列"]
    G --> H["数字孪生验收：穿透、滑移、自碰、任务完成"]
    H --> I["真机 rollout：限速、力限、急停、人工接管"]
    I --> J["Dataset Registry：版本、谱系、质量分、许可证"]
    J --> K["预训练 / 中训练 / 目标本体后训练"]
    K --> L["失败挖掘与补采"]
    L --> C
```

这个架构将“重建准确”与“机器人可执行”设为两个独立验收门。单纯的重投影效果好，不代表接触轨迹在目标手上成立；仿真成功也不代表真实摩擦、柔顺性和传感延迟足够。

## 4. 各环节技术方案

### 4.1 采集与传感器

#### 方案 A：普通单目 Ego RGB

最低硬件成本，适合盘活存量视频和互联网视频。代价是绝对尺度、深度、被遮挡手指、物体背面几何、接触力都需要模型推断。Do As I Do 在已经过手物交互筛选的 100DOH 中抽样 2,000 个 10 秒片段，最终只有 83 个（4%）通过重建质检；论文认为理想情况下也约 5%，相当于约 20 倍的无效数据惩罚。[`SRC-robotics-241`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md)

因此，单目路线必须把“候选视频池 → 自动粗筛 → 重建 → 自动/人工质检”当作产品核心，而不是假设每小时视频都能变成一小时动作数据。

#### 方案 B：同步 RGB-D + IMU + 手姿

这是建议的 PoC 起点。UniDex-Cap 使用同步 RGB-D 与人手姿态，并将其转为机器人可执行轨迹；UniDex 还在显式点云中遮掉人手，以缩小人手与机器人手的视觉差异。[`SRC-robotics-278`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md)

工程上应保留：

- 每帧硬件时间戳和同步误差；
- RGB、depth、IMU、手姿、触觉的各自原始帧率；
- 相机内参、深度尺度、手姿传感器到相机的外参；
- 掉帧、曝光、运动模糊、深度无效区和温漂；
- 每次穿戴/开机后的标定版本。

#### 方案 C：便携动捕/外骨骼/同构接口

DexCap 通过 SLAM、电磁感知和环境 3D 观测，提供对遮挡更稳健的腕部和手指跟踪，并用 IK 与点云模仿学习生成策略；还支持 rollout 中的人在环修正。[`SRC-robotics-277`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md)

DexUMI 使用可穿戴手部外骨骼，在采集阶段把人手动作约束到机器人手的可行运动，并提供触觉反馈；软件侧通过机器人手图像修复缩小视觉域差异。论文在两种灵巧手平台上报告平均 86% 任务成功率，但这是作者实验，不应直接外推到其他本体和任务。[`SRC-robotics-276`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-276-dexumi-using-human-hand-as-the-universal-manipulation-interface-for-dexterous-ma.md)

RealDexUMI 更进一步，让采集端和部署端共享灵巧末端执行器、手内视觉与指尖触觉，降低重定向和 embodiment gap；论文在 3 种机器人本体、8 个任务上报告 88.75% 平均成功率，同样属于作者报告。[`SRC-robotics-134`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md)

### 4.2 手部世界坐标重建

HaWoR 针对第一人称视频中“相机和手同时运动”的问题，把任务拆为相机坐标中的手部重建与世界坐标中的相机轨迹估计，并使用自适应 Ego SLAM；手移出画面时，再用 motion infiller 补全缺失段。[`SRC-robotics-275`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-275-hawor-world-space-hand-motion-reconstruction-from-egocentric-videos.md)

建议输出不只是 21 点，而是：

- 手腕世界位姿 `T_world_wrist`；
- MANO 或兼容手网格参数、关节角与指尖位置；
- 每个关节的可见度、置信度和被补帧标志；
- 左右手身份与跨帧 track id；
- 相机世界轨迹和漂移/重定位事件；
- 原始 2D 观测与 3D 重建的映射。

MediaPipe 可放在这里做低成本候选检测和退化 fallback，但它输出的 world landmarks 仍是手部局部几何估计，不等价于稳定的场景世界坐标轨迹。详见 [[ai/research-notes/google-mediapipe-comprehensive-guide-2026-07-14|Google MediaPipe 全面调研]]。

### 4.3 物体形状、6D 位姿与手物对齐

这是从“手骨架”走向“操作数据”的关键增量。

**已知物体**应优先使用 CAD/扫描 mesh、标定尺寸和模型式 6D pose tracker；这比每段视频都生成 mesh 更稳定，也更容易建立摩擦、质量和碰撞参数。

**开放世界物体**可参考 Do As I Do：SAM 3 做手物分割，MoGe 估计深度和内参，SAM 3D 生成物体 mesh，再通过逐帧 guided diffusion 跟踪物体姿态，并把物体、HaWoR 手与相机对齐到一致的近似度量空间。[`SRC-robotics-241`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md)

必须记录以下不确定性：

- mesh 来自已知资产、扫描还是单图生成；
- 物体尺度是否有外部真值；
- 6D pose 是否发生漂移、丢锁、重捕获或对称性跳变；
- 手物间距和接触是观测、几何推断还是物理优化结果；
- 柔性、铰接、透明、反光和低纹理物体是否超出系统支持范围。

### 4.4 从人手到机器人手的运动学重定向

运动学重定向的目标不是逐关节复制，而是保留任务相关的几何功能：腕部轨迹、指尖路径、抓取类型、手掌朝向、拇指对指、接触顺序和物体相对运动。

推荐采用分层目标：

1. 首先保证机器人关节限位、自碰和工作空间可行；
2. 再匹配腕部 SE(3)、指尖和掌心；
3. 对抓取阶段提高接触/物体相对位姿权重；
4. 对自由运动阶段提高轨迹平滑与速度约束；
5. 保留多个候选解，而不是只保存单一 IK 结果。

GeoRT 用无监督几何目标学习人手指关键点到机器人关键点的映射，论文报告 1 kHz 推理，并覆盖运动保真、配置空间覆盖、响应平坦性、捏合对应与防自碰目标；适合实时遥操或作为离线优化初值。[`SRC-robotics-283`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-283-geometric-retargeting-a-principled-ultrafast-neural-hand-retargeting-algorithm.md)

UniDex 的 FAAS 按功能相近的执行器建立共享坐标，面向 6–24 DoF、8 种灵巧手的数据迁移；其数据生成还加入人类在环，以保留指尖轨迹和合理手物接触。[`SRC-robotics-278`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md)

### 4.5 物理重定向与动态可行性

运动学上相似的轨迹仍可能因为摩擦、惯性、力矩、关节速度、接触刚度和控制延迟而失败。SPIDER 将人类示教视为“全局任务结构和目标”，再通过大规模物理采样和虚拟接触引导，把只有运动学信息的人类动作转为动态可行轨迹。论文覆盖 9 种本体和 6 个数据集，并报告相对标准采样成功率提高 18%、比 RL baseline 快 10 倍及生成 240 万帧数据；这些均需在目标本体复现。[`SRC-robotics-281`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-281-spider-scalable-physics-informed-dexterous-retargeting.md)

其官方实现已经给出从视频/数据集到机器人动作的处理链，支持 MuJoCo Warp、Genesis 和 IsaacGym 等仿真后端，可作为工程 PoC 的离线物理优化底座。[`SRC-robotics-282`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-282-spider-official-implementation.md)

Do As I Do 也显示物理优化的必要性：其 reconstruction 参考上的重定向成功率从基础 annealed sampling 的 0.25 提升到加入 warmup、perturbation 和 transition reward 后的 0.71；OakInk2 上为 0.72 到 0.81。论文最终生成 500 条人工验证轨迹，其中 53% 来自互联网、31% 来自 Ego、16% 来自生成视频；真机使用 22-DoF Sharpa Wave 手与 UR3e，并以 50 Hz 下发命令。[`SRC-robotics-241`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md)

## 5. 数据格式建议

应保存人类参考、机器人动作、交互状态、质量与谱系，而不是只保存一组重定向后的关节角。最小 schema 可设计为：

```yaml
episode:
  episode_id: string
  task_id: string
  source_type: controlled_ego | internet_video | dexumi | real_robot
  timestamp_ns: int64[]
  instruction: string
  outcome: success | partial | failure | unknown

observation:
  rgb: video_or_frame_ref
  depth: optional_array_ref
  camera_intrinsics: matrix3x3
  T_world_camera: se3[]
  imu: optional_array_ref
  tactile: optional_array_ref
  force_torque: optional_array_ref

human_reference:
  hand_side: left | right | bimanual
  T_world_wrist: se3[]
  mano_parameters: optional_array_ref
  joints_3d_world: float[T, J, 3]
  fingertips_3d_world: float[T, 5, 3]
  visibility: float[T, J]
  reconstruction_confidence: float[T]
  infilled_mask: bool[T]

object:
  object_id: string
  mesh_ref: string
  mesh_source: cad | scan | generated
  scale_source: measured | depth | inferred
  T_world_object: se3[]
  tracking_confidence: float[T]
  reacquired_mask: bool[T]

robot_action:
  embodiment_id: string
  controller_type: position | velocity | torque | hybrid
  control_hz: float
  T_world_robot_wrist: se3[]
  joint_position: float[T, D]
  joint_velocity: optional_float[T, D]
  joint_torque: optional_float[T, D]
  normalized_function_action: optional_float[T, F]

interaction:
  contact_links: list
  contact_points: optional_float[T, C, 3]
  contact_source: observed | geometric | simulated | tactile
  penetration_depth: float[T]
  slip_score: float[T]

quality:
  sync_error_ms: float
  calibration_version: string
  reconstruction_pass: bool
  retarget_pass: bool
  simulation_pass: bool
  real_rollout_pass: optional_bool
  reviewer: optional_string
  rejection_reason: optional_string

lineage:
  raw_source_ref: string
  source_license: string
  model_versions: map
  retarget_config_hash: string
  simulator_version: string
  human_edits: list
```

同一 episode 可以有多个 `robot_action` 变体，分别对应不同灵巧手、不同控制器或不同物理参数。不要覆盖旧结果；所有重建、重定向和人工修订都应可回溯。

## 6. 训练方案

### 6.1 三阶段数据混合

1. **人类 Ego 预训练**：学习语义、手物交互阶段、腕部与指尖运动先验；允许较弱动作标签，但必须保留置信度。
2. **人—机器人对齐中训练**：使用同场景或相似任务中同时具有人类参考与机器人动作的数据，学习 embodiment adapter 和视觉域对齐。
3. **目标本体后训练**：用真机示教、成功/失败 rollout、人类接管和触觉数据对控制稳定性做最后校准。

EgoScale 在超过 20,854 小时的动作标注 Ego 视频上训练 VLA，并采用“人类预训练 → 少量对齐人—机器人中训练”的两阶段迁移；论文在 22-DoF 灵巧手上报告相对无预训练 baseline 的平均成功率提升 54%，并观察到人类数据规模与验证损失的 log-linear 关系。[`SRC-robotics-280`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-280-egoscale-scaling-dexterous-manipulation-with-diverse-egocentric-human-data.md)

这支持“人类视频提供可复用运动先验”的方向，但也明确说明：**规模不能替代对齐数据**。如果目标是精确接触和力控，仍需要少量但高质量、与目标机器人同域的数据。

### 6.2 训练时的样本权重

建议按以下因素加权或分桶，而不是把所有轨迹视为等价：

- 数据源：真机成功 > 同构接口 > 受控 RGB-D > 普通 Ego > 互联网视频；
- 质量门：真机通过、仿真通过、仅重建通过、仅粗标签；
- 置信度：手部可见、物体位姿连续、接触有传感器证据；
- 任务阶段：接近、预抓取、接触、操作、释放；
- 本体距离：目标手、同构手、功能相似手、远异构手；
- 稀缺性：少见抓型、失败恢复、遮挡、滑移、双手配合。

## 7. 质量门与评测指标

### 7.1 分层质量门

| 质量门 | 必查项 | 不通过时的处理 |
|---|---|---|
| 采集门 | 同步误差、标定、掉帧、曝光、深度有效率 | 重采或降级为弱标签 |
| 内容门 | 任务完整、手物都在画面、无镜头切换 | 丢弃或重新切段 |
| 重建门 | 手身份稳定、相机漂移、物体 pose 连续、尺度合理 | 重跑、人工校正或丢弃 |
| 几何门 | 指尖/掌心保真、关节限位、自碰、腕部可达 | 调整权重或保留其他候选解 |
| 物理门 | 穿透、滑移、接触序列、摩擦敏感性、任务完成 | 物理优化或降级 |
| 真机门 | 限速/力、急停、稳定抓取、最终 outcome | 进入失败/接管数据而非删除 |
| 训练门 | 数据加入前后离线损失与闭环成功率变化 | 无边际收益则降权或剔除 |

### 7.2 核心指标

- 候选视频利用率与各拒绝原因占比；
- 每条有效轨迹的计算、人审和真机成本；
- 手部/物体重建置信度、轨迹连续率和重捕获次数；
- 重定向可行率、仿真任务成功率、真实 rollout 成功率；
- 仿真到真机的成功率折损；
- 不同物体、抓型、操作者、场景和本体上的覆盖度；
- 数据加入训练后的闭环成功率、任务进度和失败恢复提升；
- P50/P95 数据处理延迟、失败重跑率和版本可复现率。

最终北极星指标不是 MPJPE 或关键点准确率，而是：**新增一批数据后，目标机器人在留出任务和真实扰动下的闭环能力提升，除以这批数据的全成本与风险。** 这一口径与 [[robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]] 一致。

## 8. 三套落地配置

### 8.1 配置一：存量单目视频挖掘

适合已经有大量第一人称/互联网视频，但无法重新采集的团队。

- 手：HaWoR；MediaPipe/WiLoR 只做粗筛或 fallback。
- 物体：已知物体走 CAD + 6D tracker；未知刚体走分割 + 生成 mesh + pose tracking。
- 对齐：深度/点图建立近似尺度，显式记录尺度来源和不确定性。
- 重定向：GeoRT/IK 生成初值，SPIDER 做物理优化。
- 验收：MuJoCo/Isaac 数字孪生 + 小批量真机 rollout。
- 预期：利用率可能是个位数百分比，必须把拒绝原因和人工校正成本纳入单位有效轨迹成本。

### 8.2 配置二：建议的首个 PoC

适合从零启动数据链路、希望 6–8 周看到闭环的团队。时间为工程建议，不是论文结论。

- 硬件：头戴或胸前 RGB-D、IMU、可选手套/标记；固定外部相机用于验收。
- 范围：1 种目标灵巧手、2–3 个刚体物体任务、单手优先。
- 样本：先采 200–500 个短 episode 候选，数量为规划估计，应以首周通过率修正。
- 软件：同步/标定 → 手物重建 → 运动学重定向 → 仿真门 → 真机门 → LeRobot/RLDS/HDF5 导出。
- 成功定义：至少一种任务可从人类采集稳定生成机器人轨迹，并证明数据加入后比不加入有闭环增益。

建议周次：

1. 第 1 周锁定目标手、控制接口、任务和物体资产；建立标定与急停。
2. 第 2 周跑通同步 RGB-D、手姿和 episode schema。
3. 第 3–4 周完成手物重建、可视化和拒绝原因统计。
4. 第 4–5 周完成运动学/物理重定向和仿真验收。
5. 第 6 周小批量真机 rollout，收集失败与人工接管。
6. 第 7–8 周训练 baseline、做数据增量 A/B 并决定扩量方向。

### 8.3 配置三：生产级高接触数据工厂

适合旋拧、插拔、在手操作、双手协同等任务。

- 采集端使用 DexUMI/RealDexUMI 类接口或目标手同构装置；
- 指尖触觉、腕部力矩和控制器内部状态作为一级数据；
- 同一任务保留成功、失败、滑移、人工接管和恢复片段；
- 为每种物体维护数字资产、质量/摩擦分布和仿真校准版本；
- 在线 GeoRT/控制器保障低延迟，离线 SPIDER/轨迹优化生成训练版本；
- 每次模型/控制器更新都用固定留出任务与真实扰动回归测试。

## 9. 主要风险与应对

| 风险 | 为什么发生 | 应对 |
|---|---|---|
| 单目尺度和深度错 | 相机运动、遮挡、低纹理导致几何歧义 | RGB-D/已知尺寸锚点；保留尺度置信度 |
| 物体 pose 漂移 | 手遮挡、对称物体、透明反光、运动模糊 | CAD tracker、多视角、重捕获标志、人工关键帧 |
| 接触“看起来对”但力学错误 | 视频没有法向力、摩擦和柔顺性真值 | 触觉/力觉、物理优化、参数随机化和真机门 |
| 人手到机器人手形态差异 | DoF、指长、拇指结构和耦合不同 | 功能目标、多个候选解、FAAS/adapter、人类在环 |
| 仿真成功但真机失败 | 摩擦、时延、结构柔顺、控制带宽不一致 | 数字孪生校准、保守限速、少量真机后训练 |
| 大量视频无法使用 | 内容不完整、手物出画、镜头切换、重建失败 | 先做内容门；优化利用率而非只追求视频小时数 |
| 数据泄漏与许可证 | 互联网视频、MANO/模型/代码许可不同 | episode 级 license、来源谱系、商用前法律复核 |
| 作者 benchmark 被误当产线指标 | 任务、本体和评测分布不同 | 所有数字标“作者报告”，在目标任务独立复现 |

## 10. 中国团队的落地判断

### 10.1 更适合先做的场景

中国团队的优势不只是低成本采集，而是硬件、夹具、工装、相机和制造现场可以快速协同。因此首批任务应选择：

- 物体 CAD/尺寸可得、刚体为主；
- 成功判定客观，如插入深度、旋转角度、是否抓稳；
- 可重复布置且有真实产业价值；
- 允许先单手、后双手；
- 失败不会产生高安全或高材料成本。

比起直接挑战开放家庭长程任务，工业装配、分拣后处理、工具递送、旋盖/插拔等约束任务更容易建立“数据—策略—真机指标”闭环。

### 10.2 可形成的产品能力

产业机会可能不在单一手姿模型，而在以下系统层：

1. 多源 Ego/手套/机器人数据统一接入与标定；
2. 手—物 4D 重建、物体资产和质量分管理；
3. 多品牌灵巧手的重定向 adapter 与统一动作空间；
4. 仿真批量验收、真机回放和失败归因；
5. 数据谱系、授权、版本和对下游模型的边际价值评估。

这与 [[vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA 与世界模型数据基建平台]] 的 episode-first、自动质检、dataset registry 和失败补采闭环可以直接合并。

## 11. 事实、判断与待验证假设

### 已有一级来源支持的事实

- HaWoR 面向 Ego 视频中的世界坐标手部运动重建，联合相机内手部重建、自适应 Ego SLAM 与缺失段补全。
- Do As I Do 展示了普通视频经手物重建、运动学/动力学重定向到真机回放的完整链路，也暴露了约 4% 的严格视频通过率。
- UniDex 提供 Ego 视频到 8 种灵巧手、统一动作空间、VLA 与 RGB-D 采集的一体化路线；官方代码覆盖数据准备、重定向、预训练和后训练。
- DexCap、DexUMI 与 RealDexUMI 证明受控传感器和采集接口可以显著缩小遮挡、运动学和视觉差距。
- GeoRT 解决低延迟几何重定向，SPIDER 解决离线动力学可行性，二者承担不同角色。
- EgoScale 支持“大规模人类视频先验 + 少量对齐数据”的训练范式，但没有消除目标机器人数据需求。

### 本文的工程判断

- 对首个 PoC，RGB-D + 手姿传感比纯单目更优；它减少的重建和人工成本通常比新增硬件成本更重要。
- 单目存量视频适合扩充预训练与动作候选，不宜直接作为高精度接触控制的唯一真值。
- 运动学与物理重定向应分层，实时链路与离线训练数据链路也应分开。
- 数据价值必须以闭环任务提升验收，而不是以视频小时、关键点帧数或重建视觉效果验收。

### 待目标项目验证的假设

- 目标任务在 200–500 个候选 episode 内能获得足够的高质量成功/失败数据；
- SPIDER/GeoRT 对目标国产灵巧手的 URDF、耦合关节和控制接口适配成本可控；
- RGB-D 深度在目标物体材质上稳定；透明/反光物体可能需要额外传感器；
- 仿真门能够显著减少危险或无效真机 rollout；
- 人类 Ego 预训练对目标任务的边际收益高于同等预算的纯机器人示教。

## 12. 最终建议

如果当前还没有确定硬件，建议按以下顺序决策：

1. 先定目标灵巧手、控制频率、任务和是否需要力控；
2. 用同步 RGB-D + 手姿传感搭建最小闭环，不先追求海量互联网视频；
3. 用 GeoRT/IK 解决实时初始映射，用 SPIDER/物理优化生成离线训练版本；
4. 建立仿真和真机双质量门，失败与人工接管作为正式数据保留；
5. 闭环跑通后，再接入 Do As I Do 式存量视频扩大覆盖；
6. 多本体和基础模型阶段，再引入 UniDex FAAS 与 EgoScale 式分阶段训练。

因此，**“MediaPipe + 关节角映射”适合演示；“RGB-D/动捕 + 手物 4D 重建 + 运动学/物理重定向 + rollout 验收”才是训练数据系统。**

## 主要来源

- [`SRC-robotics-241` Do As I Do](../../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md)
- [`SRC-robotics-275` HaWoR](../../../raw/robotics-embodied-ai/documents/SRC-robotics-275-hawor-world-space-hand-motion-reconstruction-from-egocentric-videos.md)
- [`SRC-robotics-276` DexUMI](../../../raw/robotics-embodied-ai/documents/SRC-robotics-276-dexumi-using-human-hand-as-the-universal-manipulation-interface-for-dexterous-ma.md)
- [`SRC-robotics-134` RealDexUMI](../../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md)
- [`SRC-robotics-277` DexCap](../../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md)
- [`SRC-robotics-278` UniDex 论文](../../../raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md)
- [`SRC-robotics-279` UniDex 官方实现](../../../raw/robotics-embodied-ai/documents/SRC-robotics-279-unidex-official-implementation.md)
- [`SRC-robotics-280` EgoScale](../../../raw/robotics-embodied-ai/documents/SRC-robotics-280-egoscale-scaling-dexterous-manipulation-with-diverse-egocentric-human-data.md)
- [`SRC-robotics-281` SPIDER 论文](../../../raw/robotics-embodied-ai/documents/SRC-robotics-281-spider-scalable-physics-informed-dexterous-retargeting.md)
- [`SRC-robotics-282` SPIDER 官方实现](../../../raw/robotics-embodied-ai/documents/SRC-robotics-282-spider-official-implementation.md)
- [`SRC-robotics-283` GeoRT](../../../raw/robotics-embodied-ai/documents/SRC-robotics-283-geometric-retargeting-a-principled-ultrafast-neural-hand-retargeting-algorithm.md)

## 关联连接

- [[robotics-embodied-ai/00-index|机器人（具身智能）研究入口]]
- [[robotics-embodied-ai/07-training-data|训练数据生产与处理]]
- [[robotics-embodied-ai/09-training-data-deep-dive|训练数据深度调研]]
- [[_syntheses/bilibili-do-as-i-do-dexterous-video-data-deep-dive-2026-07-07|Do As I Do 灵巧操作视频数据深度调研]]
- [[vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA 与世界模型数据基建平台系统调研与设计]]
- [[teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据成本与占比]]
- [[embodied-ai-training-data-hour-requirements-2026-07-09|具身智能训练数据需求量与小时数]]
- [[open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
- [[robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]
- [[ai/research-notes/google-mediapipe-comprehensive-guide-2026-07-14|Google MediaPipe 全面调研]]
