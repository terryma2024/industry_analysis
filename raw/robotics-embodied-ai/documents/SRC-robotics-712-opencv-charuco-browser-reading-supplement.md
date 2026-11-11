---
source_id: SRC-robotics-712
title: OpenCV ChArUco官方文档网页核阅补录
type: raw-source-note
url: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
capture_method: web-open-analyst-paraphrase
captured_at: 2026-11-10
evidence_grade: S
---

# 核阅摘记

Defuddle及直接HTML下载均403，原failed记录保留。web.open成功读取官方4.13.0页面，此为分析者释义而非全文镜像：

- 标定求相机内参与畸变系数，需环境点与像素投影对应。
- ChArUco角点比普通ArUco标记角点更适合高精度标定。
- 从多个视角获取板角点，允许局部遮挡；不要求每张都看见全部角点。
- 官方示例返回重投影误差和各视角相对标定板的位姿。
- 页面没有保证具体设备误差，也不等价于腕部相机的机器人手眼标定。

本方案的采集数量、RMS门槛和操作流程是工程设计值，非该页面实测结论。
