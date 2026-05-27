---
source_id: "SRC-robotics-101"
title: "UMI-3D hardware repository"
source_type: "open_source_repository"
publisher: "Physical Intelligence Laboratory"
source_date: "2026"
url: "https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/open-source-repository
  - evidence/s
aliases:
  - SRC-robotics-101
---
# UMI-3D hardware repository

## UMI-3D Hardware Building Guide

| [**🔧 UMI-3D Hardware**](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware) | [**🛰️ UMI-3D SLAM Pipeline**](https://github.com/hku-mars/UMI-3D) | [**🤖 UMI-3D Policy**](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Policy) |
| --- | --- | --- |
| [![UMI-3D Hardware](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/nav_hardware.jpg)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware) | [![UMI-3D SLAM Pipeline](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/nav_processing.jpg)](https://github.com/hku-mars/UMI-3D) | [![UMI-3D Policy](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/nav_policy.jpg)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Policy) |
| Hardware design, BOM, CAD, 3D-print parts | SLAM, synchronization, calibration, and data processing | Policy training, deployment, inference      [**📦 Dataset & Models**](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Dataset) |

---

## 1\. Bill of Materials (BOM)

> **Target total cost:** ≈ ¥5,000 (≈ $700, subject to actual purchase)

### UMI-3D Handheld Gripper

[![UMI-3D Handheld Gripper](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/umi-3d-gripper.jpg)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/umi-3d-gripper.jpg) [![UMI-3D CAD Overview](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/umi3d_cad_overview.jpg)](https://cad.onshape.com/documents/c9e31f296203311b15bbef9f/w/4cbb703a6e56db74890e5c7c/e/bc366516274ebba7413ed208)

<sub>Left: real UMI-3D handheld gripper. Right: CAD overview (<a href="https://cad.onshape.com/documents/c9e31f296203311b15bbef9f/w/4cbb703a6e56db74890e5c7c/e/bc366516274ebba7413ed208">view in Onshape</a>).</sub>

#### Mechanical Components

<table><tbody><tr><th>Component</th><th>Description</th><th>STL Files</th><th>Price</th><th>Preview</th><th>Assembled View</th></tr><tr><td>Gripper Mount</td><td>3D Print, PLA<br>Infill: 20% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/3d_print_mount.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/3d_print_mount.png" width="100"></a></td><td rowspan="3" align="center"><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/gripper_assembled.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/gripper_assembled.png" width="220"></a></td></tr><tr><td>Soft Finger</td><td>3D Print, TPU 95A<br>Infill: 100% Lines</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/soft_finger_TPU_95A">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/finger.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/finger.png" width="80"></a></td></tr><tr><td>150mm MG9NC Linear Module</td><td>Aluminum,<br>CNC Bracket</td><td>—</td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/rail_spring.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/rail_spring.png" width="100"></a></td></tr></tbody></table>

#### Sensors

| Component | Model / Name | Price | Image |
| --- | --- | --- | --- |
| LiDAR | [Livox MID-360/MID-360S](https://www.livoxtech.com/cn/mid-360) | ¥3999/¥3599 ($560/$510) | [![](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/lidar.png)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/lidar.png) |
| Camera | [Hikrobot MV-CB013-A0UC-S](https://www.hikrobotics.com/cn/machinevision/productdetail/?id=9707) | ¥700 (≈ $100) | [![](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/camera.png)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/camera.png) |
| Lens | [ZLKC MTV185IR12MP](https://zlkc.com.cn/pro.php?id=868) | ¥139 (≈ $20) | [![](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/lens.png)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/lens.png) |

#### Electrical & Wiring

| Component | Model / Name | Price | Image |
| --- | --- | --- | --- |
| Synchronizer | [LiDAR–Camera   Hardware Synchronizer](https://item.taobao.com/item.htm?id=1043626844436&mi_id=0000CL74-49ru_M-i5NleNFb314JOKmTP30UfDURPJsCu98&spm=a21xtw.29178619.0.0&xxc=shop&skuId=6228552263781) | ¥288 (≈ $40) | [![](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/sync.png)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/sync.png) |
| Battery | [12V DC Battery](https://detail.tmall.com/item.htm?id=657166348854&skuId=5850365218489) | ¥79 (≈ $10) | [![](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/battery.png)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/battery.png) |

---

### UMI-3D Ego (Under Development):

#### Mechanical Components

<table><tbody><tr><th>Component</th><th>Description</th><th>STL Files</th><th>Price</th><th>Preview</th><th>Assembled View</th></tr><tr><td>Sensor Mount</td><td>3D Print, PLA<br>Infill: 20% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/ego">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/head_sensor_mount.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/head_sensor_mount.png" width="80"></a></td><td rowspan="2" align="center"><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/umi-3d-ego1.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/umi-3d-ego1.png" width="220"></a></td></tr><tr><td>Headband</td><td><a href="https://detail.tmall.com/item.htm?app=chrome&bxsign=scdg6YIK_-5XbyWEs_Me-WbVexnwHfyQ0IpLEK2GPXfpgCMUOBT6PDQ-JP-7M6prttytDlVMfpxYcAW1cWagph1dxLIQ1LjtlEYbHGjqJSAOBvMFRuwqmFhTdKfcxtHFtZR&cpp=1&id=722552252155&price=35.9&share_crt_v=1&shareurl=true&short_name=h.ihgFXjkIycZevzM&sourceType=item&sp_tk=c0pDWFVBTkdCSjM%3D&spm=a2159r.13376460.0.0&suid=A31E4AAC-20F0-408C-A997-30F2429C0CC7&tbSocialPopKey=shareItem&tk=sJCXUANGBJ3%20MF168&un=ef262fcb26524492b4d2888dab66570f&un_site=0&ut_sk=1.Y8UeMsdau94DAJZRqhhTa%2Bkr_21380790_1774113745450.Copy.ShareGlobalNavigation_1&skuId=5199322371215">TELESIN GoPro Headband</a></td><td>—</td><td>¥35.9 (≈ $5)</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/headband.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/headband.png" width="100"></a></td></tr></tbody></table>

#### Sensors (Same as Above)

#### Electrical & Wiring (Same as Above)

---

### UMI-3D Robot Arms (Manipulator-Side Mounts)

#### ARX L5/R5/X5

<table><tbody><tr><th>Component</th><th>Description</th><th>STL Files</th><th>Price</th><th>Preview</th><th>Assembled View</th></tr><tr><td>Finger Mount</td><td>3D Print, PLA<br>Infill: 40% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/arx">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/arx_finger_mount.jpg"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/arx_finger_mount.jpg" width="100"></a></td><td rowspan="2" align="center"><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/arx_assembled.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/arx_assembled.png" width="220"></a><br><sub><b>ARX-mounted UMI-3D setup</b></sub></td></tr><tr><td>Camera Mount</td><td>3D Print, PLA<br>Infill: 40% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/arx">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/arx_camera_mount.jpg"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/arx_camera_mount.jpg" width="100"></a></td></tr></tbody></table>

#### Agilex Piper (Under Development)

<table><tbody><tr><th>Component</th><th>Description</th><th>STL Files</th><th>Price</th><th>Preview</th><th>Assembled View</th></tr><tr><td>Finger Mount</td><td>3D Print, PLA<br>Infill: 40% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/piper">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/piper_finger_mount.jpg"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/piper_finger_mount.jpg" width="100"></a></td><td rowspan="2" align="center"><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/piper_assembled.png"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/piper_assembled.png" width="220"></a></td></tr><tr><td>Camera Mount</td><td>3D Print, PLA<br>Infill: 40% Gyroid</td><td>📁 <a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/3d_print_STL/piper">Link</a></td><td>—</td><td><a href="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/piper_camera_mount.jpg"><img src="https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/piper_camera_mount.jpg" width="100"></a></td></tr></tbody></table>

---

## 2\. Electrical & Wiring

[![UMI-3D wiring diagram](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/raw/main/docs/assets/UMI-3D-wiring.jpg)](https://github.com/Physical-Intelligence-Laboratory/UMI-3D-Hardware/blob/main/docs/assets/UMI-3D-wiring.jpg)

<sub><b>UMI-3D wiring overview.</b> The 12V battery powers the LiDAR and the hardware synchronizer. The synchronizer provides trigger/sync signals between the LiDAR and camera. LiDAR data and camera images are transmitted to the host computer, recorded in rosbag format, and subsequently used for SLAM, sensor calibration, data processing, and policy training.</sub>

### Connection Overview

| Module | Connects To | Purpose |
| --- | --- | --- |
| 12V Battery | LiDAR | Main power supply for Livox MID-360 |
| 12V Battery | Hardware Synchronizer | Power supply for synchronization board |
| Hardware Synchronizer | Camera | Trigger / sync signal for image capture |
| Hardware Synchronizer | LiDAR | Shared timing reference |
| LiDAR | Host Computer | Point cloud data transmission |
| Camera | Host Computer | Power supply and Image data transmission |

> **Note**
> 
> - Please make sure the battery polarity is correct before powering on.
> - Power on the synchronizer and LiDAR first, then check whether the camera trigger is working properly.
> - Secure all cables to avoid motion-induced looseness during handheld or robot-arm operation.

---

## 3\. UMI-3D ROS Driver

This repository provides the ROS drivers and helper scripts for the UMI-3D sensing setup:

- **Livox MID-360 / MID-360S** LiDAR driver
- **Hikrobot industrial camera** ROS driver
- **MVS launcher** (for camera configuration)
- **Rosbag recording tools**

---

### Repository Structure

```
umi_3d_ros_driver/
├── camera.sh
├── lidar.sh
├── mvs.sh
├── record.sh
└── src/
    ├── livox_ros_driver2/
    └── mvs_ros_driver/
```

---

### Environment

- Ubuntu 20.04
- ROS Noetic
- System Python (**required**)

> **Note**
> 
> - Always run `conda deactivate` before building or launching ROS drivers. Using Conda may cause ROS dependency conflicts.

---

### Dependencies

- **MVS (camera SDK)**  
	[https://github.com/bitcat-tech/MVS\_V3.0.1](https://github.com/bitcat-tech/MVS_V3.0.1)
- **Livox-SDK2**  
	[https://github.com/Livox-SDK/Livox-SDK2](https://github.com/Livox-SDK/Livox-SDK2)
- ROS Noetic

---

### Quick Start

```
cd ~/umi_3d_ros_driver
conda deactivate

# 1. Build Livox driver
cd src/livox_ros_driver2
./build.sh ROS1
cd ../..

# 2. Build full workspace
catkin_make
source devel/setup.bash

# 3. Configure camera if needed
bash mvs.sh
# → set trigger mode, then CLOSE MVS

# 4. Launch drivers
bash lidar.sh
bash camera.sh

# 5. Record data
bash record.sh
```

> **Note**
> 
> - `livox_ros_driver2` must be built with:` ./build.sh ROS1`

---

### Manual Launch (Optional)

#### LiDAR

```
conda deactivate
source devel/setup.bash
roslaunch livox_ros_driver2 msg_MID360.launch
```

#### Camera

```
conda deactivate
export LD_LIBRARY_PATH=/opt/MVS/lib/64:/opt/MVS/lib/32:/opt/ros/noetic/lib:$LD_LIBRARY_PATH
source devel/setup.bash
roslaunch mvs_ros_driver mvs_camera_trigger.launch
```

#### Record

```
rosbag record /livox/lidar /livox/imu /left_camera/image
```

> **Note**
> 
> - Before launching the camera ROS driver, make sure:
> 	- MVS has been **closed**
> 		- the camera has already been set to **hardware trigger mode**
> 		- `LD_LIBRARY_PATH` includes the MVS runtime libraries

---

### Verification

```
rostopic hz /livox/lidar
rostopic hz /left_camera/image
```

Expected:

- LiDAR publishes normally
- Camera ≈ **20 Hz**

> **Note**
> 
> - Do **not** run MVS and `mvs_ros_driver` at the same time. Use MVS only for camera configuration, then **close it before launching ROS**.
> - If the image publishing rate is lower than **20 Hz**, check the **USB 3.0 port** and **USB 3.0 cable quality**.
> - If build issues occur, re-run:
> 	```
> 	cd src/livox_ros_driver2
> 	./build.sh ROS1
> 	cd ../..
> 	catkin_make
> 	```
> - Data is recorded in **rosbag format** and can be used for:
> 	- SLAM
> 		- Sensor calibration
> 		- Data processing for Policy learning

---

## Citation

If you find this work useful for your research, please consider citing:

```
@misc{wang2026umi3dextendinguniversalmanipulation,
  title={UMI-3D: Extending Universal Manipulation Interface from Vision-Limited to 3D Spatial Perception},
  ={Ziming Wang},
  year={2026},
  eprint={2604.14089},
  archivePrefix={arXiv},
  primaryClass={cs.RO},
  url={https://arxiv.org/abs/2604.14089}
}
```

## Acknowledgements

This work builds upon several outstanding open-source projects, including [UMI (Universal Manipulation Interface)](https://github.com/real-stanford/universal_manipulation_interface), [UMI-on-Legs](https://github.com/real-stanford/umi-on-legs), and [LIV-Eye](https://github.com/hku-mars/LIV_handhold_2). We gratefully acknowledge the authors for their pioneering contributions to embodied intelligence, perception, and robot learning.
