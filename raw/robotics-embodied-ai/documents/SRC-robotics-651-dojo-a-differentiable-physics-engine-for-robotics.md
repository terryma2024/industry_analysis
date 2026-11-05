---
source_id: "SRC-robotics-651"
title: "Dojo A Differentiable Physics Engine for Robotics"
source_type: "paper"
publisher: "Howell et al."
source_date: "待验证"
url: "https://arxiv.org/abs/2203.00806"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-651
---
# Dojo A Differentiable Physics Engine for Robotics

## Computer Science > Robotics

## Title:Dojo: A Differentiable Physics Engine for Robotics

[View PDF](https://arxiv.org/pdf/2203.00806) [HTML (experimental)](https://arxiv.org/html/2203.00806v5)

> Abstract:We present Dojo, a differentiable physics engine for robotics that prioritizes stable simulation, accurate contact physics, and differentiability with respect to states, actions, and system parameters. Dojo models hard contact and friction with a nonlinear complementarity problem with second-order cone constraints. We introduce a custom primal-dual interior-point method to solve the second order cone program for stable forward simulation over a broad range of sample rates. We obtain smooth gradient approximations with this solver through the implicit function theorem, giving gradients that are useful for downstream trajectory optimization, policy optimization, and system identification applications. Specifically, we propose to use the central path parameter threshold in the interior point solver as a user-tunable design parameter. A high value gives a smooth approximation to contact dynamics with smooth gradients for optimization and learning, while a low value gives precise simulation rollouts with hard contact. We demonstrate Dojo's differentiability in trajectory optimization, policy learning, and system identification examples. We also benchmark Dojo against MuJoCo, PyBullet, Drake, and Brax on a variety of robot models, and study the stability and simulation quality over a range of sample frequencies and accuracy tolerances. Finally, we evaluate the sim-to-real gap in hardware experiments with a Ufactory xArm 6 robot. Dojo is an open source project implemented in Julia with Python bindings, with code available at [this https URL](https://github.com/dojo-sim/Dojo.jl).

| Subjects: | Robotics (cs.RO) |
| --- | --- |
| Cite as: | [arXiv:2203.00806](https://arxiv.org/abs/2203.00806) \[cs.RO\] |
|  | (or [arXiv:2203.00806v5](https://arxiv.org/abs/2203.00806v5) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2203.00806](https://doi.org/10.48550/arXiv.2203.00806) |

## Submission history

From: Jiankai Sun \[[view email](https://arxiv.org/show-email/75820714/2203.00806)\]  
**[\[v1\]](https://arxiv.org/abs/2203.00806v1)** Wed, 2 Mar 2022 00:56:23 UTC (4,928 KB)  
**[\[v2\]](https://arxiv.org/abs/2203.00806v2)** Thu, 3 Mar 2022 06:12:42 UTC (4,927 KB)  
**[\[v3\]](https://arxiv.org/abs/2203.00806v3)** Mon, 27 Jun 2022 18:09:13 UTC (2,421 KB)  
**[\[v4\]](https://arxiv.org/abs/2203.00806v4)** Fri, 31 Mar 2023 01:31:26 UTC (5,213 KB)  
**\[v5\]** Tue, 26 Aug 2025 17:27:30 UTC (3,171 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2203.00806) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
