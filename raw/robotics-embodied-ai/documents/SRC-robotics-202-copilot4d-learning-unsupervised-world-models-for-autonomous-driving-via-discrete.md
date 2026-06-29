---
source_id: "SRC-robotics-202"
title: "Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion"
source_type: "paper"
publisher: "arXiv"
source_date: "2023-11-01"
url: "https://arxiv.org/abs/2311.01017"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-202
---
# Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion

## Title:Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion

Authors:[Lunjun Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+L), [Yuwen Xiong](https://arxiv.org/search/cs?searchtype=author&query=Xiong,+Y), [Ze Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Z), [Sergio Casas](https://arxiv.org/search/cs?searchtype=author&query=Casas,+S), [Rui Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+R), [Raquel Urtasun](https://arxiv.org/search/cs?searchtype=author&query=Urtasun,+R)

[View PDF](https://arxiv.org/pdf/2311.01017) [HTML (experimental)](https://arxiv.org/html/2311.01017v4)

> Abstract:Learning world models can teach an agent how the world works in an unsupervised manner. Even though it can be viewed as a special case of sequence modeling, progress for scaling world models on robotic applications such as autonomous driving has been somewhat less rapid than scaling language models with Generative Pre-trained Transformers (GPT). We identify two reasons as major bottlenecks: dealing with complex and unstructured observation space, and having a scalable generative model. Consequently, we propose Copilot4D, a novel world modeling approach that first tokenizes sensor observations with VQVAE, then predicts the future via discrete diffusion. To efficiently decode and denoise tokens in parallel, we recast Masked Generative Image Transformer as discrete diffusion and enhance it with a few simple changes, resulting in notable improvement. When applied to learning world models on point cloud observations, Copilot4D reduces prior SOTA Chamfer distance by more than 65% for 1s prediction, and more than 50% for 3s prediction, across NuScenes, KITTI Odometry, and Argoverse2 datasets. Our results demonstrate that discrete diffusion on tokenized agent experience can unlock the power of GPT-like unsupervised learning for robotics.

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Robotics (cs.RO) |
| Cite as: | [arXiv:2311.01017](https://arxiv.org/abs/2311.01017) \[cs.CV\] |
|  | (or [arXiv:2311.01017v4](https://arxiv.org/abs/2311.01017v4) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2311.01017](https://doi.org/10.48550/arXiv.2311.01017) |

## Submission history

From: Lunjun Zhang \[[view email](https://arxiv.org/show-email/eb7180d5/2311.01017)\]  
**[\[v1\]](https://arxiv.org/abs/2311.01017v1)** Thu, 2 Nov 2023 06:21:56 UTC (40,188 KB)  
**[\[v2\]](https://arxiv.org/abs/2311.01017v2)** Fri, 24 Nov 2023 00:24:06 UTC (40,943 KB)  
**[\[v3\]](https://arxiv.org/abs/2311.01017v3)** Tue, 16 Jan 2024 18:02:27 UTC (39,838 KB)  
**\[v4\]** Mon, 1 Apr 2024 15:41:50 UTC (39,838 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2311.01017) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
