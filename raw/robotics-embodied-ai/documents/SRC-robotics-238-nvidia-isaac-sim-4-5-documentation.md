---
source_id: "SRC-robotics-238"
title: "NVIDIA Isaac Sim 4.5 documentation"
source_type: "product_documentation"
publisher: "NVIDIA"
source_date: "2025-09-25"
url: "https://docs.isaacsim.omniverse.nvidia.com/4.5.0/index.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-07T01:22:12+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-238
---
# NVIDIA Isaac Sim 4.5 documentation

![_images/hero_shot.png](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/_images/hero_shot.png)

## What Is Isaac Sim?

NVIDIA Isaac Sim™ is a reference application built on NVIDIA Omniverse that enables developers to develop, simulate, and test AI-driven robots in physically-based virtual environments.

## Design

Isaac Sim comes with a collection of workflows for importing and tuning mechanical systems designed in the most common formats including [Onshape](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html#isaac-onshape-importer), the [Unified Robotics Description Format (URDF)](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/robot_setup/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf), and the [MuJoCo XML Format (MJCF)](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/robot_setup/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf). This is made possible through the use of the [Universal Scene Description (USD)](https://openusd.org/release/index.html), an easily extensible, open source 3D scene description API that serves as the unifying data interchange format at the heart of Isaac Sim.

## Tune and Train

The core functionality of Isaac Sim is the simulation itself: a high fidelity GPU based [PhysX engine](https://developer.nvidia.com/physx-sdk), capable of supporting [multi-sensor RTX rendering](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/sensors/index.html#isaac-sim-sensor-simulation) at an industrial scale. Isaac Sim’s direct access to the GPU enables the platform to support the simulation of various kinds of sensors including [cameras](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/sensors/isaacsim_sensors_camera.html#isaacsim-sensors-camera), [LiDAR](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/sensors/isaacsim_sensors_rtx_lidar.html#isaacsim-sensors-rtx-lidar-sensor), and [contact sensors](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/sensors/isaacsim_sensors_physics_contact.html#isaacsim-sensors-physics-contact). This in turn facilitates the simulation of digital twins, allowing your end-to-end pipelines to run before ever needing to turn on a real robot. Isaac Sim provides a suite of tools for collecting synthetic data with [Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html), orchestrating simulated environments through [Omnigraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html), tuning [PhysX simulation](https://docs.omniverse.nvidia.com/extensions/latest/ext_simulation.html) parameters to match reality, and finally training control agents through various methods like Reinforcement Learning (RL) with [Isaac Lab](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/isaac_lab_tutorials/index.html#isaac-lab-tutorials-page).

## Deploy

Isaac Sim comes pre-equipped with all of the components necessary to not only deploy agents to real robots, but also build applications that are fully integrable with such systems. [Omniverse](https://docs.omniverse.nvidia.com/dev-guide/latest/index.html) provides [APIs](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/kit_overview.html) for app infrastructure including GUI creation and file management. The Isaac Sim platform also provides bridge APIs to [ROS](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/ros_tutorials/index.html#isaac-ros-tutorials-page) and [ROS2](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/ros2_tutorials/index.html#isaac-ros2-tutorials-page), for direct communication between live robots and the simulation, as well as [NVIDIA Isaac ROS](https://nvidia-isaac-ros.github.io/), a collection of performant, hardware accelerated ROS 2 packages for making autonomous robots.

## Useful API links

- [USD API](https://graphics.pixar.com/usd/release/index.html)
- [GUI API](https://docs.omniverse.nvidia.com/kit/docs/omni.ui/latest/API.html)

## Useful Manuals

- [Omniverse Kit Programming Manual](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/kit_overview.html)
- [Scripting Guides](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/python_scripting/util_snippets.html#isaac-sim-app-util-snippets)

## Getting Started

- [Workstation Installation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/install_workstation.html#isaac-sim-app-install-workstation): Installation guide for a local workstation.
- [Container Installation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/install_container.html#isaac-sim-app-install-container): Installation guide for a remote headless server.
- [Getting Started](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/quickstart_isaacsim.html#isaac-sim-app-intro-quickstart): The quick introductory tutorials to get your feet wet with NVIDIA Isaac Sim.
- [Development Tools](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/development_tools/index.html#isaac-sim-development-tools-tutorials): The tools and environments for debugging and development.
- [Python Scripting](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/python_scripting/index.html#isaac-sim-app-python-scripting-overview): Tools and tutorials for building environments, robots, and tasks using NVIDIA Isaac Sim Core Python APIs.
- [GUI](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/gui/index.html#isaac-sim-gui-tutorials-page): The fundamental concepts of robotics in NVIDIA Isaac Sim via GUI.
- [Robot setup](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/robot_setup/index.html#isaac-sim-robot-setup-tutorials): Importing and modifying robots and manipulators from external sources.
- [Robot simulation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/robot_simulation/index.html#isaac-sim-robot-simulation): Controllers, motion generation tools for simulating robots.
- [ROS](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/ros2_tutorials/ros2_landing_page.html#isaac-sim-ros-ros2-tutorials): ROS and ROS2 bridges and interfaces.
- [Isaac Lab](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/isaac_lab_tutorials/index.html#isaac-lab-tutorials-page): Reinforcement learning framework and Cloner APIs.
- [Replicator](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/replicator_tutorials/index.html#isaac-replicator-tutorials-page): Synthetic data generation.
- [Digital Twin](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/digital_twin/index.html#isaac-sim-app-digital-twin-index): Tools for building and operating digital twins, such as [Warehouse logistics](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/digital_twin/index.html#isaac-sim-app-warehouse-logistics-index), [Cortex](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/cortex_tutorials/tutorial_cortex_1_overview.html#isaac-sim-app-tutorial-cortex-1-overview), and [Mapping](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/digital_twin/ext_isaacsim_asset_generator_occupancy_map.html#ext-isaacsim-asset-generator-occupancy-map).

## System Architecture

![Your Image](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/_images/Isaac_Sim_System_Diagram.png)

The purpose of Isaac Sim is to support the creation of new robotics tools and empower the ones that already exist. The platform provides a flexible API for both C++ and Python and can be integrated into a project to varying degrees depending on your needs. The goal of the platform is not to compete with current or existing software, but to collaborate with and enhance it. To this end, many components of Isaac Sim are open source, and freely available for independent use. You may want to design your robot in OnShape, simulate its sensors with Isaac Sim, and control the stage through ROS or some other messaging system. Likewise, it is also possible to build a complete, stand alone, application entirely on the platform provided by Isaac Sim!

## Omniverse Kit

Isaac Sim uses the Omniverse™ Kit, a toolkit for building native Omniverse applications and microservices. Omniverse Kit provides a wide variety of functionality through a set of light-weight plugins. Plugins are authored with C interfaces for persistent API compatibility; however, a Python interpreter is also provided for accessible scripting and customization.

The Python API can be used to write new extensions to Omniverse Kit or new experiences for Omniverse.

## Development Workflows

![_images/Isaac_Sim_Workflows_Diagram.png](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/_images/Isaac_Sim_Workflows_Diagram.png)

Isaac Sim is built on C++ and Python, and operates most commonly through the use of compiled plugins and bindings respectively. This means the platform is capable of supporting a wide variety of workflows for building and interacting with projects that make use of Isaac Sim. Isaac Sim comes with a full, stand alone, Omniverse application for interacting with and simulating robots, and while this is the most common way users interact with the platform, it is by no means the only method. Isaac Sim also provides direct Python development support in the form of extensions for VS Code and Jupyter Notebooks. Isaac Sim is not limited to synchronous operation either, and can operate with hardware in the loop through ROS and ROS2, facilitating sim-to-real transfer and digital twins.

## USD

NVIDIA Isaac Sim uses the USD interchange file format to represent scenes. Universal Scene Description (USD) is an easily extensible, open-source 3D scene description file format developed by Pixar for content creation and interchange among different tools. Because of its power and versatility, USD is being adopted widely, not only in the visual effects community, but also in architecture, design, robotics, manufacturing, and other disciplines.

- For a more in-depth look at USD in Omniverse, see the NVIDIA USD primer [What is USD?](https://developer.nvidia.com/usd).
- See the [USD API](https://graphics.pixar.com/usd/release/index.html) docs for more details.
- see the [NVIDIA USD API](https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr.html) for our Python wrappers around USD.
- See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.
- See the [NVIDIA USD tutorials](https://developer.nvidia.com/usd/tutorials) for a step-by-step introduction to USD.
