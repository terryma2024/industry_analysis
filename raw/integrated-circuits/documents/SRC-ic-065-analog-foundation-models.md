---
source_id: "SRC-ic-065"
title: "Analog Foundation Models"
source_type: "research_paper"
publisher: "NeurIPS / IBM Research"
source_date: "2025-12-02"
url: "https://research.ibm.com/publications/analog-foundation-models"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:35:06+00:00"
tags:
  - raw/source
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-ic-065
---
# Analog Foundation Models

## Abstract

Analog in-memory computing (AIMC) is a promising compute paradigm to improve speed and power efficiency of neural network inference beyond the limits of conventional von Neumann-based architectures. However, AIMC introduces fundamental challenges such as noisy computations and strict constraints on input and output quantization. Because of these constraints and imprecisions, off-the-shelf LLMs are not able to achieve 4-bit-level performance when deployed on AIMC-based hardware. While researchers previously investigated recovering this accuracy gap on small, mostly vision-based models, a generic method applicable to LLMs pre-trained on trillions of tokens does not yet exist. In this work, we introduce a general and scalable method to robustly adapt LLMs for execution on noisy, low-precision analog hardware. Our approach enables state-of-the-art models — including Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct — to retain performance comparable to 4-bit weight, 8-bit activation baselines, despite the presence of analog noise and quantization constraints. Additionally, we show that as a byproduct of our training methodology, analog foundation models can be quantized for inference on low-precision digital hardware. Finally, we show that our models also benefit from test-time compute scaling, showing better scaling behavior than models trained with 4-bit weight and 8-bit static input quantization. Our work bridges the gap between high-capacity LLMs and efficient analog hardware, offering a path toward energy-efficient foundation models. Code is available at github.com/IBM/analog-foundation-models.

## Related

Paper

### A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference

Manuel Le Gallo, Riduan Khaddam-Aljameh, et al.

Nature Electronics

Conference paper

### An Architecture for Heterogeneous High-Performance Computing Systems: Motivation and Requirements

Christoph Hagleitner, Charles Johns, et al.

IEEE JVA Symposium 2023

Conference paper

### FailureSensorIQ: A Multi-Choice QA Dataset for Understanding Sensor Relationships and Failure Modes

Christodoulos Constantinides, Dhaval Patel, et al.

NeurIPS 2025

Chris Bottoms, Rick Johnson, et al.

SPIE Advanced Lithography + Patterning 2025
