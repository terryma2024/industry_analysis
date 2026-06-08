---
title: NVIDIA Cosmos 3 上手调研与计划
type: news-summary
date_created: 2026-06-05
last_updated: 2026-06-05
sources:
  - https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai
  - https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/
  - https://research.nvidia.com/labs/cosmos-lab/cosmos3/
  - https://github.com/NVIDIA/Cosmos
  - https://huggingface.co/collections/nvidia/cosmos3
  - https://arxiv.org/abs/2606.02800
tags:
  - news
  - ai
  - robotics
  - embodied-ai
  - nvidia
  - world-model
status: active
---

# NVIDIA Cosmos 3 上手调研与计划

## 基本信息

- **事件**: NVIDIA 在 COMPUTEX/GTC Taipei 2026 期间发布 Cosmos 3，定位为面向 Physical AI 的开放 omnimodal world foundation model。
- **发布时间**: NVIDIA 新闻稿为 2026-06-01；arXiv 技术报告提交时间为 2026-06-01；Hugging Face 模型卡记录的发布入口为 2026-05-31。
- **平台/发布方**: NVIDIA Newsroom、NVIDIA Developer Blog、NVIDIA Research Cosmos Lab、GitHub、Hugging Face、arXiv。
- **提取方式**: Web 检索并核对官方新闻稿、技术博客、研究页、GitHub release/README、Hugging Face collection/model card、arXiv 摘要。

## 关键事实

1. Cosmos 3 当前公开家族包括 Cosmos3-Nano、Cosmos3-Super、Cosmos3-Super-Text2Image、Cosmos3-Super-Image2Video、Cosmos3-Nano-Policy-DROID。
2. Cosmos3-Nano 为 16B 参数，面向较高效率的研究、开发与推理；Cosmos3-Super 为 64B 参数，面向更高质量的世界生成、推理与数据合成。
3. 模型使用 Mixture-of-Transformers 架构，把 Reasoner tower 和 Generator tower 放到统一框架中：Reasoner 处理图像、视频、文本等理解任务；Generator 生成图像、视频、音频和动作序列。
4. 支持输入/输出覆盖 text、image、video、audio、action。典型任务包括视频理解、物理推理、text-to-image、text-to-video、image-to-video、action-conditioned rollout、robot policy、inverse dynamics 和 forward dynamics。
5. NVIDIA 同步开放模型、代码、训练/后训练资源、合成数据集和 benchmark；Hugging Face collection 中列出了 Cosmos3 模型和 PhysicalAI-WorldModel-Synthetic 系列数据集。
6. 上手入口有三类：`build.nvidia.com` 托管试用、Hugging Face/GitHub 本地开发、NVIDIA NIM 微服务部署。当前 Reasoner NIM 已可用；Generator NIM 按技术博客表述仍需等待后续发布。
7. 官方 README 把本地/服务端路线分为 Diffusers、vLLM-Omni、vLLM Reasoner、NIM Reasoner。Generator 侧适合先跑 Diffusers 或 vLLM-Omni；Reasoner 侧适合先跑 NIM 或 vLLM。
8. 模型卡显示 Cosmos3-Nano 支持商用和非商用，许可证为 OpenMDW 1.1；正式商用前仍需要逐条核对 OpenMDW 1.1 约束、数据合规和输出安全要求。

## 我的判断

Cosmos 3 对机器人和具身智能的价值，不只是“更强视频生成”。更重要的是它把三件事接近合在一起：世界理解、未来状态生成、动作预测。对 [[robotics-embodied-ai/00-index|机器人与具身智能]] 学习者来说，最值得上手的是 Reasoner + action workflow，而不是一开始就追求 720p 视频生成。

对中国相关方向，Cosmos 3 的直接意义在于三类场景：一是机器人训练数据扩增，尤其是稀有交互和失败样本；二是自动驾驶和仓储/工厂视觉场景的合成数据；三是作为 [[_entities/HuggingFaceLeRobot|LeRobot]]、[[_entities/UniversalManipulationInterface|UMI]]、[[_entities/DiffusionPolicy|Diffusion Policy]] 等学习路线的世界模型补充。主要约束是 NVIDIA 高端算力可得性、云服务成本、模型许可证、以及生成数据能否通过真实任务验证。

## 上手计划

### 第 0 步：先定目标

建议目标不要定成“完整掌握 Cosmos 3”，而是定成一个 2 周可验收目标：

> 用 Cosmos 3 完成一个机器人/仓储场景 demo：输入图片或短视频，先让 Reasoner 做物理理解和下一步动作分析，再用 Generator 生成一个 5-8 秒的未来状态或动作条件视频，并记录失败样本。

### 第 1 步：0.5 天，云端试用

- 打开 NVIDIA Cosmos 页面和 `build.nvidia.com` 体验 Cosmos3-Nano Reasoner。
- 任务：准备 3 个视频/图片提示词，分别测试物理推理、物体状态判断、下一步动作预测。
- 输出：记录 prompt、输入媒体、输出结果、明显错误，形成一个小评测表。
- 验收：知道 Reasoner 能回答什么、容易幻觉什么、是否适合你的机器人学习目标。

### 第 2 步：1 天，读最小资料包

- 读 NVIDIA Developer Blog 的 “What is new / supported modalities / training recipes / NIM” 部分。
- 读 GitHub README 的 model family、quickstart、vLLM-Omni、Reasoner with NIM、limitations。
- 浏览 arXiv 摘要和 benchmark 结论，不需要第一遍啃完整技术报告。
- 验收：能解释 Nano vs Super、Reasoner vs Generator、Diffusers vs vLLM-Omni vs NIM 的差异。

### 第 3 步：1-2 天，本地或云端跑 Reasoner

优先路线：NIM Reasoner。原因是它是 OpenAI-compatible API，工程负担最低。

前置条件：

- NVIDIA GPU 环境，Linux/Docker/NVIDIA Container Toolkit。
- NGC API key。
- 若无本地 NVIDIA GPU，先用云 GPU 或继续走托管体验。

最小命令形态参考：

```bash
docker run --gpus=all \
  -e NGC_API_KEY=$NGC_API_KEY \
  -e NIM_MODEL_SIZE=nano \
  -p 8000:8000 \
  nvcr.io/nim/nvidia/cosmos3-reasoner:latest
```

验收：

- 用 `http://127.0.0.1:8000/v1/chat/completions` 跑通一张图片或一个短视频理解请求。
- 能输出结构化 JSON，例如 `objects`、`state`、`risk`、`next_action`、`uncertainty`。

### 第 4 步：2-3 天，跑 Generator 的最小 demo

建议先跑 Cosmos3-Nano，不直接上 Super。

两条路线：

- **Diffusers**: 适合 Python-first 探索和理解 pipeline，但生成视频会很慢。
- **vLLM-Omni**: 适合搭 OpenAI-compatible 服务，后续做 demo 和批量调用更顺。

优先任务：

1. Text-to-image: 先确认模型、依赖、CUDA、HF token 都通。
2. Image-to-video: 用一张机器人/仓储图片生成 5-8 秒短视频。
3. Text-to-video: 用结构化 prompt 生成仓储移动机器人场景。

验收：

- 至少生成 3 个可播放 MP4。
- 记录分辨率、帧数、推理时间、显存占用、prompt、seed。
- 记录失败模式：物体穿模、动作不连续、机器人形态漂移、物理不合理、文字/标志错误。

### 第 5 步：3-5 天，转向机器人动作相关任务

如果目标是具身智能，下一步重点不是漂亮视频，而是 action workflow：

- 跑 Cosmos3-Nano-Policy-DROID 的示例或模型卡相关 cookbook。
- 用 DROID/BridgeData2/LeRobot v3 相关数据理解 action schema。
- 对比 [[_entities/ActionChunkingTransformer|ACT]]、[[_entities/DiffusionPolicy|Diffusion Policy]]、OpenPI/OpenVLA 类路线：Cosmos 3 是世界模型和动作生成补充，不一定直接替代传统策略模型。

验收：

- 能说明一个样本中的 observation、instruction、action chunk 分别是什么。
- 能跑通一次 action prediction 或 forward dynamics 示例。
- 能把输出动作和视频 rollout 放到同一份实验记录中。

## 推荐学习顺序

| 顺序 | 内容 | 目标 | 暂不深挖 |
| --- | --- | --- | --- |
| 1 | Cosmos3-Nano Reasoner | 建立物理理解能力直觉 | Super、多机部署 |
| 2 | Nano image/video generation | 跑通图像和视频生成链路 | 720p 高质量生成 |
| 3 | vLLM-Omni API | 把生成能力服务化 | 复杂并行优化 |
| 4 | Policy-DROID/action examples | 进入机器人动作模型 | 真机部署 |
| 5 | 后训练 recipes | 用自己的机器人/仓储数据适配 | 大规模训练 |

## 风险与待验证

- **算力**: 16B 的 Nano 也不是消费级轻量模型；视频生成尤其吃显存和时间。需要先确认本地 GPU 型号、显存、CUDA driver，再选择 Diffusers、vLLM-Omni 或 NIM。
- **许可证**: OpenMDW 1.1 允许范围需要在商用、再分发、数据服务场景下逐条核对。
- **模型可靠性**: 物理合理视频不等于可执行策略。用于机器人训练前必须用真实或仿真 benchmark 验证。
- **数据闭环**: 生成样本如果不能进入 LeRobot/UMI/DROID 类 schema 并通过质检，就只是素材，不是训练数据资产。
- **版本状态**: 当前资料显示 Cosmos 3 Edge coming soon、Generator NIM 待后续发布；工具链可能在未来数周快速变化。

## 关联连接

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
- [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]]
- [[_entities/DiffusionPolicy|Diffusion Policy]]
