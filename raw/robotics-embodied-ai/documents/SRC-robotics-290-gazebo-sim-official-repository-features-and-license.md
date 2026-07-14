---
source_id: "SRC-robotics-290"
title: "Gazebo Sim official repository features and license"
source_type: "code_repository"
publisher: "Open Robotics"
source_date: "2026-07-14"
url: "https://github.com/gazebosim/gz-sim"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T03:30:40+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/a
aliases:
  - SRC-robotics-290
---
# Gazebo Sim official repository features and license

## Gazebo Sim: A Robotic Simulator

**Maintainer:** arjoc AT intrinsic DOT ai

[![GitHub open issues](https://camo.githubusercontent.com/96d2a50448417f8fad12193879522904f6cd4396b37a09dc4f8a330de2d3f369/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d7261772f67617a65626f73696d2f677a2d73696d2e737667)](https://github.com/gazebosim/gz-sim/issues) [![GitHub open pull requests](https://camo.githubusercontent.com/1bf787a75d1645e74a30f56394e55738f7816b0ee22ae9a70eafc9c8049c01ca/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722d7261772f67617a65626f73696d2f677a2d73696d2e737667)](https://github.com/gazebosim/gz-sim/pulls) [![Discourse Topics](https://camo.githubusercontent.com/b3cf1995c79475566f6a8da974378a9e8384053ad376d87041408df9f3aa9f5f/68747470733a2f2f696d672e736869656c64732e696f2f646973636f757273652f746f706963733f7365727665723d6874747073253341253246253246646973636f757273652e6f70656e726f626f746963732e6f7267253246)](https://discourse.openrobotics.org/c/gazebo) [![Hex.pm](https://camo.githubusercontent.com/78e12fef66dd65f28b12579146b6831bf5276dc1118783c03daa9801fa0c130c/68747470733a2f2f696d672e736869656c64732e696f2f686578706d2f6c2f706c75672e737667)](https://www.apache.org/licenses/LICENSE-2.0)

| Build | Status |
| --- | --- |
| Test coverage | [![codecov](https://camo.githubusercontent.com/0703214250bf7eec958e80bd074f02f80f56ef01b944a3b874b91770ed0de376/68747470733a2f2f636f6465636f762e696f2f67682f67617a65626f73696d2f677a2d73696d2f747265652f6d61696e2f67726170682f62616467652e737667)](https://codecov.io/gh/gazebosim/gz-sim/tree/main) |
| Ubuntu Noble | [![Build Status](https://camo.githubusercontent.com/1438e03fc9f48e3168fd52aab9d99fe13fbee0654ffcc59694fd82e9269c42f3/68747470733a2f2f6275696c642e6f7372666f756e646174696f6e2e6f72672f6275696c645374617475732f69636f6e3f6a6f623d677a5f73696d2d63692d6d61696e2d6e6f626c652d616d643634)](https://build.osrfoundation.org/job/gz_sim-ci-main-noble-amd64) |
| Homebrew | [![Build Status](https://camo.githubusercontent.com/dfdad435599b62e790760817ae2388195cc8693b17d066445443ec77f5bff374/68747470733a2f2f6275696c642e6f7372666f756e646174696f6e2e6f72672f6275696c645374617475732f69636f6e3f6a6f623d677a5f73696d2d63692d6d61696e2d686f6d65627265772d616d643634)](https://build.osrfoundation.org/job/gz_sim-ci-main-homebrew-amd64) |
| Windows | [![Build Status](https://camo.githubusercontent.com/6105c6bd087adeff4ae4a12f2095b3025b5882bf772256b8613d37937af3558b/68747470733a2f2f6275696c642e6f7372666f756e646174696f6e2e6f72672f6275696c645374617475732f69636f6e3f6a6f623d677a5f73696d2d6d61696e2d636e6c77696e)](https://build.osrfoundation.org/job/gz_sim-main-cnlwin/) |

Gazebo Sim is an open source robotics simulator. Through Gazebo Sim, users have access to high fidelity physics, rendering, and sensor models. Additionally, users and developers have multiple points of entry to simulation including a graphical user interface, plugins, and asynchronous message passing and services.

Gazebo Sim is derived from [Gazebo Classic](http://classic.gazebosim.org/) and represents over 16 years of development and experience in robotics and simulation. This library is part of the [Gazebo](https://gazebosim.org/) project.

## Table of Contents

[Features](#features)

[Install](#install)

[Usage](#usage)

[Documentation](#documentation)

[Testing](#testing)

[Folder Structure](#folder-structure)

[Contributing](#contributing)

[Code of Conduct](#code-of-conduct)

[Versioning](#versioning)

[License](#license)

## Features

- **Dynamics simulation**: Access multiple high-performance physics engines through [Gazebo Physics](https://github.com/gazebosim/gz-physics).
- **Advanced 3D graphics**: Through [Gazebo Rendering](https://github.com/gazebosim/gz-rendering), it's possible to use rendering engines such as OGRE v2 for realistic rendering of environments with high-quality lighting, shadows, and textures.
- **Sensors and noise models**: Generate sensor data, optionally with noise, from laser range finders, 2D/3D cameras, Kinect style sensors, contact sensors, force-torque, IMU, GPS, and more, all powered by [Gazebo Sensors](https://github.com/gazebosim/gz-sensors)
- **Plugins**: Develop custom plugins for robot, sensor, and environment control.
- **Graphical interface**: Create, introspect and interact with your simulations through plugin-based graphical interfaces powered by [Gazebo GUI](https://github.com/gazebosim/gz-gui).
- **Simulation models**: Access numerous robots including PR2, Pioneer2 DX, iRobot Create, and TurtleBot, and construct environments using other physically accurate models available through [Gazebo Fuel](https://app.gazebosim.org/fuel). You can also build a new model using [SDF](http://sdformat.org/).
- **TCP/IP Transport**: Run simulation on remote servers and interface to Gazebo Sim through socket-based message passing using [Gazebo Transport](https://github.com/gazebosim/gz-transport).
- **Command line tools**: Extensive command line tools for increased simulation introspection and control.

## Install

For installing Gazebo, see the [getting started guide](https://gazebosim.org/docs/latest/getstarted/). If you want to use `libgz-sim` as a library, see the [installation tutorial](https://gazebosim.org/api/sim/9/install.html)

## Usage

Gazebo Sim can be run from the command line, once [installed](#install), using:

```
gz sim
```

For help, and command line options use:

```
gz sim -h
```

## Known issue of command line tools

In the event that the installation is a mix of Debian and from source, command line tools from `gz-tools` may not work correctly.

A workaround is to define the environment variable `GZ_CONFIG_PATH` to point to the different locations of the Gazebo libraries installations, where the YAML files for the packages are found, such as

```
export GZ_CONFIG_PATH=/usr/local/share/gz:$HOME/ws/install/share/gz
```

where `$HOME/ws` is an example colcon workspace used to build Gazebo.

On Windows, `gz sim` (i.e. running both server and GUI in one command) doesn't yet work. To run Gazebo Sim on Windows, you need to run the server in one terminal (`gz sim -s <other args>`) and the GUI in another terminal (`gz sim -g <other args>`). Remember this when reading through all Gazebo Sim tutorials. Also remember that Conda and `install\setup.bat` need to be sourced in both terminals (as well as any changes to `GZ_PARTITION` and other environment variables).

## Documentation

See the [installation tutorial](https://gazebosim.org/api/sim/9/install.html).

## Testing

See the [installation tutorial](https://gazebosim.org/api/sim/9/install.html).

See the [Writing Tests section of the contributor guide](https://gazebosim.org/docs/all/contributing/#writing-tests) for help creating or modifying tests.

## Folder Structure

Refer to the following table for information about important directories and files in this repository.

```
gz-sim
├── examples                     Various examples that can be run against binary or source installs of gz-sim.
│   ├── plugin                   Example plugins.
│   ├── standalone               Example standalone programs that use gz-sim as a library.
│   └── worlds                   Example SDF world files.
├── include/gz/sim               Header files that downstream users are expected to use.
│   └── detail                   Header files that are not intended for downstream use, mainly template implementations.
├── python                       Python wrappers
├── src                          Source files and unit tests.
│   ├── gui                      Graphical interface source code.
│   └── systems                  System source code.
├── test
│   ├── integration              Integration tests.
│   ├── performance              Performance tests.
│   ├── plugins                  Plugins used in tests.
│   ├── regression               Regression tests.
├── tutorials                    Tutorials, written in markdown.
├── Changelog.md                 Changelog.
├── CMakeLists.txt               CMake build script.
├── Migration.md                 Migration guide.
└── README.md                    This readme.
```

## Contributing

Please see the [contribution guide](https://gazebosim.org/docs/all/contributing/).

## Code of Conduct

Please see [CODE\_OF\_CONDUCT.md](https://github.com/gazebosim/gz-sim/blob/main/CODE_OF_CONDUCT.md).

## Versioning

This library uses [Semantic Versioning](https://semver.org/). Additionally, this library is part of the [Gazebo project](https://gazebosim.org/) which periodically releases a versioned set of compatible and complimentary libraries. See the [Gazebo website](https://gazebosim.org/) for version and release information.
