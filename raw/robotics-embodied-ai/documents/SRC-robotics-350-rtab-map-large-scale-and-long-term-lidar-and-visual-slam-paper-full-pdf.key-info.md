---
source_id: "SRC-robotics-350"
title: "RTAB-Map large-scale and long-term lidar and visual SLAM paper full PDF"
source_type: "research_paper"
publisher: "Mathieu Labbe and Francois Michaud / Journal of Field Robotics"
source_date: "2019"
url: "https://arxiv.org/pdf/2403.06341.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-05T06:50:30+00:00"
source_markdown: "SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-robotics-350
---
# RTAB-Map large-scale and long-term lidar and visual SLAM paper full PDF - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-350`
- Raw Markdown: [SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md](SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md)
- Evidence grade: `S`

## Page-Level Leads

- [p. 1] This is a preprint version of an article accepted in Journal of Field Robotics.
- [p. 1] The final authenticated version will be available online at: https://doi.org/10.1002/rob.21831 RTAB-Map as an Open-Source Lidar and Visual SLAM Library for Large-Scale and Long-Term Online Operation arXiv:2403.06341v1 [cs.RO] 10 Mar 2024 Mathieu Labbé Interdisciplinary Institute of Technological Innovation (3IT) Department of Electrical Engineerin
- [p. 2] limiting the size of the map so that loop closure detections are always processed under a fixed time limit, thus satisfying online requirements for long-term and large-scale environment mapping.
- [p. 2] Initiated in 2009 and released as an open source library in 2013, RTAB-Map has since be extended to a complete graph- based SLAM approach [Stachniss et al., 2016] to be used in various setups and applications [Laniel et al., 2017, Foresti et al., 2016, Chen et al., 2015, Goebel, 2014].
- [p. 3] Operating System (ROS) [Quigley et al., 2009], introduced in 2008, contributes greatly to standardize sensor data format, thus improving interoperability between robot platforms and making it possible to compare SLAM approaches.
- [p. 3] But still, visual SLAM approaches integrated in ROS are not often tested on autonomous robots: only SLAM by teleoperation or by a human moving the sensor [Mur-Artal and Tardós, 2017, Engel et al., 2015, Dai et al., 2017].
- [p. 4] ping in real-world autonomous navigation scenarios, like those in RoboCup Rescue Robot League competition [Kohlbrecher et al., 2016].
- [p. 4] It can also use external sensors like an IMU to estimate the robot position in 3D.
- [p. 5] obstacle avoidance and path planning.
- [p. 5] To keep processing time bounded for large-scale environments, VINS-Mono limits the size of the graph, removing nodes without loop closures first, then removing others depending on the density of the graph.
- [p. 6] Table 1: Popular ROS-compatible lidar and visual SLAM approaches with their supported inputs and online outputs.
- [p. 6] Inputs Online Outputs Camera Lidar Odom Pose Occupancy Point Stereo RGB-D Multi IMU 2D 3D 2D 3D Cloud GMapping ✓ ✓ ✓ ✓ TinySLAM ✓ ✓ ✓ ✓ Hector SLAM ✓ ✓ ✓ ETHZASL-ICP ✓ ✓ ✓ ✓ ✓ Dense Karto SLAM ✓ ✓ ✓ ✓ Lago SLAM ✓ ✓ ✓ ✓ Cartographer ✓ ✓ ✓ ✓ ✓ Dense BLAM ✓ ✓ Dense SegMatch ✓ Dense VINS-Mono ✓ ✓ ORB-SLAM2 ✓ ✓ S-PTAM ✓ ✓ Sparse DVO-SLAM ✓ ✓ RGBiD-SLAM 
- [p. 7] RGB-D Image(s) rtabmap_ros/rtabmap Transferred LTM Retrieved Stereo Image Nodes Nodes WM Map Data TF New Node Loop Closure and STM Map Graph Proximity Detection New Link(s) Odometry Node Odometry TF Sensor Data Graph Optimization /map -> /odom Optional Graph OctoMap Laser Scan Synchronization Point Cloud Global Map Point Cloud Assembling 2D Occupan
- [p. 7] 1: The required inputs are: TF to define the position of the sensors in relation to the base of the robot; Odometry from any source (which can be 3DoF or 6DoF); one of the camera inputs (one or multiple RGB-D images, or a stereo image) with corresponding calibration messages.
- [p. 8] using past locations [Labbé and Michaud, 2017].
- [p. 8] The next sections explain in more details RTAB-Map’s pipeline, starting from Odometry Node to Global Map Assembling.
- [p. 9] RGB-D Image Stereo Image Feature Detection Stereo Correspondence (GFTT/BRIEF) (Optical Flow) Features TF Feature Matching Motion (NNDR) (Optical Flow) Prediction Legend: Features (with Frame-To-Frame (F2F) correspondences) Frame-To-Map (F2M) Motion Estimation (PnP RANSAC ) Velocity Key Frame Features, Feature Map Features Transform Features, Update
- [p. 9] 2: Block diagram of rgbd odometry and stereo odometry ROS nodes.
- [p. 10] all features in Feature Map, then another transformation is computed.
- [p. 10] For F2F, to be more robust to invalid correspondences, feature matching with NNDR is done instead of optical flow, and thus BRIEF descriptors have to be extracted.
- [p. 11] Laser Scan Point Cloud Point Cloud Filtering Point cloud TF ICP Registration Motion (libpointmatcher, P2P or P2N) Prediction Legend: Point cloud, Scan-To-Scan (S2S) Transform Velocity /odom -> /base_link Scan-To-Map (S2M) Ignoring or using external /odom -> /base_link odometry as motion prediction Pose /odom_icp -> /odom TF Update Pose Key Frame Od
- [p. 11] end point cloud Yes Subtract Filtered and Filtering Transformed transformed point cloud point cloud Fig.
- [p. 12] remaining points are added to the Point Cloud Map.
- [p. 12] When the Point Cloud Map has reached the fixed maximum threshold “OdomF2M/ScanMaxSize”, oldest points are removed.
- [p. 13] /map TF rtabmap_ros/ rtabmap /odom/map TF RGB Image rtabmap_ros/ RGB Camera Info rtabmap Registered Depth Image Odometry /base_link /odom RGB Image RGB Camera Info rtabmap_ros/ Registered Depth Image Odometry /base_link /camera_link rgbd_odometry rtabmap_ros/ /camera_link /camera_rgb_op@cal_frame rgbd_odometry /camera_rgb_op@cal_frame Fig.
- [p. 13] 4: Visual SLAM with a RGB-D camera like the Kinect for Xbox 360.
- [p. 14] 2D Ray yes Tracing Laser 2D Local scan end Occupancy Grid topic?
- [p. 14] no true no Point Grid/RayTracing false false cloud topic?
- [p. 15] from the point cloud: the normals of the point cloud are computed, then all points with their normal parallel to z-axis (upward) within the fixed maximum angle “Grid/MaxGroundAngle” are libelled as ground, others are obstacles.
- [p. 15] • Projection: If “Grid/3D” is false, the 3D ground and obstacle point clouds are projected on ground plane (e.g., x-y plane).
- [p. 16] 2D Occupancy Grid Projec@on /grid_map Projec@on 2D Occupancy Grid /octomap_grid 2D Local OctoMap 3D Occupancy Grid /octomap Occupancy Grid 2D/3D Point Cloud /cloud_map 2D/3D Point Cloud 3D Local Voxel Filter (Obstacles) + /cloud_obstacles Occupancy Grid 2D/3D Point Cloud Voxel Filter (Ground) /cloud_ground Fig.
- [p. 16] 8: Global map assembling.
- [p. 17] Table 2: RTAB-Map (version 0.16.3) Default Parameters GFTT/MinDistance 3 pixels RGBD/OptimizeMaxError 1 GFTT/QualityLevel 0.001 RGBD/ProximityMaxGraphDepth 50 nodes Kp/MaxFeatures 500 features Rtabmap/DetectionRate 2 Hz Odom/KeyFrameThr (F2M) 0.3 Rtabmap/TimeThr 0 ms Odom/KeyFrameThr (F2F) 0.6 Rtabmap/MemoryThr 0 nodes Odom/ScanKeyFrameThr 0.9 Rtab
- [p. 17] These datasets have a variety of sensors (i.e., stereo and RGB-D cameras, 2D and 3D lidars, combined wheel and IMU odometry).
- [p. 18] 00-F2M 01-F2M 08-F2M 00-F2M 01-F2M 08-F2M 00-F2M 01-F2M 500 500 500 08-F2M z (m) 0 500 400 0 400 400 400 300 -200 0 -200 -200 400 400 200 300 -400 300 300 300 300 -400 z (m) z (m) z (m) -400 200 z (m) z (m) z (m) 200 z (m) 200 200 00-F2M 00-F2M -600 z (m) -600 -600 F2M -800 01-F2M 01-F2M 200 100 z (m) 200 400 100 08-F2M 08-F2M 00-F2M 01-F2M 08-F2M 
- [p. 18] Errors -100 -100 0 between poses estimated by RTAB-Map -200 -100 0-200 0 (blue) -100 100 0 and 200 100the200 300 ground 300 truths 0 (black) 0 500 are 500 1000 shown 1000 1500 red.
- [p. 19] Table 3: ATE (m) results for the KITTI sequences in relation to the odometry approach and the sensor used using a single CPU core RTAB-Map KITTI Sequence oavg Sensor Odometry 00 01 02 03 04 05 06 07 08 09 10 (msec) S2S 1.0 24.0 3.1 0.7 0.4 0.6 0.5 0.3 4.2 1.1 1.8 62 Lidar S2M 1.1 17.2 2.9 0.7 0.5 0.7 0.5 0.3 7.7 1.1 1.7 82 LOAM-RTAB 1.8 23.3 47 1.1
- [p. 19] Table 3 summarizes trajectory accuracy in terms of ATE for all odometry configurations available in RTAB-Map, along with performance reported for ORB-SLAM2 [Mur-Artal and Tardós, 2017], LSD-SLAM [Engel et al., 2015] and SOFT-SLAM [Cvišić et al., 2018].
- [p. 20] Table 4: Average translational error (%) results for the KITTI sequences in relation to the odometry approach and the sensor used RTAB-Map KITTI Sequence Sensor Odometry 00 01 02 03 04 05 06 07 08 09 10 S2S 0.82 3.17 1.26 1.02 1.21 0.51 0.58 0.58 1.11 0.90 1.64 Lidar S2M 0.86 2.52 1.14 1.03 1.18 0.56 0.58 0.65 1.25 0.90 1.52 LOAM-RTAB 1.2 2.9 4.4 1
- [p. 20] 10: Trajectories using RTAB-Map with RGB-D odometry F2M (blue) against ground truths (black) for three TUM sequences.
- [p. 21] Table 6: ATE (cm) results for the TUM sequences in relation to the odometry approach RTAB-Map TUM fr1 TUM fr2 TUM fr3 oavg Odometry desk desk2 room desk xyz office nst (msec) F2F 7.2 10.1 8.8 2.2 0.5 2.6 7.4 37 F2M 2.9 4.4 6.6 2.4 0.5 2.1 1.7 70 DVO 5.9 6.7 10.7 6.0 0.8 10.8 3.5 37 Fovis 4.8 8.8 11.9 4.7 0.7 5.1 10.6 21 ORB2-RTAB 1.9 4.3 10.3 1.2 0
- [p. 21] In the fr1 sequence, the camera is moving and rotating faster than in other sequences, resulting in an estimated trajectory diverging more from the ground truth.
- [p. 22] V1-02-medium-F2M V1-02-medium-F2M V1-02-medium-F2M V2-03-difficult-F2M V2-03-difficult-F2M V2-03-difficult-F2M MH-04-difficult-F2M MH-04-difficult-F2M MH-04-difficult-F2M 3 3 3 3 3 3 10 10 10 2 2 2 2 2 2 5 5 5 1 1 1 1 1 1 y (m) y (m) y (m) y (m) y (m) y (m) y (m) y (m) y (m) 0 0 0 V1-02-medium-F2M V1-02-medium-F2M V1-02-medium-F2M 0 0 0 V2-03-diffi
- [p. 22] 11: Trajectories using RTAB-Map with stereo odometry F2M (top) and visual-inertial odometry -1 -1 -1 OKVIS (bottom) against ground-1 truths-1 for three -1 EuRoC sequences.
- [p. 23] for the MH sequences.
- [p. 23] LSD-SLAM has only been tested on V1 sequence, and results are slightly better than F2M on two out of three sequences.
- [p. 24] 2012-01-25-12-14-25-F2M 2012-01-25-12-33-29-F2M 2012-01-25-12-14-25-F2M 2012-01-25-12-33-29-F2M 20 2012-01-25-12-14-25-F2M 20 2012-01-25-12-33-29-F2M 2012-01-25-12-14-25-F2M 2012-01-25-12-33-29-F2M 20 20 30 30 10 30 30 10 20 10 10 20 y (m) y (m) y (m) y (m) y (m) y (m) 20 20 0 0 y (m) 10 y (m) 10 0 0 10 10 -10 0 -10 0 -10 -10 0 0 -20 -10 0 10 20 30
- [p. 24] 12: Trajectories using RTAB-Map (blue) against ground truths (black) for the 2012-01-25-12-14-25 (left) and 2012-01-25-12-33-29 (right) Stata Center sequences using stereo camera (top) or long-range lidar (bottom).
- [p. 25] Table 8: Online results for the MIT Stata Center 2012-01-25-xx-xx-xx sequences in relation to the sensor used and the odometry approach 12-14-25 12-33-29 ATEend ATEmax ATEend ATEmax oavg Sensor Odometry (m) (m) (m) (m) (msec) WheelIMU→S2S 0.06 0.08 0.08 0.09 15 WheelIMU→S2M 0.05 0.05 0.08 0.09 25 Long-Range S2S 0.05 0.08 0.07 0.10 15 Lidar S2M 0.05
- [p. 25] In term of computation time, lidar odometry approaches are faster than visual odometry ones (lowest oavg ), with S2S approaches faster for all lidar experiments.
- [p. 26] 2012-01-25-12-14-25Short-Range Lidar 2012-01-25-12-33-29Short-Range Lidar 1e+2 1e+1 1e+1 1e+0 1e+0 1e-1 ATE (m) ATE (m) 1e-1 1e-2 1e-2 Cartographer Cartographer HectorSLAM 1e-3 HectorSLAM 1e-3 GMapping GMapping Karto Karto RTAB-Map RTAB-Map Odometry Odometry 1e-4 1e-4 0 200 400 600 800 1000 1200 0 200 400 600 800 Time (s) Time (s) (a) 2012-01-25-12
- [p. 26] 13: Comparison of RTAB-Map’s WheelIMU→S2M with other lidar-based SLAM approaches approaches.
- [p. 27] Table 9: ATE (m) results of RTAB-Map’s WheelIMU→S2M and popular lidar-based SLAM approaches on 2012-01-25 sequences.
- [p. 27] 12-14-25 12-33-29 Sensor Odometry SLAM ATEend ATEmax ATEend ATEmax WheelIMU→S2M RTAB-Map 0.05 0.05 0.08 0.09 WheelIMU Cartographer 0.11 0.11 0.10 0.12 Long-Range WheelIMU GMapping 0.19 0.19 0.10 0.16 Lidar WheelIMU Karto SLAM 0.22 0.29 0.15 0.17 - Hector SLAM 0.06 0.07 0.09 0.09 WheelIMU→S2M RTAB-Map 0.07 0.08 0.09 0.10 WheelIMU Cartographer 0.45 0
- [p. 28] Table 10: Occupancy grid performance using MIT Stata Center 2012-01-25-12-14-25 sequence after 860 nodes added to the graph (or 350 meters in 19 minutes) Global Occupancy Grid Local Occupancy Grid Type Time Type Sensor Time Update+Pub With Loop (msec) (msec) (msec) GFD0 →2D Long-Range Lidar 4 2D 2+0 +600 GFD0 →2D Short-Range Lidar 1 2D 1+0 +200 GFD
- [p. 28] Figure 14 presents examples of generation of local 2D occupancy grids depending on the sensor and approach used.
- [p. 29] (a) Lidar (b) Lidar (top view) (c) RGB-D camera view (d) RGB-D segmenta- (e) RGB-D projection (f) RGB-D projection (g) RGB-D top tion with 2D ray tracing view (h) Stereo camera view (i) Stereo segmenta- (j) Stereo projection (k) Stereo projection (l) Stereo top view tion with 2D ray tracing Fig.
- [p. 29] 14: Local occupancy grid examples.
- [p. 30] (a) Short-range lidar (b) RGB-D projection with- (c) RGB-D projection with (d) RGB-D OctoMap pro- out ray tracing 2D ray tracing jection with 3D ray tracing (e) Long-range lidar (f) Stereo projection with- (g) Stereo projection with (h) Stereo OctoMap projec- out ray tracing 2D ray tracing tion with 3D ray tracing Fig.
- [p. 30] 16: 2D occupancy grid map examples.
- [p. 31] 17: OctoMap of depth a) 16 and b) 14 using the RGB-D camera.
- [p. 31] 5.1 Examining the Use of RTAB-Map’s Memory Management Mechanism For large-scale and long-term SLAM where the graph is constantly adding new nodes, these previous solutions to adjust computation load based on occupancy grid type may not be sufficient.
- [p. 32] 800 800 Synchronization + STM Synchronization + STM Proximity Detection Proximity Detection Loop Closure Detection Loop Closure Detection Graph Optimization Graph Optimization Global Map Assembling Global Map Assembling Real-Time Constraint (2 Hz) Memory Management (WM <--> LTM) 600 600 Real-Time Constraint (2 Hz) Processing Time (ms) Processing Ti
- [p. 32] 18: Processing time required for each module inside rtabmap ROS node without (a) and with (b) memory management, for a map update rate of 2 Hz using the combined sessions of the MIT Stata Center sequences.
- [p. 33] t=1170 sec Start/End t=225 sec Session 2 t=460 sec t=1400 sec Session 1 t=930 sec (a) (b) (c) Fig.
- [p. 33] 19: Global maps created with (a,b) and without (c) memory management using the combined sessions of the MIT Stata Center sequences.
- [p. 34] Consequently, RTAB-Map can be used to conduct trials with different sensors and identify early on if a sensor is suitable for the targeted application.
- [p. 34] Based on the results presented in this paper, guidelines can be derived regarding when using SLAM (without external global localization) in an indoor environment.
- [p. 35] ATEmax metric presented in this paper is important for navigation: the lower the odometry drifts, the faster the localization recovery happens after the robot changes course for some reasons and has to come back to follow the original planned path.
- [p. 35] In these application examples using short-range sensors, clearing dynamic obstacles (after they moved) would not always be possible using the current ray tracing approach if the sensor rays could not “hit” something behind where the obstacles were in order to clear the space, keeping some fake obstacles on the map that can affect planning afterward
- [p. 36] Burhanpurkar, M., Labbé, M., Guan, C., Michaud, F., and Kelly, J.
- [p. 36] the practical realization of self-driving wheelchair technology.
- [p. 37] Fox, D., Burgard, W., Dellaert, F., and Thrun, S.
- [p. 37] Monte Carlo localization: Efficient position esti- mation for mobile robots.
- [p. 38] Small vision systems: Hardware and implementation.
- [p. 38] In Robotics Research, pages 203–212.
- [p. 39] Rublee, E., Rabaud, V., Konolige, K., and Bradski, G.
- [p. 39] ORB: An efficient alternative to SIFT or SURF.
- [p. 40] Low-drift and real-time lidar odometry and mapping.
- [p. 40] Autonomous Robots, 41(2):401–416.

## Extracted Tables

- needs-verification: no Markdown-style tables detected.

## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
