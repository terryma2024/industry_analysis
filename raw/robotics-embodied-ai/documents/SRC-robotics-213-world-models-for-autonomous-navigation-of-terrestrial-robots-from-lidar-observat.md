---
source_id: "SRC-robotics-213"
title: "World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations"
source_type: "paper"
publisher: "arXiv"
source_date: "2025-12-03"
url: "https://arxiv.org/abs/2512.03429"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-29T03:29:07+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-213
---
# World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations

## Title:World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations

[View PDF](https://arxiv.org/pdf/2512.03429) [HTML (experimental)](https://arxiv.org/html/2512.03429v1)

> Abstract:Autonomous navigation of terrestrial robots using Reinforcement Learning (RL) from LIDAR observations remains challenging due to the high dimensionality of sensor data and the sample inefficiency of model-free approaches. Conventional policy networks struggle to process full-resolution LIDAR inputs, forcing prior works to rely on simplified observations that reduce spatial awareness and navigation robustness. This paper presents a novel model-based RL framework built on top of the DreamerV3 algorithm, integrating a Multi-Layer Perceptron Variational Autoencoder (MLP-VAE) within a world model to encode high-dimensional LIDAR readings into compact latent representations. These latent features, combined with a learned dynamics predictor, enable efficient imagination-based policy optimization. Experiments on simulated TurtleBot3 navigation tasks demonstrate that the proposed architecture achieves faster convergence and higher success rate compared to model-free baselines such as SAC, DDPG, and TD3. It is worth emphasizing that the DreamerV3-based agent attains a 100% success rate across all evaluated environments when using the full dataset of the Turtlebot3 LIDAR (360 readings), while model-free methods plateaued below 85%. These findings demonstrate that integrating predictive world models with learned latent representations enables more efficient and robust navigation from high-dimensional sensory data.

| Comments: |
| --- |
| Subjects: | Robotics (cs.RO); Artificial Intelligence (cs.AI) |
| Cite as: | [arXiv:2512.03429](https://arxiv.org/abs/2512.03429) \[cs.RO\] |
|  | (or [arXiv:2512.03429v1](https://arxiv.org/abs/2512.03429v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2512.03429](https://doi.org/10.48550/arXiv.2512.03429) |

## Submission history

From: Raul Steinmetz \[[view email](https://arxiv.org/show-email/0c60935e/2512.03429)\]  
**\[v1\]** Wed, 3 Dec 2025 04:15:31 UTC (950 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2512.03429) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
