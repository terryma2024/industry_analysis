---
title: LingBot-Depth 2.0 视频深度调研
type: synthesis
date_created: 2026-07-11
last_updated: 2026-07-11
sources:
  - knowledge/_sources/bilibili-bv15pmb68eb5-lingbot-depth-2-0.md
  - raw/_inbox/transcripts/2026-07-11-bilibili-bv15pmb68eb5-lingbot-depth-2-0.json
tags: [bilibili, embodied-ai, perception, depth-completion]
status: active
---

# LingBot-Depth 2.0 视频深度调研

> [!summary]
> 视频正确指出玻璃、镜面、透明/低纹理物体会造成深度缺失。论文 `SRC-robotics-272` 确认 LingBot-Vision 面向稠密空间感知预训练，并支撑 LingBot-Depth 2.0 深度补全；补全值仍是模型预测，不能等同传感器真值。

## 事实、估计、判断与假设

| 类型 | 内容 |
|---|---|
| 事实 | 深度补全将 RGB 空间表征与原始有效深度结合，服务稠密空间感知。`SRC-robotics-272` |
| 视频线索 | 对透明/反光场景的具体效果与图示是 B 级教学线索。 |
| 判断 | 机器人栈应同时保存 raw/refined depth 和不确定性掩码；动作规划不能把补全像素当测距真值。 |
| 假设 | 更低深度误差会转化为更高透明物体抓取率和更低玻璃碰撞率。 |

## 产业启发

- 数据层应保存标定、时间戳、raw depth、补全版本和置信度，以支持回放与模型回归。
- 投资评测应看 held-out 抓取成功率、SLAM 漂移、碰撞率、端侧吞吐和传感器兼容矩阵，而非只看 RMSE。
- 职业上可做透明物体抓取的 raw-vs-refined A/B 测试，覆盖标定、点云、不确定性与任务评测。

## 风险与后续验证

- 在逆光、动态遮挡、不同材质和跨相机域上测量失效模式。
- 核验代码/权重开放范围、许可证、benchmark mask 协议与推理资源；作者报告性能需独立复现。
- 关键安全任务维持接触/力觉或冗余传感器与保守降级。

## 关联连接

- [[_entities/LiDAR|LiDAR 激光雷达]]
- [[_entities/SLAM|SLAM]]
- [[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练]]
