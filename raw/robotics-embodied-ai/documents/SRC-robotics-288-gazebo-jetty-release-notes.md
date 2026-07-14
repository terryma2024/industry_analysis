---
source_id: "SRC-robotics-288"
title: "Gazebo Jetty release notes"
source_type: "product_documentation"
publisher: "Open Robotics"
source_date: "2025-09"
url: "https://gazebosim.org/docs/latest/release_notes/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T03:30:40+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-288
---
# Gazebo Jetty release notes

## Release Notes

[![Gazebo Jetty Artwork](https://gazebosim.org/docs/latest/_images/jetty.png)](https://gazebosim.org/docs/latest/_images/jetty.png)

The Gazebo team is happy to announce the 10th major release of Gazebo, code named Jetty! Jetty is a long term support (LTS) release, meaning it has a longer support lifetime, May 2031 to be exact.

## Highlights

Here’s a brief summary of all the new features in Gazebo Jetty:

### A new Jetty Demo World

We created a realistic warehouse environment designed to highlight the latest Jetty features. This free, downloadable demo includes shelving and an autonomous forklift for loading and unloading. As an added bonus, it also features an [Open-RMF](https://www.open-rmf.org/) demonstration.

![jetty_demo_warehouse](https://gazebosim.org/docs/latest/_images/jetty_demo_warehouse.png)

![jetty_packing_station](https://gazebosim.org/docs/latest/_images/jetty_packing_station.png)

![jetty_loading_dock](https://gazebosim.org/docs/latest/_images/jetty_loading_dock.png)

![jetty_upstairs](https://gazebosim.org/docs/latest/_images/jetty_upstairs.png)

### Zenoh transport support, working towards improved ROS integration

Up until Ionic, Gazebo used ZeroMQ (0MQ) as its primary message transport protocol. Gazebo now supports [Zenoh](https://zenoh.io/) as an alternative transport implementation, offering improved discovery, interoperability, and performance. To enable Zenoh, set the environment variable `` `export GZ_TRANSPORT_IMPLEMENTATION=zenoh` ``. This allows Gazebo to leverage Zenoh’s features and potentially integrate more seamlessly with ROS 2 Jazzy and other systems utilizing Zenoh.

### New reinforcement learning demo code and tutorials

Based on community feedback we’ve added a full tutorial on performing reinforcement learning using Gazebo Jetty and the [Stable Baselines3 Python library](https://stable-baselines3.readthedocs.io/en/master/). These tutorials walk you through using reinforcement learning to build a controller for an inverted pole mounted on a robot cart. StableBaselines3 is just the beginning, and more advanced developers can use the tutorial as a starting point for integrating other reinforcement learning frameworks into Gazebo.

![../_images/rl.gif](https://gazebosim.org/docs/latest/_images/rl.gif)

Demo of a classic cartpole trained to balance itself #

### ROS Standard Sim Interface

Members of the ROS community have [built a standard simulation interface](https://github.com/ros-simulation/simulation_interfaces) to improve the portability of robot code between simulators. This new standard interface should allow ROS developers to quickly and easily switch between simulators based on their development needs.

![../_images/sim_ifaces.gif](https://gazebosim.org/docs/latest/_images/sim_ifaces.gif)

Simple demo showing conveyor belt based test setup using Simulation Interfaces #

### New occupancy grid export functionality

Occupancy grids are simple 2D maps that robots use for path planning. Open source navigation frameworks [like Nav2](https://docs.nav2.org/tutorials/docs/navigation2_with_slam.html) use these maps to guide robots safely to their destination. You can now easily export these occupancy grid maps from Gazebo using the `/scan_image` topic and running the following command:  
`gz topic -t /start_exploration -m gz.msgs.Boolean -p 'data: true'`

![../_images/occupancy.gif](https://gazebosim.org/docs/latest/_images/occupancy.gif)

New occupancy grid export functionality #

### New auto-inertia calculation makes adding objects easier

Previously, the `inertial/@auto` attribute in SDFormat required you to specify an object’s density to automatically compute its inertial properties. Now you can specify an object’s mass in SDFormat and Gazebo will automatically compute its density and inertial parameters!

![../_images/auto_inertia_mass.gif](https://gazebosim.org/docs/latest/_images/auto_inertia_mass.gif)

From left to right: drills using default, auto, manually computed inertias #

### A new and improved Qt6 interface!

Qt is the cross-platform GUI subsystem used by Gazebo and we recently upgraded to the latest version, Qt6. Qt version 5 went end of life on May 26th, 2025 forcing us to upgrade to version 6. This upgrade was no small feat, as it required updating hundreds of files across the Gazebo project. \_Gazebo plugin developers will need to update their Gazebo GUI plugins to QT6 to maintain compatibility. [We’ve created a Gazebo plugin QT migration guide to help developers update their plugins.](https://gazebosim.org/api/gui/10/migration_qt6.html)

![../_images/qt6.jpg](https://gazebosim.org/docs/latest/_images/qt6.jpg)

Things might look slightly different in Qt6 #

### Dynamically adjust wheel slip / friction

We’ve added a new LookupWheelSlip system to gz-sim that uses an 8bit RGB lookup map to dynamically change a materials friction parameters. This new feature allows users to map specific colors in a texture image to specific friction values. Want to add an oil slick to the floor of your simulation? Simply draw the oil patch on the texture image and set the desired friction value!

![../_images/wheelslip.gif](https://gazebosim.org/docs/latest/_images/wheelslip.gif)

Dynamically adjust wheel slip / friction #

### New Gazebo standalone executables

We’ve modified how the \`gz\` tool works to make debugging your application easier and to improve cross-platform support for Windows and MacOS. To do this we’ve moved away from the Ruby-based CLI loading libraries back to loading standalone applications.

### Refactored package names to remove major versions

Including major versions in package names was done to allow side-by-side installation of two different Gazebo versions. While helpful for some users, this approach caused major headaches for developers who had to regularly update these version numbers. We’ve ended the practice to make Gazebo simpler to maintain and easier to use for package developers.

### Bazel Module Migration

We have migrated `gz` packages from the legacy Bazel workspace-based setup to the new Bazel module system (Bzlmod). As part of this effort, key third-party dependencies including DARTSim, Bullet, FreeImage, Assimp and more were packaged and published to the Bazel Central Registry (BCR). All Jetty and Ionic versions of the libraries have been uploaded to BCR.

![../_images/bazel.gif](https://gazebosim.org/docs/latest/_images/bazel.gif)

Demo showing Bazel based client program using gz-transport #

## Contributors and Supporters

We’d like to give a special thanks to the community members who helped us make this Gazebo release happen by reviewing tutorials during our Jetty Test and Tutorial Party. The results from our [Jetty Test and Tutorial Party](https://discourse.openrobotics.org/t/gazebo-jetty-test-and-tutorial-party-instructions/49779) were quite impressive and we were so happy to see so many new contributors! Our tutorial party went incredibly well! We had 25 participants help us with testing the Jetty release which allowed us to:

- Close 388 Issues, **68% of our total issues**
	- Close **148** out of 148 Ubuntu tickets (**100%**)
		- Close **65** out of 83 MacOS tickets **(44%**)
		- Close **47** out of 147 Windows tickets (**32%**)
		- Close 128 out of 128 all platform tickets (**100%**)
- Create 74 PRs fixing the issues that were found!

Our top twenty contributors to the T&T Party are:

| **Place** | **User** | **Points** |
| --- | --- | --- |
| 1 | **akky20** | 719.2 |
| 2 | **Creator-1705** | 410.6 |
| 3 | **nikodemj9** | 310.0 |
| 4 | **saiaravind19** | 273.6 |
| 5 | **jmackay2** | 269.0 |
| 6 | **Physic69** | 234.0 |
| 7 | **srmainwaring** | 187.2 |
| 8 | **jasmeet0915** | 165.6 |
| 9 | **avanmalleghem** | 114.0 |
| 10 | **Narashima1808** | 111.0 |
| 11 | **AronLapp** | 100.0 |
| 12 | **matosinho** | 84.4 |
| 13 | **mukul2020** | 79.2 |
| 14 | **SuperGops7** | 76.0 |
| 15 | **pratik-adhikari** | 75.0 |
| 16 | **mohamedsayed18** | 66.0 |
| 17 | **shreya-ramesh** | 53.0 |
| 18 | **CursedRock17** | 45.0 |
| 19 | **s0um0r0y** | 40.0 |
| 20 | **chen-harrison** | 40.0 |

**We would also like to thank everyone that contributed to Jetty:**
