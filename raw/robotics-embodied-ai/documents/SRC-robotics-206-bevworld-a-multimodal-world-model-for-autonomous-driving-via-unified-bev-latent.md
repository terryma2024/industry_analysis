---
source_id: "SRC-robotics-206"
title: "BEVWorld: A Multimodal World Model for Autonomous Driving via Unified BEV Latent Space"
source_type: "paper"
publisher: "arXiv"
source_date: "2024-07-07"
url: "https://arxiv.org/abs/2407.05679"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-206
---
# BEVWorld: A Multimodal World Model for Autonomous Driving via Unified BEV Latent Space

## Title:BEVWorld: A Multimodal World Simulator for Autonomous Driving via Scene-Level BEV Latents

Authors:[Yumeng Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Y), [Shi Gong](https://arxiv.org/search/cs?searchtype=author&query=Gong,+S), [Kaixin Xiong](https://arxiv.org/search/cs?searchtype=author&query=Xiong,+K), [Xiaoqing Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+X), [Xiaofan Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+X), [Xiao Tan](https://arxiv.org/search/cs?searchtype=author&query=Tan,+X), [Fan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+F), [Jizhou Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+J), [Hua Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+H), [Haifeng Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+H)

[View PDF](https://arxiv.org/pdf/2407.05679) [HTML (experimental)](https://arxiv.org/html/2407.05679v3)

> Abstract:World models have attracted increasing attention in autonomous driving for their ability to forecast potential future scenarios. In this paper, we propose BEVWorld, a novel framework that transforms multimodal sensor inputs into a unified and compact Bird's Eye View (BEV) latent space for holistic environment modeling. The proposed world model consists of two main components: a multi-modal tokenizer and a latent BEV sequence diffusion model. The multi-modal tokenizer first encodes heterogeneous sensory data, and its decoder reconstructs the latent BEV tokens into LiDAR and surround-view image observations via ray-casting rendering in a self-supervised manner. This enables joint modeling and bidirectional encoding-decoding of panoramic imagery and point cloud data within a shared spatial representation. On top of this, the latent BEV sequence diffusion model performs temporally consistent forecasting of future scenes, conditioned on high-level action tokens, enabling scene-level reasoning over time. Extensive experiments demonstrate the effectiveness of BEVWorld on autonomous driving benchmarks, showcasing its capability in realistic future scene generation and its benefits for downstream tasks such as perception and motion prediction.

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI) |
| Cite as: | [arXiv:2407.05679](https://arxiv.org/abs/2407.05679) \[cs.CV\] |
|  | (or [arXiv:2407.05679v3](https://arxiv.org/abs/2407.05679v3) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2407.05679](https://doi.org/10.48550/arXiv.2407.05679) |

## Submission history

From: Yumeng Zhang \[[view email](https://arxiv.org/show-email/d33bdc08/2407.05679)\]  
**[\[v1\]](https://arxiv.org/abs/2407.05679v1)** Mon, 8 Jul 2024 07:26:08 UTC (30,536 KB)  
**[\[v2\]](https://arxiv.org/abs/2407.05679v2)** Thu, 18 Jul 2024 08:33:43 UTC (24,889 KB)  
**\[v3\]** Wed, 30 Apr 2025 13:43:51 UTC (31,614 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2407.05679) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
