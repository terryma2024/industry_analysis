---
source_id: "SRC-robotics-321"
title: "LingBot-VLA 官方代码与部署文档"
source_type: "code_repository"
publisher: "Robbyant / 蚂蚁灵波"
source_date: "2026-07-23"
url: "https://github.com/Robbyant/lingbot-vla"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-23T01:06:56+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-321
---
# LingBot-VLA 官方代码与部署文档

## LingBot-VLA: A Pragmatic VLA Foundation Model

[![](https://camo.githubusercontent.com/36a5efa37954e18b1772eac6452de30c7235f5f23bca55d9745c1a9a31d07758/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d5061706572266d6573736167653d50444626636f6c6f723d726564266c6f676f3d6172786976)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/LingBot-VLA.pdf) [![](https://camo.githubusercontent.com/ef58686ae4a9a27ea6d58703624fc087088f98f23d2ae66bcf316cd849ed02fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d576562736974652d626c7565)](https://technology.robbyant.com/lingbot-vla) [![](https://camo.githubusercontent.com/e6aa3abafb1aecbd6378597807d6662136476709647f6d292e8372a46c0d7d8c/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d2546302539462541342539372532304d6f64656c266d6573736167653d48756767696e674661636526636f6c6f723d79656c6c6f77)](https://huggingface.co/collections/robbyant/lingbot-vla) [![](https://camo.githubusercontent.com/5aab4e1b393f43f9fd5547edb83eca66dedda8990f8a1835773bd9938e111182/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d2546302539462541342539362532304d6f64656c266d6573736167653d4d6f64656c53636f706526636f6c6f723d707572706c65)](https://modelscope.cn/collections/Robbyant/LingBot-VLA) [![](https://camo.githubusercontent.com/976b443d31dc4fc829281906bf1075402e58be986564a4fe3ded403a24386fe0/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d254630253946254134253937253230474d2d313030266d6573736167653d48756767696e674661636526636f6c6f723d79656c6c6f77)](https://huggingface.co/datasets/robbyant/gm100) [![](https://camo.githubusercontent.com/54a591a708d9e41adc220d00e0caa979b5a5c035327d4eebaab67748cc889e4a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368652d2d322e302d677265656e)](https://github.com/Robbyant/lingbot-vla/blob/main/LICENSE)

[![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/Teaser.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/Teaser.png)

## 🥳 We are excited to introduce LingBot-VLA, a pragmatic Vision-Language-Action foundation model.

**LingBot-VLA** has focused on being **Pragmatic**:

- **Large-scale Pre-training Data**: 20,000 hours of real-world data from 9 popular dual-arm robot configurations.

[![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/scale_sr.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/scale_sr.png) [![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/scale_ps.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/scale_ps.png)

- **Strong Performance**: Achieves clear superiority over competitors on simulation and real-world benchmarks.
- **Training Efficiency**: Represents a 1.5 ∼ 2.8× (depending on the relied VLM base model) speedup over existing VLA-oriented codebases.

## 🚀 News

- **\[2026-04-30\]** Update of Our codebase:
	- Add recommended post-training setting with real robot data.
		- Upgrade to LeRobot v3.0.
		- Support open-loop evaluation.
		- Optimize GPU memory usage during training.
		- Enable Torch Compile for inference.
- **\[2026-01-27\]** LingBot-VLA Technical Report is available on Arxiv.
- **\[2026-01-27\]** Weights and code released!

---

## 🛠️ Installation

Requirements

- Python 3.12.3
- Pytorch 2.8.0
- CUDA 12.8
```
conda create -n lingbotvla python=3.12 -y
conda activate lingbotvla

git clone https://github.com/Robbyant/lingbot-vla.git
cd lingbot-vla
bash install.sh
```

---

## 📦 Model Download

We release LingBot-VLA pre-trained weights in two configurations: depth-free version and a depth-distilled version.

#### Pretrained Checkpoints for Post-Training with and without depth

| Model Name | Huggingface | ModelScope | Description |
| --- | --- | --- | --- |
| LingBot-VLA-4B | [🤗 lingbot-vla-4b](https://huggingface.co/robbyant/lingbot-vla-4b) | [🤖 lingbot-vla-4b](https://modelscope.cn/models/Robbyant/lingbot-vla-4b) | LingBot-VLA *w/o* Depth |
| LingBot-VLA-4B-Depth | [🤗 lingbot-vla-4b-depth](https://huggingface.co/robbyant/lingbot-vla-4b-depth) | [🤖 lingbot-vla-4b-depth](https://modelscope.cn/models/Robbyant/lingbot-vla-4b-depth) | LingBot-VLA *w/* Depth |

```
# Download Pretrained Checkpoints
python3 scripts/download_hf_model.py --repo_id robbyant/lingbot-vla-4b --local_dir lingbot-vla-4b
```

> ⚠️
>
> **Note for users who downloaded before 2026/05/01 (click to expand)**
>
> If you downloaded `LingBot-VLA-4B` or `LingBot-VLA-4B-Depth` before **2026/05/01**, you may encounter the following error when loading the model:
>
> ```
> draccus.utils.DecodingError: The fields \`resize_imgs_with_padding\`, \`adapt_to_pi_aloha\`, \`use_delta_joint_actions_aloha\`, \`proj_width\`, \`num_steps\`, \`use_cache\`, \`attention_implementation\`, \`freeze_vision_encoder\`, \`train_expert_only\`, \`train_state_proj\` are not valid for PI0Config
> ```
>
> This is caused by our migration from **LeRobot v2.1** to **v3.0**.
> To fix this, please **re-download the latest checkpoint**, or manually remove the above fields from `config.json` in your local `lingbot-vla-4b/` or `lingbot-vla-4b-depth/` directory.

To train LingBot with our codebase, weights from [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct), [MoGe-2-vitb-normal](https://huggingface.co/Ruicheng/moge-2-vitb-normal), and [LingBot-Depth](https://huggingface.co/robbyant/lingbot-depth-pretrain-vitl-14) are also required.

---

## 💻 Post-Training Example

### Data Preparation

Post-training requires three preparation steps. For a complete guide on customizing your own dataset, see the [Custom Data Guide](https://github.com/Robbyant/lingbot-vla/blob/main/lingbotvla/data/vla_data/README.md).

| Step | Description | Output |
| --- | --- | --- |
| 1\. Prepare LeRobot Dataset | Convert your demonstration data to [LeRobot v3.0](https://github.com/huggingface/lerobot) format | LeRobot dataset directory |
| 2\. Prepare Robot Config | Define feature mapping (states / actions / images) from raw keys to unified feature space | `configs/robot_configs/<data_name>.yaml` |
| 3\. Compute Norm Statistics | Calculate normalization statistics over your dataset | `assets/norm_stats/<name>.json` |

> **Note:** If you already have data in LeRobot v2.1 format, you can use [convert\_dataset\_v21\_to\_v30.py](https://github.com/huggingface/lerobot/blob/v0.4.2/src/lerobot/datasets/v30/convert_dataset_v21_to_v30.py) to quickly convert it to v3.0.

Below we use **RoboTwin 2.0** (5 tasks: "open\_microwave", "click\_bell", "stack\_blocks\_three", "place\_shoe", "put\_object\_cabinet") as an example.

- **Step 1 — RoboTwin Data**: Follow [RoboTwin2.0 Preparation](https://github.com/Robbyant/lingbot-vla/blob/main/experiment/robotwin/README.md) to download and convert.
- **Step 2 — Robot Config**: See [`configs/robot_configs/robotwin.yaml`](https://github.com/Robbyant/lingbot-vla/blob/main/configs/robot_configs/robotwin.yaml) for the RoboTwin feature mapping.
- **Step 3 — Normalization**: Pre-computed stats are provided at `assets/norm_stats/robotwin_50.json`. To recompute for a custom task subset, see the [Custom Data Guide](https://github.com/Robbyant/lingbot-vla/blob/main/lingbotvla/data/vla_data/README.md).

### Training

We provide a post-training example of LingBot-VLA on 5 RoboTwin 2.0 tasks ("open\_microwave", "click\_bell", "stack\_blocks\_three", "place\_shoe", "put\_object\_cabinet"):

```
# without depth
bash train.sh tasks/vla/train_lingbotvla.py ./configs/vla/robotwin_load20000h.yaml \
    --data.train_path /path/to/mixed_robotwin_5tasks \
    --data.data_name robotwin \
    --data.norm_stats_file assets/norm_stats/robotwin_50.json \
    --train.output_dir output/

# with depth
bash train.sh tasks/vla/train_lingbotvla.py ./configs/vla/robotwin_load20000h_depth.yaml \
    --data.train_path /path/to/mixed_robotwin_5tasks \
    --data.data_name robotwin \
    --data.norm_stats_file assets/norm_stats/robotwin_50.json \
    --train.output_dir output/
```

### 🤖 Real-Robot Post-Training

Also, we provide recommended training configurations specifically tailored for **real-world scenarios**: [`real_load20000h.yaml`](https://github.com/Robbyant/lingbot-vla/blob/main/configs/vla/real_load20000h.yaml) (w/o depth) and [`real_load20000h_depth.yaml`](https://github.com/Robbyant/lingbot-vla/blob/main/configs/vla/real_load20000h_depth.yaml) (w/ depth). For a detailed explanation of all training configuration parameters (batch size, gradient accumulation, training duration, checkpointing, depth injection, etc.), see the [Training Configuration Guide](https://github.com/Robbyant/lingbot-vla/blob/main/configs/vla/Training_Config.md).

### Evaluation

#### Open-Loop Eval

```
export QWEN25_PATH=Qwen/Qwen2.5-VL-3B-Instruct
python scripts/open_loop_eval.py --model_path path_to_posttraining_ckpt --data_path path_to_validation_data --use_length 50
# If \`--data_path\` is omitted, the script defaults to the training dataset specified in the YAML config (\`data.train_path\`).
```

> **Note:**
> For inference, the model path (`path_to_posttraining_ckpt`, located in `train.output_dir/checkpoints/*/hf_ckpt`) must include:
>
> - weights in `.safetensors` format
> - `config.json`
> - `lingbotvla_cli.yaml`

#### Robotwin

```
export QWEN25_PATH=path_to_Qwen2.5-VL-3B-Instruct
python -m deploy.lingbot_vla_policy \
 --model_path path_to_posttraining_ckpt \
 --use_compile \
 --use_length 50 \
 --port port
```

#### Real-Robot Deployment

```
export QWEN25_PATH=path_to_Qwen2.5-VL-3B-Instruct
python -m deploy.lingbot_vla_policy \
 --model_path path_to_posttraining_ckpt \
 --use_compile \
 --use_length 25
# You can set --num_denoising_step to 5 if you want to speed up the evaluation.
```

---

## 🏗️ Efficiency

[![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/QwenPI_PaliGemmaPI.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/QwenPI_PaliGemmaPI.png)

We evaluate the training efficiency of our codebase against established baselines for both **Qwen2.5-VL-3B-π** and **PaliGemma-3B-pt-224-π** models. The results demonstrate that our codebase achieved the fastest training speeds in both model settings. The above figures detail the training throughput across configurations of 8, 16, 32, 128, and 256 GPUs, alongside the theoretical linear scaling limit.

> **📢 Note on Throughput Metrics:** All throughput values (e.g., 261 samples/sec) represent the **total aggregate throughput across all GPUs**, not per-GPU performance.
> <sup>(Updated: Previously mislabeled as per-GPU in earlier versions. We apologize for the confusion.)</sup>

---

## 📊 Performance

Our LingBot-VLA achieves state-of-the-art results on real-world and simulation benchmarks:

- **GM-100 across 3 robot platforms**

<table><thead><tr><th rowspan="2">Platform</th><th colspan="2">WALL-OSS</th><th colspan="2">GR00T N1.6</th><th colspan="2">π <sub>0.5</sub></th><th colspan="2">Ours w/o depth</th><th colspan="2">Ours w/ depth</th></tr><tr><th>SR</th><th>PS</th><th>SR</th><th>PS</th><th>SR</th><th>PS</th><th>SR</th><th>PS</th><th>SR</th><th>PS</th></tr></thead><tbody><tr><td>Agibot G1</td><td>2.99%</td><td>8.75%</td><td>5.23%</td><td>12.63%</td><td>7.77%</td><td>21.98%</td><td><b>12.82%</b></td><td>30.04%</td><td>11.98%</td><td><b>30.47%</b></td></tr><tr><td>AgileX</td><td>2.26%</td><td>8.16%</td><td>3.26%</td><td>10.52%</td><td>17.20%</td><td>34.82%</td><td>15.50%</td><td>36.31%</td><td><b>18.93%</b></td><td><b>40.36%</b></td></tr><tr><td>Galaxea R1Pro</td><td>6.89%</td><td>14.13%</td><td>14.29%</td><td>24.83%</td><td>14.10%</td><td>26.14%</td><td>18.89%</td><td>34.71%</td><td><b>20.98%</b></td><td><b>35.40%</b></td></tr><tr><td><b>Average</b></td><td>4.05%</td><td>10.35%</td><td>7.59%</td><td>15.99%</td><td>13.02%</td><td>27.65%</td><td>15.74%</td><td>33.69%</td><td><b>17.30%</b></td><td><b>35.41%</b></td></tr></tbody></table>

- **RoboTwin 2.0 (Clean and Randomized)**

<table><thead><tr><th rowspan="2"><b>Simulation Tasks</b></th><th colspan="2"><b>π <sub>0.5</sub></b></th><th colspan="2"><b>Ours w/o depth</b></th><th colspan="2"><b>Ours w/ depth</b></th></tr><tr><th><b>Clean</b></th><th><b>Rand.</b></th><th><b>Clean</b></th><th><b>Rand.</b></th><th><b>Clean</b></th><th><b>Rand.</b></th></tr></thead><tbody><tr><td><b>Average SR</b></td><td>82.74%</td><td>76.76%</td><td>86.50%</td><td>85.34%</td><td>88.56%</td><td>86.68%</td></tr></tbody></table>

📢 We have released our checkpoints of LingBot-VLA-Posttrain-Robotwin:

| Model Name | Huggingface | ModelScope | Description |
| --- | --- | --- | --- |
| LingBot-VLA-4B-Posttrain-Robotwin | [🤗 lingbot-vla-4b-posttrain-robotwin](https://huggingface.co/robbyant/lingbot-vla-4b-posttrain-robotwin) | [🤖 lingbot-vla-4b-posttrain-robotwin](https://modelscope.cn/models/Robbyant/lingbot-vla-4b-posttrain-robotwin) | LingBot-VLA-Posttrain-Robotwin *w/o* Depth |
| LingBot-VLA-4B-Depth-Posttrain-Robotwin | [🤗 lingbot-vla-4b-depth-posttrain-robotwin](https://huggingface.co/robbyant/lingbot-vla-4b-depth-posttrain-robotwin) | [🤖 lingbot-vla-4b-depth-posttrain-robotwin](https://modelscope.cn/models/Robbyant/lingbot-vla-4b-depth-posttrain-robotwin) | LingBot-VLA-Posttrain-Robotwin *w/* Depth |

> ⚠️
>
> **Note for users who downloaded before 2026/05/01 (click to expand)**
>
> If you downloaded `lingbot-vla-4b-posttrain-robotwin` or `lingbot-vla-4b-depth-posttrain-robotwin` before **2026/05/01**, you may encounter the following error when loading the model:
>
> ```
> draccus.utils.DecodingError: The fields \`resize_imgs_with_padding\`, \`adapt_to_pi_aloha\`, \`use_delta_joint_actions_aloha\`, \`proj_width\`, \`num_steps\`, \`use_cache\`, \`attention_implementation\`, \`freeze_vision_encoder\`, \`train_expert_only\`, \`train_state_proj\` are not valid for PI0Config
> ```
>
> To fix this, please re-download the latest checkpoint, or manually remove the above fields from `config.json` and add them to the `train` section of `lingbotvla_cli.yaml` in your local directory.

[![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/exp-gm-100.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/exp-gm-100.png) [![](https://github.com/Robbyant/lingbot-vla/raw/main/assets/exp-robotwin.png)](https://github.com/Robbyant/lingbot-vla/blob/main/assets/exp-robotwin.png)

---

## 📝 Citation

If you find our work useful in your research, feel free to give us a cite.

```
@article{wu2026pragmatic,
  title={A Pragmatic VLA Foundation Model},
  ={Wei Wu and Fan Lu and Yunnan Wang and Shuai Yang and Shi Liu and Fangjing Wang and Shuailei Ma and He Sun and Yong Wang and Zhenqi Qiu and Houlong Xiong and Ziyu Wang and Shuai Zhou and Yiyu Ren and Kejia Zhang and Hui Yu and Jingmei Zhao and Qian Zhu and Ran Cheng and Yong-Lu Li and Yongtao Huang and Xing Zhu and Yujun Shen and Kecheng Zheng},
  journal={arXiv preprint arXiv:2601.18692v1},
  year={2026}
}
```

---

## 📄 License Agreement

This project is licensed under the [Apache-2.0 License](https://github.com/Robbyant/lingbot-vla/blob/main/LICENSE).

## 😊 Acknowledgement

We would like to express our sincere gratitude to the developers of [VeOmni](https://arxiv.org/abs/2508.02317), [LeRobot](https://github.com/huggingface/lerobot#), and Baidu Cloud for their technical support. This project benefits significantly from their outstanding work and contributions. Baidu Cloud's optimization solutions notably reduced our GPU memory consumption by **29.2%** during model training.
