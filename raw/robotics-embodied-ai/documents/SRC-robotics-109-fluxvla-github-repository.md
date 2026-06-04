---
source_id: "SRC-robotics-109"
title: "FluxVLA GitHub repository"
source_type: "open_source_repository"
publisher: "FluxVLA/LimX Dynamics"
source_date: "2026"
url: "https://github.com/FluxVLA/FluxVLA"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-04T05:45:45+00:00"
tags:
  - raw/source
  - source-type/open-source-repository
  - evidence/s
aliases:
  - SRC-robotics-109
---
# FluxVLA GitHub repository

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

[![FluxVLA](https://github.com/FluxVLA/FluxVLA/raw/main/assets/fluxvla.png)](https://github.com/FluxVLA/FluxVLA/blob/main/assets/fluxvla.png)

[![Hugging Face](https://camo.githubusercontent.com/86e1ac5d0fd07b33c33bcc2401bca241087a7d69fb27148c05a5d116e3eabc8d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48756767696e67466163652d79656c6c6f773f6c6f676f3d68756767696e6766616365266c6f676f436f6c6f723d7768697465)](https://huggingface.co/limxdynamics/FluxVLAEngine) [![](https://camo.githubusercontent.com/11b8e0412521bc020ed010ee1fee24067a8466855e05c33800a86b5f531b12a0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f63756d656e746174696f6e2d507572706c653f636f6c6f723d384132424532266c6f676f3d72656164746865646f6373)](https://fluxvla.limxdynamics.com/) [![](https://camo.githubusercontent.com/ab718625e7cf08bd457ce19f5ea5b8c021a340f4d98bd0a9884a360d243ab930/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe4b8ade69687e69687e6a1a32d7265643f6c6f676f3d72656164746865646f6373)](https://fluxvla.limxdynamics.com/zh/) [![](https://camo.githubusercontent.com/0e0f05555e9ffb977a29230619049a650086b30243adba5ae0b4efc80f72f756/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765436861742d677265656e3f6c6f676f3d776563686174)](https://github.com/limxdynamics/FluxVLA/issues/1) [![](https://camo.githubusercontent.com/6b397c7638dc31ad6f230442d372042bb9d0cc6f7877292d1df4cef2d271aeb9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4665697368752d3333373046463f6c6f676f3d6c61726b266c6f676f436f6c6f723d7768697465)](https://github.com/limxdynamics/FluxVLA/issues/1)

English | [简体中文](https://github.com/FluxVLA/FluxVLA/blob/main/README_zh-CN.md) | [日本語](https://github.com/FluxVLA/FluxVLA/blob/main/README_ja.md)

FluxVLA Engine is a full-stack, end-to-end engineering platform for deploying embodied intelligence applications. Built on the core design principles of unified configuration, standardized interfaces, module decoupling, and deployability, it creates a complete engineering loop from data to real-device deployment. With the goal of providing a standardized industry–academia–research foundation, it significantly lowers the engineering barrier for VLA research and development.

## Framework

[![Framework Architecture](https://github.com/FluxVLA/FluxVLA/raw/main/assets/framework.png)](https://github.com/FluxVLA/FluxVLA/blob/main/assets/framework.png)

## Performance

| Codebase | Libero-Spatial | Libero-Object | Libero-Goal | Libero-Long | Libero-Average |
| --- | --- | --- | --- | --- | --- |
| FluxVLA(SmolVLA) | [86.2](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/smolvla_libero_spatial_full_finetune_bs64) | [92.4](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/smolvla_libero_object_full_finetune_bs64) | [91.4](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/smolvla_libero_goal_full_finetune_bs64) | [68.8](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/smolvla_libero_10_full_finetune_bs64) | 84.7 |
| FluxVLA(GR00T) | [97.4](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/gr00t_eagle_3b_libero_spatial_full_finetune_bs64) | [96.2](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/gr00t_eagle_3b_libero_object_full_finetune_bs64) | [94.6](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/gr00t_eagle_3b_libero_goal_full_finetune_bs64) | [93.0±1.5](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/gr00t_eagle_3b_libero_10_full_finetune_bs64) | 95.3 |
| FluxVLA(DreamZero) | [98.2](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/dreamzero_libero_spatial_full_finetune_w_cache_bs64) | [98.8](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/dreamzero_libero_object_full_finetune_w_cache_bs64) | [93.2](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/dreamzero_libero_goal_full_finetune_w_cache_bs64) | [94.8](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/dreamzero_libero_10_full_finetune_w_cache_bs64) | 96.25 |
| FluxVLA(Qwen3VL 0.6B+GR00T) | 98.6 | 99.6 | 95.6 | 92.2±1.8 | 96.50 |
| FluxVLA(PI0) | [98.6](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi0_paligemma_libero_spatial_full_finetune_bs64) | [98.8](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi0_paligemma_libero_object_full_finetune_bs64) | [96.8](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi0_paligemma_libero_goal_full_finetune_bs64) | [93.2](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi0_paligemma_libero_10_full_finetune_bs64) | 96.85 |
| FluxVLA(PI0.5) | [98.6](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_paligemma_libero_spatial_full_finetune_bs64) | [99.6](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_paligemma_libero_object_full_finetune_bs64) | [98.0](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_paligemma_libero_goal_full_finetune_bs64) | [95.6±1.0](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_paligemma_libero_10_full_finetune_bs64) | 97.95 |

*Linked scores point to the corresponding checkpoints.*

## 📢 Latest News

**\[2026/05/28\]** 🔥 [FluxDAgger](https://github.com/FluxVLA/FluxDAgger) is now released: a model-decoupled DAgger pipeline for dual-arm manipulation, making it easy to integrate different VLAs and reward models.

**\[2026/05/28\]** 🔥 The embodied manipulation simulation benchmark [FluxBisim](https://github.com/FluxVLA/FluxBisim) is now released.

**\[2026/05/09\]** 🔥 SmolVLA is now supported.

**\[2026/04/24\]** 🔥 Pi0.5-RTC is now supported.

**\[2026/04/22\]** 🔥 ZMQ-based remote inference framework is now supported.

**\[2026/04/15\]** 🔥 DreamZero WAM is now supported.

**\[2026/04/08\]** 🔥 FluxVLA has been open-sourced.

## 🛠️ Installation

**1\. Create a conda environment**
```
conda create -n fluxvla python=3.10 -y
conda activate fluxvla
```
**2\. Install PyTorch (CUDA version)**

> **Important**: Before running `pip install -r requirements.txt`, you must install PyTorch from the official CUDA index first. The default PyPI index cannot fetch CUDA-enabled builds.

```
# CUDA 12.8
pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128
```

For other CUDA versions, replace `cu128` with the corresponding value (e.g., `cu118`, `cu121`). See: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) and [https://pytorch.org/get-started/previous-versions/](https://pytorch.org/get-started/previous-versions/).

**3\. Install flash-attention**

Method 1: Install directly via pip:

```
pip install psutil ninja packaging
# MAX_JOBS controls the number of parallel build threads; tune it based on your machine resources
MAX_JOBS=8 pip install flash-attn==2.5.5 --no-build-isolation --find-links https://github.com/Dao-AILab/flash-attention/releases
```

Method 2: Build from source (recommended if method 1 fails):

```
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout v2.5.5
# MAX_JOBS controls the number of parallel build threads; tune it based on your machine resources
MAX_JOBS=8 python setup.py install
```
**4\. Install av**
```
conda install -c conda-forge av=14.4.0
```
**5\. Install fluxvla and other dependencies**
```
pip install -r requirements.txt
pip install --no-build-isolation -e .
```

> **Note**: `requirements.txt` pins `torch==2.6.0` to prevent pip from accidentally replacing the CUDA-enabled PyTorch installed in step 2. If you need to use another torch version, update both the step-2 command and the torch version in `requirements.txt`.

**Online evaluation environment (LIBERO / EGL)**

If you want to evaluate LIBERO on devices that do not support ray tracing (e.g., A100), please refer to [EGL Device GPU Rendering Configuration](https://github.com/google-deepmind/mujoco/issues/572#issuecomment-2419965230).

**Install system dependencies**

```
export MUJOCO_GL=egl
sudo apt install libegl-dev libgl1-mesa-dev libx11-dev libglew-dev libosmesa6-dev
```

**Environment checks**

Make sure `/proc/1/environ` contains the following environment variables:

- `NVIDIA_DRIVER_CAPABILITIES=all`
- `NVARCH=x86_64`
- `NVIDIA_REQUIRE_CUDA=cuda>=12.4`
- `brand=tesla` and `driver>=470`

**Create an EGL configuration file**

Create file `/usr/share/glvnd/egl_vendor.d/10_nvidia.json` with the following content:

```
{
    "file_format_version": "1.0.0",
    "ICD": {
        "library_path": "libEGL_nvidia.so.0"
    }
}
```
**Configure pre-commit hooks (optional but recommended)**

To ensure code quality and consistency (especially for C++/CUDA code), install pre-commit hooks:

```
pip install pre-commit
pre-commit install
```

This will automatically check and format code before every commit.

**Configure Weights & Biases (wandb)**

[Weights & Biases](https://wandb.ai/) is used for experiment tracking and visualization. Configure it as follows:

1. Install wandb (included in `requirements.txt`):
```
pip install wandb
```
2. Log in to your wandb account:
```
wandb login
```
3. Set environment variables:
```
export WANDB_PROJECT=fluxvla        # project name (default: fluxvla)
export WANDB_ENTITY=your-team-name  # team name or username (default: None)
export WANDB_MODE=online            # online, offline, or disabled (default: online)
```
4. If you want to disable wandb logging during training, set:
```
export WANDB_MODE=disabled
```

Note: all wandb configuration is read from environment variables; no additional settings are needed in config files.

**Configure TensorBoard (optional)**

[TensorBoard](https://www.tensorflow.org/tensorboard) is supported as an optional logging backend for experiment metric visualization. Configure it as follows:

1. Add `'tensorboard'` to `active_trackers` in your config file:
```
metric=dict(
    type='VLAMetric',
    active_trackers=('jsonl', 'wandb', 'tensorboard'),
    ...
)
```

Alternatively, enable it via command line without modifying the config file:

```
--cfg-options 'runner.metric.active_trackers=[jsonl,wandb,tensorboard]'
```
2. After training, launch TensorBoard to view metrics:
```
tensorboard --logdir work_dirs/tensorboard
```

Note: event files are saved to `{work_dir}/tensorboard/{run_id}/` per run, enabling automatic comparison across experiments. If the `TENSORBOARD_LOG_PATH` environment variable is set, it will be used directly as the log directory.

## Data Preparation

**Use the datasets we prepared directly**

Download the required datasets and place them under `./datasets`. Download only the datasets you need according to your configuration.

| Dataset | Download link |
| --- | --- |
| libero-object | [limxdynamics/FluxVLAData/libero\_object\_no\_noops\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/libero_object_no_noops_lerobotv2.1) |
| libero-spatial | [limxdynamics/FluxVLAData/libero\_spatial\_no\_noops\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/libero_spatial_no_noops_lerobotv2.1) |
| libero-10 | [limxdynamics/FluxVLAData/libero\_10\_no\_noops\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/libero_10_no_noops_lerobotv2.1) |
| libero-goal | [limxdynamics/FluxVLAData/libero\_goal\_no\_noops\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/libero_goal_no_noops_lerobotv2.1) |
| modified\_libero\_rlds | [openvla/modified\_libero\_rlds](https://huggingface.co/datasets/openvla/modified_libero_rlds) |
| RealRobot\_AgileX\_aloha | [limxdynamics/FluxVLAData/RealRobot\_AgileX\_aloha\_lerobot\_v2](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/RealRobot_AgileX_aloha_lerobot_v2) |
| RealRobot\_UR3\_Chem | [limxdynamics/FluxVLAData/RealRobot\_UR3\_Chem\_lerobot\_v2](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/RealRobot_UR3_Chem_lerobot_v2) |

For example, download the `libero-10` dataset:

```
huggingface-cli download limxdynamics/FluxVLAData --repo-type dataset --include "libero_10_no_noops_lerobotv2.1/*" --local-dir ./datasets
```

Replace `libero_10_no_noops_lerobotv2.1` with the corresponding folder name of the dataset you want to download.

**SARM datasets**

FluxVLA SARM workflows accept standard LeRobot v2.1 or v3.x datasets. Besides the usual observation / action fields, the dataset must carry SARM subtask annotations in episodes metadata.

Published SARM example datasets on Hugging Face:

- LeRobot v3.x manual sparse+dense annotations for training / inference: [limxdynamics/FluxVLAData/SARM\_manual\_test\_10Episodes\_lerobotv3.0](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/SARM_manual_test_10Episodes_lerobotv3.0)
- LeRobot v3.x unlabeled dataset kept for manual or VLM labeling: [limxdynamics/FluxVLAData/SARM\_vlm\_test\_10Episodes\_lerobotv3.0](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/SARM_vlm_test_10Episodes_lerobotv3.0)
- New LeRobot v2.1 manual conversion for training / inference and legacy-tool compatibility: [limxdynamics/FluxVLAData/SARM\_manual\_test\_10Episodes\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/SARM_manual_test_10Episodes_lerobotv2.1)
- New LeRobot v2.1 unlabeled conversion for manual or VLM labeling workflows: [limxdynamics/FluxVLAData/SARM\_vlm\_test\_10Episodes\_lerobotv2.1](https://huggingface.co/datasets/limxdynamics/FluxVLAData/tree/main/SARM_vlm_test_10Episodes_lerobotv2.1)

Download them under `./datasets` with:

```
huggingface-cli download limxdynamics/FluxVLAData --repo-type dataset --include "SARM_manual_test_10Episodes_lerobotv3.0/*" --local-dir ./datasets
huggingface-cli download limxdynamics/FluxVLAData --repo-type dataset --include "SARM_vlm_test_10Episodes_lerobotv3.0/*" --local-dir ./datasets
huggingface-cli download limxdynamics/FluxVLAData --repo-type dataset --include "SARM_manual_test_10Episodes_lerobotv2.1/*" --local-dir ./datasets
huggingface-cli download limxdynamics/FluxVLAData --repo-type dataset --include "SARM_vlm_test_10Episodes_lerobotv2.1/*" --local-dir ./datasets
```

Use the `manual_*` datasets directly for training / inference. Use the `vlm_*` datasets as clean starting points for manual stage writing or VLM auto-annotation. Prefer the v2.1 pair when another tool expects `meta/episodes.jsonl` plus per-episode videos; prefer the v3.0 pair when you want to keep native LeRobot v3.x metadata layout.

Before using a LeRobot v3.x SARM dataset, sanity-check the video metadata:

- LeRobot v3.x allows either many episodes in one MP4 or one MP4 per episode.
- If many episodes share one MP4, each episode that points to that file must use correct `from_timestamp` / `to_timestamp` offsets.
- If videos are already split as `file-000.mp4`, `file-001.mp4`,..., each episode should point to its own `file_index`, and `from_timestamp` will usually reset to `0.0`.
- If the directory contains multiple MP4 files but all episodes still point to `file-000.mp4`, the dataset metadata is malformed and should be fixed before use.
- For ready-to-use SARM dataset structure, annotation columns, and progress inference usage, see [docs/sarm.md](https://github.com/FluxVLA/FluxVLA/blob/main/docs/sarm.md).
- For writing manual stages or generating VLM-based annotations, see [tools/sarm\_annotate/README.md](https://github.com/FluxVLA/FluxVLA/blob/main/tools/sarm_annotate/README.md).
**Private dataset directory structure**

If you train with fluxvla on private datasets, you need to convert your raw data (e.g., HDF5 files collected by ALOHA robots) into the LeRobot Dataset v2.1 format. For a step-by-step conversion guide, see [Data Conversion Guide](https://github.com/FluxVLA/FluxVLA/blob/main/docs/data_convert.md).

For SARM specifically, FluxVLA supports both LeRobot v2.1 and v3.x datasets as long as the required SARM annotation columns are present. The SARM-specific metadata contract is documented in [docs/sarm.md](https://github.com/FluxVLA/FluxVLA/blob/main/docs/sarm.md).

The converted dataset should follow this directory structure:

```
├── data
│   └── chunk000
│   │   └── episode_000000.parquet
│   │   └── episode_000001.parquet
│   │   └── ... (more parquet files)
│   │   └── episode_00000N.parquet
│   └── chunk001
│   └── ... (more chunks)
│   └── chunk00N
├── meta
│   └── episodes.jsonl
│   └── episodes_stats.jsonl
│   └── info.json
│   └── tasks.jsonl
├── videos
│   └── chunk000
│   │   └── camera name 0
│   │   │   └── episode_000000.mp4
│   │   │   └── episode_000001.mp4
│   │   │   └── ...(more mp4 files)
│   │   │   └── episode_00000N.mp4
│   │   └── camera name 1
│   └── chunk001
│   └── ... (more chunks)
│   └── chunk00N
```

## 🤗 Checkpoint Preparation

Download the required pretrained checkpoints and place them under `./checkpoints`. Download only the checkpoints you need based on your configuration.

For SARM workflows, you typically need a CLIP checkpoint for training / inference and optionally a Qwen3-VL checkpoint for VLM-based annotation. Detailed usage is documented in [docs/sarm.md](https://github.com/FluxVLA/FluxVLA/blob/main/docs/sarm.md).

**VLA models**

| Model | Size | Download link |
| --- | --- | --- |
| GR00T N1.5 | 3B | [🤗 Hugging Face](https://huggingface.co/nvidia/GR00T-N1.5-3B/tree/main) |
| OpenVLA | 7B | [🤗 Hugging Face](https://huggingface.co/openvla/openvla-7b-finetuned-libero-10) |
| PI0\_base | 3B | [🤗 Hugging Face](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi0_base) |
| PI05\_base | 3B | [🤗 Hugging Face](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_base) |
| PI05\_libero | 3B | [🤗 Hugging Face](https://huggingface.co/limxdynamics/FluxVLAEngine/tree/main/pi05_libero) |
| SmolVLA | 450M | [🤗 Hugging Face](https://huggingface.co/lerobot/smolvla_base) |

**Vision-Language Models (VLM)**

| Model | Size | Download link |
| --- | --- | --- |
| Qwen2.5-VL | 3B | [🤗 Hugging Face](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) |
| Qwen3-VL | 30B | [🤗 Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct) |
| SmolVLM2 | 500M | [🤗 Hugging Face](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct) |

**Large Language Models (LLM)**

| Model | Size | Download link |
| --- | --- | --- |
| Qwen 2.5 | 3B | [🤗 Hugging Face](https://huggingface.co/Qwen/Qwen2.5-3B) |
| Qwen 2.5 | 7B | [🤗 Hugging Face](https://huggingface.co/Qwen/Qwen2.5-7B) |
| Llama 2 | 7B | [🤗 Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-hf/tree/main) |

**Vision backbone networks**

| Model | Download link |
| --- | --- |
| CLIP ViT-B/32 | [🤗 Hugging Face](https://huggingface.co/openai/clip-vit-base-patch32) |
| ViT-Large (DINOv2) | [🤗 Hugging Face](https://huggingface.co/timm/vit_large_patch14_reg4_dinov2.lvd142m) |
| ViT-SO400M (SigLIP) | [🤗 Hugging Face](https://huggingface.co/timm/ViT-SO400M-14-SigLIP) |
| SigLIP2 | [🤗 Hugging Face](https://huggingface.co/google/siglip2-base-patch16-224) |
| paligemma | [🤗 Hugging Face](https://huggingface.co/google/paligemma-3b-pt-224) |

> **Tip**: You can speed up downloads with `huggingface-cli download <model-name> --local-dir ./checkpoints/<model-name>`.

For the built-in SARM configs, place the CLIP files under `./checkpoints/clip-vit-base-patch32`. If you use VLM-based SARM annotation, place the official SARM VLM under `./checkpoints/Qwen3-VL-30B-A3B-Instruct`.

**Trained models**

Checkpoints are available on [🤗 limxdynamics/FluxVLAEngine](https://huggingface.co/limxdynamics/FluxVLAEngine). Linked scores in the [Performance](#performance) table point to the corresponding checkpoints.

```
# Example: download the PI0.5 checkpoint from limxdynamics/FluxVLAEngine
huggingface-cli download limxdynamics/FluxVLAEngine --include "pi05_paligemma_libero_10_full_finetune_bs64/*" --local-dir ./checkpoints/pi05_paligemma_libero_10_full_finetune_bs64
```

## 🌟 Features

**All-in-one: One configuration file manages the full workflow**
- Manage key parameters for data, models, training, evaluation, inference, and deployment through a single config file (easier to reproduce and deploy).
**Supports different VLA models**
- Supports OpenVLA, LlavaVLA, Gr00t, Pi0, and Pi0.5.
**Supports different modules**
- Supports Llama, Gemma, and Qwen-family LLM backbones.
- Supports DINOv2 and SigLIP vision backbones.
- Supports PaliGemma and Qwen-VL VLM backbones.
**Supports SARM workflows**
- Supports [SARM](https://github.com/xdofai/opensarm) training, annotation, and progress inference on LeRobot v2.1/v3.x datasets. See [docs/sarm.md](https://github.com/FluxVLA/FluxVLA/blob/main/docs/sarm.md) for details.
**Supports different training strategies**
- Supports FSDP together with DDP, and supports LoRA training mode.
- Supports eval-after-train.
- Supports resuming training from checkpoints.
**Data and weight formats**
- Supports Parquet datasets and loading LeRobot-format data.
- Supports model weights in safetensors format.
**Evaluation and inference capabilities**
- Supports multi-GPU evaluating libero on devices without ray tracing.
- Supports remote inference infrastructure with ZMQ-based server/client architecture, enabling GPU-offloaded inference for resource-constrained edge devices. See [Remote Inference Serving](https://github.com/FluxVLA/FluxVLA/blob/main/docs/remote_inference_serving.md).
- Supports [RTC (Real-Time Chunking)](https://github.com/FluxVLA/FluxVLA/blob/main/docs/rtc.md) to improve cross-chunk trajectory continuity.
- Supports accelerated inference for GR00T and PI0.5; see [Inference Acceleration](https://github.com/FluxVLA/FluxVLA/blob/main/docs/inference_acceleration.md), including Triton fused kernels, CUDA Graph capture, and CUDA custom operators.

[![VLA Speedup](https://github.com/FluxVLA/FluxVLA/raw/main/assets/VLA_speedup.png)](https://github.com/FluxVLA/FluxVLA/blob/main/assets/VLA_speedup.png)

## Usage

**Local debugging**

```
/root/miniconda3/envs/fluxvla/bin/torchrun --standalone --nnodes 1 --nproc-per-node [NUM_GPUS] scripts/train.py --config [CONFIG_PATH] --work-dir [WORK_DIR] --cfg-options train_dataloader.per_device_batch_size=[PER_DEVICE_BATCH_SIZE]
```

Example:

```
export WANDB_MODE=disabled
/root/miniconda3/envs/fluxvla/bin/torchrun --standalone --nnodes 1 --nproc-per-node 2 scripts/train.py --config configs/pi05/pi05_paligemma_libero_10_full_finetune.py --work-dir ./checkpoints/pi05_paligemma_libero_10_full_finetune --cfg-options train_dataloader.per_device_batch_size=2
```

**Local evaluation**

```
/root/miniconda3/envs/fluxvla/bin/torchrun --standalone --nnodes 1 --nproc-per-node [NUM_GPUS] scripts/eval.py --config [CONFIG_PATH] --ckpt-path [CKPT_PATH] --cfg-options [CFG_OPTIONS]
```

Example:

```
export WANDB_MODE=disabled
/root/miniconda3/envs/fluxvla/bin/torchrun --standalone --nnodes 1 --nproc-per-node 2 scripts/eval.py --config configs/pi05/pi05_paligemma_libero_10_full_finetune.py --ckpt-path checkpoints/pi05_paligemma_libero_10_full_finetune_bs64/checkpoints/step-028548-epoch-18-loss=0.0111.safetensors
```

**Cluster training**

```
export WANDB_MODE=disabled
bash scripts/train.sh [CONFIG] [WORK_DIR] --cfg-options train_dataloader.per_device_batch_size=[PER_DEVICE_BATCH_SIZE] train_dataloader.batch_size=[GLOBAL_BATCH_SIZE] runner.max_steps=[MAX_STEPS] runner.save_interval=[SAVE_INTERVAL] runner.max_keep_ckpts=[MAX_KEEP_CKPTS] --eval-after-train
```

**Resume training from a checkpoint**

To resume training from a checkpoint, use the `--resume-from` argument to specify the checkpoint file path. Training will continue from the saved global step, epoch, model state, and optimizer state.

**Local training example:**

```
export WANDB_MODE=disabled
/root/miniconda3/envs/fluxvla/bin/torchrun --standalone --nnodes 1 --nproc-per-node 2 scripts/train.py \
  --config configs/pi05/pi05_paligemma_libero_10_full_finetune.py \
  --work-dir ./work_dirs/pi05_paligemma_libero_10_full_finetune \
  --resume-from ./work_dirs/pi05_paligemma_libero_10_full_finetune/checkpoints/checkpoint_epoch_5.pt \
  --cfg-options train_dataloader.per_device_batch_size=2
```

**Cluster training example:**

```
export WANDB_MODE=disabled
bash scripts/train.sh [CONFIG] [WORK_DIR] \
  --resume-from [CHECKPOINT_PATH] \
  --cfg-options train_dataloader.per_device_batch_size=[PER_DEVICE_BATCH_SIZE] runner.max_steps=[MAX_STEPS]
```

**Cluster evaluation**

```
export WANDB_MODE=disabled
bash scripts/eval.sh [CONFIG] [CKPT_PATH] --cfg-options [CFG_OPTIONS]
```

**Real-robot inference**

When running inference on a real robot, first install the environment on the robot side, and then run:

```
python scripts/inference_real_robot.py --config [CONFIG] -- ckpt-path [CKPT_PATH]
```

## FAQ

**Q: Problems connecting to Hugging Face when downloading models or datasets.**

**A:** If you encounter Hugging Face connectivity issues (e.g., slow downloads, timeouts, or connection refused), set the following environment variable before running the command and use [hf-mirror](https://hf-mirror.com/):

```
export HF_ENDPOINT="https://hf-mirror.com"
```
**Q: `conda install av` is very slow at resolving the environment.**

**A:** You can use the `libmamba` solver to speed up dependency resolution:

```
conda install -c conda-forge av=14.4.0 --solver=libmamba
```
**Q: GR00T evaluation on LIBERO is unstable.**

**A:** This is expected. GR00T's performance on LIBERO is sensitive to random seeds, the hardware environment, and the number of training epochs. Small changes in these factors may cause noticeable fluctuations in evaluation results. It is recommended to run experiments with multiple random seeds and select the best checkpoint based on evaluation performance.

**Q: When running `pip install -r requirements.txt`, building `egl_probe` fails with `RuntimeError: CMake must be installed`.**

**A:** `egl_probe` needs CMake to build. Install it via conda (recommended) or apt:

```
conda install -c conda-forge cmake
# or
sudo apt install cmake
```

> **Note**: Do not use `pip install cmake`. The pip package is a Python wrapper and may fail because pip isolates the build environment.

**Q: `egl_probe` build fails and reports `Compatibility with CMake < 3.5 has been removed from CMake`.**

**A:** This is usually because your CMake version is too new for the `egl_probe` CMakeLists.txt. Set the following environment variable before installing:

```
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install -r requirements.txt
```
**Q: After installation, I get NumPy version errors (e.g., `RuntimeError: Numpy is not available` or version incompatibility warnings).**

**A:** During installation, some dependencies may overwrite the pinned NumPy version. Reinstall the correct version directly:

```
pip install numpy==1.26.4
```

## Contributing

Please see the contribution workflow and guidelines in [docs/CONTRIBUTING.md](https://github.com/FluxVLA/FluxVLA/blob/main/docs/CONTRIBUTING.md).

Quick conventions:

- **Discuss first**: for new features/models or other large changes, please open a GitHub Issue to align on scope and design.
- **Branch from upstream**: create your branch from `upstream/main` and use prefixes like `feat/`, `fix/`, `docs/`, etc. (details in the contributing guide).
- **Run checks before PR**: make sure local pre-commit passes and CI is green.
- **Commit messages**: we recommend Conventional Commits (examples in the contributing guide).

## Support

If you encounter any issues while using this repository, feel free to contact us. You can reach us directly at [mason@limxdynamics.com](https://github.com/FluxVLA/FluxVLA/blob/main/mason@limxdynamics.com) and [wayne@limxdynamics.com](https://github.com/FluxVLA/FluxVLA/blob/main/wayne@limxdynamics.com), or open a GitHub issue for help.

## 🙏 Citation & Acknowledgements

If you use FluxVLA in your research or projects, please cite it as:

```
@software{FluxVLA2026,
    = {Li, Yinhao and Mao, Weixin and Lan, Zihan and Rong, Jikun and Zhu, Minzhao and Mao, Yiming and Shen, Bowen and Huang, Xu},
  title   = {{FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence}},
  year    = {2026},
  month   = apr,
  version = {1.0.0},
  doi     = {10.5281/zenodo.20049506},
  url     = {https://github.com/FluxVLA/FluxVLA},
  license = {Apache-2.0},
}
```

**Acknowledgements:** This project benefits from the following open-source projects and community efforts. Thanks to: [LeRobot](https://github.com/huggingface/lerobot), [NVIDIA Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T/tree/main), [DreamZero](https://arxiv.org/abs/2602.15922) ([code](https://github.com/dreamzero0/dreamzero)), [OpenVLA](https://github.com/openvla/openvla), [OpenPI (pi0)](https://github.com/Physical-Intelligence/openpi), [LLaVA](https://github.com/haotian-liu/LLaVA), [DeepSpeed](https://github.com/deepspeedai/DeepSpeed), [Qwen](https://github.com/QwenLM), [Triton](https://github.com/triton-lang/triton), [RTC](https://github.com/Physical-Intelligence/real-time-chunking-kinetix), [Training RTC](https://arxiv.org/pdf/2512.05964), and [Realtime-VLA](https://github.com/Dexmal/realtime-vla). If we missed your project or contribution, please open an issue or pull request so we can properly acknowledge it.

## Roadmap

- Support more vision backbone networks.
- Support more VLM backbones.
- Support more VLA methods.
- Support training with VLM data or reasoning-chain-of-thought (CoT) data.
- RLDS datasets will be deprecated and replaced by Parquet datasets.
- Full implementation of the logger feature.
- Support Isaac Sim.
