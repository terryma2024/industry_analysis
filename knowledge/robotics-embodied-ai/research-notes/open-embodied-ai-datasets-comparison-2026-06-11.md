---
title: 开源具身智能训练与评估数据集横向调研
type: synthesis
date_created: 2026-06-11
last_updated: 2026-06-11
sources:
  - raw/robotics-embodied-ai/data/open_embodied_ai_datasets_comparison_2026-06-11.csv
  - raw/robotics-embodied-ai/data/robotics_dataset_schema_comparison.csv
  - raw/robotics-embodied-ai/data/training_data_papers.csv
  - raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-054-open-x-embodiment-robotic-learning-datasets-and-rt-x-models.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-055-droid-a-large-scale-in-the-wild-robot-manipulation-dataset.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-057-robomind-benchmark-on-multi-embodiment-intelligence-normative-data-for-robot-man.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-058-agibot-world-colosseo-a-large-scale-manipulation-platform-for-scalable-and-intel.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-059-robotwin-dual-arm-robot-benchmark-with-generative-digital-twins.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-077-mobile-aloha-learning-bimanual-mobile-manipulation-with-low-cost-whole-body-tele.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-080-learning-fine-grained-bimanual-manipulation-with-low-cost-hardware.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-119-libero-documentation.md
  - https://arxiv.org/abs/2308.12952
  - https://arxiv.org/abs/2307.00595
  - https://arxiv.org/abs/2410.00425
  - https://arxiv.org/abs/2406.02523
  - https://arxiv.org/abs/2506.18088
  - https://arxiv.org/abs/2112.03227
  - https://arxiv.org/abs/1909.12271
  - https://arxiv.org/abs/1910.10897
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - robot-learning
  - dataset
  - benchmark
  - vla
status: active
aliases:
  - 开源具身智能数据集对比
  - Embodied AI Dataset Comparison
---

# 开源具身智能训练与评估数据集横向调研

> [!summary]
> 快速理解：**没有一个数据集同时适合所有具身智能模型训练和评估**。大模型预训练看 [[#1. 预训练/跨本体混合]]，真机微调看 [[#2. 真实机器人微调/后训练]]，长时程/双臂/触觉看 [[#3. 特定能力数据集]]，仿真评测看 [[#4. 仿真与评估 benchmark]]。格式上，研究生态仍以 **RLDS/OXE** 为主，工程互通正在向 **LeRobot v3: Parquet + MP4 + metadata** 收敛；老牌仿真 benchmark 则多用各自环境格式。

机器可读表：[open_embodied_ai_datasets_comparison_2026-06-11.csv](../../../raw/robotics-embodied-ai/data/open_embodied_ai_datasets_comparison_2026-06-11.csv)

## 先给结论

如果只想快速选型：

| 目标 | 优先看 | 原因 |
|---|---|---|
| 训练/理解通用 VLA 预训练数据 | Open X-Embodiment, LeRobot ecosystem, AgiBot World | OXE 是 RT-X/Octo/OpenVLA 代表性混合；LeRobot 是工程格式；AgiBot 是中国大规模真实机器人数据平台信号 |
| 微调 OpenVLA/类似 VLA | BridgeData V2, DROID, 自有 LeRobot/RLDS 数据 | OpenVLA 原生支持 RLDS/OXE，示例明确使用 BridgeData V2；DROID 已被 OpenPI 等新栈接入 |
| 微调 OpenPI / pi0 系列 | LeRobot 格式, LIBERO 示例, DROID | OpenPI 文档把“转成 LeRobot 数据集”作为自有数据微调入口，并提供 DROID/LIBERO 示例 |
| 做中国具身数据平台 | AgiBot World, RoboMIND, DROID, LeRobot v3 | 这四个最能启发生产级 schema：多相机、状态/动作、任务、失败、元数据、质检 |
| 研究失败/接管/纠错 | RoboMIND, AgiBot World, Oopsie/LeRobot HIL 线索 | 普通成功示教不够，失败原因、接管点、恢复动作才是部署闭环资产 |
| 研究双臂/移动操作 | ALOHA/Mobile ALOHA, RoboTwin 2.0, RoboMIND 2.0, AgiBot | 覆盖真实低成本双臂、仿真双臂生成、多本体双臂和企业级双臂/人形 |
| 快速跑仿真评测 | LIBERO, ManiSkill3, RoboCasa, CALVIN, RLBench, Meta-World | 各自测试不同能力：VLA/终身学习、GPU 并行 RL、厨房长时程、语言条件、经典多任务/元学习 |

## 快速地图

### 1. 预训练/跨本体混合

| 数据集 | 格式 | 适合任务 | 完整度 | 主要注意 |
|---|---|---|---|---|
| Open X-Embodiment / OXE | RLDS / TFDS / TFRecord | 跨本体 VLA/RT-X/Octo/OpenVLA 预训练和混合训练 | 广度高，字段一致性中等 | 每个子数据集 license、fps、相机、动作空间不同；商用前必须逐项核查 |
| LeRobot ecosystem | LeRobot v3: Parquet + MP4/images + metadata | PyTorch 训练、Hub streaming、数据互通、低成本硬件数据采集 | 工程完整度高 | 它是格式/工具链，不是单一数据集；每个 HF dataset 许可不同 |
| AgiBot World / AgiBot World 2026 | LeRobot-compatible + 扩展 metadata | 长时程、多相机、真实场景、企业级 VLA 数据 | 很高，但公开全集边界待核 | 数据许可非商用；公开子集、论文 1M+ 规模和实际可下载内容要分清 |

**判断**：预训练不只是“数据越多越好”。OXE 的价值是跨本体广度，AgiBot 的价值是长时程和生产级 annotation，LeRobot 的价值是让数据真的能被现代训练栈加载。

### 2. 真实机器人微调/后训练

| 数据集 | 格式 | 适合任务 | 完整度 | 主要注意 |
|---|---|---|---|---|
| DROID | RLDS + raw HDF5/MP4/SVO | in-the-wild tabletop manipulation、VLA 微调、真实泛化 | 高 | 固定 Franka 平台，不是多本体；下载体量大 |
| BridgeData V2 | RLDS/TFDS | OpenVLA fine-tune、WidowX/低成本机械臂、goal/language-conditioned manipulation | 中高 | OXE 内版本可能旧；OpenVLA 建议使用官方 BridgeData V2 |
| RoboMIND | HDF5 + 多本体配置 | 中国多本体操作、失败数据、VLA/IL benchmark | 高，但访问 gated | 需要下载核验 v2.0 schema、失败标签和许可 |
| Galaxea Open-World Dataset | 待验证 | 单一本体真实生活/工作环境、subtask language、G0 训练/评估 | 潜力高，公开细节待核 | 需要补项目页、下载方式、schema、license |

**判断**：如果目标是快速把 VLA 跑起来，BridgeData V2 和 DROID 比 OXE 更“可落地”；如果目标是设计中国数据平台，DROID 的固定硬件采集 SOP 和 RoboMIND/AgiBot 的多本体/失败/分段标注更值得拆。

### 3. 特定能力数据集

| 能力 | 数据集 | 格式 | 适合任务 | 主要注意 |
|---|---|---|---|---|
| 双臂/移动操作 | ALOHA / Mobile ALOHA | HDF5 episodes | ACT、BC、Diffusion Policy、低成本双臂/mobile manipulation | 任务数量少但示教质量高；硬件绑定强 |
| 双臂仿真生成 | RoboTwin / RoboTwin 2.0 | RoboTwin simulator/dataset | 双臂 VLA、sim-to-real、合成预训练 + 少量真机 | 生成任务有效性和真实迁移要逐任务验证 |
| 接触/力觉/音频 | RH20T | 待验证 | one-shot imitation、contact-rich manipulation、多模态学习 | 与现代 VLA/LeRobot/RLDS 训练栈的适配需要额外工程 |
| 人类手持示教 | UMI community datasets | Zarr，常可转 LeRobot | 快速收集人类 manipulation demos、Diffusion Policy | retargeting、pose/calibration、任务元数据是瓶颈 |
| 少量示教扩增 | MimicGen | robosuite/MimicGen | 用少量 human demos 生成大量仿真示教 | 是数据生成系统，不是泛化能力最终评测 |

**判断**：这些不是“通用预训练数据集”，而是能力补丁。要做双臂就看 ALOHA/RoboTwin；要做接触就看 RH20T；要低成本采集就看 UMI；要从少量 demo 放大仿真数据就看 MimicGen。

### 4. 仿真与评估 benchmark

| Benchmark | 格式/环境 | 主要测试 | 完整度 | 主要注意 |
|---|---|---|---|---|
| LIBERO | LIBERO env/dataset；OpenVLA 有 RLDS 转换示例 | lifelong learning、VLA/IL、知识迁移 | 高 | 标准分数容易高估泛化；要加扰动评测 |
| ManiSkill3 | SAPIEN/ManiSkill GPU simulation | RL/IL、接触丰富任务、点云/体素、GPU 并行 | 高 | 语言条件和真实世界结论取决于任务设计 |
| RoboCasa | robosuite/RoboCasa | 厨房/家庭长时程、资产/场景多样性、合成数据 | 高 | 场景偏厨房，真实迁移需额外验证 |
| CALVIN | CALVIN dataset/env | language-conditioned long-horizon manipulation | 中高 | 经典但近年 benchmark 审计提醒不能只看固定分数 |
| RLBench | CoppeliaSim/RLBench | 100 个经典视觉操作任务、few-shot/multitask | 中高 | 老牌 benchmark，VLA 适配要额外处理语言/格式 |
| Meta-World | MuJoCo/Gym style | 50 个多任务/元 RL 操作任务 | 中 | 偏状态控制算法调试，不适合作为现代 VLA 数据集 |

**判断**：评估层不要只用一个 benchmark。最低组合可以是 `LIBERO + ManiSkill3 + 一个真实小任务 rollout`；如果做家庭/厨房，加 RoboCasa；如果做双臂，加 RoboTwin；如果做语言长时程，加 CALVIN。

## 关键差异维度

### 格式差异

| 格式 | 代表 | 优点 | 缺点 | 适合谁 |
|---|---|---|---|---|
| RLDS / TFDS / TFRecord | OXE, DROID, BridgeData V2, OpenVLA workflows | 学术/VLA 预训练生态成熟，episode/step 结构清楚 | TensorFlow/TFDS 心智负担高；子数据集字段不统一 | 做 OpenVLA/OXE/RT-X 复现 |
| LeRobot v3 | LeRobot datasets, AgiBot-compatible release | Parquet + MP4 + metadata，PyTorch 友好，HF Hub streaming | 仍在快速迭代；工业级本体/标定/权限字段需扩展 | 做工程平台、数据交付、个人作品集 |
| HDF5 | RoboMIND, ALOHA, many IL datasets | 简单、单文件/轨迹结构直观、科研常用 | 大规模 streaming、跨数据集合并和 Hub 展示不如 LeRobot/RLDS | 做离线 IL/ACT/Diffusion Policy |
| Zarr | UMI/Diffusion Policy style | chunked/compressed，适合大数组和并行访问 | 社区数据规范不如 LeRobot/OXE 统一 | 做 UMI-like 采集和高性能本地训练 |
| 仿真环境原生格式 | ManiSkill, RoboCasa, RLBench, Meta-World, CALVIN | 能生成新数据和在线评测 | 不是天然跨平台训练数据格式 | 做 RL/IL benchmark 和合成数据 |

### 任务完整度差异

我用“任务完整度”指一个数据集是否足以支撑可复现训练/评估，而不是论文里有多少条轨迹。

| 维度 | 低完整度表现 | 高完整度表现 | 最值得参考的数据集 |
|---|---|---|---|
| episode 边界 | 只有视频或散帧 | 每条 episode 有 start/end、timestamp、success/failure | LeRobot, DROID, AgiBot |
| observation | 只有单路 RGB | 多相机 + state + 深度/力/触觉可选 + 标定 | DROID, RoboMIND, AgiBot, RH20T |
| action | 只给离散标签或缺少控制模式 | robot-native action + canonical action + 坐标/单位 | DROID, OXE, LeRobot schema |
| language/task | 无任务文本或只有文件夹名 | task text、subtask、skill、instruction segment | AgiBot, Galaxea, LIBERO, CALVIN |
| embodiment metadata | 只知道机器人名字 | robot_type、joint names、URDF/calibration/control mode | DROID 做得清楚；LeRobot/自建平台需补充 |
| failure/intervention | 只保留成功 | failure cause、intervention frame、recovery/outcome | RoboMIND, AgiBot, Oopsie/HIL 线索 |
| evaluation protocol | 只给训练集 | heldout task/env/object、seed、success metric、脚本 | LIBERO, ManiSkill, RoboCasa, CALVIN |

## 与开源模型/算法的适配

| 模型/算法栈 | 最顺的数据集 | 格式偏好 | 说明 |
|---|---|---|---|
| OpenVLA | OXE, BridgeData V2, LIBERO, 自定义 RLDS | RLDS | 官方代码原生支持 OXE/RLDS mixture；自定义数据推荐转 RLDS |
| OpenPI / pi0 | LeRobot, DROID, LIBERO example | LeRobot | 官方微调路径强调先把自有数据转 LeRobot dataset |
| Octo / RT-X | OXE mixture | RLDS | 典型跨本体预训练路线 |
| ACT | ALOHA/Mobile ALOHA, LeRobot-converted datasets | HDF5 或 LeRobot | 适合动作 chunk、双臂和低成本硬件示教 |
| Diffusion Policy | UMI/Zarr, ALOHA, robomimic/MimicGen | Zarr/HDF5 | 对连续动作、多模态动作分布很友好 |
| RL / offline RL | ManiSkill3, Meta-World, RLBench, BridgeData V2 | 环境原生/RLDS | 需要 reward、reset、online rollout 或离线 reward 信息 |
| VLA 评估 | LIBERO, DROID/Bridge real eval, RoboCasa/RoboTwin/ManiSkill | 各自 adapter | 重点是 adapter 和评测协议，而不是单一格式 |

## 推荐学习顺序

### 1 周快速理解版

1. 读 [[research-notes/lerobot-beginner-guide-2026-05-28|LeRobot 初学者教学]]，理解 episode、observation、action、task。
2. 读 [[research-notes/dataset-schema-comparison-2026-05-27|具身智能数据集 Schema 横向比较]]，看 OXE/DROID/RoboMIND/AgiBot/LeRobot 的字段差异。
3. 用本页表格建立“数据集不是一个东西”的心智：真实数据、仿真 benchmark、生成器、格式标准是四类对象。
4. 选一个最小实验：LIBERO 或 LeRobot 小数据集，跑一次 BC/ACT/VLA fine-tune/eval。

### 面向平台工程作品集

做一个 `robot-dataset-inspector`，功能比“训练一个模型”更贴近平台工程：

- 加载 LeRobot/RLDS/HDF5/Zarr 四类样例。
- 自动输出数据体检表：episode 数、任务分布、action 维度、camera 数、fps、缺帧、静止动作占比、success/failure 比例。
- 支持把 ALOHA/HDF5 或 UMI/Zarr 转成 LeRobot v3。
- 支持把 LIBERO 评测结果、失败视频和 success matrix 做成 dashboard。

这个作品能证明你理解的是数据闭环，不只是会调用训练脚本。

## 对中国具身智能数据平台的启发

中国数据平台不能只追求“大”。真正有价值的数据集要满足五件事：

- **能训练**：字段可被 LeRobot/RLDS/OpenVLA/OpenPI/ACT/Diffusion Policy 直接加载。
- **能复现**：版本、seed、任务切分、baseline、评测脚本齐全。
- **能追责**：每条 episode 有采集人/设备/场景/许可/质检/隐私处理记录。
- **能解释失败**：失败、接管、恢复、重试和最终 outcome 被结构化记录。
- **能迁移**：同时保留 robot-native action 和 canonical action，避免只服务单一机器人。

短期最值得对标的不是单个数据集，而是三种模式：

| 模式 | 代表 | 中国团队可学什么 |
|---|---|---|
| 固定硬件分布式采集 | DROID | 统一硬件包、采集 SOP、raw + training-ready 双发布 |
| 大规模企业数据工厂 | AgiBot World | 长时程任务、分段指令、质检、人机协同验证、LeRobot-compatible 交付 |
| 开源格式和工具链 | LeRobot | 把数据从“私有脚本可读”变成“社区工具可加载、可训练、可可视化” |

## 待验证

- BridgeData V2、RH20T、Galaxea Open-World 的当前下载入口、license 和完整 schema 需要后续抓取 raw artifact。
- AgiBot World 论文 1M+ trajectories 与 HF/ModelScope 当前开放内容的对应关系需要按文件级别核验。
- RoboMIND 2.0 的公开状态、下载格式、许可和 v1/v2 schema 差异需要继续确认。
- LeRobot v3 在 `lerobot >= 0.4.0` 稳定后，metadata 文件名和 converter 行为需要复核。
- 对求职/作品集最有价值的下一步不是继续读论文，而是下载 2-3 个小样例做 dataset inspector。

## 来源 URL

- Open X-Embodiment: https://arxiv.org/abs/2310.08864
- DROID: https://arxiv.org/abs/2403.12945
- BridgeData V2: https://arxiv.org/abs/2308.12952
- RoboMIND: https://arxiv.org/abs/2412.13877
- AgiBot World: https://arxiv.org/abs/2503.06669
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/lerobot-dataset-v3
- OpenVLA GitHub: https://github.com/openvla/openvla
- OpenPI GitHub: https://github.com/Physical-Intelligence/openpi
- RH20T: https://arxiv.org/abs/2307.00595
- ManiSkill3: https://arxiv.org/abs/2410.00425
- RoboCasa: https://arxiv.org/abs/2406.02523
- RoboTwin 2.0: https://arxiv.org/abs/2506.18088
- CALVIN: https://arxiv.org/abs/2112.03227
- RLBench: https://arxiv.org/abs/1909.12271
- Meta-World: https://arxiv.org/abs/1910.10897

## 关联连接

- [[../09-training-data-deep-dive|机器人训练数据深度调研]]
- [[dataset-schema-comparison-2026-05-27|具身智能数据集 Schema 横向比较]]
- [[lerobot-beginner-guide-2026-05-28|LeRobot 初学者教学]]
- [[libero-lifelong-robot-learning-platform-2026-06-11|LIBERO 终身学习仿真平台调研]]
- [[../12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/lerobot-dataset-schema|LeRobot Dataset Schema]]
