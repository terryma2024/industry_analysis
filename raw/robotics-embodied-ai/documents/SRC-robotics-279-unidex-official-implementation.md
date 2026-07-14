---
source_id: "SRC-robotics-279"
title: "UniDex official implementation"
source_type: "code_repository"
publisher: "UniDex authors"
source_date: "2026"
url: "https://github.com/unidex-ai/UniDex"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T02:34:32+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/a
aliases:
  - SRC-robotics-279
---
# UniDex official implementation

## UniDex

[![UniDex teaser](https://github.com/unidex-ai/UniDex/raw/main/assets/new_teaser.png)](https://github.com/unidex-ai/UniDex/blob/main/assets/new_teaser.png)

**Official implementation of the CVPR 2026 paper**  
**UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos**

[![arXiv](https://camo.githubusercontent.com/02ba5da4d239bf47c47665226b8880e4657eab2f892aac816166cd985a05650d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323630332e32323236342d6466326132612e737667)](https://arxiv.org/html/2603.22264) [![Project Page](https://camo.githubusercontent.com/e14a655eb52c3862564b1b7811dec0a341f79c002768a71bff669b9c0130812e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d506167652d61)](https://unidex-ai.github.io/) [![Hugging Face Model](https://camo.githubusercontent.com/6277032f67e1c404ded866b18d8c1c89130df96b0773d1030512320ea39f1ffc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48756767696e67253230466163652d4d6f64656c2d79656c6c6f77)](https://huggingface.co/UniDex-ai/UniDex) [![License](https://camo.githubusercontent.com/08cef40a9105b6526ca22088bc514fbfdbc9aac1ddbf8d4e6c750e3a88a44dca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667)](https://github.com/unidex-ai/UniDex/blob/main/LICENSE)

UniDex provides the codebase for dataset preparation, hand retargeting, pre-training, and finetuning for universal dexterous hand control from egocentric human videos.

## Table of Contents

## Overview

This repository includes:

- environment setup and dependency instructions
- dataset preparation for H2O, HOI4D, Hot3D, and Taco
- retargeting from human hand motion to multiple robot hands
- pre-training and real-world post-training pipelines

## Setup

Detailed environment instructions are available in [doc/SETUP.md](https://github.com/unidex-ai/UniDex/blob/main/doc/SETUP.md). A minimal setup looks like:

```
conda create -n unidex python=3.10 -y
conda activate unidex
pip install -r requirements.txt
pip install -e .
```

You also need to install `pytorch3d` and `manopth` separately:

```
git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d
pip install -e .
cd ..

git clone https://github.com/hassony2/manopth.git
cd manopth
pip install -e .
cd ..
```

Then download the required pretrained assets:

- Uni3D point-cloud encoder
- PaliGemma tokenizer and weights
- MANO hand model
- optionally `SAM2` and `WiLoR` for full Taco preprocessing

Please refer to [doc/SETUP.md](https://github.com/unidex-ai/UniDex/blob/main/doc/SETUP.md) for the exact commands and paths.

## Dataset

### Pre-train Datasets

All pre-train datasets will be under the `data/` directory by default. After all processing, it will take up to 80TB of disk space. So make full use of soft links to avoid `No space Left on Device`.

Before starting, download datasets annotations from our Hugging Face repository:

```
hf download UniDex-ai/UniDex --include dataset_annotations/* --local-dir .
```

#### H2o (2 Hands and Objects)

Download all `subjectX_ego_v1_1.tar.gz` (X=1,2,3,4) files from [H2o official website](https://h2odataset.ethz.ch/) and unpack them under `data/H2o/all_img`. After unpacking, the directory structure should look like:

```
H2o/
└── all_img/
    ├── subject1_ego/
    ├── subject2_ego/
    ├── subject3_ego/
    └── subject4_ego/
```

For language instructions, run the following command:

```
# Assuming you are in the root directory of the project
cd data/H2o
cp ../../dataset_annotations/H2o_annotations.tar.gz .
tar -xzvf H2o_annotations.tar.gz
rm H2o_annotations.tar.gz
cd ../..
```

#### HOI4D (4D Egocentric Dataset for Category-Level Human-Object Interaction)

From [HOI4D official website](https://hoi4d.github.io/), download `HOI4D_color`, `HOI4D_depth`, `HOI4D_annotation` and unpack them under `data/HOI4D/HOI4D_release`. Also download `HOI4D_Handpose` and `HOI4D_cameras` and unpack them under `data/HOI4D/Hand_pose` and `data/HOI4D/camera` respectively. After unpacking, the directory structure should look like:

```
HOI4D/
├── HOI4D_release/
│   ├── ZY20210800001/
│   │   ├── H1/
│   │   │   ├── C1/
│   │   │   │   ├── N01/
│   │   │   │   │   ├── S000/
│   │   │   │   │   │   ├── s01/
│   │   │   │   │   │   │   ├── T1/
│   │   │   │   │   │   │   │   ├── align_rgb/
│   │   │   │   │   │   │   │   ├── align_depth/
│   │   │   │   │   │   │   │   ├── 2Dseg/
│   │   │   │   │   │   │   │   └── ...
│   │   │   │   │   │   │   └── ...
│   │   │   │   │   │   └── ...
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── camera/
└── Hand_pose/
```

Then run the following command to unpack the rgb and depth images from video files:

```
# Assuming you are in the root directory of the project
python scripts/process_HOI4D.py
```

#### Hot3D (An egocentric dataset for 3D hand and object tracking)

Follow instructions from [Hot3D github repository](https://github.com/facebookresearch/hot3d) to download the dataset and put them under `data/hot3d/`. After unpacking, the directory structure should look like:

```
├── P0001_4bf4e21a/
├── ...
└── P0020_ff537251/
```

We manually labeled all language instructions for Hot3D. To add them to the dataset, run the following command:

```
# Assuming you are in the root directory of the project
cd data/hot3d
cp ../../dataset_annotations/hot3d_prompts.tar.gz .
tar -xzvf hot3d_prompts.tar.gz
rm hot3d_prompts.tar.gz
cd ../..
```

#### Taco (Benchmarking Generalizable Bimanual Tool-ACtion-Object Understanding)

Download the Taco dataset from [Taco dataset](https://www.dropbox.com/scl/fo/8w7xir110nbcnq8uo1845/AOaHUxGEcR0sWvfmZRQQk9g?rlkey=xnhajvn71ua5i23w75la1nidx&e=2&st=9t8ofde7&dl=0), including `Egocentric_RGB_Videos`, `Egocentric_Depth_Videos`, `Egocentric_Camera_Parameters` and `Hand_Poses`. After unpacking, the directory structure should look like:

```
├── Egocentric_RGB_Videos/
├── Egocentric_Depth_Videos/
├── Egocentric_Camera_Parameters/
└── Hand_Poses/
```

Then run the following command to process the Taco dataset:

```
# Assuming you are in the root directory of the project
python scripts/process_Taco.py
```

### Staged Results

If you have followed the intructions above, you should have your `data/` directory structured as follows:

```
data/
├── H2o/
│   ├── all_img/
│   │   ├── subject1_ego/
│   │   ├── subject2_ego/
│   │   ├── subject3_ego/
│   │   └── subject4_ego/
│   └── annotation/
├── HOI4D/
│   ├── HOI4D_release/
│   ├── camera/
│   └── Hand_pose/
├── hot3d/
│   ├── P0001_4bf4e21a/
│   ...
│   └── P0020_ff537251/
└── Taco/
    ├── Egocentric_RGB_Videos/
    ├── Egocentric_Depth_Videos/
    ├── Egocentric_Camera_Parameters/
    └── Hand_Poses/
```

### Retarget Robotic Hands

To generate retargeted robotic hand data from the above datasets, run the following command:

```
python HandAdapter/hand_processor.py --hand_type {Allegro, Ability, Inspire, Leap, Oymotion, Shadow, Wuji, Xhand} --dataset {H2o, HOI4D, Hot3D, Taco} --cont
```

You can add `--randperm` to randomly permute the data order for parallel processing. The retargeted data will be saved under `data/${dataset}/retarget_RGBD/${sequence_relative_path}/${hand_type}.h5` by default.

### Add New Robotic Hands

First place your new hand urdf files under `HandAdapter/urdf/base`, where left and right hand urdf files should be named as `left/main.urdf` and `right/main.urdf` respectively. Then add a `config.json` file under `HandAdapter/urdf/${YourHandName}/config.json` to specify the parameters for your new hand, following the format of existing config files.

Then ensure the coordinate frame of the new hand URDF is set so that the X-axis points into the palm and the Z-axis points along the fingers. Also add the new hand type to the `HAND_TYPES` list in `HandAdapter/visualizer.py`.

Finally run `python HandAdapter/visualizer.py` and adjust inverse kinematics parameters of the new hand on all datasets in the web interface until satisfactory retargeting results are achieved. Now you can use the new hand type in `hand_processor.py` to generate retargeted data.

## Pre-training

After setting up the datasets and pretrained assets, launch UniDex pre-training with the default config:

```
python train.py
```

The default setup in [config/train.yaml](https://github.com/unidex-ai/UniDex/blob/main/config/train.yaml) uses:

- `8` GPUs
- `batch_size = 4`
- `accumulate_grad_batches = 4`
- `max_epochs = 32`

If you only want to finetune from the released checkpoints, you can skip the full pre-training dataset setup.

## Finetuning

Real-world post-training is launched with:

```
python finetune.py
```

Before running it, update [config/finetune.yaml](https://github.com/unidex-ai/UniDex/blob/main/config/finetune.yaml) to point to:

- your pretrained checkpoint
- your real-world dataset
- your preferred run name and hardware configuration

The default finetuning config uses `2` GPUs and loads a pretrained checkpoint from `train.load_checkpoint`.

## Checkpoints and Model Assets

We provide UniDex checkpoints and released assets on [Hugging Face](https://huggingface.co/UniDex-ai/UniDex).

## Acknowledgement

Our code is built upon: [open-pi-zero](https://github.com/allenzren/open-pi-zero) and [Uni3D](https://github.com/baaivision/Uni3D). We thank all these authors for their open sourced code.

Contact [Gu Zhang](https://github.com/unidex-ai/UniDex/blob/main/www.gu-zhang.com) and [Qicheng Xu](https://github.com/unidex-ai/UniDex/blob/main/xuqc24@mails.tsinghua.edu.cn) if you have more questions.

## Citation

If you find UniDex useful, please cite:

```
@article{zhang2026unidex,
  title={UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos},
  ={Zhang, Gu and Xu, Qicheng and Zhang, Haozhe and Ma, Jianhan and He, Long and Bao, Yiming and Ping, Zeyu and Yuan, Zhecheng and Lu, Chenhao and Yuan, Chengbo and others},
  journal={arXiv preprint arXiv:2603.22264},
  year={2026}
}
```
