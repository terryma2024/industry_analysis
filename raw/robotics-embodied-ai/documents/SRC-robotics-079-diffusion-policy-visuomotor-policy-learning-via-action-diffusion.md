---
source_id: "SRC-robotics-079"
title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
source_type: "paper"
publisher: "arXiv"
source_date: "2023"
url: "https://arxiv.org/abs/2303.04137"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T01:34:04+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-079
---
# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

## Title:Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

[View PDF](https://arxiv.org/pdf/2303.04137) [HTML (experimental)](https://arxiv.org/html/2303.04137v5)

> Abstract:This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 12 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer. We hope this work will help motivate a new generation of policy learning techniques that are able to leverage the powerful generative modeling capabilities of diffusion models. Code, data, and training details is publicly available [this http URL](http://diffusion-policy.cs.columbia.edu/)

| Comments: |
| --- |
| Subjects: | Robotics (cs.RO) |
| Cite as: | [arXiv:2303.04137](https://arxiv.org/abs/2303.04137) \[cs.RO\] |
|  | (or [arXiv:2303.04137v5](https://arxiv.org/abs/2303.04137v5) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2303.04137](https://doi.org/10.48550/arXiv.2303.04137) |

## Submission history

From: Cheng Chi \[[view email](https://arxiv.org/show-email/b0721e9e/2303.04137)\]  
**[\[v1\]](https://arxiv.org/abs/2303.04137v1)** Tue, 7 Mar 2023 18:50:03 UTC (8,406 KB)  
**[\[v2\]](https://arxiv.org/abs/2303.04137v2)** Fri, 10 Mar 2023 01:51:37 UTC (8,406 KB)  
**[\[v3\]](https://arxiv.org/abs/2303.04137v3)** Mon, 22 May 2023 00:51:08 UTC (8,416 KB)  
**[\[v4\]](https://arxiv.org/abs/2303.04137v4)** Thu, 1 Jun 2023 15:27:43 UTC (8,416 KB)  
**\[v5\]** Thu, 14 Mar 2024 04:36:31 UTC (9,772 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2303.04137) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
