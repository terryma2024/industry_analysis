---
source_id: "SRC-robotics-341"
title: "ORB-SLAM3 v1.0 calibration tutorial"
source_type: "product_documentation"
publisher: "UZ-SLAMLab / University of Zaragoza"
source_date: "2021-12-22"
url: "https://raw.githubusercontent.com/UZ-SLAMLab/ORB_SLAM3/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/Calibration_Tutorial.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-05T06:10:43+00:00"
source_markdown: "SRC-robotics-341-orb-slam3-v1-0-calibration-tutorial.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-341
---
# ORB-SLAM3 v1.0 calibration tutorial - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-341`
- Raw Markdown: [SRC-robotics-341-orb-slam3-v1-0-calibration-tutorial.md](SRC-robotics-341-orb-slam3-v1-0-calibration-tutorial.md)
- Evidence grade: `S`

## Page-Level Leads

- [p. 1] Calibration Tutorial for ORB-SLAM3 v1.0 Juan J.
- [p. 1] Gómez Rodríguez, Carlos Campos, Juan D.
- [p. 2] Figure 1: Reference systems defined for ORB-SLAM3 stereo-inertial.
- [p. 2] Cameras and body poses relate as: TWC1 = TWB TBC1 (1) TWC2 = TWB TBC1 TC1 C2 (2) where, for example, TWC1 ∈ SE(3) is the homogeneous transformation that passes points expressed in camera one reference to the world reference: xW = TWC1 xC1 (3) The extrinsic parameters that the calibration file needs to provide are: • Stereo-inertial: TBC1 and TC1 C2
- [p. 3] 3.1 Camera intrinsic parameters Depending on camera set-up we will need to provide different calibration parameters.
- [p. 3] Those can be calibrated using OpenCV or Kalibr [3].
- [p. 4] When integrating the IMU measurements and estimating their covariances, the used noise densities σa,f will depend on the IMU sampling frequency f , which must be provided in the calibration √ file.
- [p. 4] This is internally managed by ORB-SLAM3, which computes σa,f = σa / f Regarding biases, they are assumed to evolve according to a Brownian motion.
- [p. 5] 1 python3 ./ Examples / Calibration / python_scripts / process_imu .
- [p. 5] py ./ Examples / Calibration / recorder / Listing 4: Run visual-inertial recorder • Nest, you will need to convert this dataset to a rosbag with rosbag creater from Kalibr.
- [p. 6] Table 1: Comparative factory/Kalibr calibration for Realsense D435i.
- [p. 6] Factory Kalibr fx 382.613 381.69830045 ± 0.47867208 fy 382.613 381.6587096 ± 0.48696699 cx 320.183 321.58237544 ± 0.40096812 cy 236.455 236.20193592 ± 0.38600065 k1 0 -0.00469988 ± 0.00171615 k2 0 0.00110469 ± 0.00196003 r1 0 -0.00029279 ± 0.00028587 r2 0 0.00066225 ± 0.00034486 fixed during this calibration.
- [p. 7] 5 Reference for the new calibration files This section summarizes all parameters that are required by ORB-SLAM3 in any of its stages, including intrinsic and extrinsic calibration parameters, ORB extraction param- eters and visualization settings.
- [p. 7] All this configuration parameters must be passed to ORB-SLAM3 in a yaml file.
- [p. 8] • Camera1.p1, Camera1.p2 (float) [REQUIRED]: corresponds to the tangential distortion coefficients.
- [p. 8] • Camera1.k3 (float) [OPTIONAL]: sometimes a third radial distortion parameter is used.
- [p. 9] • IMU.AccWalk (float) [REQUIRED]: Random walk variance of the accelerometer.
- [p. 9] • IMU.Frequency (float) [REQUIRED]: IMU frequency.
- [p. 10] 5.8 Viewer parameters These are some parameters related to the ORB-SLAM3 user interface: • Viewer.KeyFrameSize (float) [REQUIRED]: size in which the KeyFrames are drawn in the map viewer.
- [p. 10] • Viewer.KeyFrameLineWidth (float) [REQUIRED]: line width of the KeyFrame drawing.

## Extracted Tables

### Table 1 (p. 5)

          those whose mean is close to zero pixels (|µ| < 10−4 ) and its standard deviation


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
