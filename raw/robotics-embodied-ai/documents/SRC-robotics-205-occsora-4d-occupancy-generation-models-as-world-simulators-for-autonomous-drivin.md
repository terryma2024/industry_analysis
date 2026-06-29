---
source_id: "SRC-robotics-205"
title: "OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving"
source_type: "paper"
publisher: "arXiv"
source_date: "2024-05-30"
url: "https://arxiv.org/abs/2405.20337"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-205
---
# OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving

## Title:OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving

Authors:[Lening Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+L), [Wenzhao Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+W), [Yilong Ren](https://arxiv.org/search/cs?searchtype=author&query=Ren,+Y), [Han Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+H), [Zhiyong Cui](https://arxiv.org/search/cs?searchtype=author&query=Cui,+Z), [Haiyang Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+H), [Jiwen Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+J)

[View PDF](https://arxiv.org/pdf/2405.20337) [HTML (experimental)](https://arxiv.org/html/2405.20337v1)

> Abstract:Understanding the evolution of 3D scenes is important for effective autonomous driving. While conventional methods mode scene development with the motion of individual instances, world models emerge as a generative framework to describe the general scene dynamics. However, most existing methods adopt an autoregressive framework to perform next-token prediction, which suffer from inefficiency in modeling long-term temporal evolutions. To address this, we propose a diffusion-based 4D occupancy generation model, OccSora, to simulate the development of the 3D world for autonomous driving. We employ a 4D scene tokenizer to obtain compact discrete spatial-temporal representations for 4D occupancy input and achieve high-quality reconstruction for long-sequence occupancy videos. We then learn a diffusion transformer on the spatial-temporal representations and generate 4D occupancy conditioned on a trajectory prompt. We conduct extensive experiments on the widely used nuScenes dataset with Occ3D occupancy annotations. OccSora can generate 16s-videos with authentic 3D layout and temporal consistency, demonstrating its ability to understand the spatial and temporal distributions of driving scenes. With trajectory-aware 4D generation, OccSora has the potential to serve as a world simulator for the decision-making of autonomous driving. Code is available at: [this https URL](https://github.com/wzzheng/OccSora).

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI) |
| Cite as: | [arXiv:2405.20337](https://arxiv.org/abs/2405.20337) \[cs.CV\] |
|  | (or [arXiv:2405.20337v1](https://arxiv.org/abs/2405.20337v1) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2405.20337](https://doi.org/10.48550/arXiv.2405.20337) |

## Submission history

From: Wenzhao Zheng \[[view email](https://arxiv.org/show-email/1b315fd6/2405.20337)\]  
**\[v1\]** Thu, 30 May 2024 17:59:42 UTC (4,577 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2405.20337) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
