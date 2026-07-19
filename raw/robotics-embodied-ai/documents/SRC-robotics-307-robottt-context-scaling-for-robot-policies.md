---
source_id: "SRC-robotics-307"
title: "RoboTTT Context Scaling for Robot Policies"
source_type: "paper"
publisher: "NVIDIA / Stanford University / University of Texas at Austin"
source_date: "2026-07-16"
url: "https://arxiv.org/abs/2607.15275"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-18T03:24:23+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-307
---
# RoboTTT Context Scaling for Robot Policies

## Title:RoboTTT: Context Scaling for Robot Policies

[View PDF](https://arxiv.org/pdf/2607.15275) [HTML (experimental)](https://arxiv.org/html/2607.15275v1)

> Abstract:Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger performance on multi-stage, long-horizon tasks. We also observe, for the first time, steady gains in closed-loop performance as pretraining context length scales. At its core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-Language-Action policies, yielding a sequence model whose recurrent state consists of fast weights, parameters updated by gradient descent during both training and inference, compressing histories into weight space and retrieving contextual information for long-context conditioning. To scale training context length, the recipe combines sequence action forcing with truncated backpropagation through time. On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for robot foundation models. Videos are available at [this https URL](https://research.nvidia.com/labs/gear/robottt/)

| Comments: |
| --- |
| Subjects: | Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2607.15275](https://arxiv.org/abs/2607.15275) \[cs.RO\] |
|  | (or [arXiv:2607.15275v1](https://arxiv.org/abs/2607.15275v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2607.15275](https://doi.org/10.48550/arXiv.2607.15275) |

## Submission history

From: Yunfan Jiang \[[view email](https://arxiv.org/show-email/75b711db/2607.15275)\]
**\[v1\]** Thu, 16 Jul 2026 17:59:06 UTC (11,180 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2607.15275) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
