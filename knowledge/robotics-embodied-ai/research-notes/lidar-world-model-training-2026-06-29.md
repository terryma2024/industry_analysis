---
title: 激光雷达数据融合进入世界模型训练论文与方案调研
type: synthesis
date_created: 2026-06-29
last_updated: 2026-06-29
aliases:
  - LiDAR world model training survey
  - 激光雷达世界模型训练调研
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - knowledge/_entities/LiDAR.md
  - knowledge/_concepts/joint-embedding-predictive-architecture.md
tags:
  - industry/robotics-embodied-ai
  - world-model
  - lidar
  - autonomous-driving
  - embodied-ai
status: draft
---

# 激光雷达数据融合进入世界模型训练论文与方案调研

## 摘要

当前把 [[_entities/LiDAR|LiDAR 激光雷达]] 融入世界模型训练，主战场仍在自动驾驶，机器人移动导航和室内 3D occupancy 方向开始出现论文。最稳妥的理解不是“把点云直接喂给大模型”，而是把 LiDAR 变成可预测、可对齐、可规划的空间状态：

- **用于规划/碰撞安全：** 优先用 BEV、3D/4D occupancy、semantic occupancy 或 voxel flow 作为中间表示。
- **用于传感器仿真/数据合成：** 保留 LiDAR 原生几何，采用 range image、ray-centric token、点云 token、动态/静态分解和扩散/Mamba/Transformer 生成。
- **用于多模态世界模型：** 用 camera/video VAE 与 LiDAR VAE、BEV latent 或 voxel latent 做跨模态对齐，让模型同时生成未来图像和 LiDAR。
- **用于少标注预训练：** JEPA 路线直接预测 latent BEV/occupancy embedding，避免像素/点云重建的高成本。

**初步判断：** 如果目标是“训练能辅助规划的世界模型”，先做 occupancy/BEV 世界模型；如果目标是“生成真实 LiDAR 数据训练感知模型”，走 LiDAR-native generative model；如果目标是“物理 AI 多模态仿真底座”，再做 camera-LiDAR unified latent。

## 问题定义

世界模型训练可以抽象为：

```text
z_{t+1:t+k} = f(z_{<=t}, a_{t:t+k}, c)
```

其中 `z` 是环境状态 latent，`a` 是 ego action、trajectory、steering、velocity 或机器人控制，`c` 是 map、language、layout、task prompt 或 scene condition。LiDAR 可以在四个位置进入训练：

1. **Observation encoder：** 点云、range image、ray、voxel 或 BEV 特征进入 tokenizer/VAE/encoder。
2. **Spatial state：** LiDAR 约束 3D occupancy、semantic occupancy、flow、dynamic/static scene decomposition。
3. **Cross-modal alignment：** camera latent 与 LiDAR latent 在 BEV/voxel/ray 空间对齐，做未来多模态生成。
4. **Evaluation/planning：** 用未来 occupancy、point cloud 或 ray consistency 计算碰撞、可通行空间、未来障碍和 downstream perception uplift。

## 论文地图

| 方向 | 论文 | LiDAR/空间表示 | 核心方案 | 可借鉴点 | 主要边界 |
|---|---|---|---|---|---|
| 多模态 MBRL | [`SRC-robotics-200`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-200-sense-imagine-act-multimodal-world-models-for-robotic-control.md) Sense, Imagine, Act, 2023 | F1TENTH egocentric LiDAR + RGB | Dreamer 类 model-based RL，LiDAR/RGB 自监督融合 | 机器人/赛车场景中，LiDAR 可提升 world model 的状态估计鲁棒性 | 任务较窄，偏仿真赛车，不是通用世界模型 |
| 多模态 voxel | [`SRC-robotics-201`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-201-muvo-a-multimodal-world-model-for-autonomous-driving-with-geometric-representati.md) MUVO, 2023 | raw camera + LiDAR -> spatial voxel | 学 sensor-agnostic geometric representation，并预测未来图像和点云 | 早期 camera-LiDAR world model 融合范式 | 规模和生成能力弱于后续扩散/DiT 路线 |
| 点云 token | [`SRC-robotics-202`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-202-copilot4d-learning-unsupervised-world-models-for-autonomous-driving-via-discrete.md) Copilot4D, 2023 | point cloud observations -> VQ-VAE tokens | VQ-VAE tokenization + discrete diffusion 预测未来点云 | LiDAR 原生序列建模基线，适合点云预测 MVP | 点云无序、稀疏和动态对象仍难处理 |
| Occupancy token | [`SRC-robotics-203`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-203-occworld-learning-a-3d-occupancy-world-model-for-autonomous-driving.md) OccWorld, 2023 | 3D occupancy，来自 sparse LiDAR points 或视觉 | scene tokenizer + GPT-like spatiotemporal transformer，预测未来 occupancy 与 ego | 把 LiDAR 转成 occupancy 后进入 planning，是最清晰路线之一 | occupancy 标注/构建质量决定上限 |
| LiDAR 生成仿真 | [`SRC-robotics-204`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-204-lidardm-generative-lidar-simulation-in-a-generated-world.md) LidarDM, 2024 | 4D LiDAR point cloud | latent diffusion 生成 3D scene + dynamic actors，再渲染 LiDAR videos | 适合“生成 LiDAR 数据训练/测试感知模型” | 更偏 sensor simulation，不直接给出控制策略 |
| 4D occupancy diffusion | [`SRC-robotics-205`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-205-occsora-4d-occupancy-generation-models-as-world-simulators-for-autonomous-drivin.md) OccSora, 2024 | 4D occupancy tokens | 4D scene tokenizer + diffusion transformer，trajectory prompt 条件生成 | 长时序 occupancy world simulator 参考 | 依赖 occupancy annotations，主要是 nuScenes/Occ3D |
| 统一 BEV latent | [`SRC-robotics-206`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-206-bevworld-a-multimodal-world-model-for-autonomous-driving-via-unified-bev-latent.md) BEVWorld, 2024 | multimodal sensors -> compact BEV latent | multimodal tokenizer + latent BEV sequence diffusion，ray-casting 解码 LiDAR/图像 | 适合 camera-LiDAR 融合和 action-conditioned future generation | BEV latent 会丢失部分原生 LiDAR 细节 |
| 4D occupancy planning | [`SRC-robotics-207`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-207-drive-occworld-4d-pre-trained-world-model-for-autonomous-driving.md) Drive-OccWorld, 2024 | historical BEV embeddings -> future occupancy/flow | action conditions 注入 velocity、steering、trajectory、commands；occupancy cost 选轨迹 | 从“生成未来”走向“规划可用”的关键范式 | 仍主要是自动驾驶结构化道路 |
| 高效 occupancy | [`SRC-robotics-208`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-208-dfit-occworld-an-efficient-occupancy-world-model-via-decoupled-dynamic-flow-and.md) DFIT-OccWorld, 2024 | 3D occupancy + dynamic voxel flow | 动态/静态体素解耦，image-assisted rendering consistency | 工程上降低计算成本，适合轻量化 occupancy world model | 需要仔细验证跨数据集泛化 |
| VLA occupancy | [`SRC-robotics-209`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-209-occllama-an-occupancy-language-action-generative-world-model-for-autonomous-driv.md) OccLLaMA, 2024 | semantic occupancy tokens | VQVAE-like scene tokenizer + unified vision-language-action vocabulary + LLaMA | 把 occupancy、语言、动作放进统一 token 序列 | 复杂度高，训练数据/任务设计门槛高 |
| LiDAR JEPA | [`SRC-robotics-210`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-210-ad-l-jepa-self-supervised-spatial-world-models-from-lidar-for-autonomous-driving.md) AD-L-JEPA, 2025 | LiDAR BEV embeddings | 非生成、非对比 JEPA，预测 BEV embedding | 适合少标注 LiDAR encoder 预训练和下游检测迁移 | 2025 版本偏空间表征，还不是完整时序世界模型 |
| 室内 occupancy robot | [`SRC-robotics-211`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-211-robooccworld-benchmarking-3d-occupancy-world-models-for-robots.md) RoboOccWorld, 2025 | indoor 3D occupancy | guided autoregressive transformer + spatiotemporal aggregation | 把 occupancy world model 从道路拓展到室内机器人 | 论文不等同于 LiDAR 专项方案，但对机器人场景有参考价值 |
| Ray-centric LiDAR | [`SRC-robotics-212`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-212-listar-lidar-spatial-temporal-aggregation-and-rendering-for-ray-centric-world-mo.md) LiSTAR, 2025 | LiDAR native rays / HCS representation | Ray-Centric Transformer + Masked Generative START | 保留 LiDAR 球面/射线几何，适合高保真可控 4D LiDAR | 主要目标是 LiDAR 合成和预测 |
| LiDAR navigation RL | [`SRC-robotics-213`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-213-world-models-for-autonomous-navigation-of-terrestrial-robots-from-lidar-observat.md) World Models for Terrestrial Robots, 2025 | 360 readings LiDAR | MLP-VAE 压缩 LiDAR，DreamerV3 world model 做 imagination policy optimization | 对移动机器人“从 LiDAR 读数到世界模型控制”最直接 | 仿真 TurtleBot3，尚非真实复杂场景 |
| LiDAR spatiotemporal JEPA | [`SRC-robotics-214`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-214-ad-list-jepa-joint-embedding-predictive-architecture-for-spatial-temporal-world.md) AD-LiST-JEPA, 2026 | LiDAR occupancy completion / forecasting | JEPA 预测未来时空演化，用 OCF 评估 | 少标注 LiDAR occupancy forecasting 值得重点跟踪 | 当前是 proof of concept |
| 3D understanding + generation | [`SRC-robotics-215`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-215-hermes-a-self-supervised-framework-for-simultaneous-3d-scene-understanding-and-g.md) HERMES++, 2026 | BEV + future point cloud geometry | LLM-enhanced world queries + Current-to-Future Link + geometric constraints | 将 3D scene understanding 与未来几何预测合并 | LLM 语义和几何预测如何稳定耦合仍需验证 |
| LiDAR Mamba | [`SRC-robotics-216`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-216-gem-generating-lidar-world-models-with-deformable-mamba.md) GEM, 2026 | LiDAR sweep tokens + dynamic/static separator | LiDAR tokenizer + deformable Mamba + optional planner/BEV layout controller | 2026 最新 LiDAR-native world model 之一，可做 what-if rollout | 仍需看代码、复现成本和真实闭环价值 |
| 单阶段多模态生成 | [`SRC-robotics-217`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-217-unidrivedreamer-unified-latent-anchoring-for-multimodal-driving-world-models.md) UniDriveDreamer, 2026 | LiDAR VAE + video VAE | Unified Latent Anchoring 对齐 LiDAR/video latent，DiT 联合建模 | 当前 camera-LiDAR 统一生成路线的重要参考 | 训练成本高，数据清洗/同步是瓶颈 |

## 技术路线拆解

### 1. LiDAR-native generative world model

代表论文：Copilot4D、LidarDM、LiSTAR、GEM。

这条路线尽量保留 LiDAR 的原始几何：点云、range image、ray、spherical/cylindrical 表示或 LiDAR sweep token。训练目标通常是重建、预测或条件生成未来 LiDAR sequence。它适合做：

- 自动驾驶感知模型的数据增强。
- 稀有场景、动态障碍、what-if rollout 的传感器级仿真。
- 传感器规格、安装位姿、扫描模式变化下的鲁棒性测试。

工程难点是点云无序、稀疏、距离分布极不均匀，且动态对象和静态背景混在一起。GEM 的 dynamic/static separator 与 LiSTAR 的 ray-centric modeling 都是在处理这个痛点。

### 2. Occupancy/BEV world model

代表论文：OccWorld、OccSora、BEVWorld、Drive-OccWorld、DFIT-OccWorld、OccLLaMA、HERMES++。

这条路线把 LiDAR 作为几何监督或输入之一，先构建 3D/4D occupancy、semantic occupancy、BEV latent 或 voxel flow，再训练未来预测/生成模型。优点是和规划、碰撞、安全边界天然对齐：

- occupancy 可直接计算碰撞成本和 freespace。
- semantic occupancy 比 3D box 更细，能表示路沿、障碍物形状、非 box 物体和可通行空间。
- BEV/occupancy 比原始点云更适合和 map、trajectory、command、language token 对齐。

如果要做自动驾驶 planning-oriented world model，这条路线优先级最高。

### 3. Camera-LiDAR unified latent

代表论文：MUVO、BEVWorld、UniDriveDreamer。

多模态世界模型的核心不是简单 concat，而是找到共同空间：

- MUVO 用 spatial voxel representation 做 sensor-agnostic geometry。
- BEVWorld 把多模态 sensor 输入 tokenize 到统一 BEV latent，并可解码回 LiDAR 和 image。
- UniDriveDreamer 用 LiDAR-specific VAE 与 video VAE，再通过 Unified Latent Anchoring 对齐 latent distribution。

这条路线适合物理 AI 仿真平台，但对数据工程要求最高：时间同步、外参标定、rolling shutter、LiDAR motion compensation、camera-LiDAR occlusion 和坐标系一致性都会影响训练。

### 4. JEPA/latent predictive world model

代表论文：AD-L-JEPA、AD-LiST-JEPA；相关概念见 [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]]。

JEPA 不直接生成点云或图像，而是预测 latent representation。它适合两类需求：

- 用海量未标注 LiDAR 数据做 encoder 预训练，再迁移到检测、occupancy completion、forecasting。
- 在算力或标注不足时，先证明 LiDAR latent 是否学到可迁移空间结构。

边界是：JEPA 表征好不等于可以闭环规划。要进入真实控制链路，仍需和 action-conditioned prediction、planning cost、rollout evaluation 绑定。

### 5. 机器人移动导航路线

代表论文：Sense, Imagine, Act；World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations。

这条路线更接近具身智能和移动机器人：LiDAR 不是为了合成传感器视频，而是作为 observation 进入 Dreamer/DreamerV3 类 world model，学习 latent dynamics 并通过 imagination 训练策略。适合用 TurtleBot3、F1TENTH、Gazebo/Isaac Sim 做小规模可复现实验。

## 推荐工程方案

### 方案 A：自动驾驶 occupancy world model MVP

目标：用 LiDAR 参与构建 occupancy/BEV state，训练短时未来预测，并验证规划/感知收益。

1. **数据集：** 从 nuScenes 起步；需要 occupancy 标签时用 Occ3D 或 nuScenes-Occupancy；点云预测可补 KITTI Odometry、Argoverse2。
2. **数据结构：** `history sweeps + ego pose + calibration + future ego trajectory/action + occupancy/flow labels`。
3. **表示：** 先做 BEV voxel/occupancy，不要一开始做 raw point cloud generative model。
4. **模型：** VQ-VAE/tokenizer 或 sparse voxel encoder；时序模型用 Transformer/DiT；条件输入用 future trajectory、steering、velocity 或 high-level command。
5. **训练目标：** occupancy BCE/focal loss、semantic CE、flow regression、temporal consistency、ego trajectory prediction；可加 LiDAR ray consistency。
6. **评估：** occupancy IoU/mIoU、future forecasting IoU、flow error、collision rate、trajectory L2、下游 detector 或 motion prediction uplift。

适合先复现：OccWorld -> Drive-OccWorld -> DFIT-OccWorld。

### 方案 B：LiDAR-native 传感器仿真/数据增强

目标：生成可控 LiDAR sequence，用于感知模型训练、稀有场景测试和 what-if 仿真。

1. **表示选择：** range image/ray-centric/HCS 优先于粗糙 Cartesian voxel，减少量化损失。
2. **Tokenizer：** LiDAR VAE/VQ-VAE，把一帧或多帧 sweep 压成 compact tokens。
3. **动态建模：** 显式区分 static background 和 dynamic actors；使用 object layout、BEV layout 或 trajectory prompt 条件生成。
4. **生成模型：** 离散扩散、latent diffusion、Mamba 或 ray-centric Transformer。
5. **评估：** Chamfer Distance、F-score、MMD、range L1、temporal coherence、layout consistency，以及 downstream detector mAP。

适合先复现：Copilot4D -> LidarDM -> LiSTAR/GEM。

### 方案 C：Camera-LiDAR 多模态世界模型

目标：同一个 world model 生成未来多相机视频和 LiDAR，供仿真、感知训练、规划评测使用。

1. **数据清洗优先级：** timestamp sync、camera-LiDAR extrinsic、ego-motion compensation、coordinate frame canonicalization。
2. **双 encoder：** video VAE + LiDAR VAE，或统一 BEV/voxel latent tokenizer。
3. **对齐机制：** cross-modal contrastive loss、Unified Latent Anchoring、ray-casting reconstruction、camera depth / LiDAR projection consistency。
4. **条件输入：** HD map、route、ego trajectory、object/layout boxes、language command。
5. **生成模型：** diffusion transformer 或 autoregressive transformer 统一建模时间演化。
6. **评估：** 单模态真实度之外，必须测 camera-LiDAR 几何一致性、遮挡一致性、未来动态一致性和下游任务收益。

适合先读：MUVO -> BEVWorld -> UniDriveDreamer。

### 方案 D：移动机器人 LiDAR world model

目标：让移动机器人从 2D/3D LiDAR observation 中学习 latent dynamics，用于导航、避障和策略优化。

1. **仿真起步：** TurtleBot3、F1TENTH、Gazebo、Isaac Sim 或 ManiSkill mobile base。
2. **Observation：** LiDAR scan/range vector、RGB/depth optional、odom、goal、action。
3. **模型：** MLP-VAE 或 1D/2D encoder 压缩 LiDAR；DreamerV3/RSSM 预测 latent dynamics。
4. **训练：** model-based RL 用 imagined rollouts 训练 actor-critic。
5. **评估：** success rate、collision rate、path efficiency、unseen maps zero-shot、dynamic obstacle robustness。

适合先复现：Sense, Imagine, Act -> World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations。

## 数据 schema 草案

```yaml
episode_id: str
platform: car | mobile_robot | humanoid | manipulator
calibration:
  lidar_to_ego: matrix4x4
  camera_to_ego: matrix4x4
  intrinsics: dict
frames:
  - timestamp_ns: int
    ego_pose_world: matrix4x4
    action:
      velocity: float
      steering: float
      trajectory: optional[list[x, y, yaw]]
      robot_cmd: optional[list[float]]
    lidar:
      sweep_path: raw/...
      range_image_path: optional
      point_count: int
      motion_compensated: bool
    cameras:
      front: raw/...
      ...
    derived:
      bev_feature_path: optional
      occupancy_path: optional
      semantic_occupancy_path: optional
      flow_path: optional
    quality_flags:
      synced: bool
      calibration_ok: bool
      rain_fog_dust: optional[str]
      occlusion_level: optional[str]
```

## 中国/产业启发

- 对自动驾驶与机器人公司，LiDAR 数据的商业价值不在“点云文件很大”，而在**标定、同步、动作条件、场景标签、失败/接管、可训练 schema 和评测闭环**。
- 对中国 LiDAR/感知供应链，世界模型路线会提高“传感器数据资产化”需求：不同线数、FOV、扫描模式、安装位置的数据，需要能转成 occupancy/BEV/ray token 并和 camera、map、trajectory 对齐。
- 对具身数据平台，LiDAR 适合做空间 QA、导航、移动操作和弱纹理/遮挡环境补强；但对近距离灵巧操作，触觉、腕部相机、深度相机和力控数据未必比 LiDAR 次要。
- 对个人学习/作品集，最有迁移价值的是：sensor calibration、ROS bag/MCAP 数据管线、LiDAR tokenization、occupancy forecasting、world model evaluation service，而不是单纯复现一个大生成模型 demo。

## 下一步可做

- 选一个目标域：自动驾驶、移动机器人导航、还是机器人数据平台。
- 代码复现优先级：OccWorld/Drive-OccWorld、Copilot4D/LidarDM、AD-L-JEPA/AD-LiST-JEPA、UniDriveDreamer。
- 若继续沉淀，可为每篇重点论文建立 `knowledge/_sources/` source card，并把 arXiv PDF/项目页抽取到 `raw/robotics-embodied-ai/documents/`。

## 关联连接

- [[_entities/LiDAR|LiDAR 激光雷达]]
- [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]]
- [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]]
