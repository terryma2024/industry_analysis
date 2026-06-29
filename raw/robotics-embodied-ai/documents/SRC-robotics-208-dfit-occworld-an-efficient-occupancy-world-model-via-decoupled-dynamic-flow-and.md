---
source_id: "SRC-robotics-208"
title: "DFIT-OccWorld: An Efficient Occupancy World Model via Decoupled Dynamic Flow and Image-assisted Training"
source_type: "paper"
publisher: "arXiv"
source_date: "2024-12-18"
url: "https://arxiv.org/abs/2412.13772"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-208
---
# DFIT-OccWorld: An Efficient Occupancy World Model via Decoupled Dynamic Flow and Image-assisted Training

## Title:An Efficient Occupancy World Model via Decoupled Dynamic Flow and Image-assisted Training

Authors:[Haiming Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+H), [Ying Xue](https://arxiv.org/search/cs?searchtype=author&query=Xue,+Y), [Xu Yan](https://arxiv.org/search/cs?searchtype=author&query=Yan,+X), [Jiacheng Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+J), [Weichao Qiu](https://arxiv.org/search/cs?searchtype=author&query=Qiu,+W), [Dongfeng Bai](https://arxiv.org/search/cs?searchtype=author&query=Bai,+D), [Bingbing Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+B), [Shuguang Cui](https://arxiv.org/search/cs?searchtype=author&query=Cui,+S), [Zhen Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z)

[View PDF](https://arxiv.org/pdf/2412.13772) [HTML (experimental)](https://arxiv.org/html/2412.13772v1)

> Abstract:The field of autonomous driving is experiencing a surge of interest in world models, which aim to predict potential future scenarios based on historical observations. In this paper, we introduce DFIT-OccWorld, an efficient 3D occupancy world model that leverages decoupled dynamic flow and image-assisted training strategy, substantially improving 4D scene forecasting performance. To simplify the training process, we discard the previous two-stage training strategy and innovatively reformulate the occupancy forecasting problem as a decoupled voxels warping process. Our model forecasts future dynamic voxels by warping existing observations using voxel flow, whereas static voxels are easily obtained through pose transformation. Moreover, our method incorporates an image-assisted training paradigm to enhance prediction reliability. Specifically, differentiable volume rendering is adopted to generate rendered depth maps through predicted future volumes, which are adopted in render-based photometric consistency. Experiments demonstrate the effectiveness of our approach, showcasing its state-of-the-art performance on the nuScenes and OpenScene benchmarks for 4D occupancy forecasting, end-to-end motion planning and point cloud forecasting. Concretely, it achieves state-of-the-art performances compared to existing 3D world models while incurring substantially lower computational costs.

| Subjects: | Computer Vision and Pattern Recognition (cs.CV) |
| --- | --- |
| Cite as: | [arXiv:2412.13772](https://arxiv.org/abs/2412.13772) \[cs.CV\] |
|  | (or [arXiv:2412.13772v1](https://arxiv.org/abs/2412.13772v1) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2412.13772](https://doi.org/10.48550/arXiv.2412.13772) |

## Submission history

From: Haiming Zhang \[[view email](https://arxiv.org/show-email/01268221/2412.13772)\]  
**\[v1\]** Wed, 18 Dec 2024 12:10:33 UTC (6,162 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2412.13772) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
