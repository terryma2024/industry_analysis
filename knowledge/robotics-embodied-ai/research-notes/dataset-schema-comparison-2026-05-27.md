---
title: 具身智能数据集 Schema 横向比较
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-note
  - dataset-schema
  - training-data
aliases:
  - 机器人数据集 Schema 比较 2026-05-27
  - Dataset Schema Comparison 2026-05-27
---

# 具身智能数据集 Schema 横向比较

> [!summary]
> 横向看 Open X-Embodiment、DROID、RoboMIND、AgiBot World 和 LeRobot，事实标准正在收敛到“episode/frame 轨迹 + 多模态 observation + robot-specific action + language/task + metadata manifest + 可训练导出格式”。RLDS 仍是 OXE/DROID 的研究标准；LeRobot 的 Parquet + MP4 + metadata 更像工程交付和平台互通标准。

机器可读横向表：[`robotics_dataset_schema_comparison.csv`](../../../raw/robotics-embodied-ai/data/robotics_dataset_schema_comparison.csv)

## 资料范围

| 数据集/格式 | 主要来源 | 本地证据 |
|---|---|---|
| Open X-Embodiment | 官方 GitHub、项目页、论文 | [`SRC-robotics-054`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-054-open-x-embodiment-robotic-learning-datasets-and-rt-x-models.md) |
| DROID | 官方 Docs、GitHub、论文 | [`SRC-robotics-055`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md) |
| RoboMIND | 项目页、HF dataset card、GitHub HDF5 docs、论文 | [`SRC-robotics-057`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-057-robomind-benchmark-on-multi-embodiment-intelligence-normative-data-for-robot-man.md) |
| AgiBot World | HF/ModelScope README、Colosseo/GO-1 论文 | [`SRC-robotics-044`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md), [`SRC-robotics-058`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md) |
| LeRobot | Hugging Face GitHub、LeRobotDataset v3 docs | [`SRC-robotics-052`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md), [`SRC-robotics-053`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md) |

## 横向对比

| 维度 | Open X-Embodiment | DROID | RoboMIND | AgiBot World 2026 | LeRobot v3 |
|---|---|---|---|---|---|
| 核心定位 | 跨本体聚合数据集 | 单一标准硬件的真实场景分布式采集 | 中国多本体操作数据集 | 企业级长时程双臂/人形数据平台 | 开源格式与训练工具链 |
| 主格式 | RLDS / TFRecord / TFDS | RLDS + raw HDF5/MP4/SVO | HDF5 | LeRobot-compatible Parquet/MP4/JSONL | Parquet + MP4/images + metadata |
| observation | 多源传感器字典，RT-X 训练取 canonical RGB + task string | gripper/cartesian/joint state + 3 路 RGB | RGB/depth + joint/end-effector 等，随本体变化 | observation.state + observation.images.*，支持多相机/深度/鱼眼/手眼 | observation.state + observation.images.* |
| action | 原始动作保留；训练时粗对齐到 7D EE + gripper | 7D action；另有 action_dict 多种控制空间 | puppet/master 组，joint/end-effector，按本体配置 | action 向量由 field_descriptions 解释 | action tensor，语义由 features 声明 |
| language/task | instruction/task string，覆盖不均 | 最多 3 条 language_instruction | task CSV + frame-level language annotation | tasks.jsonl + subtask/skill/instruction_segments | tasks.jsonl + task_index |
| episode metadata | RLDS episode/step flags + dataset spreadsheet | episode_metadata + raw metadata_*.json | 目录层级 + HDF5 文件 + task/failure 资料 | episodes.jsonl + info.json + optional annotations.json | meta/info.json + stats + episodes + tasks |
| embodiment metadata | 22 本体，更多是 dataset-level | 固定 Franka Panda 平台 | robomind.yaml 映射 camera/action/state/color order | G2 平台、模块化夹爪/灵巧手/触觉，论文级描述 | robot_type + feature schema，机器人细节需扩展 |
| 视频/相机 | RLDS 图像张量，源数据差异大 | RLDS 180x320；raw MP4/SVO | HDF5 object image datasets | 每相机每 episode 一个 MP4 | 多 episode 拼接为 MP4 shards |
| 频率 | 源数据差异；RT-X 3-10 Hz | 15 Hz 控制 | 公开文档未统一；仿真 state 约 4x camera | 论文披露 30 Hz | 每 dataset 在 info.json 声明 fps |
| 许可/下载 | code Apache-2.0，materials CC-BY；GCS/TFDS | CC-BY 4.0；GCS 1.7TB RLDS / raw 5.6-8.7TB | HF card Apache-2.0，但 gated | CC BY-NC-SA 4.0；HF/ModelScope/git-lfs | code Apache-2.0；数据集各自许可 |

## 识别出的事实标准

1. **Episode/frame 是最小组织骨架**  
   所有路线都围绕 episode/trajectory 展开；每个 frame/step 绑定 observation、action、timestamp/index 和 task/instruction。国内平台应避免只交付视频或只交付 HDF5，必须保留 episode 边界和 frame 对齐。

2. **Observation 是多模态字典，不是单一路 RGB**  
   OXE 接受源数据差异，DROID 固定三路相机，RoboMIND/AgiBot 走多相机 + 本体状态，LeRobot 用 `observation.images.*` 和 `observation.state` 抽象。事实标准是“图像通道可扩展、低维状态可解释、字段有 dtype/shape/单位”。

3. **Action 需要同时保留 raw control 与 canonical action**  
   OXE 的 7D end-effector + gripper 是跨本体训练的粗对齐标准，但 DROID/RoboMIND/AgiBot 都保留更丰富的 robot-specific action。国内平台建议同时保存：`action.raw.*`、`action.ee_delta_7d`、`action.joint_position/velocity`、`action.gripper`，并记录控制模式和坐标系。

4. **LeRobot 正在成为工程互通格式，RLDS 仍是研究生态资产**  
   OXE/DROID 延续 RLDS；AgiBot World 2026 已直接采用 LeRobot-compatible 结构并提供 split 脚本；LeRobot v3 用 Parquet/MP4/metadata 解决大规模文件数、流式读取和 PyTorch 训练接入问题。国内平台最好默认导出 LeRobot v3，并保留 RLDS exporter。

5. **长时程与失败/接管标注正在变成高价值字段**  
   DROID 记录成功/失败但主要用成功数据，RoboMIND 强调 5k failure demonstrations，AgiBot 把 Error/Success/Intervention/Task Frame、2D bbox、instruction segments 放进 metadata。下一阶段稀缺资产不是“更多正常轨迹”，而是可解释的失败、恢复、接管和分段技能。

## 对国内数据平台的 Schema 建议

### 第一层：原始保真层

保留采集现场的完整信息，服务审计、重处理和客户交付复盘。

| 模块 | 必备字段 |
|---|---|
| `episode` | `episode_id`, `task_id`, `scenario_id`, `operator_id_hash`, `robot_id`, `start_time`, `duration`, `success`, `failure_reason`, `intervention_count`, `license_id`, `consent_scope` |
| `timebase` | `timestamp_ns`, `frame_index`, `sensor_timestamp_ns`, `sync_status`, `dropped_frame_count`, `clock_source` |
| `robot` | `robot_type`, `serial_hash`, `urdf_hash`, `end_effector_type`, `control_mode`, `joint_names`, `joint_limits`, `firmware_version`, `calibration_version` |
| `sensors` | `camera_id`, `intrinsics`, `extrinsics`, `resolution`, `fps`, `codec`, `color_order`, `depth_unit`, `tactile_unit`, `force_torque_frame` |
| `raw_action` | robot-native joint/Cartesian/base/gripper command, controller output, teleop input, coordinate frame |
| `quality` | missing frames, action bounds, time drift, camera occlusion, human face/privacy flag, reviewer decision |

### 第二层：训练互通层

默认导出 LeRobot v3，补充 RLDS 和客户自定义格式。

| 字段 | 建议 |
|---|---|
| `observation.images.<camera>` | MP4 shards；每个 camera 有 fps/codec/shape/intrinsics/extrinsics |
| `observation.state` | 扁平向量 + `field_descriptions`，每一段给 `indices`, `dims`, `unit`, `coordinate_frame` |
| `observation.depth.*` / `observation.tactile.*` / `observation.force_torque` | 不要塞进黑盒 state；应作为可选命名模态 |
| `action` | 训练默认 action；同时在 metadata 记录从 raw_action 的转换函数版本 |
| `task_index` / `tasks.jsonl` | 高层任务文本、场景、对象、技能 taxonomy、中文/英文双语描述 |
| `instruction_segments` | 长时程任务分段，包含 `skill`, `instruction`, `start_frame_index`, `end_frame_index`, `success_frame_index` |
| `key_frame` | Error/Success/Intervention/Task/Object bbox 等关键帧 |
| `meta/stats.json` | mean/std/min/max/p01/p99，按 robot_type 和 task_id 也要能分组 |

### 第三层：商业交付层

国内 ToB 数据服务不要只卖“数据量”，要交付可验收资产包。

- **标准交付物**：LeRobot v3 数据包、RLDS exporter、schema 文档、字段单位表、相机标定包、URDF/本体配置、数据质检报告、样例训练脚本、baseline checkpoint。
- **质检指标**：episode 完整率、视频/状态同步误差、动作越界率、失败/恢复标签覆盖率、任务分布、对象分布、场景分布、重复轨迹率、隐私处理状态。
- **客户验收**：至少提供 3 个 baseline：BC/ACT 或 Diffusion Policy 单任务、VLA 微调、多任务 holdout；用训练结果反向证明数据不是“能打开”，而是“能训练”。
- **合规字段**：场地授权、人物隐私处理、数据使用范围、是否可商用训练、是否可再分发、是否允许合成扩增、数据删除/撤回机制。

## 待验证项

- Open X-Embodiment 每个子数据集的具体 license、fps、camera calibration 和 robot metadata 需要逐项查官方 spreadsheet 或源数据集。
- RoboMIND v2.0 ModelScope 的正式 schema、失败标签文件结构、真实世界采集 fps、gated terms 需要登录/下载后核验。
- AgiBot World 2026 的公开 HF 样本规模与 Colosseo 论文中 1M+ trajectories 的关系需要继续拆分：哪些是完整开放、哪些是样例、哪些是 ModelScope 托管。
- LeRobot v3 仍在快速迭代，`tasks.jsonl`/`tasks.parquet`、episodes metadata 的具体文件名和版本兼容策略需要随 `lerobot >= 0.4.0` 稳定版复核。

## 来源 URL

- Open X-Embodiment GitHub: https://github.com/google-deepmind/open_x_embodiment
- Open X-Embodiment project: https://robotics-transformer-x.github.io/
- Open X-Embodiment paper: https://arxiv.org/abs/2310.08864
- DROID docs: https://droid-dataset.github.io/droid/the-droid-dataset
- DROID GitHub: https://github.com/droid-dataset/droid
- DROID paper: https://arxiv.org/abs/2403.12945
- RoboMIND project: https://x-humanoid-robomind.github.io/
- RoboMIND Hugging Face: https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND
- RoboMIND GitHub: https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io
- RoboMIND paper: https://arxiv.org/abs/2412.13877
- AgiBot World 2026 Hugging Face: https://huggingface.co/datasets/agibot-world/AgiBotWorld2026
- AgiBot World 2026 ModelScope: https://modelscope.cn/datasets/agibot_world/AgiBotWorld2026
- AgiBot World Colosseo paper: https://arxiv.org/abs/2503.06669
- AgiBot GO-1 PDF: https://agibot-world.com/blog/agibot_go1.pdf
- LeRobot GitHub: https://github.com/huggingface/lerobot
- LeRobotDataset v3 docs: https://github.com/huggingface/lerobot/blob/main/docs/source/lerobot-dataset-v3.mdx
