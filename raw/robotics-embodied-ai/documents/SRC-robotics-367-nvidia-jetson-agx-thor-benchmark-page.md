---
source_id: "SRC-robotics-367"
title: "NVIDIA Jetson AGX Thor benchmark page"
source_type: "benchmark"
publisher: "NVIDIA"
source_date: "2026-08-05"
url: "https://developer.nvidia.com/embedded/jetson-benchmarks"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-05T06:54:25+00:00"
tags:
  - raw/source
  - source-type/benchmark
  - evidence/s
aliases:
  - SRC-robotics-367
---
# NVIDIA Jetson AGX Thor benchmark page

Jetson is used to deploy a wide range of popular DNN models, optimized transformer models and ML frameworks to the edge with high performance inferencing, for tasks like real-time classification and object detection, pose estimation, semantic segmentation, and natural language processing (NLP).

## MLPerf Inference Benchmarks

The tables below show inferencing benchmarks from the NVIDIA Jetson submissions to the MLPerf Inference Edge category.

### NVIDIA® Jetson AGX Thor™ Benchmarking Results

<table><thead><tr><th></th><th>Model</th><th colspan="2">NVIDIA Jetson AGX Thor</th></tr></thead><tbody><tr><td></td><td></td><td>Max Concurrency 1<br>(tokens/sec)</td><td>Max Concurrency 8<br>(tokens/sec)</td></tr><tr><td rowspan="6">LLM</td><td>Llama 3.1 8B</td><td>41.3</td><td>150.8</td></tr><tr><td>Llama 3.3 70B</td><td>4.7</td><td>12.6</td></tr><tr><td>Qwen 3 30B-A3B</td><td>61</td><td>226.4</td></tr><tr><td>Qwen 3 32B</td><td>13.19</td><td>79.1</td></tr><tr><td>Deepseek R1 7B</td><td>41.32</td><td>304.8</td></tr><tr><td>Deepseek R1 32B</td><td>13.31</td><td>82.6</td></tr><tr><td rowspan="3">VLM</td><td>Qwen2.5-VL 3B</td><td>71.7</td><td>356.86</td></tr><tr><td>Qwen2.5-VL 7B</td><td>45</td><td>252</td></tr><tr><td>LLama 3.2 11B Vision</td><td>26.31</td><td>69.63</td></tr></tbody></table>

- These results were achieved with the NVIDIA Jetson AGX Thor Developer Kit running NVIDIA JetPack™ 7.0, NVIDIA CUDA® 13.0, and NVIDIA TensorRT™ 10.13. LLM and VLM benchmarks were performed using VLLM with ISL/OSL as 2048/128.

NOTE: Future software optimizations will deliver additional performance improvements.

## MLPerf Inference Benchmarks

The tables below show inferencing benchmarks from the NVIDIA Jetson submissions to the MLPerf Inference Edge category.

### Jetson AGX Orin™ MLPerf v4.0 Results

<table><thead><tr><th>Model</th><th colspan="2"><a href="https://developer.nvidia.com/embedded/jetson-orin">NVIDIA Jetson AGX Orin (TensorRT)</a></th></tr></thead><tbody><tr><td></td><td>Single Stream Latency (ms)</td><td>Offline (Samples/s)</td></tr><tr><td>LLM Summarization<br>GPT-J 6B</td><td>10204.46</td><td>0.15</td></tr><tr><td>Image Generation<br>stable-diffusion-xl</td><td>12941.92</td><td>0.08</td></tr></tbody></table>

- Full Results can be found at [v4.0 Results | MLCommons](https://mlcommons.org/en/inference-edge-11/)
- These results were achieved with the NVIDIA Jetson AGX Orin Developer Kit running JetPack 5.1.1, TensorRT 9.0.1 and CUDA 11.4
- These MLPerf Results can be reproduced with the code in the following link: [https://github.com/mlcommons/inference\_results\_v4.0/tree/main/closed/NVIDIA](https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/NVIDIA)

### Jetson AGX Orin and Jetson Orin NX MLPerf v3.1 Results

<table><thead><tr><th>Model</th><th colspan="3"><a href="https://developer.nvidia.com/embedded/jetson-orin">NVIDIA Jetson AGX Orin (TensorRT)</a></th><th colspan="2"><a href="https://developer.nvidia.com/embedded/jetson-orin">NVIDIA Orin MaxQ (TensorRT)</a></th><th><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/">NVIDIA Jetson Orin NX</a></th><th colspan="2"><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/">NVIDIA Jetson Orin NX MaxQ</a></th></tr></thead><tbody><tr><td></td><td>Single Stream Latency (ms)</td><td>Offline (Samples/s)</td><td>Multi Stream Latency(ms)</td><td>Offline (Samples/s)</td><td>System Power(W)</td><td>Offline (Samples/s)</td><td>Offline (Samples/s)</td><td>System Power(W)</td></tr><tr><td>Image Classification<br>ResNet</td><td>0.64</td><td>6423.63</td><td>2.18</td><td>3526.29</td><td>23.57</td><td>2640.51</td><td>1681.87</td><td>14.95</td></tr><tr><td>Object Detection<br>Retinanet</td><td>11.67</td><td>148.71</td><td>82.92</td><td>74.71</td><td>22.27</td><td>66.5</td><td>47.59</td><td>15.57</td></tr><tr><td>Medical Imaging<br>3D-Unet-99.0</td><td>4371.46</td><td>0.51</td><td>N/A</td><td>N/A</td><td>N/A</td><td>0.2</td><td>0.19</td><td>22.04</td></tr><tr><td>Speech-to-text<br>RNN-T</td><td>94.01</td><td>1169.98</td><td>N/A</td><td>N/A</td><td>N/A</td><td>431.92</td><td>327.79</td><td>17.25</td></tr><tr><td>Natural Language Processing<br>BERT</td><td>5.71</td><td>553.69</td><td>N/A</td><td>N/A</td><td>N/A</td><td>194.5</td><td>136.59</td><td>17.04</td></tr></tbody></table>

- Full Results can be found at [v3.1 Results | MLCommons](https://mlcommons.org/en/inference-edge-11/)
- These results were achieved with the NVIDIA Jetson AGX Orin Developer Kit and Orin NX 16GB running JetPack 5.1.1, TensorRT 8.5.2 and CUDA 11.4 A
- These MLPerf Results can be reproduced with the code in the following link: [https://github.com/mlcommons/inference\_results\_v3.1/tree/main/closed/NVIDIA](https://github.com/mlcommons/inference_results_v3.1/tree/main/closed/NVIDIA)

### Jetson AGX Orin Jetson Orin NX MLPerf v3.0 Results

<table><thead><tr><th rowspan="2">Model</th><th colspan="3"><a href="https://developer.nvidia.com/embedded/jetson-xavier-nx">NVIDIA Jetson AGX Orin (TensorRT)</a></th><th colspan="2"><a href="https://developer.nvidia.com/embedded/jetson-orin">NVIDIA Orin MaxQ (TensorRT)</a></th><th colspan="2"><a href="https://developer.nvidia.com/embedded/jetson-orin-nx">NVIDIA Jetson Orin NX</a></th></tr></thead><tbody><tr><td></td><td>Single Stream (Samples/s)</td><td>Offline (Samples/s)</td><td>Multi Stream (Samples/s)</td><td>Offline (Samples/s)</td><td>System Power(W)</td><td>Offline (Samples/s)</td></tr><tr><td>Image Classification<br>ResNet-50</td><td>1538</td><td>6438.10</td><td>3686</td><td>3525.91</td><td>23.06</td><td>2517.99</td></tr><tr><td>Object Detection<br>Retinanet</td><td>51.57</td><td>92.40</td><td>60.00</td><td>34.6</td><td>22.4</td><td>36.14</td></tr><tr><td>Medical Imaging<br>3D-Unet</td><td>.26</td><td>.51</td><td>N/A</td><td>3.28</td><td>28.64</td><td>.19</td></tr><tr><td>Speech-to-text<br>RNN-T</td><td>9.822</td><td>1170.23</td><td>N/A</td><td>14472</td><td>25.64</td><td>405.27</td></tr><tr><td>Natural Language Processing<br>BERT</td><td>144.36</td><td>544.24</td><td>N/A</td><td>3685.36</td><td>25.91</td><td>163.57</td></tr></tbody></table>

- Steps to reproduce these results can be found at [v3.0 Results | MLCommons](https://mlcommons.org/en/inference-edge-30/)
- These results were achieved with the NVIDIA Jetson AGX Orin Developer Kit running a preview of TensorRT 8.5.0, and CUDA 11.4
- Note different configurations were used for single stream, offline and multistream. Reference the MLCommons page for more details

## Gen AI Benchmarks

NVIDIA Jetson AI Lab is a collection of tutorials showing how to run optimized models on NVIDIA Jetson, including the latest generative AI and transformer models. These tutorials span a variety of model modalities like LLMs (for text), VLMs (for text and vision data), ViT (Vision Transformers), image generation, and ASR or TTS (for audio).

### Large Language Models (LLM)

<iframe width="600" height="371" frameborder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTJ9lFqOIZSfrdnS_0sa2WahzLbpbAbBCTlS049jpOchMCum1hIk-wE_lcNAmLkrZd0OQrI9IkKBfGp/pubchart?oid=2126319913&amp;format=interactive"></iframe>

### Small Language Models (SLM)

<iframe width="916" height="507" frameborder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTJ9lFqOIZSfrdnS_0sa2WahzLbpbAbBCTlS049jpOchMCum1hIk-wE_lcNAmLkrZd0OQrI9IkKBfGp/pubchart?oid=1746097360&amp;format=interactive"></iframe>

### Vision Transformers (ViT)

<iframe width="600" height="371" frameborder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTJ9lFqOIZSfrdnS_0sa2WahzLbpbAbBCTlS049jpOchMCum1hIk-wE_lcNAmLkrZd0OQrI9IkKBfGp/pubchart?oid=702230147&amp;format=interactive"></iframe>

### Riva

<iframe width="600" height="371" frameborder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTJ9lFqOIZSfrdnS_0sa2WahzLbpbAbBCTlS049jpOchMCum1hIk-wE_lcNAmLkrZd0OQrI9IkKBfGp/pubchart?oid=1167153335&amp;format=interactive"></iframe>  

- Full Results can be found at [Jetson AI Lab Benchmarks](https://www.jetson-ai-lab.com/benchmarks.html)
