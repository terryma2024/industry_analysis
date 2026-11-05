---
source_id: "SRC-robotics-672"
title: "Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis"
source_type: "paper"
publisher: "Conti et al."
source_date: "2026-06-27"
url: "https://arxiv.org/abs/2606.28805"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:38:59+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-672
---
# Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis

## Computer Science > Robotics

## Title:Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis

Authors:[Christian Conti](https://arxiv.org/search/cs?searchtype=author&query=Conti,+C) (1), [Bilan Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+B) (1), [Alexander Sigrist](https://arxiv.org/search/cs?searchtype=author&query=Sigrist,+A) (2), [Lorenzo Miele](https://arxiv.org/search/cs?searchtype=author&query=Miele,+L) (2), [Yamen Saraiji](https://arxiv.org/search/cs?searchtype=author&query=Saraiji,+Y) (1), [Peter Dürr](https://arxiv.org/search/cs?searchtype=author&query=D%C3%BCrr,+P) (2), [Naoya Takahashi](https://arxiv.org/search/cs?searchtype=author&query=Takahashi,+N) (2) ((1) Sony AI, Tokyo, Japan, (2) Sony AI, Zurich, Switzerland)

[View PDF](https://arxiv.org/pdf/2606.28805) [HTML (experimental)](https://arxiv.org/html/2606.28805v2)

> Abstract:At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

| Comments: |  |
| --- | --- |
| Subjects: | Robotics (cs.RO) |
| Cite as: | [arXiv:2606.28805](https://arxiv.org/abs/2606.28805) \[cs.RO\] |
|  | (or [arXiv:2606.28805v2](https://arxiv.org/abs/2606.28805v2) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2606.28805](https://doi.org/10.48550/arXiv.2606.28805) |

## Submission history

From: Christian Conti \[[view email](https://arxiv.org/show-email/aca88db7/2606.28805)\]  
**[\[v1\]](https://arxiv.org/abs/2606.28805v1)** Sat, 27 Jun 2026 08:18:49 UTC (943 KB)  
**\[v2\]** Wed, 1 Jul 2026 02:30:35 UTC (944 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2606.28805) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
