---
source_id: "SRC-robotics-239"
title: "NVIDIA Isaac Sim 4.5 system requirements"
source_type: "product_documentation"
publisher: "NVIDIA"
source_date: "2025-09-25"
url: "https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/requirements.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-07T01:22:12+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-239
---
# NVIDIA Isaac Sim 4.5 system requirements

## Isaac Sim Requirements

> [!note] Hint
> Before installing Isaac Sim, install and run the lightweight app to check if the machine meets the system requirements and compatibility.

## System Requirements

> [!note] Note
> - The Isaac Sim container is only supported on Linux.
> - Ubuntu 18.04 is only supported up to Isaac Sim 2022.2.0.
> - An Internet connection is required to access the Isaac Sim assets online and to run some extensions.
> - GPUs without RT Cores (A100, H100) are not supported.

## Driver Requirements

The recommended driver version for Isaac Sim is **537.58** for Windows and **535.129.03** for Linux.

| Driver Version Support | Windows | Linux |
| --- | --- | --- |
| Recommended | 537.58 (GameReady, Studio), 537.70 (RTX/Quadro, Grid/vGPU) | 535.129.03 (GameReady, Studio, RTX/Quadro, Grid/vGPU) |
| Minimum | 537.58 (GameReady, Studio), 537.70 (RTX/Quadro, Grid/vGPU) | 535.129.03 (GameReady, Studio, RTX/Quadro, Grid/vGPU) |

> [!note] Note
> - See [Technical Requirements](https://docs.omniverse.nvidia.com/dev-guide/latest/common/technical-requirements.html "(in Omniverse Developer Guide)") for updates.
> - See [Linux Troubleshooting](https://docs.omniverse.nvidia.com/dev-guide/latest/linux-troubleshooting.html "(in Omniverse Developer Guide)") to resolve driver installation issues on Linux.
> - We recommend installing the **Latest Production Branch Version drivers** from the [Unix Driver Archive](https://www.nvidia.com/en-us/drivers/unix/) using the `.run` installer on Linux, if you are on a new GPU or experiencing issues with the current drivers.
> - NVIDIA driver version **535.216.01** or later is recommended when upgrading to **Ubuntu 22.04.5 kernel 6.8.0-48-generic** or later.

## Isaac Sim Compatibility Checker

The **Isaac Sim Compatibility Checker** is a lightweight application that programmatically checks the above requirements and indicates which of them are valid, or not, for running Isaac Sim on the machine.

### Installation

1. Download the [Latest Release](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/download.html#isaac-sim-latest-release) of **Isaac Sim Compatibility Checker**.
2. Unzip package to a folder.
3. Run the **omni.isaac.sim.compatibility\_check.sh** script on Linux or **omni.isaac.sim.compatibility\_check.bat** on Windows.

### Checking

The application checks the points described below, highlighting in color the following states: **green** (excellent), **light-green** (good), **orange** (enough, more is recommended) and **red** (not enough/unsupported):

- **NVIDIA GPU:** Driver version, RTX-capable GPU, GPU VRAM
- **CPU, RAM and Storage:** CPU processor, Number of CPU cores, RAM, Available storage space
- **Others:** Operating system, Display
![Isaac Sim Compatibility Checker app examples](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/_images/isaac_sim_compatibility_checker.png)

Isaac Sim Compatibility Checker app examples

The **Test Kit** button, launches a minimal Kit application (in headless mode) and checks if its execution was successful or not, reporting the result on the panel next to it.

[^1]: 32GB

[^2]: 64GB

[^3]: 64GB

[^4]: 8GB
