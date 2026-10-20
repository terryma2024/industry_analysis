---
source_id: "SRC-robotics-597"
title: "XenseGripper SAFE mode documentation"
source_type: "technical_documentation"
publisher: "Xense Robotics"
source_date: "待验证"
url: "https://xensesdk-cn.readthedocs.io/en/latest/GripperSDK/user/API/mode.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-20T05:41:11+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-597
---
# XenseGripper SAFE mode documentation

## mode Method

XenseGripper supports three control modes, which can be switched via the `mode` method (context manager) or the `enable_mode` / `disable_mode` methods:

- **POSITION**: Position control mode (default), precisely controls the gripper to reach a specified position.
- **SPEED**: Speed control mode, drives the gripper to move at the set speed.
- **SAFE**: Safe control mode (sensor required), enables safe operation with force feedback.

XenseGripper.mode(*self*, *control\_mode*, *serial\_number=None*) [](#xensegripper.XenseGripper.mode "Link to this definition")

A context manager for temporarily switching the gripper’s control mode. The original mode is automatically restored when exiting the context (recommended for use). Use this method with a `with` statement to ensure the mode is automatically reset after the code block is executed, preventing abnormalities caused by residual modes.

Parameters:

- **control\_mode** (*XenseGripper.ControlMode*) – Enumerated value of the control mode. `XenseGripper.ControlMode.POSITION`: Position control mode. `XenseGripper.ControlMode.SPEED`: Speed control mode. `XenseGripper.ControlMode.SAFE`: Safe control mode.
- **serial\_number** (*str**,* *optional*) – Sensor serial number (required only for SAFE mode; defaults to the first detected sensor).

Returns:

Context manager object, used to temporarily switch modes in a `with` statement block.

Return type:

context manager

XenseGripper.enable\_mode(*self*, *control\_mode*, *serial\_number=None*) [](#xensegripper.XenseGripper.enable_mode "Link to this definition")

Manually enables the specified control mode.

Parameters:

- **control\_mode** (*XenseGripper.ControlMode*) – Enumerated value of the control mode (same as the `mode` method).
- **serial\_number** (*str**,* *optional*) – Sensor serial number (required only for SAFE mode).

Returns:

Whether the operation is successful.

Return type:

bool

XenseGripper.disable\_mode(*self*) [](#xensegripper.XenseGripper.disable_mode "Link to this definition")

Manually disables the current control mode, automatically restores to the default mode, and stops the action.

Returns:

Whether the operation is successful.

Return type:

bool

## Example Code

1. Position Control Mode (default mode, no manual switching required)

```python
from xensegripper import XenseGripper

gripper = XenseGripper.create(mac_addr="9a14e81bb832")
gripper.set_position(30)  # Directly set position (defaults to POSITION mode)
```

2. Speed Control Mode

```python
# Use context manager (recommended)
with gripper.mode(XenseGripper.ControlMode.SPEED):
    gripper.set_speed(50)   # Set speed to 50 mm/s
    time.sleep(2)
    gripper.set_speed(0)    # Stop

# Manual mode switching
gripper.enable_mode(XenseGripper.ControlMode.SPEED)
gripper.set_speed(30)
gripper.disable_mode()  # Automatically stop and restore original mode
```

3. Safe Control Mode (sensor required)

```python
# Use context manager (recommended)
# Sensor serial number can be specified; defaults to the first detected sensor
with gripper.mode(XenseGripper.ControlMode.SAFE, serial_number=None):
    # Set control parameters (optional; stiffness range: 0.1~0.6)
    gripper.set_control_param(stiffness=0.35)

    # Position control (with force feedback protection)
    gripper.set_position(20)

# Manual mode switching
gripper.enable_mode(XenseGripper.ControlMode.SAFE, serial_number="OG000285")
gripper.set_control_param(stiffness=0.4)
gripper.set_position(15)
gripper.disable_mode()  # Automatically stop and restore original mode
```
