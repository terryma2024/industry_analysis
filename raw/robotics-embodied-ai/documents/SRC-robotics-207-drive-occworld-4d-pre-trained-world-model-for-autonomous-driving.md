---
source_id: "SRC-robotics-207"
title: "Drive-OccWorld: 4D Pre-trained World Model for Autonomous Driving"
source_type: "paper"
publisher: "arXiv"
source_date: "2024-08-25"
url: "https://arxiv.org/abs/2408.14197"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-207
---
# Drive-OccWorld: 4D Pre-trained World Model for Autonomous Driving

## Title:Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving

Authors:[Yu Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Y), [Jianbiao Mei](https://arxiv.org/search/cs?searchtype=author&query=Mei,+J), [Yukai Ma](https://arxiv.org/search/cs?searchtype=author&query=Ma,+Y), [Siliang Du](https://arxiv.org/search/cs?searchtype=author&query=Du,+S), [Wenqing Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+W), [Yijie Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+Y), [Yuxiang Feng](https://arxiv.org/search/cs?searchtype=author&query=Feng,+Y), [Yong Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Y)

[View PDF](https://arxiv.org/pdf/2408.14197) [HTML (experimental)](https://arxiv.org/html/2408.14197v3)

> Abstract:World models envision potential future states based on various ego actions. They embed extensive knowledge about the driving environment, facilitating safe and scalable autonomous driving. Most existing methods primarily focus on either data generation or the pretraining paradigms of world models. Unlike the aforementioned prior works, we propose Drive-OccWorld, which adapts a vision-centric 4D forecasting world model to end-to-end planning for autonomous driving. Specifically, we first introduce a semantic and motion-conditional normalization in the memory module, which accumulates semantic and dynamic information from historical BEV embeddings. These BEV features are then conveyed to the world decoder for future occupancy and flow forecasting, considering both geometry and spatiotemporal modeling. Additionally, we propose injecting flexible action conditions, such as velocity, steering angle, trajectory, and commands, into the world model to enable controllable generation and facilitate a broader range of downstream applications. Furthermore, we explore integrating the generative capabilities of the 4D world model with end-to-end planning, enabling continuous forecasting of future states and the selection of optimal trajectories using an occupancy-based cost function. Comprehensive experiments conducted on the nuScenes, nuScenes-Occupancy, and Lyft-Level5 datasets illustrate that our method can generate plausible and controllable 4D occupancy, paving the way for advancements in driving world generation and end-to-end planning. Project page: [this https URL](https://drive-occworld.github.io/)

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV) |
| Cite as: | [arXiv:2408.14197](https://arxiv.org/abs/2408.14197) \[cs.CV\] |
|  | (or [arXiv:2408.14197v3](https://arxiv.org/abs/2408.14197v3) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2408.14197](https://doi.org/10.48550/arXiv.2408.14197) |

## Submission history

From: Yu Yang \[[view email](https://arxiv.org/show-email/3ff516c1/2408.14197)\]  
**[\[v1\]](https://arxiv.org/abs/2408.14197v1)** Mon, 26 Aug 2024 11:53:09 UTC (37,278 KB)  
**[\[v2\]](https://arxiv.org/abs/2408.14197v2)** Sat, 12 Oct 2024 06:36:28 UTC (37,278 KB)  
**\[v3\]** Fri, 17 Jan 2025 06:46:00 UTC (37,276 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2408.14197) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
