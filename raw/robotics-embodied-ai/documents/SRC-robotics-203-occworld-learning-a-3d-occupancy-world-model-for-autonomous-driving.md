---
source_id: "SRC-robotics-203"
title: "OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving"
source_type: "paper"
publisher: "arXiv"
source_date: "2023-11-27"
url: "https://arxiv.org/abs/2311.16038"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-203
---
# OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving

## Title:OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving

Authors:[Wenzhao Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+W), [Weiliang Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+W), [Yuanhui Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+Y), [Borui Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+B), [Yueqi Duan](https://arxiv.org/search/cs?searchtype=author&query=Duan,+Y), [Jiwen Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+J)

[View PDF](https://arxiv.org/pdf/2311.16038)

> Abstract:Understanding how the 3D scene evolves is vital for making decisions in autonomous driving. Most existing methods achieve this by predicting the movements of object boxes, which cannot capture more fine-grained scene information. In this paper, we explore a new framework of learning a world model, OccWorld, in the 3D Occupancy space to simultaneously predict the movement of the ego car and the evolution of the surrounding scenes. We propose to learn a world model based on 3D occupancy rather than 3D bounding boxes and segmentation maps for three reasons: 1) expressiveness. 3D occupancy can describe the more fine-grained 3D structure of the scene; 2) efficiency. 3D occupancy is more economical to obtain (e.g., from sparse LiDAR points). 3) versatility. 3D occupancy can adapt to both vision and LiDAR. To facilitate the modeling of the world evolution, we learn a reconstruction-based scene tokenizer on the 3D occupancy to obtain discrete scene tokens to describe the surrounding scenes. We then adopt a GPT-like spatial-temporal generative transformer to generate subsequent scene and ego tokens to decode the future occupancy and ego trajectory. Extensive experiments on the widely used nuScenes benchmark demonstrate the ability of OccWorld to effectively model the evolution of the driving scenes. OccWorld also produces competitive planning results without using instance and map supervision. Code: [this https URL](https://github.com/wzzheng/OccWorld).

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2311.16038](https://arxiv.org/abs/2311.16038) \[cs.CV\] |
|  | (or [arXiv:2311.16038v1](https://arxiv.org/abs/2311.16038v1) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2311.16038](https://doi.org/10.48550/arXiv.2311.16038) |

## Submission history

From: Wenzhao Zheng \[[view email](https://arxiv.org/show-email/febb4e32/2311.16038)\]  
**\[v1\]** Mon, 27 Nov 2023 17:59:41 UTC (8,857 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2311.16038) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
