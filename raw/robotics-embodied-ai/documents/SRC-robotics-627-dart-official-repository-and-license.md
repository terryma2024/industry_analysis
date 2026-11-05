---
source_id: "SRC-robotics-627"
title: "DART official repository and license"
source_type: "repository"
publisher: "DART"
source_date: "待验证"
url: "https://github.com/dartsim/dart"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/repository
  - evidence/s
aliases:
  - SRC-robotics-627
---
# DART official repository and license

## DART

[![DART: Dynamic Animation and Robotics Toolkit](https://raw.githubusercontent.com/dartsim/dart/main/docs/dart_logo_377x107.jpg)](https://raw.githubusercontent.com/dartsim/dart/main/docs/dart_logo_377x107.jpg)

[![CI Linux](https://github.com/dartsim/dart/actions/workflows/ci_ubuntu.yml/badge.svg)](https://github.com/dartsim/dart/actions/workflows/ci_ubuntu.yml) [![CI macOS](https://github.com/dartsim/dart/actions/workflows/ci_macos.yml/badge.svg)](https://github.com/dartsim/dart/actions/workflows/ci_macos.yml) [![CI Windows](https://github.com/dartsim/dart/actions/workflows/ci_windows.yml/badge.svg)](https://github.com/dartsim/dart/actions/workflows/ci_windows.yml)  
[![Documentation Status](https://camo.githubusercontent.com/69dc1c5dda1d0fd1bc627359c12027071fa6409a756f63eb8ddf82b641a65fab/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f646172742f62616467652f3f76657273696f6e3d6c6174657374)](https://dart.readthedocs.io/en/latest/) [![codecov](https://camo.githubusercontent.com/61736206798803ae96712b17bd66279a80a241e8921443093df747711489f448/68747470733a2f2f636f6465636f762e696f2f67682f6461727473696d2f646172742f6272616e63682f6d61696e2f67726170682f62616467652e737667)](https://codecov.io/gh/dartsim/dart) [![Codacy Badge](https://camo.githubusercontent.com/cc882aec26d460e7d36a0a56e681c9ea8f71b54999205ffef87e342ef423f26f/68747470733a2f2f6170702e636f646163792e636f6d2f70726f6a6563742f62616467652f47726164652f3264393561396239353162653462373361373130393736373065633335316538)](https://app.codacy.com/gh/dartsim/dart/dashboard)  
[![PyPI Version](https://camo.githubusercontent.com/4972e0c79df25a41aa6114fe4125e969fbc9968353c0a48a450b2fe4451758ca/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646172747079)](https://pypi.org/project/dartpy/) [![conda-forge Version](https://camo.githubusercontent.com/d2221d23ef3e2bfa963d344e710265130755b50070cd91d1a530b696f27d350b/68747470733a2f2f696d672e736869656c64732e696f2f636f6e64612f766e2f636f6e64612d666f7267652f6461727473696d3f6c6162656c3d636f6e64612d666f726765)](https://anaconda.org/conda-forge/dartsim) [![License](https://camo.githubusercontent.com/3ce287b09b23d96b82dbbc325362de6f5989c410e228ddb93b002d8dc31d7dde/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4253445f322d2d436c617573652d626c75652e737667)](https://github.com/dartsim/dart/blob/main/LICENSE)

DART (Dynamic Animation and Robotics Toolkit) is an open-source C++17 library, with Python bindings (dartpy), for the kinematics, dynamics, and contact simulation of articulated rigid and soft bodies in robotics and computer animation. It represents articulated systems in generalized coordinates and computes their motion with Featherstone's Articulated Body Algorithm, which makes it accurate and stable.

> [!note] Note
> `main` is the development branch. For the latest stable release, install a package below.

[![Four DART demos: an Atlas humanoid walking under a SIMBICON controller, a Unitree G1 humanoid posed with inverse kinematics, a soft-body worm crawling, and a soft ball landing with adaptive soft contact](https://raw.githubusercontent.com/dartsim/dart/main/docs/assets/dart_demos.gif)](https://raw.githubusercontent.com/dartsim/dart/main/docs/assets/dart_demos.gif)  
<sub>Atlas, soft-worm, and soft-contact scenes available in the Python demo catalog (<code>pixi run demos</code>), plus a Unitree G1 IK puppet from an earlier example</sub>

## Why DART?

- **Research-grade dynamics** — Featherstone's algorithms in generalized coordinates, with direct access to the mass matrix, Coriolis and gravity forces, Jacobians, and their derivatives
- **Contacts and constraints** — LCP-based contact with Dantzig and PGS solvers, joint limits, closed kinematic loops, and soft bodies; collision detection through FCL (default), Bullet, ODE, or DART's native detector
- **Model loading** — URDF, SDF, SKEL, and MJCF (experimental) parsers
- **Kinematics and control** — hierarchical whole-body inverse kinematics with analytical solver support, plus operational-space and stable-PD control examples
- **C++ and Python** — the same engine through dartpy, packages on PyPI, conda-forge, and major package managers, and reproducible source builds with pixi
- **Battle-tested** — powers [Gazebo](https://gazebosim.org/) through gz-physics, and is used by [research labs worldwide](https://dart.readthedocs.io/en/latest/community/who_uses_dart.html)

## Quick Start

**Python**

```
import dartpy as dart

world = dart.simulation.World()  # 1 ms time step, gravity along -z

# A shapeless 1 kg rigid body (the default inertia) free-falling from z = 1 m.
body = dart.dynamics.Skeleton("body")
body.createFreeJointAndBodyNodePair()
body.setPosition(5, 1.0)  # FreeJoint DOFs: rotation (0-2), translation (3-5)
world.addSkeleton(body)

for _ in range(100):
    world.step()

print(f"t = {world.getTime():.3f} s, z = {body.getPosition(5):.3f} m")
# t = 0.100 s, z = 0.950 m
```

**C++**

```
#include <dart/dart.hpp>

#include <iostream>

int main()
{
  auto world = dart::simulation::World::create();

  // A shapeless 1 kg rigid body (the default inertia) free-falling from z = 1 m.
  auto body = dart::dynamics::Skeleton::create("body");
  body->createJointAndBodyNodePair<dart::dynamics::FreeJoint>();
  body->setPosition(5, 1.0); // FreeJoint DOFs: rotation (0-2), translation (3-5)
  world->addSkeleton(body);

  for (int i = 0; i < 100; ++i)
    world->step();

  std::cout << "t = " << world->getTime() << " s, z = " << body->getPosition(5)
            << " m\n";
}
```
```
# CMakeLists.txt next to main.cpp
cmake_minimum_required(VERSION 3.22.1)
project(my_app CXX)
find_package(DART REQUIRED CONFIG)
add_executable(my_app main.cpp)
target_link_libraries(my_app PUBLIC dart)
```

## Installation

### Python

| Method | Command |
| --- | --- |
| **pip** | `pip install dartpy` |
| **uv** | `uv add dartpy` |
| **pixi** | `pixi add dartpy` |
| **conda** | `conda install -c conda-forge dartpy` |

PyPI wheels cover the most common platforms and Python versions; see the [Python installation guide](https://dart.readthedocs.io/en/latest/dartpy/user_guide/installation.html) for the exact list.

### C++

| Platform | Command |
| --- | --- |
| **Cross-platform** (recommended) | `pixi add dartsim-cpp` or `conda install -c conda-forge dartsim-cpp` |
| Ubuntu / Debian | `sudo apt install libdart-all-dev` |
| Arch Linux (AUR) | `yay -S libdart` |
| FreeBSD | `pkg install dartsim` |
| macOS (Homebrew) | `brew install dartsim` |
| Windows (vcpkg) | `vcpkg install dartsim:x64-windows` |

Distribution packages can lag behind the latest release: [all distributions →](https://repology.org/project/dart-sim/versions). See the [C++ installation guide](https://dart.readthedocs.io/en/latest/dart/user_guide/installation.html) for details.

### Build from source

```
git clone https://github.com/dartsim/dart.git
cd dart
pixi run test   # configure, build, and run the C++ tests
pixi run demos  # build dartpy and launch the Python demo catalog
```

See the [build guide](https://dart.readthedocs.io/en/latest/dart/developer_guide/build.html) for options and other platforms.

## Documentation

- **User guide**: [English](https://dart.readthedocs.io/) | [한국어](https://dart.readthedocs.io/ko/latest/)
- **Gallery**: [videos and projects](https://dart.readthedocs.io/en/latest/gallery.html) · **Performance**: [benchmark dashboard](https://dartsim.github.io/dart/performance/dart6/)
- **Questions**: [GitHub Discussions](https://github.com/dartsim/dart/discussions) · **AI Q&A (experimental)**: [DeepWiki](https://deepwiki.com/dartsim/dart)

## Contributing

Contributions are welcome; start with the [contributing guide](https://github.com/dartsim/dart/blob/main/CONTRIBUTING.md).

- [Architecture](https://github.com/dartsim/dart/blob/main/docs/onboarding/architecture.md) — components and compatibility boundaries
- [Building](https://github.com/dartsim/dart/blob/main/docs/onboarding/building.md) and [testing](https://github.com/dartsim/dart/blob/main/docs/onboarding/testing.md)
- [Background theory](https://github.com/dartsim/dart/blob/main/docs/background/README.md) — dynamics, contact solving, and mathematical foundations
- [Changelog](https://github.com/dartsim/dart/blob/main/CHANGELOG.md)
- [AGENTS.md](https://github.com/dartsim/dart/blob/main/AGENTS.md) — guidelines for AI coding agents

### Branches

`main` is the development branch for the next release: pull requests target it, and all new patches land on it. Stable versions are available as [tagged releases](https://github.com/dartsim/dart/releases) and as the packages above.

## Citation

If you use DART in an academic publication, please consider citing the [JOSS paper](https://doi.org/10.21105/joss.00500):

```
@article{Lee2018,
  doi       = {10.21105/joss.00500},
  url       = {https://doi.org/10.21105/joss.00500},
  year      = {2018},
  publisher = {The Open Journal},
  volume    = {3},
  number    = {22},
  pages     = {500},
      = {Jeongseok Lee and Michael X. Grey and Sehoon Ha and Tobias Kunz and Sumit Jain and Yuting Ye and Siddhartha S. Srinivasa and Mike Stilman and C. Karen Liu},
  title     = {DART: Dynamic Animation and Robotics Toolkit},
  journal   = {Journal of Open Source Software}
}
```

## License

DART is licensed under the [BSD 2-Clause License](https://github.com/dartsim/dart/blob/main/LICENSE).

[

![Star History Chart](https://camo.githubusercontent.com/c9f0c429c48a31ae0c80c38a9865ee3a739adf7aaa7b2508e925c8b2716fc6c2/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6461727473696d2f6461727426747970653d44617465)

](https://star-history.com/#dartsim/dart&Date)
