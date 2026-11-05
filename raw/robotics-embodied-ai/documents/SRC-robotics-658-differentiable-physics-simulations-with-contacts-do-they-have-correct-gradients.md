---
source_id: "SRC-robotics-658"
title: "Differentiable Physics Simulations with Contacts Do They Have Correct Gradients"
source_type: "paper"
publisher: "Zhong et al."
source_date: "待验证"
url: "https://arxiv.org/abs/2207.05060"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-658
---
# Differentiable Physics Simulations with Contacts Do They Have Correct Gradients

## Computer Science > Machine Learning

## Title:Differentiable Physics Simulations with Contacts: Do They Have Correct Gradients w.r.t. Position, Velocity and Control?

[View PDF](https://arxiv.org/pdf/2207.05060) [HTML (experimental)](https://arxiv.org/html/2207.05060v1)

> Abstract:In recent years, an increasing amount of work has focused on differentiable physics simulation and has produced a set of open source projects such as Tiny Differentiable Simulator, Nimble Physics, diffTaichi, Brax, Warp, Dojo and DiffCoSim. By making physics simulations end-to-end differentiable, we can perform gradient-based optimization and learning tasks. A majority of differentiable simulators consider collisions and contacts between objects, but they use different contact models for differentiability. In this paper, we overview four kinds of differentiable contact formulations - linear complementarity problems (LCP), convex optimization models, compliant models and position-based dynamics (PBD). We analyze and compare the gradients calculated by these models and show that the gradients are not always correct. We also demonstrate their ability to learn an optimal control strategy by comparing the learned strategies with the optimal strategy in an analytical form. The codebase to reproduce the experiment results is available at [this https URL](https://github.com/DesmondZhong/diff_sim_grads).

| Comments: |  |
| --- | --- |
| Subjects: | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Robotics (cs.RO) |
| Cite as: | [arXiv:2207.05060](https://arxiv.org/abs/2207.05060) \[cs.LG\] |
|  | (or [arXiv:2207.05060v1](https://arxiv.org/abs/2207.05060v1) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2207.05060](https://doi.org/10.48550/arXiv.2207.05060) |

## Submission history

From: Yaofeng Desmond Zhong \[[view email](https://arxiv.org/show-email/d473ef57/2207.05060)\]  
**\[v1\]** Fri, 8 Jul 2022 19:30:09 UTC (932 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2207.05060) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
