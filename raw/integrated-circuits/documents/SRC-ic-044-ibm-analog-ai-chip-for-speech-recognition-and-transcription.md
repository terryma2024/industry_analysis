---
source_id: "SRC-ic-044"
title: "IBM analog AI chip for speech recognition and transcription"
source_type: "research_paper"
publisher: "IBM Research / Nature"
source_date: "2023-08-23"
url: "https://research.ibm.com/publications/an-analog-ai-chip-for-energy-efficient-speech-recognition-and-transcription"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-21T02:06:23+00:00"
tags:
  - raw/source
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-ic-044
---
# IBM analog AI chip for speech recognition and transcription

## Abstract

Models of artificial intelligence (AI) that have billions of parameters can achieve high accuracy across a range of tasks1,2, but they exacerbate the poor energy efficiency of conventional general-purpose processors, such as graphics processing units or central processing units. Analog in-memory computing (analog-AI)3–7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’. However, analog-AI has yet to demonstrate software-equivalent (SWeq) accuracy on models that require many such tiles and efficient communication of neural-network activations between the tiles. Here we present an analog-AI chip that combines 35 million phase-change memory devices across 34 tiles, massively parallel inter-tile communication and analog, low-power peripheral circuitry that can achieve up to 12.4 tera-operations per second per watt (TOPS/W) chip-sustained performance. We demonstrate fully end-to-end SWeq accuracy for a small keyword-spotting network and near-SWeq accuracy on the much larger MLPerf8 recurrent neural-network transducer (RNNT), with more than 45 million weights mapped onto more than 140 million phase-change memory devices across five chips.

## Related

Workshop paper

### Revisiting Disaggregated Large Language Model Serving for Performance and Energy Implications

Jiaxi Li, Yue Zhu, et al.

EuroSys 2026

Paper

### Toward Software-Equivalent Accuracy on Transformer-Based Deep Neural Networks With Analog Memory Devices

Katherine Spoon, Hsinyu Tsai, et al.

Frontiers in Computational Neuroscience

Venkata Vamsikrishna Meduri, Abdul Quamar, et al.

VLDB Journal

Marcelo Amaral, Tatsuhiro Chiba

Kubecon + CloudNativeCon NA 2023
