---
source_id: "SRC-robotics-633"
title: "Genesis World official repository and license"
source_type: "repository"
publisher: "Genesis AI"
source_date: "待验证"
url: "https://github.com/Genesis-Embodied-AI/genesis-world"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/repository
  - evidence/s
aliases:
  - SRC-robotics-633
---
# Genesis World official repository and license

[![Genesis World teaser](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/HeroShot_Final.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/HeroShot_Final.png)

## Genesis World

[![PyPI - Version](https://camo.githubusercontent.com/914622492998fec3693567edd057e7ec9c0ce7a012be610282583d5530a6117f/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f67656e657369732d776f726c64)](https://pypi.org/project/genesis-world/) [![PyPI Downloads](https://camo.githubusercontent.com/5d92c99fe898bf8baee23af138d13a3b9e26e46daf7ead79d2c07d03f2ad8603/68747470733a2f2f7374617469632e706570792e746563682f62616467652f67656e657369732d776f726c64)](https://pepy.tech/projects/genesis-world) [![Documentation](https://camo.githubusercontent.com/4ab7ff03f0d5c362b3395643e699d06a82b393e6415e05ed95ef9f1fc6af3e30/68747470733a2f2f6170702e72656164746865646f63732e6f72672f70726f6a656374732f67656e657369732d776f726c642f62616467652f3f76657273696f6e3d6c6174657374)](https://genesis-world.readthedocs.io/en/latest/) [![GitHub Issues](https://camo.githubusercontent.com/b04564c267053accae44ee86f6d33692cba2b061b6b14a137701953f395eeea2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f47656e657369732d456d626f646965642d41492f67656e657369732d776f726c64)](https://github.com/Genesis-Embodied-AI/genesis-world/issues) [![GitHub Discussions](https://camo.githubusercontent.com/d236e6c7ee24815433bf45a6d9b9ed8a1cdef36b6e54ea792c68cb08cc730f6f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f64697363757373696f6e732f47656e657369732d456d626f646965642d41492f67656e657369732d776f726c64)](https://github.com/Genesis-Embodied-AI/genesis-world/discussions)

**Genesis World** is a simulation platform for physical AI developments. It combines a unified multi-physics engine, a photo-realistic renderer ([Nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)), and a cross-platform compiler ([Quadrants](https://github.com/Genesis-Embodied-AI/quadrants)) behind a Pythonic simulation interface. Genesis World is designed to scale from a single laptop kernel to datacenter-grade GPUs, while remaining easy to read, extend, and embed in research code.

It was previously named **Genesis** and started as an academic project since Dec 2024, and its development is now officially supported by [Genesis AI](https://www.genesis.ai/).

For more technical details, refer to our [blog post](https://genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward).

## Table of Contents

## What is Genesis World?

[![Genesis World stack](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/diagram_white_lum.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/diagram_white_lum.png)

Genesis World occupies the four layers inside the dashed box. Above sits whatever you build (robotics environments, ML pipelines, data generation, agentic simulation); below sits whatever compute backend you have.

- **Simulation Interface** — the user-facing API: asset parsing (URDF, MJCF, OBJ, GLB, USD, …), entity accessors, controllers, sensors, parallel and heterogeneous environments, and a built-in GUI.
- **Physics** — a unified multi-physics engine integrating Rigid, FEM, MPM, Particle (PBD / SPH), [uipc](https://github.com/spiriMirror/libuipc), an explicit coupler, and SAP, all sharing one scene and one state.
- **Render** — three rendering paths plug in as camera sensors: **[Nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)** (our in-house renderer designed for robotics), Luisa (DSL ray tracer), and Pyrender (rasterizer).
- **Compiler** — **[Quadrants](https://github.com/Genesis-Embodied-AI/quadrants)** lowers Python kernel code to CUDA, AMD ROCm, Apple Metal, Vulkan, x86, and ARM64. It carries Genesis's autodiff, GPU graphs, and fastcache machinery.

### Documentation

- [Genesis World](https://genesis-world.readthedocs.io/en/latest/)
- [Quadrants](https://genesis-embodied-ai.github.io/quadrants/index.html)
- [Nyx](https://genesis-embodied-ai.github.io/genesis-nyx/latest/)

## Catalogue

Three sections, mirroring the Genesis layers that ship runnable demos: **Physics** (solvers and multi-solver coupling), **Rendering** (in-repo camera setups plus the Nyx walkthroughs hosted in [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)), and **Simulation Interface** (sensors, GUI, controllers, parallel/heterogeneous envs, and tutorials). Most scripts run end-to-end after `pip install -e ".[dev]"`; demos that depend on optional backends (e.g. the IPC and Nyx examples) need the extras listed in [Optional extras](#optional-extras).

### Physics

|  |  |  |
| --- | --- | --- |
| [Rigid: franka cube](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rigid/franka_cube.py) | [Rigid: collision tower](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/collision/tower.py) | [Rigid: contype](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/collision/contype.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_franka_cube.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_franka_cube.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_tower.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_tower.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contype.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contype.webp) |
| [FEM: hard & soft constraint](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/deformable/fem_hard_and_soft_constraint.py) | [MPM: tutorial](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/mpm.py) | [MPM: sand wheel](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/sand_wheel.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/fem_hard_and_soft_constraint.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/fem_hard_and_soft_constraint.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_mpm.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_mpm.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sand_wheel.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sand_wheel.webp) |
| [SPH: rigid](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/sph_rigid.py) | [SPH: + MPM](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/sph_mpm.py) | [PBD: liquid](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/deformable/pbd_liquid.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_rigid.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_rigid.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_mpm.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_mpm.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/pbd_liquid.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/pbd_liquid.webp) |
| [PBD: cloth](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/pbd_cloth.py) | [Stable Fluid: smoke](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/fluid/smoke.py) | [IPC: robot cloth teleop](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/ipc/ipc_robot_cloth_teleop.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_pbd_cloth.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_pbd_cloth.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/smoke.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/smoke.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/ipc_cloth_teleop.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/ipc_cloth_teleop.webp) |
| [Coupler: cloth on rigid](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/cloth_on_rigid.py) | [Coupler: rigid + MPM](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/rigid_mpm_attachment.py) | [Coupler: cut dragon](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/cut_dragon.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cloth_on_rigid.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cloth_on_rigid.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_rigid_mpm_attachment.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_rigid_mpm_attachment.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cut_dragon.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cut_dragon.webp) |
| [Coupler: water wheel](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/water_wheel.py) | [Coupler: flush cubes](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/coupling/flush_cubes.py) | [SAP: Franka grasp rigid cube](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sap_coupling/franka_grasp_rigid_cube.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_water_wheel.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_water_wheel.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_flush_cubes.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_flush_cubes.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_franka_grasp_rigid_cube.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_franka_grasp_rigid_cube.webp) |
| [Rigid: contact patch](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/collision/contact_manifold.py) |  |  |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contact_manifold.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contact_manifold.webp) |  |  |

### Rendering

Genesis exposes three rendering paths as camera sensors: built-in (Nyx / Luisa / Pyrender) and detailed Nyx walkthroughs hosted in [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx/tree/main/examples).

|  |  |  |
| --- | --- | --- |
| [Follow entity](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rendering/follow_entity.py) | [Animated camera](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rendering/moving_camera.py) | [Nyx: hello](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/01_hello_nyx.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_follow_entity.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_follow_entity.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_moving_camera.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_moving_camera.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_01_hello_nyx.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_01_hello_nyx.png) |
| [Nyx: attached camera](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/02_attached_camera.py) | [Nyx: PBR materials](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/03_materials.py) | [Nyx: light types](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/04_light_types.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_02_attached_camera.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_02_attached_camera.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_03_materials.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_03_materials.png) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_04_light_types.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_04_light_types.png) |
| [Nyx: 3D Gaussian splat](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/05_gaussian_splat.py) | [Nyx: object picking](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/06_object_picking.py) | [Nyx: multi-cam multi-env](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/07_multi_camera_multi_env.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_05_gaussian_splat.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_05_gaussian_splat.png) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_06_object_picking.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_06_object_picking.png) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_07_multi_camera_multi_env.png)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_07_multi_camera_multi_env.png) |

### Simulation Interface

|  |  |  |
| --- | --- | --- |
| [Controlling a robot](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/control_your_robot.py) | [GUI: ImGui joint control](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/gui/imgui_joint_control.py) | [Heterogeneous envs](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rigid/heterogeneous_simulation.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_control_your_robot.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_control_your_robot.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/gui_imgui_joint_control.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/gui_imgui_joint_control.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/het_articulated.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/het_articulated.webp) |
| [Domain randomization](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rigid/domain_randomization.py) | [Sensor: depth camera](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/depth_camera_custom_vverts.py) | [Sensor: IMU](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/imu_franka.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_domain_randomization.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_domain_randomization.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_depth_camera_custom_vverts.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_depth_camera_custom_vverts.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_imu_franka.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_imu_franka.webp) |
| [Sensor: lidar](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/lidar_teleop.py) | [Sensor: tactile sandbox](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/tactile_sandbox.py) | [Sensor: contact force](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/contact_force_go2.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_lidar_teleop.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_lidar_teleop.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_tactile_sandbox.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_tactile_sandbox.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_contact_force_go2.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_contact_force_go2.webp) |
| [Sensor: surface distance](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/surface_distance_shadowhand.py) | [Sensor: temperature grid](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/sensors/temperature_grid.py) | [GUI: debug drawing](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/draw_debug.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_surface_distance_shadowhand.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_surface_distance_shadowhand.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_temperature_grid.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_temperature_grid.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_draw_debug.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_draw_debug.webp) |
| [GUI: mesh point picker](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/viewer_plugin/mesh_point_selector.py) | [GUI: mouse interaction](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/viewer_plugin/mouse_interaction.py) | [Diff-IK controller](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/rigid/diffik_controller.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mesh_point_selector.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mesh_point_selector.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mouse_interaction.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mouse_interaction.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_diffik_controller.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_diffik_controller.webp) |
| [Batched IK](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/batched_IK.py) | [Drone](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/drone/hover_train.py) | [Advanced: worm](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/examples/tutorials/advanced_worm.py) |
| [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_batched_IK.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_batched_IK.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/drone_hover_train.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/drone_hover_train.webp) | [![](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_advanced_worm.webp)](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_advanced_worm.webp) |

## Quick Installation

### Using pip

Install **PyTorch** first following the [official instructions](https://pytorch.org/get-started/locally/).

Then, install Genesis via PyPI:

```
pip install genesis-world  # Requires Python>=3.10,<3.14;
```

For the latest version to date, make sure that `pip` is up-to-date via `pip install --upgrade pip`, then run command:

```
pip install git+https://github.com/Genesis-Embodied-AI/genesis-world.git
```

Note that the package must still be updated manually to sync with main branch.

Users seeking to contribute are encouraged to install Genesis in editable mode. First, make sure that `genesis-world` has been uninstalled, then clone the repository and install locally:

```
git clone https://github.com/Genesis-Embodied-AI/genesis-world.git
cd genesis-world
pip install -e ".[dev]"
```

It is recommended to systematically execute `pip install -e ".[dev]"` after moving HEAD to make sure that all dependencies and entrypoints are up-to-date.

### Optional extras

|  |  |
| --- | --- |
| IPC solver (uipc backend) | `pip install pyuipc` *(Linux / Windows x86, NVIDIA GPU)* |
| Nyx renderer | `pip install gs-nyx` — see [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx) |

Quadrants is bundled with Genesis automatically; no extra install. The standalone wheel (`pip install quadrants`) is documented at [Quadrants](https://github.com/Genesis-Embodied-AI/quadrants) for users who want the compiler outside Genesis.

### Using uv

[uv](https://docs.astral.sh/uv/) is a fast Python package and project manager.

**Install uv:**

```
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Quick start with uv:**

```
git clone https://github.com/Genesis-Embodied-AI/genesis-world.git
cd genesis-world
uv sync
```

Then install PyTorch for your platform:

```
# NVIDIA GPU (CUDA 12.6 as an example)
uv pip install torch --index-url https://download.pytorch.org/whl/cu126

# CPU only (Linux/Windows)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu

# Apple Silicon (Metal/MPS)
uv pip install torch
```

Run an example:

```
uv run examples/rigid/single_franka.py
```

## Contributing to Genesis

The Genesis project is an open and collaborative effort. We welcome all forms of contributions from the community, including:

- **Pull requests** for new features or bug fixes.
- **Bug reports** through GitHub Issues.
- **Suggestions** to improve Genesis's usability.

Refer to our [contribution guide](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/.github/contributing/PULL_REQUESTS.md) for more details.

## Support

- Report bugs or request features via GitHub [Issues](https://github.com/Genesis-Embodied-AI/genesis-world/issues).
- Join discussions or ask questions on GitHub [Discussions](https://github.com/Genesis-Embodied-AI/genesis-world/discussions).

## License and Acknowledgments

The Genesis source code is licensed under Apache 2.0.

Genesis's development has been made possible thanks to these open-source projects:

- [Taichi](https://github.com/taichi-dev/taichi): the original compiler that [Quadrants](https://github.com/Genesis-Embodied-AI/quadrants) forked from in June 2025. Kudos to the Taichi team for their technical support over the years.
- [libuipc](https://github.com/spiriMirror/libuipc): IPC solver backend.
- [FluidLab](https://github.com/zhouxian/FluidLab): Reference MPM solver implementation.
- [SPH\_Taichi](https://github.com/erizmr/SPH_Taichi): Reference SPH solver implementation.
- [Ten Minute Physics](https://matthias-research.github.io/pages/tenMinutePhysics/index.html) and [PBF3D](https://github.com/WASD4959/PBF3D): Reference PBD solver implementations.
- [MuJoCo](https://github.com/google-deepmind/mujoco): Reference for rigid body dynamics.
- [libccd](https://github.com/danfis/libccd): Reference for collision detection.
- [PyRender](https://github.com/mmatl/pyrender): Rasterization-based renderer.
- [LuisaCompute](https://github.com/LuisaGroup/LuisaCompute) and [LuisaRender](https://github.com/LuisaGroup/LuisaRender): Ray-tracing DSL.
- [Madrona](https://github.com/shacklettbp/madrona) and [Madrona-mjx](https://github.com/shacklettbp/madrona_mjx): Batch renderer backend

## Citation

If you use Genesis in your research, please consider citing:

```
@article{
   genesis2026genesisworld,
    = {Genesis AI Team},
   title = {The Role of Simulation in Scalable Robotics, Genesis World 1.0, and the Path Forward},
   journal = {Genesis AI Blog},
   month = {May},
   year = {2026},
   url = {https://www.genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward},
}
```
```
@misc{
  Genesis,
   = {Genesis Authors},
  title = {Genesis: A Generative and Universal Physics Engine for Robotics and Beyond},
  month = {December},
  year = {2024},
  url = {https://github.com/Genesis-Embodied-AI/genesis-world}
}
```
