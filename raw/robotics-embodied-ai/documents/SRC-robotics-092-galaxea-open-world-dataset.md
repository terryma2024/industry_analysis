---
source_id: "SRC-robotics-092"
title: "Galaxea Open-World Dataset"
source_type: "dataset"
publisher: "Hugging Face/OpenGalaxea"
source_date: "2026"
url: "https://huggingface.co/datasets/OpenGalaxea/Galaxea-Open-World-Dataset"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/dataset
  - evidence/s
aliases:
  - SRC-robotics-092
---
# Galaxea Open-World Dataset

## Galaxea Open-World Dataset

[![Project Page](https://img.shields.io/badge/Project%20Page-000000?style=for-the-badge&logo=github)](https://opengalaxea.github.io/G0/) [![Paper](https://img.shields.io/badge/Paper-8A2BE2?style=for-the-badge&logo=arxiv)](https://arxiv.org/abs/2509.00576) [![Videos](https://img.shields.io/badge/Videos-FF0000?style=for-the-badge&logo=youtube)](https://opengalaxea.github.io/G0/) [![Visualizer](https://img.shields.io/badge/Visualizer-FF8C00?style=for-the-badge&logo=airplayvideo)](https://opengalaxea.github.io/G0/visualizer/index.html) [![Modelscope](https://img.shields.io/badge/Modelscope-1890FF?style=for-the-badge&logo=alibabacloud)](https://www.modelscope.cn/organization/Galaxea) [![Twitter](https://img.shields.io/badge/Twitter-FF6B35?style=for-the-badge&logo=x)](https://x.com/Galaxea_x) [![Linkedin](https://img.shields.io/badge/Linkedin-5865F2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/company/galaxeadynamics/posts/?feedView=all&viewAsMember=true) [![Discord](https://img.shields.io/badge/Discord-1890FF?style=for-the-badge&logo=discord)](https://discord.gg/hB6BuUWZZA)

## Key Features

- **500+ hours** of real-world mobile manipulation data.
- All data collected using **one uniform robotic embodiment** (R1-Lite) for consistency.
- Fine-grained **subtask language annotations** (bilingual Chinese/English).
- Covers **residential**, **kitchen**, **retail**, and **office** settings.
- Dataset in **LeRobot v2.1** format.

## Dataset Structure

The dataset is organized as **227 task-level tar.gz archives** under the `lerobot/` directory. Each archive contains a self-contained LeRobot dataset for one task:

```
lerobot/
├── Adjust_The_Air_Conditioner_Temperature_20250711_006.tar.gz
├── Arrange_Fruits_20250819_011.tar.gz
├── Clean_The_Mirror_20250714_006.tar.gz
├── ...
└── Wipe_The_Sewage_Stains_With_A_Ground_Cloth_20250801_012.tar.gz
```

After extracting a task archive, the directory follows the standard LeRobot v2.1 layout:

```
<task_name>/
├── meta/
│   ├── info.json              # Dataset metadata (features, fps, splits, etc.)
│   ├── episodes.jsonl         # Per-episode info (tasks, length, source file)
│   └── episodes_stats.jsonl   # Per-episode statistics
├── data/
│   └── chunk-000/
│       ├── episode_000000.parquet
│       ├── episode_000001.parquet
│       └── ...
└── videos/
    └── chunk-000/
        ├── observation.images.head_rgb/
        │   ├── episode_000000.mp4
        │   └── ...
        ├── observation.images.head_right_rgb/
        ├── observation.images.left_wrist_rgb/
        └── observation.images.right_wrist_rgb/
```

## LeRobot Dataset Schema

A detailed schema is available in [lerobot\_info.json](https://huggingface.co/datasets/OpenGalaxea/Galaxea-Open-World-Dataset/blob/main/lerobot_info.json). Below is a summary of all features:

### Observations

| Feature | Dtype | Shape | Description |
| --- | --- | --- | --- |
| `observation.images.head_rgb` | video | (720, 1280, 3) | Head camera RGB |
| `observation.images.head_right_rgb` | video | (720, 1280, 3) | Head right camera RGB |
| `observation.images.left_wrist_rgb` | video | (720, 1280, 3) | Left wrist camera RGB |
| `observation.images.right_wrist_rgb` | video | (720, 1280, 3) | Right wrist camera RGB |
| `observation.state.left_arm` | float64 | (6,) | Left arm joint positions |
| `observation.state.left_arm.velocities` | float64 | (6,) | Left arm joint velocities |
| `observation.state.right_arm` | float64 | (6,) | Right arm joint positions |
| `observation.state.right_arm.velocities` | float64 | (6,) | Right arm joint velocities |
| `observation.state.torso` | float64 | (4,) | Torso joint positions |
| `observation.state.torso.velocities` | float64 | (4,) | Torso joint velocities |
| `observation.state.chassis` | float64 | (3,) | Chassis positions |
| `observation.state.chassis.velocities` | float64 | (3,) | Chassis velocities |
| `observation.state.chassis.imu` | float64 | (10,) | Chassis IMU (orientation, angular velocity, linear acceleration) |
| `observation.state.left_gripper` | float64 | (1,) | Left gripper state (0-close, 100-open) |
| `observation.state.right_gripper` | float64 | (1,) | Right gripper state (0-close, 100-open) |
| `observation.state.left_ee_pose` | float64 | (7,) | Left end-effector pose (position + quaternion) |
| `observation.state.right_ee_pose` | float64 | (7,) | Right end-effector pose (position + quaternion) |

### Actions

| Feature | Dtype | Shape | Description |
| --- | --- | --- | --- |
| `action.left_arm` | float64 | (6,) | Target left arm joint positions |
| `action.right_arm` | float64 | (6,) | Target right arm joint positions |
| `action.left_gripper` | float64 | (1,) | Target left gripper position |
| `action.right_gripper` | float64 | (1,) | Target right gripper position |
| `action.chassis.velocities` | float64 | (6,) | Target chassis twist (linear + angular) |
| `action.torso.velocities` | float64 | (6,) | Target torso twist (linear + angular) |

### Metadata Columns

| Feature | Dtype | Description |
| --- | --- | --- |
| `timestamp` | float32 | Timestamp within episode |
| `frame_index` | int64 | Frame index within episode |
| `episode_index` | int64 | Episode index |
| `index` | int64 | Global frame index |
| `task_index` | int64 | Subtask annotation index |
| `coarse_task_index` | int64 | Coarse-level task index |
| `quality_index` | int64 | Quality annotation index |
| `coarse_quality_index` | int64 | Coarse-level quality index |

All video streams are encoded with **AV1 codec** at **15 fps**.

## Quick Start

Below is an example of how to download and load a single task from the dataset using the Hugging Face Hub and LeRobot:

```python
import tarfile
from pathlib import Path
from huggingface_hub import hf_hub_download
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import torch

# 1. Download a single task archive
task_name = "Clean_The_Mirror_20250714_006"
tar_path = hf_hub_download(
    repo_id="OpenGalaxea/Galaxea-Open-World-Dataset",
    filename=f"lerobot/{task_name}.tar.gz",
    repo_type="dataset",
)

# 2. Extract it
extract_dir = Path("./galaxea_data")
extract_dir.mkdir(exist_ok=True)
with tarfile.open(tar_path, "r:gz") as tar:
    tar.extractall(path=extract_dir)

# 3. Load with LeRobot
dataset = LeRobotDataset.from_local(str(extract_dir / task_name / task_name))

print(f"Number of episodes: {dataset.num_episodes}")
print(f"Number of frames:   {dataset.num_frames}")
print(f"FPS:                {dataset.fps}")

# 4. Access a single frame
frame = dataset[0]
print(f"\nFrame keys: {list(frame.keys())}")
print(f"Left arm state shape:  {frame['observation.state.left_arm'].shape}")
print(f"Left arm action shape: {frame['action.left_arm'].shape}")

# 5. Iterate over an episode
from torch.utils.data import DataLoader

dataloader = DataLoader(dataset, batch_size=32, shuffle=False)
for batch in dataloader:
    print(f"Batch observation.state.left_arm shape: {batch['observation.state.left_arm'].shape}")
    break
```

## Citation

All the data and code within this repo are under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). If you use our dataset or models, please cite:

```
@article{galaxea2025,
  title={Galaxea G0: Open-World Dataset and Dual-System VLA Model},
  author={Galaxea Team},
  journal={arXiv preprint arXiv:2509.00576},
  year={2025}
}
```

Total file size:

2.87 TB

## Models trained or fine-tuned on OpenGalaxea/Galaxea-Open-World-Dataset

## Paper for OpenGalaxea/Galaxea-Open-World-Dataset[Paper • 2509.00576 • Published • 1](https://huggingface.co/papers/2509.00576)
