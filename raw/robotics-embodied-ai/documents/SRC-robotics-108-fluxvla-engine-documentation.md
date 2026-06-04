---
source_id: "SRC-robotics-108"
title: "FluxVLA Engine documentation"
source_type: "open_source_tooling"
publisher: "逐际动力 LimX Dynamics"
source_date: "2026"
url: "https://fluxvla.limxdynamics.com/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-06-04T05:45:45+00:00"
tags:
  - raw/source
  - source-type/open-source-tooling
  - evidence/s
aliases:
  - SRC-robotics-108
---
# FluxVLA Engine documentation

## FluxVLA Engine Documentation

**FluxVLA Engine** is a full-stack, end-to-end engineering platform for deploying embodied intelligence applications. Built on the core design principles of unified configuration, standardized interfaces, module decoupling, and deployability, it creates a complete engineering loop from data to real-device deployment. With the goal of providing a standardized industry–academia–research foundation, it significantly lowers the engineering barrier for VLA research and development.

Core Modules[All-in-One Configuration Single configuration surface — switch between training, evaluation, and deployment in one click.](https://fluxvla.limxdynamics.com/md_source/tutorials/framework.html)

[

Modular Training Composable, block-style VLA assembly — scale out with FSDP / DDP multi-node multi-GPU

](https://fluxvla.limxdynamics.com/md_source/start/vla.html)[

Flash Fused Kernels Fused GPU kernels and graph-friendly inference paths for high-throughput, low-latency robot foundation models

](https://fluxvla.limxdynamics.com/md_source/tutorials/inference/triton_inference.html)[

Guided Trajectory Smoothing Constrains the denoising process with known action prefixes, reducing inconsistencies between adjacent action chunks for smoother real-time control

](https://fluxvla.limxdynamics.com/md_source/tutorials/inference/rtc.html)

Demo

1-Hour Towel Folding

The towel-folding task demonstrates four stages — retrieving the towel, flattening a crumpled towel, folding it correctly, and placing it — captured in a 15× speed recording of one continuous hour with zero failures.

![1-Hour Towel Folding](https://fluxvla.limxdynamics.com/videos/thumbs/demo-20260202_RA-BC_Aiming_15x-words.jpg?v=1) ![RTC Comparison](https://fluxvla.limxdynamics.com/videos/thumbs/demo-rtc-compare-v3.jpg?v=1) ![Fine-Grained Manipulation](https://fluxvla.limxdynamics.com/videos/thumbs/demo-fine-manipulation.jpg?v=1) ![CoT-1](https://fluxvla.limxdynamics.com/videos/thumbs/demo-output2.jpg?v=1) ![CoT-2](https://fluxvla.limxdynamics.com/videos/thumbs/demo-output31.jpg?v=1) ![CoT-3](https://fluxvla.limxdynamics.com/videos/thumbs/demo-cot-fruit.jpg?v=1) ![High-Frequency Reactive Control](https://fluxvla.limxdynamics.com/videos/thumbs/demo-feishu-0401.jpg?v=1) ![Tron2 Bimanual Deployment](https://fluxvla.limxdynamics.com/videos/thumbs/demo-feishu-0326a.jpg?v=1) ![Complex Environment Manipulation](https://fluxvla.limxdynamics.com/videos/thumbs/demo-feishu-0326b.jpg?v=1)

Classroom

[![FluxVLA architecture overview diagram](https://fluxvla.limxdynamics.com/_static/svg/framework-2.png)](https://fluxvla.limxdynamics.com/md_source/tutorials/framework.html)

[Architecture Overview](https://fluxvla.limxdynamics.com/md_source/tutorials/framework.html)

[

Deep dive into FluxVLA's layered design and execution pipeline — how models, data, and engines work together.

](https://fluxvla.limxdynamics.com/md_source/tutorials/framework.html)[![FluxVLA config guide illustration](https://fluxvla.limxdynamics.com/_static/svg/config.jpg)

Config Deep-Dive

Master the four config modules — model, data, training, and inference — to flexibly compose experiments.

](https://fluxvla.limxdynamics.com/md_source/tutorials/config/index.html)[![Modular building blocks for custom VLA model assembly](https://fluxvla.limxdynamics.com/_static/svg/custom-model-blocks.svg)

Add Custom Models

Step-by-step guide to register and integrate your own VLA model into the FluxVLA framework.

](https://fluxvla.limxdynamics.com/md_source/tutorials/private_model.html)[![FluxVLA inference and deployment](https://fluxvla.limxdynamics.com/_static/svg/deplpy-card-image-1.png)

Inference Deployment

End-to-end real-robot deployment for Aloha, Tron2, and UR3 — from model export to on-device inference.

](https://fluxvla.limxdynamics.com/md_source/tutorials/inference/index.html)

Project Overview

VLA Models

OpenVLA

LlavaVLA

GR00T

Pi0

Pi0.5

▸

Backbones

LLaMA / Gemma / Qwen

DinoSigLIP

PaliGemma

QwenVL

▸

Data

Parquet

RLDS

Multi-Dataset Mix

▸

Training

FSDP / DDP

LoRA

AMP

Checkpoint Resume

Auto Post-Eval

▸

Multi-GPU Eval

LIBERO Benchmark

Real-Robot Inference

RTC Guidance

Highlights

**FluxVLA is unique with:**

**One modular VLA spine:** all models inherit from `BaseVLA` —vision encoder, language encoder, projection into the LLM space, and an action head—so you can swap OpenVLA, LlavaVLA, GR00T, Pi0, and Pi0.5 without rewriting the training story.

**Backbone breadth**

- **LLMs:** LLaMA, Gemma, and Qwen families.
- **Vision:** DinoSigLIP (DINO + SigLIP).
- **VLMs:** PaliGemma and QwenVL.

**Dataset breadth:** first-class Parquet and RLDS pipelines plus multi-dataset mixed training for heterogeneous data.

**FluxVLA is complete at scale with:**

**Distributed training:** FSDP and DDP for large-scale runs.

**Practical training stack:** LoRA, AMP, checkpoint resumption, and automatic post-training evaluation.

**From benchmarks to real robots:** multi-GPU evaluation, LIBERO (including setups without ray tracing, e.g. A100), real-robot inference scripts, and an inference mode that skips loading full pretrained weights to save memory.

**FluxVLA is flexible and easy to use with:**

**Clear project layout:** `fluxvla/` holds models (VLAs, backbones, heads, projectors), datasets, transforms, tokenizers, engines, optimizers, and collators; `configs/` is organized by family (`openvla`, `llava`, `gr00t`, `pi0`, `pi05`); `scripts/` wires train, eval, and real-robot inference.

**End-to-end data and training flow:** load Parquet or RLDS → transform and collate → forward → action loss → backprop, with pluggable runners (FSDP/DDP) and standard optimizers and logging/checkpointing.

**Proven tooling:** PyTorch 2.6, Hugging Face Transformers 4.53.x, Flash Attention 2.5.x, TensorFlow for RLDS, and LIBERO—suited to manipulation, multi-task learning, transfer learning, and VLA research iteration.

**Forward-looking roadmap:** more vision/VLM backbones and VLA methods, VLM or chain-of-thought data training, Isaac Sim integration, and richer logging.

---

- [Quick Start](https://fluxvla.limxdynamics.com/md_source/start/index.html)
	- [Installation Guide](https://fluxvla.limxdynamics.com/md_source/start/installation/index.html)
		- [From Scratch](https://fluxvla.limxdynamics.com/md_source/start/installation/zero.html)
				- [Alibaba Cloud Mirror Quick Start](https://fluxvla.limxdynamics.com/md_source/start/installation/aliyun.html)
		- [Libero - Inference with a Pre-trained Model](https://fluxvla.limxdynamics.com/md_source/start/libero-inference.html)
		- [Libero - Train Your Own Model](https://fluxvla.limxdynamics.com/md_source/start/libero-train.html)
		- [ALOHA Real-Robot Training and Deployment](https://fluxvla.limxdynamics.com/md_source/start/Agilex_Aloha.html)
		- [Frequently Asked Questions](https://fluxvla.limxdynamics.com/md_source/start/faq.html)
		- [Data Preparation](https://fluxvla.limxdynamics.com/md_source/start/data/index.html)
		- [Simulation Data Preparation](https://fluxvla.limxdynamics.com/md_source/start/data/Sim.html)
				- [Real-Robot Data Preparation](https://fluxvla.limxdynamics.com/md_source/start/data/Real_data.html)
		- [Model Training](https://fluxvla.limxdynamics.com/md_source/start/vla.html)
		- [Model Evaluation](https://fluxvla.limxdynamics.com/md_source/start/vla-eval.html)

---

- [Tutorials](https://fluxvla.limxdynamics.com/md_source/tutorials/index.html)
	- [FluxVLA Code Architecture Overview](https://fluxvla.limxdynamics.com/md_source/tutorials/framework.html)
		- [Configuration](https://fluxvla.limxdynamics.com/md_source/tutorials/config/index.html)
		- [Adding Custom Models](https://fluxvla.limxdynamics.com/md_source/tutorials/private_model.html)
		- [Adding Custom Modules](https://fluxvla.limxdynamics.com/md_source/tutorials/private_module.html)
		- [Adding Custom Engines](https://fluxvla.limxdynamics.com/md_source/tutorials/private_engine.html)
		- [Training and Deployment with Private Datasets](https://fluxvla.limxdynamics.com/md_source/tutorials/private_dataset_config.html)
		- [Inference Deployment](https://fluxvla.limxdynamics.com/md_source/tutorials/inference/index.html)

---
