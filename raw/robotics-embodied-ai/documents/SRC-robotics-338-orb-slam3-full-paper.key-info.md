---
source_id: "SRC-robotics-338"
title: "ORB-SLAM3 full paper"
source_type: "paper"
publisher: "University of Zaragoza / IEEE Transactions on Robotics"
source_date: "2021-04-23"
url: "https://arxiv.org/pdf/2007.11898.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-05T06:10:43+00:00"
source_markdown: "SRC-robotics-338-orb-slam3-full-paper.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-338
---
# ORB-SLAM3 full paper - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-338`
- Raw Markdown: [SRC-robotics-338-orb-slam3-full-paper.md](SRC-robotics-338-orb-slam3-full-paper.md)
- Evidence grade: `S`

## Page-Level Leads

- [p. 1] This paper has been accepted for publication in IEEE Transactions and Robotics.
- [p. 1] DOI: 10.1109/TRO.2021.3075644 ©2021 IEEE.
- [p. 2] 2 ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM Carlos Campos∗ , Richard Elvira∗ , Juan J.
- [p. 2] Gómez Rodrı́guez, José M.M.
- [p. 3] 3 initialization phase.
- [p. 3] The initialization method proposed A.
- [p. 4] 4 Table I: Summary of the most representative visual (top) and visual-inertial (bottom) systems, in chronological order.
- [p. 4] Estimation Multi Maps Mono IMU Stereo IMU Robustness Open source Data Accuracy Relocali- Fisheye SLAM Loop Stereo Pixels or VO used association zation closing Mono Mono-SLAM Shi SLAM Correlation EKF - - - X - - - - Fair Fair [15]1 [13], [14] Tomasi PTAM Pyramid Very SLAM FAST BA Thumbnail - - X - - - - Fair [19] [16]–[18] SSD Good LSD-SLAM FABMAP S
- [p. 5] 5 is a novel outstanding metric-semantic mapping system, but TRACKING Extract Initial Pose Estimation Frame its metric part consists in stereo-inertial odometry plus loop ORB from last frame, Track New KeyFrame Relocalization or Local Map Decision closing with DBoW2 and pose-graph optimization, achieving IMU IMU Map creation integration similar acc
- [p. 5] In this work we build on ORB-SLAM-VI and extend it to ATLAS Non-active KeyFrame Active Map Map Map stereo-inertial SLAM.
- [p. 6] 6 performs loop correction; if it belongs to a different map, rectifying a divergent stereo pair, or a stereo fisheye camera both maps are seamlessly merged into a single one, that would require severe image cropping, loosing the advantages becomes the active map.
- [p. 6] After a loop correction, a full of a large FOV.
- [p. 7] Given these preintegrated terms and states Si and Si+1 , • Ignoring sensor uncertainties during IMU initialization we adopt the definition of inertial residual rIi,i+1 from [61]: produces large unpredictable errors [64].
- [p. 7] rIi,i+1 = [r∆Ri,i+1 , r∆vi,i+1 , r∆pi,i+1 ] So, taking properly into account sensor uncertainties, we state the IMU initialization as a MAP estimation problem, r∆Ri,i+1 = Log ∆RTi,i+1 RTi Ri+1  split in three steps: r∆vi,i+1 = RTi (vi+1 − vi − g∆ti,i+1 ) − ∆vi,i+1 1) Vision-only MAP Estimation: We initialize pure   1 monocular SLAM [2] and run i
- [p. 8] 8 Map Points Up-to-scale parameters Map Points ...
- [p. 8] Inertial residual Random Walk ...
- [p. 9] 9 If the system gets lost within 15 seconds after IMU initial- distance ratio to the second-closest match [76].
- [p. 9] The steps of ization, the map is discarded.
- [p. 10] 10 the place recognition hypothesis.
- [p. 10] Visual Map Merging ...
- [p. 11] 11 and more than doubles the accuracy of VI-DSO and VINS- MH01 MH02 MH03 MH04 MH05 V101 V102 V103 MH01 MH02 MH03 MH04 MH05 V101 V102 V103 Mono, showing again the advantages of mid-term and long- 0.50 V201 V202 V203 V201 V202 V203 0.45 term data association.
- [p. 11] Compared with ORB-SLAM VI, our 2 2 0.40 novel fast IMU initialization allows ORB-SLAM3 to calibrate 0.35 4 4 Mono-Inertial 0.30 the inertial sensor in a few seconds and use it from the very Monocular 0.25 6 6 0.20 beginning, being able to complete all EuRoC sequences, and 0.15 8 8 obtaining better accuracy.
- [p. 12] 12 Table II: Performance comparison in the EuRoC dataset (RMS ATE in m., scale error in %).
- [p. 12] Except where noted, we show results reported by the authors of each system, for all the frames in the trajectory, comparing with the processed GT.
- [p. 13] 13 Table III: TUM VI Benchmark [80]: RMS ATE (m) for regions Table V: Multi-session RMS ATE (m) on the EuRoC dataset.
- [p. 13] with available ground-truth data.
- [p. 14] 14 room1+magistrale1+magistrale5+slides1 20 10 0 -10 room1 magistrale1 -20 magistrale5 slides1 -30 -20 0 20 40 60 80 100 Figure 5: Multi-session stereo-inertial result with several sequences from TUM-VI dataset (front, side and top views).
- [p. 14] Computing Time Table VI summarizes the running time of the main opera- tions performed in the tracking and mapping threads, showing that our system is able to run in real time at 30-40 frames and at 3-6 keyframes per second.
- [p. 15] 15 Table VI: Running time of the main parts of our tracking and mapping threads compared to ORB-SLAM2, on EuRoC V202 (mean time and standard deviation in ms).
- [p. 15] System ORB-SLAM2 ORB-SLAM3 ORB-SLAM3 ORB-SLAM3 ORB-SLAM3 Sensor Stereo Monocular Stereo Mono-Inertial Stereo-Inertial Resolution 752×480 752×480 752×480 752×480 752×480 Settings Cam.
- [p. 16] 16 inside the human body.
- [p. 16] Murray, “Parallel tracking and mapping for small AR About the four different sensor configurations, there is no workspaces,” in IEEE and ACM International Symposium on Mixed and Augmented Reality (ISMAR), Nara, Japan, 2007, pp.
- [p. 17] Siegwart, “Iterated [68] L.
- [p. 17] Montiel, “C2TAM: A cloud frame- extended Kalman filter based visual-inertial odometry using direct work for cooperative tracking and mapping,” Robotics and Autonomous photometric feedback,” The International Journal of Robotics Research, Systems, vol.
- [p. 18] 18 Richard Elvira received a Bachelor’s Degree in Informatics Engineering (mention in Computing) and Master’s in Biomedical Engineering (mention in Information and Communication Technologies in Biomedical Engineering) from Universidad de Zaragoza, where he is currently PhD.
- [p. 18] student in the I3A Robotics, Perception and Real-Time Group.

## Extracted Tables

### Table 1 (p. 7)

bust Huber kernel ρHub to reduce the influence of spurious                                p(Yk |I0:k ) ∝ p(I0:k |Yk )p(Yk )            (6)

### Table 2 (p. 11)

  error is computed using s from Sim(3) alignment, as |1 − s|.        stereo configurations. The stereo-inertial system has a very


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
