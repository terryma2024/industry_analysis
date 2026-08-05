---
source_id: "SRC-robotics-354"
title: "cuVSLAM CUDA accelerated visual odometry and mapping paper full PDF"
source_type: "research_paper"
publisher: "NVIDIA"
source_date: "2025-07-08"
url: "https://arxiv.org/pdf/2506.04359.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-05T06:50:30+00:00"
source_markdown: "SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-robotics-354
---
# cuVSLAM CUDA accelerated visual odometry and mapping paper full PDF - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-354`
- Raw Markdown: [SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md](SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md)
- Evidence grade: `S`

## Page-Level Leads

- [p. 1] 2025-7-9 cuVSLAM: CUDA accelerated visual odometry and mapping Alexander Korovko1 , Dmitry Slepichev1 , Alexander Efitorov1 , Aigul Dzhumamuratova1 , Viktor Kuznetsov1 , Joydeep Biswas1 , Hesam Rabeti1 and Soha Pouya1 1 NVIDIA , {akorovko, dslepichev, aefitorov, adzhumamurat, vkuznetsov, jbiswas, hrabeti, spouya}@nvidia.com Abstract Accurate and ro
- [p. 1] We present cuVSLAM, a state-of-the-art solution for visual simultaneous localization and mapping, which can arXiv:2506.04359v3 [cs.RO] 8 Jul 2025 operate with a variety of visual-inertial sensor suites, including multiple RGB and depth cameras, and inertial measurement units.
- [p. 2] cuVSLAM: CUDA accelerated visual odometry and mapping • Support for optional IMU and depth sensors • Efficient CUDA implementation enabling real-time performance on edge devices like NVIDIA Jetson • A modular architecture separating frontend pose estimation from backend map refinement • Robust feature tracking and mapping capabilities that maintain
- [p. 2] The frontend module performs real-time pose estimation using feature detection, tracking, and local mapping, while the backend handles global map consistency through pose graph optimization and loop closure.
- [p. 3] cuVSLAM: CUDA accelerated visual odometry and mapping Figure 2: 2D module implements keyframe selection, feature selection and 2D tracking.
- [p. 3] The pipeline begins with keypoint selection, which is designed to identify high-contrast features and ensure an approximately uniform distribution of keypoints across the image.
- [p. 4] cuVSLAM: CUDA accelerated visual odometry and mapping 2.2.1.
- [p. 4] Stereo Stereo mode is the default mode in cuVSLAM.
- [p. 5] cuVSLAM: CUDA accelerated visual odometry and mapping for each camera.
- [p. 5] Let 𝑆𝑐𝑢𝑟𝑟 be a set of all currently observed points from all the cameras and 𝑆𝑘𝑓 is the set of points observed in the previous keyframe.
- [p. 6] cuVSLAM: CUDA accelerated visual odometry and mapping • Visual-inertial pose estimation is used every frame.
- [p. 6] It constrains two consecutive robot states 𝑆𝑖−1 and 𝑆𝑖 with IMU and visual factors.
- [p. 7] cuVSLAM: CUDA accelerated visual odometry and mapping solver implemented on GPU: ∑︁ ∑︁ ∑︁ 𝑇ˆ21 = arg𝑇21 min( ||𝑟𝑟𝑒𝑝𝑟 (𝑝)||2Σ + (||𝑟𝐼 (𝑥)||2 + ||𝑟𝑍 (𝑥)||2𝜎𝑧 ) + ||𝑟𝑝 (𝑥, 𝑦)||2 ) (13) 𝑝∈𝑃 𝑜𝑖𝑛𝑡𝑠 𝑥∈𝑃 𝑖𝑥𝑒𝑙𝑠 (𝑥,𝑦)∈𝑇 𝑟𝑎𝑐𝑘𝑠 2.2.5.
- [p. 7] Mono Mono camera mode shares the same common approach as 2D feature tracking, with subsequent point triangu- lation and pose estimation.
- [p. 8] cuVSLAM: CUDA accelerated visual odometry and mapping Then, after shifting landmarks into the map frame, we solve for the relative pose estimate: ∑︁ ∑︁ 𝑇ˆ𝑏𝑚 = arg𝑇 𝑏𝑚 min ||𝜋(𝑇𝑘𝑐𝑏 𝑇 𝑏𝑚 𝑇 𝑚𝑤 𝑝𝑤 2 𝑗 ) − 𝑜𝑗,𝑘 ||Σ (14) 𝑗∈[1,𝑀 ] 𝑘∈[1,𝐶] • Pose graph optimization.
- [p. 8] Provided with the pose deltas between poses either by the frontend or the loop closure mechanism, cuVSLAM refines the map by minimizing the following sum across pose graph edges 𝐸: ∑︁ −1 −1 𝑇1:𝑁 = arg𝑇1:𝑁 min ||𝐿𝑜𝑔(𝐷𝑖𝑗 𝑇𝑖 𝑇𝑗 )||2 (15) 𝑖,𝑗∈𝐸 3.
- [p. 9] cuVSLAM: CUDA accelerated visual odometry and mapping employed a controlled experimental methodology: we first established baseline system utilization with the RealSense camera in motion but without cuVSLAM processing, then repeated the similar camera movement pattern with cuVSLAM visual tracking active.
- [p. 9] Resource utilization metrics were sampled at 15 ms intervals for equal durations in both experiments.
- [p. 10] cuVSLAM: CUDA accelerated visual odometry and mapping comparative analysis, we include performance metrics for the classical computer vision-based ORB-SLAM3 and the deep learning-based DPVO alongside cuVSLAM.
- [p. 10] Each library was configured according to the dataset characteristics: ORB-SLAM3 and cuVSLAM operated in their corresponding specialized modes (monocular- depth, stereo, or stereo-inertial), while DPVO consistently used monocular mode across all evaluations, utilizing the front-left camera for stereo datasets.
- [p. 11] cuVSLAM: CUDA accelerated visual odometry and mapping Table 3: Evaluation results for cuVSLAM Multi-Stereo Visual Odometry and SLAM on multi-camera datasets Dataset Method avgRTE, % avgRE, deg RMSE APE cuVSLAM Odom 0.18 1.15 0.28 R2B cuVSLAM SLAM 0.11 0.70 0.18 cuVSLAM Odom* 0.54 0.95 0.14 TartanGround cuVSLAM Odom 0.21 0.48 0.09 cuVSLAM SLAM 0.17 
- [p. 11] While TartanAir V2 results indicate room for improvement, they also demonstrate the importance of multi-camera mode for robust tracking in most environments, with some showing 2–4× improvement in multi-camera SLAM mode.
- [p. 12] cuVSLAM: CUDA accelerated visual odometry and mapping Despite these severe visual constraints, the odometry trajectory maintained stability without exhibiting jumps or discontinuities, validating the system’s robustness to partial visual obstruction.
- [p. 12] This capability represents a significant advancement for visual tracking systems.
- [p. 13] cuVSLAM: CUDA accelerated visual odometry and mapping • Computational Efficiency: The system maintains low computational overhead while delivering high- accuracy localization, enabling seamless integration into complex robotic stacks such as NVIDIA Isaac Perceptor3 , which incorporates NVBLOX Millane et al.
- [p. 13] (2024) for 3D reconstruction and Nav2 Macenski et al.
- [p. 14] cuVSLAM: CUDA accelerated visual odometry and mapping References [1] Kitti visual odometry / slam evaluation 2012.
- [p. 14] URL https://www.cvlibs.net/datasets/kitti/eval_ odometry.php.
- [p. 15] cuVSLAM: CUDA accelerated visual odometry and mapping [15] B.
- [p. 15] An iterative image registration technique with an application to stereo vision.
- [p. 16] cuVSLAM: CUDA accelerated visual odometry and mapping Figure 10: cuVSLAM evaluation results on KITTI odometry benchmark sequences 00-10.
- [p. 16] Translation and rotation errors are calculated on segments of 100-800m following the KITTI public leaderboard methodology, averaged metrics: Translation: 0.85%, Rotation: 0.0025 [deg/m].
- [p. 17] cuVSLAM: CUDA accelerated visual odometry and mapping Table 5: cuVSLAM Mono-Depth Odometry and SLAM validation results on AR table dataset ATE (degree / cm) Mode table_01 table_02 table_03 table_04 table_05 table_06 table_07 table_08 ODOM 3.77 / 2.03 9.36 / 5.41 6.09 / 2.28 3.13 / 2.21 2.27 / 1.97 3.43 / 3.39 18.5 / 6.17 13.2 / 8.18 SLAM 2.98 / 1.7
- [p. 17] TUM RGB-D Dataset To validate the Mono-Depth mode on this dataset, a subset of 10 sequences from the Freiburg3 collection was used.
- [p. 18] cuVSLAM: CUDA accelerated visual odometry and mapping Table 7: Odometry evaluation results for cuVSLAM Multi-Stereo configuration (4 stereo cameras) on Tartan- Ground dataset.
- [p. 18] Values represent averages computed per environment.
- [p. 19] cuVSLAM: CUDA accelerated visual odometry and mapping Figure 11: Example trajectories predicted by cuVSLAM (4 Multi-Stereo Odometry) on TartanAir V2 (Easy and Hard).
- [p. 19] Black lines represent ground truth, green lines represent odometry predictions.
- [p. 20] cuVSLAM: CUDA accelerated visual odometry and mapping in MAXN mode with 3 Intel RealSense D435 stereo cameras connected via USB and hardware-synchronized.
- [p. 20] Different resolutions were obtained directly from the cameras by modifying their configuration during the initialization step of each experiment.
- [p. 21] cuVSLAM: CUDA accelerated visual odometry and mapping odometry mode for 640x360 resolution and 30 FPS followed the methodology described above with free camera movement.
- [p. 21] Figure 14: Hardware utilization and callback time on Jetson Orin Nano for Multi-Stereo Visual Odometry using RealSense cameras at 640×360 resolution and 30 FPS.
- [p. 22] cuVSLAM: CUDA accelerated visual odometry and mapping Table 9: Comparative evaluation of odometry and SLAM performance for cuVSLAM Multi-Stereo (4 stereo cameras) on the TartanGround dataset.
- [p. 22] To assess the impact of SLAM mode, a subset of sequences containing looped trajectories with observable loop closures was selected.
- [p. 23] cuVSLAM: CUDA accelerated visual odometry and mapping Table 10: TartanAir V2 Hard cuVSLAM evaluation Table 11: TartanAir V2 Hard cuVSLAM evaluation results (Envs 1–35, see Appendix A.1.5 for details) results (Envs 36–71, see Appendix A.1.5 for details) Env Seq Mode RTE RRE APE Env Seq Mode RTE RRE APE Abandoned- ODOM 1.90 13.77 8.97 ModernCity ODOM

## Extracted Tables

### Table 1 (p. 3)

                                               min                               ||𝜋(𝑇𝑘𝑐𝑏 𝑇𝑖𝑏𝑤 𝑝𝑤            2
                                                                                                𝑗 ) − 𝑜𝑗,𝑘 ||Σ   (3)

### Table 2 (p. 4)

                                   𝑇ˆ𝑏𝑤 = arg𝑇 𝑏𝑤 min                      ||𝑟𝑗𝑘  ||Σ                         (4)

### Table 3 (p. 5)

                                                  |𝑆𝑐𝑢𝑟𝑟 ∩ 𝑆𝑘𝑓 |

### Table 4 (p. 5)

                                                      |𝑆𝑘𝑓 |

### Table 5 (p. 5)

                                     𝑇ˆ𝑏𝑤 = arg𝑇 𝑏𝑤 min                      ||𝑟𝑗𝑘  ||Σ                           (6)

### Table 6 (p. 7)

   𝑇ˆ21 = arg𝑇21 min(           ||𝑟𝑟𝑒𝑝𝑟 (𝑝)||2Σ +           (||𝑟𝐼 (𝑥)||2 + ||𝑟𝑍 (𝑥)||2𝜎𝑧 ) +                   ||𝑟𝑝 (𝑥, 𝑦)||2 )   (13)

### Table 7 (p. 8)

                           𝑇ˆ𝑏𝑚 = arg𝑇 𝑏𝑚 min                      ||𝜋(𝑇𝑘𝑐𝑏 𝑇 𝑏𝑚 𝑇 𝑚𝑤 𝑝𝑤            2
                                                                                       𝑗 ) − 𝑜𝑗,𝑘 ||Σ     (14)

### Table 8 (p. 8)

                                𝑇1:𝑁 = arg𝑇1:𝑁 min     ||𝐿𝑜𝑔(𝐷𝑖𝑗 𝑇𝑖 𝑇𝑗 )||2                        (15)


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
