---
source_id: "SRC-robotics-323"
title: "RLinf official repository"
source_type: "code_repository"
publisher: "RLinf"
source_date: "2026-07-28"
url: "https://github.com/RLinf/RLinf"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-28T01:13:01+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-323
---
# RLinf official repository

[![RLinf-logo](https://github.com/RLinf/misc/raw/main/pic/logo_white.svg)](https://github.com/RLinf/misc/raw/main/pic/logo_white.svg)

[![](https://camo.githubusercontent.com/ff1a5d3a06780339017b6c8b5748423402630cb3b2a51d34fbc582e9cab27407/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d50617065722d7265643f6c6f676f3d6172786976)](https://arxiv.org/abs/2509.15965) [![](https://camo.githubusercontent.com/11b8e0412521bc020ed010ee1fee24067a8466855e05c33800a86b5f531b12a0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f63756d656e746174696f6e2d507572706c653f636f6c6f723d384132424532266c6f676f3d72656164746865646f6373)](https://rlinf.readthedocs.io/en/latest/) [![](https://camo.githubusercontent.com/ab718625e7cf08bd457ce19f5ea5b8c021a340f4d98bd0a9884a360d243ab930/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe4b8ade69687e69687e6a1a32d7265643f6c6f676f3d72656164746865646f6373)](https://rlinf.readthedocs.io/zh-cn/latest/) [![Ask DeepWiki](https://camo.githubusercontent.com/437b22adcdeaede0841e97dd07287c2451dc6b974985b0e04a0c970a2cd22961/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41736b2532304465657057696b692d3144413146323f6c6f676f3d64617461627269636b73266c6f676f436f6c6f723d776869746526636f6c6f723d303041444546)](https://deepwiki.com/RLinf/RLinf) [![](https://camo.githubusercontent.com/dab940f1f50591b98f59300cc0ba499a570fc47f27234939ab7644ff5b28e370/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe5beaee4bfa12d677265656e3f6c6f676f3d77656368617426)](https://github.com/RLinf/misc/blob/main/pic/wechat.jpg?raw=true)

[![English](https://camo.githubusercontent.com/7f4faafd6717d4c7f6028612accbf0cea51d686697e485f6d46031690679a657/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e672d456e676c6973682d626c75652e737667)](https://github.com/RLinf/RLinf/blob/main/README.md) [![简体中文](https://camo.githubusercontent.com/807f3ebe7b1f7936e38979e37d6529a8cfc8199aa71ef3d3b28bae8815ef3622/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2545382541462541442545382541382538302d2545372541452538302545342542442539332545342542382541442545362539362538372d7265642e737667)](https://github.com/RLinf/RLinf/blob/main/README.zh-CN.md)

## RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI

RLinf is a flexible and scalable open-source RL infrastructure designed for Embodied and Agentic AI. The 'inf' in RLinf stands for `Infrastructure`, highlighting its role as a robust backbone for next-generation training. It also stands for `Infinite`, symbolizing the system’s support for open-ended learning, continuous generalization, and limitless possibilities in intelligence development.

[![RLinf-overview](https://github.com/RLinf/misc/raw/main/pic/overview.svg)](https://github.com/RLinf/misc/raw/main/pic/overview.svg)

## What's NEW!

- \[2026/07\] 🔥 RLinf reimplements π₀ and π₀.₅ in PyTorch with numerical behavior aligned with the JAX reference implementations. Doc: [PyTorch OpenPI](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_openpi_pytorch.html).
- \[2026/07\] 🔥 RLinf supports OPD for online policy distillation of OpenVLA-OFT on LIBERO. Doc: [OPD](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/opd.html).
- \[2026/07\] 🎉 RLinf v0.3 is released with major upgrades in the real-world RL full pipeline (data collection → SFT → RL → deployment), more simulators and SOTA models, and system-level optimizations. Release notes: [RLinf v0.3](https://rlinf.readthedocs.io/en/latest/rst_source/resources/release_v0.3.html).
- \[2026/07\] 🔥 RLinf supports RLT for online RL fine-tuning of VLA policies. Doc: [RLT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/rlt.html).
- \[2026/06\] 🔥 RLinf supports STEAM for offline advantage estimation and policy optimization. Doc: [STEAM](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/steam.html).
- \[2026/06\] 🔥 RLinf supports reinforcement learning fine-tuning for [GR00T-N1.7](https://github.com/NVIDIA/Isaac-GR00T). Doc: [RL on GR00T-N1.7](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gr00t.html).
- \[2026/06\] 🔥 RLinf supports reinforcement learning fine-tuning with the Polaris simulator. Doc: [RL on Polaris](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/polaris.html).
- \[2026/06\] 🔥 RLinf supports reinforcement learning fine-tuning for [GR00T-N1.6](https://github.com/NVIDIA/Isaac-GR00T). Doc: [RL on GR00T-N1.6](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gr00t.html).
- \[2026/06\] 🔥 RLinf supports reinforcement learning fine-tuning for Genesis. Doc: [RL on Genesis](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/genesis.html).
- \[2026/05\] 🔥 RLinf achieves **25×** end-to-end speedup for the BEHAVIOR simulator through system-level optimizations (slimming, on-demand observation, hybrid pipeline parallelism), reducing rollout latency from 1028.7 ms/step to 41.2 ms/step. Blog: [BEHAVIOR System Optimization](https://rlinf.readthedocs.io/en/latest/rst_source/resources/blog/behavior_system_optimization.html)
- \[2026/05\] 🔥 RLinf supports reinforcement learning fine-tuning for ABot-M0. Doc: [RL on ABot-M0 Model](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/abot_m0.html).
- \[2026/05\] 🔥 RLinf supports RL training and SFT with Megatron-Bridge actor beckend. Doc: [Megatron-Bridge](https://rlinf.readthedocs.io/en/latest/rst_source/extending/mbridge.html).
- \[2026/05\] 🔥 RLinf supports AgentLightning for single-agent RL training. Doc: [AgentLightning Calc-X](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/agentlightning_calc_x.html).
- \[2026/05\] 🔥 RLinf supports DreamZero SFT with a refactored training pipeline, achieving nearly **4×** throughput improvement over the official baseline and better convergence. Doc: [DreamZero](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_dreamzero.html)
- \[2026/05\] 🔥 RLinf supports GimArm. Doc: [GimArm](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gim_arm.html)
- \[2026/05\] 🔥 RLinf supports real-world reinforcement learning with a dexterous hand. Doc: [Franka + Dexterous Hand](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_dexhand.html)
- \[2026/05\] 🔥 RLinf supports DM0. In particular, RLinf and Dexbotic enable Lego-style SFT-RL integration. Link: [Dexbotic project link](https://github.com/dexmal/dexbotic/blob/main/docs/RLinfAsRLBackend.md)
- \[2026/04\] 🔥 RLinf supports Dexmal DOS-W1 for real-world reinforcement learning. Doc: [Real-World RL on Dexmal DOS-W1](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dosw1.html).
- \[2026/04\] 🔥 RLinf supports RECAP (RL with Experience and Corrections via Advantage-conditioned Policies) for offline advantage-based policy optimization. Doc: [RECAP](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/recap.html).
- \[2026/04\] 🔥 RLinf now supports offline IQL training on D4RL benchmarks. Doc: [IQL on D4RL](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/iql_d4rl.html), paper: [Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169).
- \[2026/04\] 🔥 RLinf supports EmbodiChain as an embodied environment for RL, with a reference MLP + PPO CartPole recipe. Doc: [EmbodiChain](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/embodichain.html).
- \[2026/04\] 🔥 RLinf supports reinforcement learning fine-tuning for [RoboVerse](https://github.com/RoboVerseOrg/RoboVerse). Doc: [RL on RoboVerse](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/roboverse.html).
- \[2026/04\] 🔥 RLinf supports reinforcement learning fine-tuning for [StarVLA](https://github.com/starVLA/starVLA). Doc: [StarVLA](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/starvla.html).
- \[2026/04\] 🔥 RLinf now supports HG-DAgger (Human-Gated DAgger) for real-world online training. Doc: [HG-DAgger for Real-World Franka](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/hg-dagger.html).
- \[2026/03\] 🔥 RLinf now supports Stereolabs ZED cameras and Robotiq 2F-85 / 2F-140 grippers for Franka real-world RL. Doc: [Franka with ZED & Robotiq](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_zed_robotiq.html).
**More updates**
- \[2026/03\] 🎉 RLinf v0.2 is released with major upgrades in Real-World RL and Multi-Agent RL. Release notes: [RLinf v0.2](https://rlinf.readthedocs.io/en/latest/rst_source/resources/release.html).
- \[2026/03\] 🔥 RLinf supports reinforcement learning fine-tuning for LIBERO-Pro & LIBERO-Plus. Doc: [LIBERO-Pro & LIBERO-Plus](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html#liberopro-plus-benchmark).
- \[2026/03\] 🔥 RLinf supports DAgger for embodied policies. Doc: [DAgger for Embodied Policies](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dagger.html).
- \[2026/03\] 🔥 RLinf now supports evaluating and fine-tuning LingBot-VLA within the RoboTwin environment! Doc: [LingBot-VLA](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/lingbotvla.html).
- \[2026/03\] 🔥 RLinf supports [FUSCO](https://github.com/infinigence/FUSCO) to accelerate the MoE All-to-All communication used in Megatron. Doc: [FUSCO](https://rlinf.readthedocs.io/en/latest/rst_source/examples/system/fusco.html), paper: [FUSCO: High-Performance Distributed Data Shuffling via Transformation-Communication Fusion](https://arxiv.org/pdf/2512.22036).
- \[2026/03\] 🔥 RLinf supports reinforcement learning on multiagents. Website: [WideSeek-R1](https://wideseek-r1.github.io/), quickstart: [QuickStart](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/wideseek_r1/index.html), paper: [WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2602.04634), data: [Training Data](https://huggingface.co/datasets/RLinf/WideSeek-R1-train-data) and [Corpus](https://huggingface.co/datasets/RLinf/WideSeek-R1-Corpus).
- \[2026/03\] 🔥 RLinf supports real-world RL with [XSquare](https://x2robot.com/) Turtle2 dual-arm robot. Doc: [RL on XSquare Turtle2 in the RealWorld](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/xsquare_turtle2.html).
- \[2026/02\] 🔥 RLinf supports supervised fine-tuning of Vision-Language Models. Doc: [VLM SFT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_vlm.html).
- \[2026/02\] 🔥 RLinf supports [DSRL (Diffusion Steering via Reinforcement Learning)](https://arxiv.org/abs/2506.15799) for Pi0, which steers a pre-trained diffusion policy by training a lightweight SAC agent in the latent noise space. Doc: [DSRL for Pi0](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dsrl.html).
- \[2026/02\] 🔥 RLinf supports agentic reinforcement learning on [rStar2](https://github.com/volcengine/verl/pull/3397). Doc: [rStar2](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/rstar2.html).
- \[2026/02\] 🔥 RLinf supports sim-real co-training for π₀ and π₀.₅. Doc: [Sim-Real Co-Training](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/co_training.html).
- \[2026/02\] 🔥 RLinf officially supports world-model-based reinforcement learning fine-tuning for VLA. Doc: [WoVR](https://rlinf.readthedocs.io/en/latest/rst_source/resources/publications/wovr.html), paper: [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977).
- \[2026/02\] 🔥 RLinf supports reinforcement learning fine-tuning for VLA based on [Wan World Model](https://github.com/RLinf/diffsynth-studio). Doc: [RL on Wan World Model](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/wan.html).
- \[2026/02\] 🔥 RLinf is now available on [PyPI](https://pypi.org/project/rlinf/) for installation via pip as a library. Doc: [Installation as a Library](https://rlinf.readthedocs.io/en/latest/rst_source/start/installation.html#install-as-library).
- \[2026/02\] 🔥 The Technical Report of our realworld online learning system [RLinf-USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI](https://arxiv.org/abs/2602.07837) is released. Doc: [RLinf-USER](https://rlinf.readthedocs.io/en/latest/rst_source/resources/publications/rlinf_user.html).
- \[2026/02\] 🔥 RLinf supports reinforcement learning fine-tuning for [Dexbotic](https://github.com/dexmal/dexbotic). Doc: [RL on Dexbotic Model](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dexbotic.html).
- \[2026/02\] 🔥 RLinf supports reinforcement learning with [GSEnv](https://github.com/chenkang455/ManiSkill-GS) for Real2Sim2Real. Doc: [RL with GSEnv](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gsenv.html).
- \[2026/01\] 🔥 RLinf supports reinforcement learning fine-tuning for [OpenSora World Model](https://github.com/hpcaitech/Open-Sora). Doc: [RL on OpenSora World Model](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/opensora.html).
- \[2026/01\] 🔥 RLinf supports reinforcement learning fine-tuning for [RoboTwin](https://github.com/robotwin-Platform/RoboTwin). Doc: [RL on RoboTwin](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/robotwin.html).
- \[2026/01\] 🔥 RLinf supports SAC training for flow matching policy. Doc: [SAC-Flow](https://rlinf.readthedocs.io/zh-cn/latest/rst_source/examples/embodied/sac_flow.html), paper: [SAC Flow: Sample-Efficient Reinforcement Learning of Flow-Based Policies via Velocity-Reparameterized Sequential Modeling](https://arxiv.org/abs/2509.25756).
- \[2025/12\] 🔥 RLinf supports agentic reinforcement learning on [Search-R1](https://github.com/PeterGriffinJin/Search-R1). Doc: [Search-R1](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/searchr1.html).
- \[2025/12\] 🔥 RLinf v0.2-pre is open-sourced. We support real-world RL with Franka. Doc: [RL on Franka in the RealWorld](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka.html).
- \[2025/12\] 🔥 RLinf supports reinforcement learning fine-tuning for [RoboCasa](https://github.com/robocasa/robocasa). Doc: [RL on Robocasa](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/robocasa.html).
- \[2025/12\] 🎉 RLinf official release of [v0.1](https://github.com/RLinf/RLinf/releases/tag/v0.1).
- \[2025/11\] 🔥 RLinf supports reinforcement learning fine-tuning for [CALVIN](https://github.com/mees/calvin). Doc: [RL on CALVIN](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/calvin.html).
- \[2025/11\] 🔥 RLinf supports reinforcement learning fine-tuning for [IsaacLab](https://github.com/isaac-sim/IsaacLab). Doc: [RL on IsaacLab](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/isaaclab.html).
- \[2025/11\] 🔥 RLinf supports reinforcement learning fine-tuning for [GR00T-N1.5](https://github.com/NVIDIA/Isaac-GR00T). Doc: [RL on GR00T-N1.5](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gr00t.html).
- \[2025/11\] 🔥 RLinf supports reinforcement learning fine-tuning for [Metaworld](https://github.com/Farama-Foundation/Metaworld). Doc: [RL on Metaworld](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/metaworld.html).
- \[2025/11\] 🔥 RLinf supports reinforcement learning fine-tuning for [Behavior 1k](https://github.com/StanfordVL/BEHAVIOR-1K). Doc: [RL on Behavior 1k](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/behavior.html).
- \[2025/11\] Add lora support to π₀ and π₀.₅.
- \[2025/10\] 🔥 RLinf supports reinforcement learning fine-tuning for π₀ and π₀.₅! Doc: [RL on π₀ and π₀.₅ Models](https://rlinf.readthedocs.io/en/latest/rst_source/resources/publications/pi_rl.html), paper: [RL fine-tuning for π₀ and π₀.₅ technical report](https://arxiv.org/abs/2510.25889). The report on πRL by [Machine Heart](https://mp.weixin.qq.com/s/dFlpmqmE0qfhOQmGG25X9g) and [RoboTech](https://mp.weixin.qq.com/s/S51P-Y1UYXzumnZzon2N1g) are also released.
- \[2025/10\] 🔥 RLinf now officially supports online reinforcement learning! Doc: [coding\_online\_rl](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/coding_online_rl.html), and the report [The first open-source agent online RL framework RLinf-Online](https://mp.weixin.qq.com/s/jmohmDokuWLhQHFueSHZIQ) is also published.
- \[2025/10\] 🔥 The RLinf algorithm technical report is officially released. Doc: [RLinf-VLA](https://rlinf.readthedocs.io/en/latest/rst_source/resources/publications/rlinf_vla.html), paper: [RLinf-VLA: A Unified and Efficient Framework for VLA+RL Training](https://arxiv.org/abs/2510.06710).
- \[2025/09\] 🔥 Our paper [RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation](https://arxiv.org/abs/2509.15965) is officially released. Doc: [RLinf](https://rlinf.readthedocs.io/en/latest/rst_source/resources/publications/rlinf_system.html), and the [Machine Heart report on RLinf](https://mp.weixin.qq.com/s/Xtv4gDu3lhDDGadLrzt6Aw) is also published.
- \[2025/08\] RLinf is open-sourced. The formal v0.1 will be released soon.

## Key Features

RLinf has high flexibility to support diverse RL training workflows (PPO, GRPO, SAC and so on), while hiding the complexity of distributed programming. Users can easily scale RL training to a large number of GPU nodes without modifying code, meeting the increasing demand of computation for RL training.

The high flexibility allows RLinf to explore more efficient scheduling and execution. The hybrid execution mode for embodied RL achieves up to **2.434×** throughput compared to existing frameworks.

Multiple Backend Integrations

- FSDP + HuggingFace/SGLang/vLLM: rapid adaptation to new models and algorithms, ideal for beginners and fast prototyping.
- Megatron + SGLang/vLLM: optimized for large-scale training, delivering maximum efficiency for expert users with demanding workloads.

## Examples

### Embodied AI

RLinf supports SFT, simulation RL, and real-world RL for World Action Models (WAM) and Vision-Language-Action Models (VLA). The current support list is as follows:

| Simulators | Models | Algorithms |
| --- | --- | --- |
| - [ManiSkill](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/maniskill.html) ✅ - [LIBERO](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html) ✅ - [LIBERO-Pro & LIBERO-Plus](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html#liberopro-plus-benchmark) ✅ - [RoboTwin](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/robotwin.html) ✅ - [RoboVerse](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/roboverse.html) ✅ - [BEHAVIOR](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/behavior.html) ✅ - [MetaWorld](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/metaworld.html) ✅ - [IsaacLab](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/isaaclab.html) ✅ - [CALVIN](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/calvin.html) ✅ - [RoboCasa](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/robocasa.html) ✅ - [Franka-Sim](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/frankasim.html) ✅ - [EmbodiChain](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/embodichain.html) ✅ - [Genesis](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/genesis.html) ✅ - [Polaris](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/polaris.html) ✅ - More... | - **VLA** - [π₀ / π₀.₅ (OpenPI-PyTorch)](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_openpi.html) ✅ 	- [π₀ / π₀.₅ (RLinf-PyTorch)](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_openpi_pytorch.html) ✅ 	- [OpenVLA](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/maniskill.html) ✅ 	- [LingBot-VLA](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/lingbotvla.html) ✅ 	- [OpenVLA-OFT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html) ✅ 	- [ABot-M0](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/abot_m0.html) ✅ 	- [GR00T (N1.5, N1.6, N1.7)](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gr00t.html) ✅ 	- [Dexbotic](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dexbotic.html) ✅ 	- [StarVLA](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/starvla.html) ✅ - **VLM** - [Qwen2.5-VL](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_vlm.html) ✅ 	- [Qwen3-VL](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_vlm.html) ✅ 	- [Qwen3-VL-MoE](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_vlm.html) ✅ - **World Model** - [OpenSora](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/opensora.html) ✅ - [Wan](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/wan.html) ✅ - **Custom Models** - [MLP-Policy](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/mlp.html) ✅ 	- CNN-Policy ✅ - **Reward Model** - [ResNet](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_reward_model.html) ✅ - **World Action Model** - [DreamZero](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_dreamzero.html) ✅ | - **RL Algos** - [IQL](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/iql.html) ✅ 	- [GRPO](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/grpo.html) ✅ 	- [PPO](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/ppo.html) ✅ 	- [Async PPO](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/async_ppo.html) ✅ 	- [DAPO](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/dapo.html) ✅ 	- [Reinforce++](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/reinforce.html) ✅ 	- [SAC](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/sac.html) ✅ 	- [CrossQ](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/crossq.html) ✅ 	- [RLPD](https://rlinf.readthedocs.io/en/latest/rst_source/reference/algorithms/rlpd.html) ✅ 	- [SAC-Flow](https://arxiv.org/abs/2509.25756) ✅ 	- [DSRL](https://arxiv.org/abs/2506.15799) ✅ 	- [RECAP (CFG)](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/recap.html) ✅ 	- [STEAM](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/steam.html) ✅ 	- [RLT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/rlt.html) ✅ 	- [OPD](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/opd.html) ✅ - **SFT** - [Full-parameter SFT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_openpi.html) ✅ 	- [LoRA SFT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_openpi.html) ✅ 	- [VLM SFT](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/sft_vlm.html) ✅ 	- [DAgger](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dagger.html) ✅ 	- [HG-DAgger](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/hg-dagger.html) ✅ |

| Real-world Robotics | Data Collection |
| --- | --- |
| - [Franka Arm](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka.html) - [Intel RealSense](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka.html) ✅ 	- [Stereolabs ZED](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_zed_robotiq.html) ✅ 	- Lumos Camera ✅ 	- [Franka Hand](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka.html) ✅ 	- [Ruiyan Hand](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_dexhand.html) ✅ 	- [Robotiq 2F-85 / 2F-140](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_zed_robotiq.html) ✅ - [XSquare Turtle2](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/xsquare_turtle2.html) ✅ - [Dual-franka](https://rlinf.readthedocs.io/en/latest/rst_source/guides/data_collection.html) ✅ - [DOS-W1](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/dosw1.html) ✅ - [GimArm](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/gim_arm.html) ✅ - More... | - [GELLO](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_gello.html) ✅ - [SpaceMouse](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka.html) ✅ - [PICO VR](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/franka_vr.html) ✅ |

### Agentic AI

| Single-Agent | Multi-Agent |
| --- | --- |
| - [SearchR1](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/searchr1.html) ✅ - [rStar2](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/rstar2.html) ✅ - [AgentLightning Calc-X](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/agentlightning_calc_x.html) ✅ - [Online Coder](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/coding_online_rl.html) ✅ - [Math Reasoning RL](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/reasoning.html) ✅ | - [WideSeek-R1](https://rlinf.readthedocs.io/en/latest/rst_source/examples/agentic/wideseek_r1/index.html) ✅ |

## Quick Start

**Installation:** Users can refer to our [installation guide](https://rlinf.readthedocs.io/en/latest/rst_source/start/installation.html) to install RLinf. We recommend users to use our provided docker image (i.e., [Installation Method 1](https://rlinf.readthedocs.io/en/latest/rst_source/start/installation.html#installation-method-1-docker-image)), as the environment and dependencies of embodied RL are complex.

**Run a simple example:** After setting up the environment, users can run a simple example of embodied RL with ManiSkill3 simulator following [this document](https://rlinf.readthedocs.io/en/latest/rst_source/start/vla.html).

**SOTA RL Training Reproduction:** RLinf provides end-to-end recipes that reproduce or match **state-of-the-art (SOTA) RL results** out of the box—users can directly run our configs and scripts to obtain SOTA performance without custom engineering. Check out our [example gallery](https://rlinf.readthedocs.io/en/latest/rst_source/examples/index.html) for more details.

## Awesome Community Projects with RLinf

We are excited to see a growing ecosystem of projects building on top of or integrate with RLinf, spanning embodied AI, robotics, and long-horizon agentic systems. Here are some awesome community projects:

- [i4h-workflows](https://github.com/isaac-for-healthcare/i4h-workflows/tree/main/workflows/rheo): NVIDIA team open sourced RL-based workflow built on Isaac ecosystem, integrating RLinf for healthcare-oriented embodied intelligence.
- [pi-StepNFT](https://github.com/wangst0181/pi-StepNFT): Extends RLinf for step-level training and optimization of π-series VLA models.
- [Dexbotic](https://github.com/dexmal/dexbotic): A robotics + RL system integrating RLinf for scalable training and deployment of embodied agents.
- [RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin): A digital twin + robotics platform leveraging RLinf for large-scale embodied RL training.
- [IsaacLab](https://github.com/isaac-sim/IsaacLab/tree/develop/scripts/reinforcement_learning/rlinf): Official integration of RLinf within IsaacLab, enabling seamless reinforcement learning workflows on top of NVIDIA Isaac Sim based robotics environments.
- [RISE](https://github.com/OpenDriveLab/RISE): A robot reinforcement learning framework based on a compositional world model, using RLinf for online reinforcement learning.

💡 Want to feature your project here? Open a PR and we’ll be happy to include it!

## Adoption

RLinf is a production-grade, open-source reinforcement learning framework for embodied AI. It is being adopted by leading companies and startups across AI infrastructure and robotics, including AgiBot, X Square Robot, PsiBot, Dexmal, Moore Threads, D-Robotics, DexForce, YinWang, Robbyant and GigaAI.

[![adoption](https://github.com/RLinf/misc/raw/main/pic/adoption_logos/adoption.png)](https://github.com/RLinf/misc/raw/main/pic/adoption_logos/adoption.png)

✨ If your organization is using RLinf, feel free to reach out or submit a PR to be listed here.

## CI Test Status

RLinf has comprehensive CI tests for both the core components (via unit tests) and end-to-end RL training workflows of embodied, agent, and reasoning scenarios. Below is the summary of the CI test status of the main branch:

| Test Name | Status |
| --- | --- |
| unit-tests | [![GitHub Actions Workflow Status](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573)](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573) |
| agent-reason-e2e-tests | [![GitHub Actions Workflow Status](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573)](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573) |
| embodied-e2e-tests | [![GitHub Actions Workflow Status](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573)](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573) |
| scheduler-tests | [![GitHub Actions Workflow Status](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573)](https://camo.githubusercontent.com/0d93b42c6a3a4fd553f9c962f9ccb414ceddc47bc135f8effda06a2480d6f09b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f524c696e662f524c696e662f63692d74657374732e796d6c3f6c6162656c3d537461747573) |

## Contribution Guidelines

We welcome contributions to RLinf. Please read [contribution guide](https://github.com/RLinf/RLinf?tab=contributing-ov-file#contributing-to-rlinf) before taking action. Thank the following contributors and welcome more developers to join us on this open source project.

[![](https://camo.githubusercontent.com/5b08a75818de51faa5d99a00b9c7b2097a71a26d39ec505c5a051c75515a4f89/68747470733a2f2f7374672e636f6e747269622e726f636b732f696d6167653f7265706f3d524c696e662f524c696e66266d61783d32343026636f6c756d6e733d3138)](https://github.com/RLinf/RLinf/graphs/contributors)

## Citation and Acknowledgement

If you find **RLinf** helpful, please cite the paper:

```
@article{yu2025rlinf,
  title={RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation},
  ={Yu, Chao and Wang, Yuanqing and Guo, Zhen and Lin, Hao and Xu, Si and Zang, Hongzhi and Zhang, Quanlu and Wu, Yongji and Zhu, Chunyang and Hu, Junhao and others},
  journal={arXiv preprint arXiv:2509.15965},
  year={2025}
}
```

If you use RL+VLA in RLinf, you can also cite our technical report and empirical study paper:

```
@article{zang2025rlinf,
  title={RLinf-VLA: A Unified and Efficient Framework for VLA+ RL Training},
  ={Zang, Hongzhi and Wei, Mingjie and Xu, Si and Wu, Yongji and Guo, Zhen and Wang, Yuanqing and Lin, Hao and Shi, Liangzhi and Xie, Yuqing and Xu, Zhexuan and others},
  journal={arXiv preprint arXiv:2510.06710},
  year={2025}
}
```
```
@article{liu2025can,
  title={What can rl bring to vla generalization? an empirical study},
  ={Liu, Jijia and Gao, Feng and Wei, Bingwen and Chen, Xinlei and Liao, Qingmin and Wu, Yi and Yu, Chao and Wang, Yu},
  journal={arXiv preprint arXiv:2505.19789},
  year={2025}
}
```
```
@article{chen2025pi_,
  title={$$\backslash$pi\_$\backslash$texttt $\{$RL$\}$ $: Online RL Fine-tuning for Flow-based Vision-Language-Action Models},
  ={Chen, Kang and Liu, Zhihao and Zhang, Tonghe and Guo, Zhen and Xu, Si and Lin, Hao and Zang, Hongzhi and Zhang, Quanlu and Yu, Zhaofei and Fan, Guoliang and others},
  journal={arXiv preprint arXiv:2510.25889},
  year={2025}
}
```

If you train your policies in physical world with RLinf, you can cite our paper:

```
@article{zang2026rlinfuser,
  title={RLinf-USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI}, 
  ={Hongzhi Zang and Shu'ang Yu and Hao Lin and Tianxing Zhou and Zefang Huang and Zhen Guo and Xin Xu and Jiakai Zhou and Yuze Sheng and Shizhe Zhang and Feng Gao and Wenhao Tang and Yufeng Yue and Quanlu Zhang and Xinlei Chen and Chao Yu and Yu Wang},
  year={2026},
  journal={arXiv preprint arXiv:2602.07837},
  url={https://arxiv.org/abs/2602.07837}, 
}
```

If you use World Model + VLA + RL in RLinf, you can cite our paper:

```
@article{jiang2026wovr,
  title={WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL}, 
  ={Zhennan Jiang and Shangqing Zhou and Yutong Jiang and Zefang Huang and Mingjie Wei and Yuhui Chen and Tianxing Zhou and Zhen Guo and Hao Lin and Quanlu Zhang and Yu Wang and Haoran Li and Chao Yu and Dongbin Zhao},
  year={2026},
  journal={arXiv preprint arXiv:2602.13977},
  url={https://arxiv.org/abs/2602.13977}, 
}
```

If you use RL-based sim-real co-training in RLinf, you can cite our paper:

```
@article{shi2026rlinf,
  title={Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models},
  ={Shi, Liangzhi and Chen, Shuaihang and Gao, Feng and Chen, Yinuo and Chen, Kang and Zhang, Tonghe and Zhang, Hongzhi and Zhang, Weinan and Yu, Chao and Wang, Yu},
  journal={arXiv preprint arXiv:2602.12628},
  year={2026},
  url={https://arxiv.org/abs/2602.12628},
}
```

If you use WideSeek-R1 in RLinf, you can cite our paper:

```
@article{xu2026wideseek,
  title={WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning},
  ={Xu, Zelai and Xu, Zhexuan and Zhang, Ruize and Zhu, Chunyang and Yu, Shi and Liu, Weilin and Zhang, Quanlu and Ding, Wenbo and Yu, Chao and Wang, Yu},
  journal={arXiv preprint arXiv:2602.04634},
  year={2026},
}
```

**Acknowledgements** RLinf has been inspired by, and benefits from, the ideas and tooling of the broader open-source community. In particular, we would like to thank the teams and contributors behind VeRL, AReaL, Megatron-LM, SGLang, and PyTorch Fully Sharded Data Parallel (FSDP), and if we have inadvertently missed your project or contribution, please open an issue or a pull request so we can properly credit you.

**Contact:** We welcome applications from Postdocs, PhD/Master's students, and interns. Join us in shaping the future of RL infrastructure and embodied AI!
