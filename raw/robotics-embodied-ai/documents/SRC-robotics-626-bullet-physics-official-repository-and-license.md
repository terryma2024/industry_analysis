---
source_id: "SRC-robotics-626"
title: "Bullet Physics official repository and license"
source_type: "repository"
publisher: "Bullet Physics"
source_date: "待验证"
url: "https://github.com/bulletphysics/bullet3"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/repository
  - evidence/s
aliases:
  - SRC-robotics-626
---
# Bullet Physics official repository and license

[![Travis Build Status](https://camo.githubusercontent.com/733e844e928bf7ac4ce394a4f7fcb2f2bb97b74f50570fb5c77ef294d20653dd/68747470733a2f2f6170692e7472617669732d63692e6f72672f62756c6c6574706879736963732f62756c6c6574332e706e673f6272616e63683d6d6173746572)](https://travis-ci.org/bulletphysics/bullet3) [![Appveyor Build status](https://camo.githubusercontent.com/cdd68081267ce4c14ac6d6f5426cba0ae98a08ea2376a9987a6c318f52746827/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f36736c79397578616a72367873737471)](https://ci.appveyor.com/project/erwincoumans/bullet3)

## Bullet Physics SDK

This is the official C++ source code repository of the Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc.

[![PyBullet](https://camo.githubusercontent.com/837d0d87cff7e21664178a8e2e3aacdbeb832f03e36fdbfe2928eee00b0057f2/68747470733a2f2f707962756c6c65742e6f72672f776f726470726573732f77702d636f6e74656e742f75706c6f6164732f323031392f30332f63726f707065642d707962756c6c65742e706e67)](https://camo.githubusercontent.com/837d0d87cff7e21664178a8e2e3aacdbeb832f03e36fdbfe2928eee00b0057f2/68747470733a2f2f707962756c6c65742e6f72672f776f726470726573732f77702d636f6e74656e742f75706c6f6164732f323031392f30332f63726f707065642d707962756c6c65742e706e67)

## Issues

The Issue tracker was flooded with support questions and is closed until it is cleaned up. Use the [PyBullet forums](https://bulletphysics.github.io/) to read the historic discussion forums.

## PyBullet

It is highly recommended to use PyBullet Python bindings for improved support for robotics, reinforcement learning and VR. Use pip install pybullet and checkout the [PyBullet Quickstart Guide](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3).

Installation is simple:

```
pip3 install pybullet --upgrade --user
python3 -m pybullet_envs.examples.enjoy_TF_AntBulletEnv_v0_2017may
python3 -m pybullet_envs.examples.enjoy_TF_HumanoidFlagrunHarderBulletEnv_v1_2017jul
python3 -m pybullet_envs.deep_mimic.testrl --arg_file run_humanoid3d_backflip_args.txt
```

If you use PyBullet in your research, please cite it like this:

```
@MISC{coumans2021,
author =   {Erwin Coumans and Yunfei Bai},
title =    {PyBullet, a Python module for physics simulation for games, robotics and machine learning},
howpublished = {\url{http://pybullet.org}},
year = {2016--2021}
}
```

## Requirements for Bullet Physics C++

A C++ compiler for C++ 2003. The library is tested on Windows, Linux, Mac OSX, iOS, Android, but should likely work on any platform with C++ compiler. Some optional demos require OpenGL 2 or OpenGL 3, there are some non-graphical demos and unit tests too.

## Contributors and Coding Style information

[https://docs.google.com/document/d/1u9vyzPtrVoVhYqQOGNWUgjRbfwfCdIts\_NzmvgiJ144/edit](https://docs.google.com/document/d/1u9vyzPtrVoVhYqQOGNWUgjRbfwfCdIts_NzmvgiJ144/edit)

## Requirements for experimental OpenCL GPGPU support

The entire collision detection and rigid body dynamics can be executed on the GPU.

A high-end desktop GPU, such as an AMD Radeon 7970 or NVIDIA GTX 680 or better. We succesfully tested the software under Windows, Linux and Mac OSX. The software currently doesn't work on OpenCL CPU devices. It might run on a laptop GPU but performance will not likely be very good. Note that often an OpenCL drivers fails to compile a kernel. Some unit tests exist to track down the issue, but more work is required to cover all OpenCL kernels.

## License

All source code files are licensed under the permissive zlib license ([http://opensource.org/licenses/Zlib](http://opensource.org/licenses/Zlib)) unless marked differently in a particular folder/file.

## Build instructions for Bullet using vcpkg

You can download and install Bullet using the [vcpkg](https://github.com/Microsoft/vcpkg/) dependency manager:

```
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
./vcpkg integrate install
./vcpkg install bullet3
```

The Bullet port in vcpkg is kept up to date by Microsoft team members and community contributors. If the version is out of date, please [create an issue or pull request](https://github.com/Microsoft/vcpkg) on the vcpkg repository.

## Build instructions for Bullet using premake. You can also use cmake instead.

**Windows**

Click on build\_visual\_studio\_vr\_pybullet\_double.bat and open build3/vs2010/0\_Bullet3Solution.sln When asked, convert the projects to a newer version of Visual Studio. If you installed Python in the C:\\ root directory, the batch file should find it automatically. Otherwise, edit this batch file to choose where Python include/lib directories are located.

**Windows Virtual Reality sandbox for HTC Vive and Oculus Rift**

Build and run the App\_SharedMemoryPhysics\_VR project, preferably in Release/optimized build. You can connect from Python pybullet to the sandbox using:

```
import pybullet as p
p.connect(p.SHARED_MEMORY) #or (p.TCP, "localhost", 6667) or (p.UDP, "192.168.86.10",1234)
```

**Linux and Mac OSX gnu make**

Make sure gcc and cmake is installed (`sudo apt-get install build-essential` and `sudo apt-get install cmake` for Linux, `brew install cmake` for Mac, or [https://cmake.org](https://cmake.org/))

In a terminal type:

```
./build_cmake_pybullet_double.sh
```

This script will invoke cmake and build in the build\_cmake directory. You can find pybullet in Bullet/examples/pybullet. The BulletExampleBrowser binary will be in Bullet/examples/ExampleBrowser.

You can also build Bullet using premake. There are premake executables in the build3 folder. Depending on your system (Linux 32bit, 64bit or Mac OSX) use one of the following lines Using premake:

```
cd build3
./premake4_linux --double gmake
./premake4_linux64 --double gmake
./premake4_osx --double --enable_pybullet gmake
```

Then

```
cd gmake
make
```

Note that on Linux, you need to use cmake to build pybullet, since the compiler has issues of mixing shared and static libraries.

**Mac OSX Xcode**

Click on build3/xcode4.command or in a terminal window execute

```
./premake_osx xcode4
```

## Usage

The App\_ExampleBrowser executables will be located in the bin folder. You can just run it though a terminal/command prompt, or by clicking it.

```
[--start_demo_name="Demo Name"]     Start with a selected demo  
[--mp4=moviename.mp4]               Create a mp4 movie of the window, requires ffmpeg installed
[--mouse_move_multiplier=0.400000]  Set the mouse move sensitivity
[--mouse_wheel_multiplier=0.01]     Set the mouse wheel sensitivity
[--background_color_red= 0.9]       Set the red component for background color. Same for green and blue
[--fixed_timestep= 0.0]             Use either a real-time delta time (0.0) or a fixed step size (0.016666)
```

You can use mouse picking to grab objects. When holding the ALT or CONTROL key, you have Maya style camera mouse controls. Press F1 to create a series of screenshots. Hit ESCAPE to exit the demo app.

Check out the docs folder and the Bullet physics forums for further information.
