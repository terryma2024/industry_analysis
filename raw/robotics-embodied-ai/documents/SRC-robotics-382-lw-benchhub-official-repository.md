---
source_id: "SRC-robotics-382"
title: "LW-BenchHub official repository"
source_type: "code_repository"
publisher: "LightwheelAI"
source_date: "2026-08-06"
url: "https://github.com/LightwheelAI/LW-BenchHub"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-06T02:05:23+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-382
---
# LW-BenchHub official repository

## LW-BenchHub

[![LW-BenchHub Kitchens](https://github.com/LightwheelAI/LW-BenchHub/raw/main/images/lw-benchhub-kitchens.png)](https://github.com/LightwheelAI/LW-BenchHub/blob/main/images/lw-benchhub-kitchens.png)

**A unified benchmark hub built on Isaac Lab–Arena for embodied AI, providing consistent interfaces, realistic environments, multi-robot support, and ready-to-run large-scale evaluation.**

[![Python](https://camo.githubusercontent.com/ee6bff22c661a1649ba1962f84c6200c1e37bd0e5d6bac2ed6404f40103e9321/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312d626c75652e737667)](https://www.python.org/downloads/) [![CUDA](https://camo.githubusercontent.com/5a6e8c4b35cd23b1c41acc549cc0649159863e44dad90cf4207381e6a1d2c44d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f435544412d31322e382d677265656e2e737667)](https://developer.nvidia.com/cuda-toolkit) [![Isaac Lab](https://camo.githubusercontent.com/f8ff7abcb3e491f2cd95e47afa451f6c8a5bcb0e3d3d3e338453183f04d48c45/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f49736161632532304c61622d352e302e302d6f72616e67652e737667)](https://isaac-sim.github.io/IsaacLab/) [![License](https://camo.githubusercontent.com/b29de0acdfd19013f1f02689b15c933e4a6c145be9efa718288f88ba3280b1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c75652e737667)](https://www.apache.org/licenses/LICENSE-2.0) [![Documentation](https://camo.githubusercontent.com/ae0c888400d47e5218aa43aceb6fe4d8053e1e1c3f61bfe7050ce87a02f19f8d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d6c776c61622d2d646f63732e6c69676874776865656c2e6e65742d627269676874677265656e2e737667)](https://docs.lightwheel.net/lw_benchhub)

[Documentation](https://docs.lightwheel.net/lw_benchhub) • [Dataset](https://huggingface.co/LightwheelAI/datasets) • [Quick Start](#quick-start) • [Installation](#installation) • [Project Structure](#project-structure)

---

## Overview

**LW-BenchHub** is an end-to-end robotics simulation benchmark platform developed by the **Lightwheel team**, specifically designed for evaluating robots in kitchen manipulation and loco-manipulation tasks. Built on NVIDIA's **Isaac Lab-Arena**, LW-BenchHub provides a comprehensive platform that seamlessly integrates teleoperation data collection with reinforcement learning training workflows.

### Key Features

- **Multi-Robot Support** – Features 7 adapted robot types (Unitree G1, PandaOmron, DoublePanda, Agilex Piper, ARX X7s, Franka, and LeRobot SO100/101 Arm), comprising a total of 27 specific robot variants.
- **Realistic Kitchen Environments** – Large-scale kitchen scenarios with 10 layouts and 10 style combinations, offering 100 unique configurations using high‑fidelity assets pulled via the [Lightwheel SDK](https://docs.lightwheel.net/sdk/).
- **Flexible Input Devices** - Support for keyboard, VR(Vision Pro, PICO, Meta Quest), and Leader-Follower Arm.
- **Rich Task Suite** – 268 ready-to-use tasks (130 Lightwheel-LIBERO-Tasks, 138 Lightwheel-Robocasa-Tasks), covering kitchen manipulation, loco-manipulation, table-top actions, atomic skills, navigation, and long-horizon compositional tasks.
- **Complete Data Pipeline** - End-to-end workflow from teleoperation to policy deployment.
- **Intuitive and reproducible RL configuration design** – Supports generic RL configuration for a class of robots and tasks through a decorator-based binding mechanism, enabling modular registration and effortless switching or reproduction of RL setups. Seamlessly integrates with open-source RL libraries such as rsl-rl and skrl.
- **Large-scale Kitchen Manipulation Dataset** – Released a dataset with 219 unique tasks (89 from Lightwheel-Robocasa-Tasks, 130 from Lightwheel-LIBERO-Tasks) and 4 robots (LeRobot, ARX-X7s, Unitree G1, Agilex-Piper). The dataset contains 21,500 demonstration episodes (20,537,015 frames), with 50 episodes for each (robot, task) pair, captured in diverse, interactive kitchen environments. [👉 View and download the dataset on Hugging Face](https://huggingface.co/LightwheelAI/datasets)
- **Decoupled Policy API** – Adopts a server–client architecture that decouples policy execution from simulation-side environments and framework dependencies. Built with zero-copy data exchange, the API minimizes memory overhead and enables ultra-low-latency, high-throughput policy–simulation interactions.

## Quick Start

### Prerequisites

- **OS**: Linux (Primary support) / NVIDIA GPU required
- **Python**: 3.11
- **CUDA**: 12.8 (Recommended)
- **NVIDIA Driver**: 570.133.07 (Recommended)
- **Hardware**: NVIDIA RTX GPU for optimal ray-tracing performance

### Installation

1. **Create Conda Environment**
```
conda create -n lw_benchhub python=3.11 -y
conda activate lw_benchhub
```
2. **Quick Install**
```
sudo apt-get update
sudo apt-get install git-lfs
git lfs install

git clone https://github.com/LightwheelAI/lw_benchhub
cd lw_benchhub
git lfs pull
bash ./install.sh # Refer to the Documentation for custom installation steps
```

## Launch Your Task

### Teleoperation Data Collection

Start collecting demonstration data with different data collection configurations:

```
# Use PandaOmron robot configuration, \`pandaomron.yml\`
python ./lw_benchhub/scripts/teleop/teleop_main.py --task_config pandaomron
```

To enable recording demonstrations, set `record` to `true` in the configuration file.

```
record: true
```

### Trajectory Replay

Replay collected demonstrations for analysis:

```
# State-based replay
python ./lw_benchhub/scripts/teleop/replay_demos.py --dataset_file "/path/to/your/dataset.hdf5" --enable_cameras

# Action-based replay
python ./lw_benchhub/scripts/teleop/replay_action_demo.py \
    --dataset_file /path/to/your/dataset.hdf5 \
    --replay_mode action \
    --enable_cameras

# JointTarget-based replay
python ./lw_benchhub/scripts/teleop/replay_action_demo.py \
    --dataset_file /path/to/your/dataset.hdf5 \
    --replay_mode joint_target \
    --enable_cameras
```

### Reinforcement Learning

LW-BenchHub provides a complete RL pipeline:

#### Train

```
# Start training with default configuration
bash train.sh # default preset uses LiftObj (state variant)

# Custom training configuration
python ./lw_benchhub/scripts/rl/train.py \
    --task_config lerobot_liftobj_state \
    --headless
```

#### Evaluation

```
# Evaluate with default settings
bash eval.sh

# Custom evaluation
python ./lw_benchhub/scripts/rl/play.py \
    --task_config lerobot_liftobj_state_play
```

## Project Structure

### Core Components

| Component | Description |
| --- | --- |
| **configs** | This directory contains configuration files related to data collection, as well as the training and evaluation of reinforcement learning tasks. |
| **lw\_benchhub** | This module provides `core` functionalities, including simulation scene generation, asset logic control, robot control, entry-point scripts, and utility functions. |
| **policy** | This directory focuses on the implementation of policy algorithms, covering both imitation learning (IL) and reinforcement learning (RL) strategies. The codebase is designed for modular experimentation and systematic benchmarking of various policy architectures. |
| **third\_party** | This folder contains **Isaac-Lab Arena** dependency. To ensure reproducibility and maintainability, these environments are preserved in their original form as much as possible. |
| **lw\_benchhub\_tasks** | This directory defines task specifications. Each task, such as `OpenOven`, includes its own success criteria, task-related asset control and item placement, as well as a detailed task description. |
| **lw\_benchhub\_rl** | This module implements reinforcement learning (RL) pipelines, algorithms, and training/evaluation scripts. It includes preset configurations for common RL tasks, wrappers for integrating with `lw_benchhub.core`, and utilities for distributed experiment management. Use this module to launch RL experiments, customize RL agents, and evaluate learning performance. |

### Launch Scripts

- **`teleop.sh`** - Launches the teleoperation mode, allowing real-time robot control via VR controllers or other input devices. Useful for data collection, demonstration, or manual intervention scenarios.
- **`train.sh`** - Starts the training process for reinforcement learning or imitation learning. This script automatically loads configuration files, initializes environments and policies, and begins the training loop.
- **`eval.sh`** - Evaluates trained policies or models. Supports performance testing across different tasks and environments, and outputs evaluation metrics.
- **`install.sh`** - Installs all required dependencies for the project, including Python packages, third-party libraries, and some system dependencies, ensuring a consistent development and runtime environment.

## Documentation

For comprehensive guides, API references, and advanced usage examples, visit our [Official Documentation](https://docs.lightwheel.net/lw_benchhub).

## Citation

If you use LW-BenchHub in your research or projects, please cite us:

```
@software{Lightwheel_Team_LW-BenchHub_Lightwheel_s_End-to-End,
  author = {{Lightwheel Team}},
  title = {{LW-BenchHub: Lightwheel's End-to-End Embodied AI Simulation Platform}},
  url = {https://github.com/lightwheel-ai/lw_benchhub}
}
```

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Copyright 2025 Lightwheel Team
