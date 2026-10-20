---
source_id: "SRC-robotics-601"
title: "LinkerHand Python SDK current repository"
source_type: "code_repository"
publisher: "Linkerbot"
source_date: "待验证"
url: "https://github.com/linker-bot/linkerhand-python-sdk"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-20T05:41:11+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-601
---
# LinkerHand Python SDK current repository

[![](https://github.com/linker-bot/linkerhand-python-sdk/raw/main/resource/logo.png)](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/resource/logo.png)

## LinkerHand-Python-SDK

## Overview

LinkerHand Python SDK

[中文](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/README_CN.md) | [English](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/README.md)

## Caution

- Please ensure that the dexterous hand is not running any other control methods, such as linker\_hand\_sdk\_ros, motion capture glove control, or other topics controlling the hand, to avoid conflicts.
- Please secure the dexterous hand to prevent it from falling during movement.
- Please ensure the dexterous hand's power and USB-to-CAN connection are correct.

| Name | Version | Link |
| --- | --- | --- |
| Python SDK | [![SDK Version](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265) [![Python 3.8+](https://camo.githubusercontent.com/4843be661de336244ddc0d39e32d6d48760171010b733a4128e5aff13c3cdbb4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382532422d626c75653f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/4843be661de336244ddc0d39e32d6d48760171010b733a4128e5aff13c3cdbb4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382532422d626c75653f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465) [![Windows 11](https://camo.githubusercontent.com/b8f310563a9ee8f41dae187acbcaf9e59db3c45fb5d65e11194190343a6f8dc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d57696e646f777325323031312d3030373844343f7374796c653d666c61742d737175617265266c6f676f3d77696e646f7773266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/b8f310563a9ee8f41dae187acbcaf9e59db3c45fb5d65e11194190343a6f8dc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d57696e646f777325323031312d3030373844343f7374796c653d666c61742d737175617265266c6f676f3d77696e646f7773266c6f676f436f6c6f723d7768697465) [![Ubuntu 20.04+](https://camo.githubusercontent.com/7ec488571e5c70eb6c3a002f6773ad92a1f410998cb1e5799034d497497e8df4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032302e30342532422d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/7ec488571e5c70eb6c3a002f6773ad92a1f410998cb1e5799034d497497e8df4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032302e30342532422d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465) | [![GitHub 仓库](https://camo.githubusercontent.com/18b8153f4f6f417a76b12040a74c3eef2c2264114f982792e2afe70e286b08a6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d677265793f6c6f676f3d676974687562267374796c653d666c61742d737175617265)](https://github.com/linker-bot/linkerhand-python-sdk) |
| ROS SDK | [![SDK Version](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265) [![Python 3.8+](https://camo.githubusercontent.com/4843be661de336244ddc0d39e32d6d48760171010b733a4128e5aff13c3cdbb4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382532422d626c75653f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/4843be661de336244ddc0d39e32d6d48760171010b733a4128e5aff13c3cdbb4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382532422d626c75653f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465) [![Ubuntu 20.04+](https://camo.githubusercontent.com/7ec488571e5c70eb6c3a002f6773ad92a1f410998cb1e5799034d497497e8df4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032302e30342532422d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/7ec488571e5c70eb6c3a002f6773ad92a1f410998cb1e5799034d497497e8df4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032302e30342532422d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465) [![ROS Noetic](https://camo.githubusercontent.com/209c15c70f068852f0bdbe5e8ed0afb66135c9b18a868e36747a1985e69bc68c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f524f532d4e6f657469632d3030393632343f7374796c653d666c61742d737175617265266c6f676f3d726f73)](https://camo.githubusercontent.com/209c15c70f068852f0bdbe5e8ed0afb66135c9b18a868e36747a1985e69bc68c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f524f532d4e6f657469632d3030393632343f7374796c653d666c61742d737175617265266c6f676f3d726f73) | [![GitHub 仓库](https://camo.githubusercontent.com/18b8153f4f6f417a76b12040a74c3eef2c2264114f982792e2afe70e286b08a6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d677265793f6c6f676f3d676974687562267374796c653d666c61742d737175617265)](https://github.com/linker-bot/linkerhand-ros-sdk) |
| ROS2 SDK | [![SDK Version](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/ef0dfcc987aecdea1780a5ed3688f0a6370c0c27cfba6cd00e87ca4843d092c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53444b25323056657273696f6e2d56332e302e312d627269676874677265656e3f7374796c653d666c61742d737175617265) [![Python 3.11](https://camo.githubusercontent.com/383b9e6f51634bddca302648d93307913a813939582a2d0e1390f54909688643/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31312d3337373641423f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/383b9e6f51634bddca302648d93307913a813939582a2d0e1390f54909688643/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31312d3337373641423f7374796c653d666c61742d737175617265266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465) [![Ubuntu 24.04](https://camo.githubusercontent.com/e9b78af323b7baf90b581872dcd6ff7fc4efef266488bf5770be65943812c028/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032342e30342d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/e9b78af323b7baf90b581872dcd6ff7fc4efef266488bf5770be65943812c028/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d5562756e747525323032342e30342d4539353432303f7374796c653d666c61742d737175617265266c6f676f3d7562756e7475266c6f676f436f6c6f723d7768697465) [![ROS 2 Jazzy](https://camo.githubusercontent.com/508fe176fa57b136ebc57dc8181d730ca18aea53c4415f132e2d5252a27bf3ca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f524f53253230322d4a617a7a792d3030423345363f7374796c653d666c61742d737175617265266c6f676f3d726f73)](https://camo.githubusercontent.com/508fe176fa57b136ebc57dc8181d730ca18aea53c4415f132e2d5252a27bf3ca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f524f53253230322d4a617a7a792d3030423345363f7374796c653d666c61742d737175617265266c6f676f3d726f73) [![Windows 11](https://camo.githubusercontent.com/b8f310563a9ee8f41dae187acbcaf9e59db3c45fb5d65e11194190343a6f8dc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d57696e646f777325323031312d3030373844343f7374796c653d666c61742d737175617265266c6f676f3d77696e646f7773266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/b8f310563a9ee8f41dae187acbcaf9e59db3c45fb5d65e11194190343a6f8dc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d57696e646f777325323031312d3030373844343f7374796c653d666c61742d737175617265266c6f676f3d77696e646f7773266c6f676f436f6c6f723d7768697465) | [![GitHub 仓库](https://camo.githubusercontent.com/18b8153f4f6f417a76b12040a74c3eef2c2264114f982792e2afe70e286b08a6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d677265793f6c6f676f3d676974687562267374796c653d666c61742d737175617265)](https://github.com/linker-bot/linkerhand-ros2-sdk) |

## Installation

  You can run the examples after installing the dependencies in requirements.txt. Only Python 3 is supported.

- download
```
$ git clone https://github.com/linker-bot/linkerhand-python-sdk.git
```
- install
```
$ cd linkerhand-python-sdk/
$ pip3 install -r requirements.txt
```
- 快速使用示例 by CAN Edit the config/setting.yaml configuration file and modify the parameters according to the comments inside. Set CAN:"can0" and Set MODBUS: "None"
```
# Open the CAN port
$ sudo /usr/sbin/ip link set can0 up type can bitrate 1000000 # USB-to-CAN device blue light stays solid. This step can be skipped on Ubuntu systems after modifying setting.ymal as required.
$ cd examples/gui_control
$ sudo chmod a+x gui_control.py
$ python3 gui_control.py
```

[![](https://github.com/linker-bot/linkerhand-python-sdk/raw/main/doc/gui.png)](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/doc/gui.png)

## RS485 Protocol Switching (Currently supports O6/L6/L10. For other models, please refer to the MODBUS RS485 protocol document)

Edit the config/setting.yaml configuration file and modify the parameters according to the comments inside. Set MODBUS: "/dev/ttyUSB0", meaning the "modbus" parameter in the configuration file should be "/dev/ttyUSB0". The USB-RS485 converter usually appears as /dev/ttyUSB\* or /dev/ttyACM\* on Ubuntu. modbus: "None" or "/dev/ttyUSB0"

```
# Ensure requirements.txt dependencies are installed
# Install system-level related drivers
$ pip install minimalmodbus --break-system-packages
$ pip install pyserial --break-system-packages
$ pip install pymodbus --break-system-packages
# View the USB-RS485 port number
$ ls /dev
# You should see a port similar to ttyUSB0. Grant permissions to the port:
$ sudo chmod 777 /dev/ttyUSB0
# GUI control example
$ python3 example/gui_control/gui_control.py
```

## Related Documentation

[Linker Hand API for Python Document](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/doc/API-Reference.md)

## Update Log

- > ### release\_3.0.1
- 1、Supports O6/L6/L10 RS485 communication in pymodbus mode.
- > ### release\_2.2.4
- 1、Added support for G20 industrial version dexterous hand.
- 2、Redrew the GUI.
- > ### release\_2.1.9
- 1、Added support for O6 dexterous hand.
- > ### release\_2.1.8
- 1、Fixed occasional frame collision issue.
- Position and Finger Joint Correspondence Table
	O6: \["Thumb Flexion", "Thumb Adduction/Abduction","Index Finger Flexion", "Middle Finger Flexion", "Ring Finger Flexion","Pinky Finger Flexion"\]
	L6: \["Thumb Flexion", "Thumb Adduction/Abduction","Index Finger Flexion", "Middle Finger Flexion", "Ring Finger Flexion","Pinky Finger Flexion"\]
	L7: \["Thumb Flexion", "Thumb Adduction/Abduction","Index Finger Flexion", "Middle Finger Flexion", "Ring Finger Flexion","Pinky Finger Flexion","Thumb Rotation"\]
	L10: \["Thumb CMC Pitch", "Thumb Adduction/Abduction","Index Finger MCP Pitch", "Middle Finger MCP Pitch", "Ring Finger MCP Pitch","Pinky Finger MCP Pitch","Index Finger Adduction/Abduction","Ring Finger Adduction/Abduction","Pinky Finger Adduction/Abduction","Thumb Rotation"\]
	L20: \["Thumb CMC Pitch", "Index Finger MCP Pitch", "Middle Finger MCP Pitch", "Ring Finger MCP Pitch","Pinky Finger MCP Pitch","Thumb Adduction/Abduction","Index Finger Adduction/Abduction","Middle Finger Adduction/Abduction","Ring Finger Adduction/Abduction","Pinky Finger Adduction/Abduction","Thumb CMC Yaw","Reserved","Reserved","Reserved","Reserved","Thumb Distal Tip","Index Finger Distal Tip","Middle Finger Distal Tip","Ring Finger Distal Tip","Pinky Finger Distal Tip"\]
	G20(工业版): \["Thumb CMC Pitch", "Index Finger MCP Pitch", "Middle Finger MCP Pitch", "Ring Finger MCP Pitch","Pinky Finger MCP Pitch","Thumb Adduction/Abduction","Index Finger Adduction/Abduction","Middle Finger Adduction/Abduction","Ring Finger Adduction/Abduction","Pinky Finger Adduction/Abduction","Thumb CMC Yaw","Reserved","Reserved","Reserved","Reserved","Thumb Distal Tip","Index Finger Distal Tip","Middle Finger Distal Tip","Ring Finger Distal Tip","Pinky Finger Distal Tip"\]
	L21: \["Thumb Base Pitch","Index Base Pitch","Middle Base Pitch","Ring Base Pitch","Pinky Base Pitch","Thumb Adduction/Abduction","Index Adduction/Abduction","Middle Adduction/Abduction","Ring Adduction/Abduction","Pinky Adduction/Abduction","Thumb Roll","Reserved","Reserved","Reserved","Reserved","Thumb Middle","Reserved","Reserved","Reserved","Reserved","Thumb Tip","Index Tip","Middle Tip","Ring Tip","Pinky Tip"\]
	L25: \["Thumb Base Pitch", "Index Base Pitch", "Middle Base Pitch","Ring Base Pitch","Pinky Base Pitch","Thumb Adduction/Abduction","Index Adduction/Abduction","Middle Adduction/Abduction","Ring Adduction/Abduction","Pinky Adduction/Abduction","Thumb Roll","Reserved","Reserved","Reserved","Reserved","Thumb Middle","Index Middle","Middle Middle","Ring Middle","Pinky Middle","Thumb Tip","Index Tip","Middle Tip","Ring Tip","Pinky Tip"\]

## L10\_Example

   **Before running, please modify the configuration information in [setting.yaml](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/LinkerHand/config/setting.yaml) to match your actual dexterous hand configuration.**

- #### 0000-gui\_control

When launched, a UI interface will pop up. You can control the corresponding LinkerHand dexterous hand joint movements using the sliders.

- Adding or modifying action examples. You can add or modify actions in the [constants.py](https://github.com/linker-bot/linkerhand-python-sdk/blob/main/example/gui_control/config/constants.py) file.
```
# For example, adding action sequences for L6
"L6": HandConfig(
        joint_names_en=["thumb_cmc_pitch", "thumb_cmc_yaw", "index_mcp_pitch", "middle_mcp_pitch", "pinky_mcp_pitch", "ring_mcp_pitch"],
        joint_names=["大拇指弯曲", "大拇指横摆", "食指弯曲", "中指弯曲", "无名指弯曲", "小拇指弯曲"],
        init_pos=[250] * 6,
        preset_actions={
            "张开": [250, 250, 250, 250, 250, 250],
            "壹": [0, 31, 255, 0, 0, 0],
            "贰": [0, 31, 255, 255, 0, 0],
            "叁": [0, 30, 255, 255, 255, 0], 
            "肆": [0, 30, 255, 255, 255, 255],
            "伍": [250, 250, 250, 250, 250, 250],
            "OK": [54, 41, 164, 250, 250, 250],
            "点赞": [255, 31, 0, 0, 0, 0],
            "握拳": [49, 61, 0, 0, 0, 0],
            # Add custom actions......
        }
    )
```
