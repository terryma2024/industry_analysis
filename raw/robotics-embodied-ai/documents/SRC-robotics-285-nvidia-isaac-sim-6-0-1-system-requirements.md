---
source_id: "SRC-robotics-285"
title: "NVIDIA Isaac Sim 6.0.1 system requirements"
source_type: "product_documentation"
publisher: "NVIDIA"
source_date: "2026-06"
url: "https://docs.isaacsim.omniverse.nvidia.com/6.0.1/installation/requirements.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T03:30:40+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-285
---
# NVIDIA Isaac Sim 6.0.1 system requirements

## Isaac Sim Requirements

> [!note] Hint
> By installing Isaac Sim, you can run the [Isaac Sim Compatibility Checker](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/installation/install_workstation.html#isaac-sim-compatibility-checker) lightweight app to check if your machine meets the system requirements and compatibility.

## System Requirements

Requirements for x86\_64

> | Element | Minimum Spec | Good | Ideal |
> | --- | --- | --- | --- |
> | OS | Ubuntu 22.04/24.04  Windows 11 | Ubuntu 22.04/24.04  Windows 11 | Ubuntu 22.04/24.04  Windows 11 |
> | CPU | Intel Core i7 (7th Generation)  AMD Ryzen 5 | Intel Core i7 (9th Generation)  AMD Ryzen 7 | Intel Core i9, X-series or higher  AMD Ryzen 9, Threadripper or higher |
> | Cores | 4 | 8 | 16 |
> | RAM | 32GB | 64GB | 64GB |
> | Storage | 50GB SSD | 500GB SSD | 1TB NVMe SSD |
> | GPU | GeForce RTX 4080 | GeForce RTX 5080 | RTX PRO 6000 Blackwell |
> | VRAM | 16GB | 16GB | 48GB |
> | Driver | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) |
> 
> > [!note] Note
> > - The Isaac Sim container is only supported on Linux.
> > - An Internet connection is required to access the Isaac Sim assets online and to run some extensions. Allow outbound HTTPS access to `omniverse-content-production.s3-us-west-2.amazonaws.com` when using the default online asset root.
> > - GPUs without RT Cores (A100, H100) are not supported.
> > - Due to VRAM constraints, some tutorials and benchmarks may not run on GPU below the minimum specifications. Workflows leveraging a large number of sensors are particularly affected.
> > - See [Linux Troubleshooting](https://docs.omniverse.nvidia.com/dev-guide/latest/linux-troubleshooting.html "(in Omniverse Developer Guide)") to resolve driver installation issues on Linux.
> > - We recommend installing the **Latest Production Branch Version drivers** from the [Unix Driver Archive](https://www.nvidia.com/en-us/drivers/unix/) using the `.run` installer on Linux if you are on a new GPU or experiencing issues with the current drivers.
> > - Windows 10 is not supported. Microsoft ended Windows 10 support on October 14, 2025, and no longer provides free security, feature, or technical updates for it.

Requirements for aarch64

| Element | Specifications |
| --- | --- |
| Device | NVIDIA DGX™ Spark |
| OS | NVIDIA DGX OS 7 |
| Driver | [580.159.03](https://www.nvidia.com/en-us/drivers/details/267260/) |

> [!note] Note
> - Isaac Sim aarch64 builds are currently only supported on DGX Spark system.
> - The Isaac Sim container is only supported on Linux.
> - An Internet connection is required to access the Isaac Sim assets online and to run some extensions.

Limitations

> [!warning] Warning
> Here are the limitations of running Isaac Sim 6.0 on DGX Spark:
> 
> - [cuRobo and cuMotion](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/manipulators/manipulators_curobo.html#isaac-sim-app-tutorial-curobo) is not supported.

[^1]: > | Element | Minimum Spec | Good | Ideal |
> | --- | --- | --- | --- |
> | OS | Ubuntu 22.04/24.04  Windows 11 | Ubuntu 22.04/24.04  Windows 11 | Ubuntu 22.04/24.04  Windows 11 |
> | CPU | Intel Core i7 (7th Generation)  AMD Ryzen 5 | Intel Core i7 (9th Generation)  AMD Ryzen 7 | Intel Core i9, X-series or higher  AMD Ryzen 9, Threadripper or higher |
> | Cores | 4 | 8 | 16 |
> | RAM | 32GB | 64GB | 64GB |
> | Storage | 50GB SSD | 500GB SSD | 1TB NVMe SSD |
> | GPU | GeForce RTX 4080 | GeForce RTX 5080 | RTX PRO 6000 Blackwell |
> | VRAM | 16GB | 16GB | 48GB |
> | Driver | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) | Linux: [595.58.03](https://www.nvidia.com/en-us/drivers/details/265870/)  Windows: [595.97](https://www.nvidia.com/en-us/drivers/details/265877/) |
> 
> > [!note] Note
> > - The Isaac Sim container is only supported on Linux.
> > - An Internet connection is required to access the Isaac Sim assets online and to run some extensions. Allow outbound HTTPS access to `omniverse-content-production.s3-us-west-2.amazonaws.com` when using the default online asset root.
> > - GPUs without RT Cores (A100, H100) are not supported.
> > - Due to VRAM constraints, some tutorials and benchmarks may not run on GPU below the minimum specifications. Workflows leveraging a large number of sensors are particularly affected.
> > - See [Linux Troubleshooting](https://docs.omniverse.nvidia.com/dev-guide/latest/linux-troubleshooting.html "(in Omniverse Developer Guide)") to resolve driver installation issues on Linux.
> > - We recommend installing the **Latest Production Branch Version drivers** from the [Unix Driver Archive](https://www.nvidia.com/en-us/drivers/unix/) using the `.run` installer on Linux if you are on a new GPU or experiencing issues with the current drivers.
> > - Windows 10 is not supported. Microsoft ended Windows 10 support on October 14, 2025, and no longer provides free security, feature, or technical updates for it.

[^2]: VRAM

[^3]: 16GB

[^4]: Driver

[^5]: | Element | Specifications |
| --- | --- |
| Device | NVIDIA DGX™ Spark |
| OS | NVIDIA DGX OS 7 |
| Driver | [580.159.03](https://www.nvidia.com/en-us/drivers/details/267260/) |

> [!note] Note
> - Isaac Sim aarch64 builds are currently only supported on DGX Spark system.
> - The Isaac Sim container is only supported on Linux.
> - An Internet connection is required to access the Isaac Sim assets online and to run some extensions.

Limitations

> [!warning] Warning
> Here are the limitations of running Isaac Sim 6.0 on DGX Spark:
> 
> - [cuRobo and cuMotion](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/manipulators/manipulators_curobo.html#isaac-sim-app-tutorial-curobo) is not supported.
