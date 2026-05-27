---
source_id: "SRC-robotics-075"
title: "Dobb-E: On Bringing Robots Home"
source_type: "project_page"
publisher: "New York University and collaborators"
source_date: "2023"
url: "https://www.dobb-e.com/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-05-27T01:34:04+00:00"
tags:
  - raw/source
  - source-type/project-page
  - evidence/a
aliases:
  - SRC-robotics-075
---
# Dobb-E: On Bringing Robots Home

## Hardware

## The Stick

<video controls="" src="https://www.dobb-e.com/mfiles/stick_loop_compressed.mp4"></video>

We believe one of the largest roadblocks to safe and scalable progress in home robotics, especially in imitation learning based approaches, is the lack of a cheap, ergonomic, and easy way to collect demonstrations for robots.

To address this, we built the **Stick**, a demonstration collection tool we built out of a $25 Reacher-grabber stick, some 3D printed parts, and an iPhone.

[Get the reacher-grabber](https://amazon.com/Vive-Foldable-Suction-Reacher-Grabber/dp/B08BPGJVRB/)

[Download the 3D files](https://github.com/notmahi/dobb-e/tree/main/hardware)

[Build and usage guide](https://docs.dobb-e.com/hardware/putting-together-the-stick)

[Dataset creation code](https://github.com/notmahi/dobb-e/tree/main/stick-data-collection)

## Dataset

## Homes of New York (HoNY)

22 homes

216 environments

5620 trajectories

13 hours

1.5 million frames

Homes of New York (HoNY) is a dataset containing 13 hours of interactions at 22 different homes of New York City collected with the [Stick](#hardware). The dataset contains RGB and depth videos at 30 fps, as well as full action annotations for 6D pose of the gripper as well as the gripper's opening angle normalized between (0, 1).

[RGB + actions dataset (814 MB)](https://dl.dobb-e.com/datasets/homes_of_new_york.zip)

[RGB-D + actions dataset (77 GB)](https://drive.google.com/drive/folders/1o8c6b6hSKfId8EzemVGf8c7DQoZ2IHAO?usp=sharing)

## Model

## Home Pretrained Representations (HPR)

![HPR](https://www.dobb-e.com/mfiles/images/robot_method.svg)

Home Pretrained Representation (HPR) is a model pre-trained on the [HoNY dataset](#dataset) that we used to initialize a robot policy to perform a new task in a novel enviroment. HPR is a ResNet-34 model trained on the [HoNY dataset](#dataset) using the [MoCo-v3](https://github.com/facebookresearch/moco-v3) self-supervised learning objective.

During deployment,we used HPR to initialize a policy, the trunk of which was simply our pretrained ResNet-34 model followed by two linear layers on top.

[🤗 Get the model at Huggingface](https://huggingface.co/notmahi/dobb-e)

Or if you are using 🤗 [Pytorch Image Models (TIMM)](https://huggingface.co/timm), you can simply start using it in a couple of lines:

```
import timm

model = timm.create_model(
    "hf-hub:notmahi/dobb-e",
    pretrained=True
)
```
```
import timm

model = timm.create_model("hf-hub:notmahi/dobb-e", pretrained=True)
```

## Paper

## On Bringing Robots Home

[![Paper](https://www.dobb-e.com/mfiles/images/paper_preview.jpg)

](https://arxiv.org/abs/2311.16098)

[Read the paper (Arxiv)](https://arxiv.org/abs/2311.16098)

[Read the paper (PDF)](https://www.dobb-e.com/mfiles/paper/On_Bringing_Robots_Home.pdf)

[Citation (bibtex)](https://www.dobb-e.com/more/bibtex.txt)

```
@article{shafiullah2023bringing,
  title={On bringing robots home},
  author={Shafiullah, Nur Muhammad Mahi and Rai, Anant and Etukuru, Haritheja and Liu, Yiqian and Misra, Ishan and Chintala, Soumith and Pinto, Lerrel},
  journal={arXiv preprint arXiv:2311.16098},
  year={2023}
}
```
