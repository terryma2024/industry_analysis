---
source_id: "SRC-robotics-679"
title: "VLK Learning Humanoid Loco-Manipulation official project"
source_type: "research_project"
publisher: "Amazon FAR / UC Berkeley / Stanford / CMU"
source_date: "待验证"
url: "https://vision-language-kinematics.github.io/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-09T02:28:59+00:00"
tags:
  - raw/source
  - source-type/research-project
  - evidence/s
aliases:
  - SRC-robotics-679
---
# VLK Learning Humanoid Loco-Manipulation official project

Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale.

We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction trajectories using privileged scene information, and renders paired egocentric observations after the fact. We produce 48,000 paired trajectories with no human intervention and train a VLK policy that predicts short-horizon whole-body kinematic trajectories. [A whole-body tracker](https://ericcsr.github.io/scenebot/) converts these predictions into actions on the physical humanoid.

We evaluate on the physical Unitree G1 performing navigation and single-object transport, demonstrating that synthesized interactions in reconstructed scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation.

## Real world in. Real world out. Everything in between is synthesized.

Stage 01 · Synthetic Data Generation

### Generate paired data inside a reconstructed scene.

1. 1
	**Scene Reconstruction.** iPhone → 3D Gaussian Splatting at metric scale.
2. 2
	**Waypoint Generation.** Sample feasible walk-to / pick-from / place-onto spots from scene geometry.
3. 3
	**Motion Synthesis.** Conditional diffusion produces G1 whole-body motions following the waypoints.
4. 4
	**Egocentric Rendering.** Replay motions in the 3DGS scene; randomize lighting, color, and camera for transfer.

Stage 02 · VLK Policy

### Train a vision-language-kinematics policy on the synthetic data.

1. 1
	**Inputs.** Egocentric image + language instruction + current G1 state (incl. wrist contact).
2. 2
	**Backbone.** Initialize from pretrained [π-0.5](https://www.pi.website/blog/pi05) VLA; fine-tune on synthetic data only.
3. 3
	**Output.** 1-second future whole-body kinematic trajectory at 30 Hz.
4. 4
	**Tracker.** We use [SceneBot](https://ericcsr.github.io/scenebot/), a sim-trained whole-body tracker, to convert kinematic predictions into joint commands at 50 Hz.

After training, we deploy the model in simulation and on the real Unitree G1.

## Data modes.

Six trajectory modes are synthesized in both an Apartment and a Lab 3DGS replica.

## Deployment in simulation.

Separate VLK policies are trained for the Lab and Apartment scenes; each is evaluated inside its own 3DGS replica under streamed multi-step language instructions.

## Deployment on the real Unitree G1.

We evaluate the VLK policy on five real-world task families with no real-world fine-tuning.

```
@misc{wang2026vlk,
  title   = {VLK: Learning Humanoid Loco-Manipulation
             from Synthetic Interactions in
             Reconstructed Scenes},
  author  = {Wang, Yen-Jen and Li, Jiaman and
             Chen, Sirui and Truong, Takara E. and
             Xu, Pei and Abbeel, Pieter and
             Duan, Rocky and Sreenath, Koushil and
             Kanazawa, Angjoo and Sferrazza, Carmelo and
             Shi, Guanya and Liu, C. Karen},
  year          = {2026},
  eprint        = {2606.30645},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
  url           = {https://arxiv.org/abs/2606.30645},
}
```

We thank **Xiaoyu Huang** for preparing a clean retargeted OMOMO dataset, **Alejandro Escontrela** for guidance on 3DGS training, **Jenny Zhang** and **Hunter Liu** for providing realistic box assets for rendering, and **Eric Lalumiere** for providing the camera mount. We also thank **Zhen Wu**, **Shibo Zhao**, and **Yunsheng Tian** for valuable discussions on motion synthesis and Real2Sim pipelines. We are grateful to **Haozhi Qi**, **Linda Shih**, **Youjian Huang**, and **Roberto Ceja** for their support with the experimental hardware, and to **Shuying Deng**, **Zihan Wang**, and **Charlie Cheng** for their valuable feedback on the design and visual presentation of the paper figures and video.
