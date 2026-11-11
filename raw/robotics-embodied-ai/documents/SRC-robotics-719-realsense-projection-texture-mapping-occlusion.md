---
source_id: "SRC-robotics-719"
title: "RealSense projection texture mapping occlusion"
source_type: "documentation"
publisher: "RealSense"
source_date: "2026-11-10"
url: "https://dev.realsenseai.com/docs/projection-texture-mapping-and-occlusion-with-intel-realsense-depth-cameras/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T02:33:26+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-719
---
# RealSense projection texture mapping occlusion

> 📘 This article is also available in [PDF format](https://dev.realsenseai.com/download/12849/)

## 1\. Introduction

In order to understand its 3D environment, RealSense™ Depth Cameras combine information from multiple internal sensors. This paper offers an illustrated guide of the underlying multi-view geometry, including key concepts, algorithms and challenges. We will discuss camera intrinsic and extrinsic calibration parameters, the process of texture-mapping and stream alignment, challenges posed by occlusions and how they can be addressed efficiently using CPU and GPU computational resources.

## 2\. Single Sensor

## 2.1 Camera and World Coordinates

There are two common coordinate systems used with a single camera – camera pixel coordinates and world coordinates. Each video stream is specified in pixels, with coordinates (0,0) referring to the center of the top left pixel in the image, and (w-1,h-1) to the center of the bottom right. From the perspective of the camera, the x-axis points to the right and the y-axis points down. Objects in 3D space are represented in meters, with the coordinate (0,0,0) referring to the center of the physical sensor \[1\]. Within this space, the positive x-axis points to the right, the positive y-axis points down, and the positive z-axis points forward.

Figure 1. Camera Pixel Coordinates on the left vs World Coordinates on the right.

## 2.2 Projection to Camera Coordinates

| Parameter | Description |
| --- | --- |
| *(w,h)* | Width and height of video stream in pixels |
| *P=(p <sub>x</sub>,p <sub>y</sub>)* | Principal Point, as a pixel offset from the left edge |
| *F=(f <sub>x</sub>,f <sub>y</sub>)* | Focal Length in multiple of pixel size |
| *Model* | Lens Distortion Model |
| *Coeffs=(k <sub>1</sub>,k <sub>2</sub>,k <sub>3</sub>,k <sub>4</sub>,k <sub>5</sub>)* | Lens Distortion Coefficients |

*Table 1. Camera Intrinsic Calibration Parameters.*

Projection of point (x,y,z) is defined as:

![](https://dev.realsenseai.com/wp-content/uploads/2026/02/6b2285b-eq1-1.png)

Where D\_Model: R^2→R^2 is the lens distortion function (Appendix 1)

Horizontal and Vertical Field-of-View of the camera define the limits of camera’s view frustum (Figure 2).  
These parameters can be derived from Focal Length and Principle Point parameters:

![](https://dev.realsenseai.com/wp-content/uploads/2026/02/93ea76c-eq2-1.png)

Ratio of Field-of-View to Max Resolution define Pixel Density. Increasing Field-of-View allows the camera to see more of its surroundings, but it also means that each image pixel is stretched over larger physical area.

Projection point can be calculated using [rs2\_project\_point\_to\_pixel](https://github.com/IntelRealSense/librealsense/blob/master/include/librealsense2/rsutil.h#L19) method. Camera Field-of-View can be calculated using rs2\_fov method. The intrinsic parameters can be obtained through [get\_intrinsics](https://github.com/IntelRealSense/librealsense/wiki/API-How-To#get-video-stream-intrinsics) API:

```
rs2::pipeline pipe;
rs2::pipeline_profile selection = pipe.start();
auto depth_stream = selection.get_stream(RS2_STREAM_DEPTH)
 .as<rs2::video_stream_profile>();
auto resolution = std::make_pair(depth_stream.width(), depth_stream.height());
auto i = depth_stream.get_intrinsics();
auto principal_point = std::make_pair(i.ppx, i.ppy);
auto focal_length = std::make_pair(i.fx, i.fy);
rs2_distortion model = i.model;
```
```
import pyrealsense2 as rs2
pipe = rs2.pipeline()
selection = pipe.start()
depth_stream = selection.get_stream(rs2.stream.depth).as_video_stream_profile()
resolution = (depth_stream.width(), depth_stream.height())
i = depth_stream.get_intrinsics()
principal_point = (i.ppx, i.ppy)
focal_length = (i.fx, i.fy)
model = i.model
```

The core process of projection can be explained geometrically by building a line segment connecting 3D point to sensor origin, and checking for intersection with the camera plane:

![{866}](https://files.readme.io/a8362b7-fig2.png)

Figure 2. Projection to camera coordinates and the view frustum

Lens distortion model is applied to the result in order to account for lens non-linear geometry. Different lenses have different types of distortion and these are estimated during production-line calibration.

![{1299}](https://files.readme.io/381ac58-fig3.png)

Figure 3. Effects of distortion. Left to right:\\ No distortion, Positive Radial Distortion, Extreme Distortion with a wide-FOV lens

For RealSense D400 Series cameras, distortion and other related calibration parameters for unrectified frames can be queried through Calibration API. The rectified left/right and depth frames have no distortion parameters since those are processed images and hardware undistorts images during the rectification process.

On models with RGB sensor, for example, RealSense D435 and D415 cameras, RGB also do not have distortion parameters since the small distortion was determined to have insignificant performance impact and excluded in the calibration process. On models with larger RGB distortion, distortion parameters will be available.

## 2.3 De-projection to World Coordinates

The process of projecting 3D point to pixel is not reversible. Given single pixel we can cast a ray from camera through that pixel, but it is not sufficient to reconstruct original 3D coordinates:

![{581}](https://files.readme.io/465546b-fig4.png)

Figure 4. Ray-casting away from the camera

We can, however, complete this process if we know the depth of the pixel or its distance from the camera. These two concepts are related but are not the same. Distance of point (x,y,z) is defined as √(x^2+y^2+z^2 ) while its Depth is simply the Z-component. While these two representations are equivalent, depth maps are easier to work with and RealSense Depth Cameras provide depth and not distance information.

![{778}](https://files.readme.io/df0236a-fig5.png)

Figure 5. Distance map (left) vs Depth map (right)

Given depth pixel we can reconstruct the original point in world coordinates using the following formula:

![](https://dev.realsenseai.com/wp-content/uploads/2026/02/0296ef0-eq3-1.png)

Where U <sub>Model</sub>:R <sup>2</sup> →R <sup>2</sup> is the undo lens distortion function.

This process will only reconstruct points visible from the camera. The resulting matrix of 3D coordinates is referred to as Point-Cloud in the SDK. Point-cloud class is designed to convert entire depth frame into point-cloud. This class is optimized differently for different platforms, but the resulting vertices should be equivalent to calling de-project on every depth pixel. Reconstructing object from 360 degrees would require multiple depth images and a process of point-cloud stitching (Reference 4).

## 3\. Multi Sensor

## 3.1 Extrinsic Calibration Parameters

It is relatively rare to get both color and depth information from the same physical sensor. Having multiple sensors in a single device complicates projection process slightly. In addition to having different intrinsic calibration parameters, sensors are mounted at different positions and orientations relative to each other. Between every pair of sensors, Extrinsic calibration parameters are defined as the translation vector t and rotation matrix R connecting the two viewports

![{711}](https://files.readme.io/4c94c33-fig6.png)

Figure 6. Translation and rotation components of extrinsic calibration between two sensors

Moving between world coordinates with respect to sensor A to world coordinates with respect to sensor B is done via matrix multiplication:

![](https://dev.realsenseai.com/wp-content/uploads/2026/02/63531a8-eq4-1.png)

This is accomplished using [rs2\_transform\_point\_to\_point](https://github.com/IntelRealSense/librealsense/blob/master/include/librealsense2/rsutil.h#L126) method.

Every RealSense Depth Camera contain multiple sensors, each with its individual viewport defined by both intrinsic and extrinsic calibration parameters (Figure 8). When using stereo depth and infrared stream with Z16 and Y8 formats respectively, D4 ASIC is generating synthetic views for the left and right infrared sensors, as if they were perfectly aligned. Querying extrinsic calibration parameters between left and right infrared streams will return R=Id and t=(b,0,0) where b is the distance between the left and the right infrared sensors, also referred to as Stereo Baseline. The L515 ASIC is doing something similar – there are no physical lenses inside the L515 camera, but rather single rectified view is being simulated by the ASIC based on responses from the LiDAR receiver.

![{1078}](https://files.readme.io/8549926-fig7.png)

Figure 7. Unrectified (left) and rectified (right) camera views

## 3.2 Texture-Mapping

Using the de-projection method, we are able to generate point-cloud from depth image. The process of assigning RGB value from the color sensor to each point in the point-cloud is called Texture-Mapping.  
Simply copying RGB value from same pixel in the color image will not work – the color image may be of a different resolution, may have different intrinsic calibration parameters and offset as a result of extrinsic calibration parameters between the two streams.

![{885}](https://files.readme.io/ab39e31-fig9.png)

Figure 9. View from the color camera (left), view from the depth sensor (right), color and depth frames overlaid on top of each other (middle)

Texture-mapping process is performed using the following steps:

![{525}](https://files.readme.io/e4da963-99a.png)

Step 1. De-project depth pixel to 3D point

![{750}](https://files.readme.io/71b1ebf-99b.png)

Step 2. Apply camera extrinsic matrix\\ (note that color sensor is becoming the new origin)

![{730}](https://files.readme.io/6644cff-99c.png)

Step 3. Project point to color camera coordinates

![{495}](https://files.readme.io/7ff2ab2-99d.png)

Step 4. Using camera coordinates query color value for every point (Note that not all points receive color because some are outside the field-of-view of the color sensor)

## 3.3 The uv-map

A notable side-product of the texture-mapping process is what’s called a uv-map. The uv-map is generated if we stop the process at step 3 (project to color) and just keep normalized pixel coordinates, instead of fetching the actual pixel value. It is the second output from SDK Pointcloud class, stored inside rs2::points alongside the vertices.

![{600}](https://files.readme.io/49e192a-fig10.png)

Figure 10. uv-map generated during texture mapping process

By itself, the uv-map is not very useful, but it will come handy later when dealing with alignment and occlusion.

## 3.4 Stream Alignment

In addition to having points in world space, it is useful to be able to generate synthetic views of how one stream would look like if it was captured from point of view of another stream.

![{1004}](https://files.readme.io/4dfb41e-fig11.png)

Figure 11. Color image aligned to Depth camera coordinates (left) Depth frame aligned to Color camera coordinates (right)

To calculate Color-Aligned-to-Depth all you need is to apply the uv-Map – instead of assigning fetched RGB value to the 3D point, assign it to original pixel coordinates (i, j).

```
Align Color to Depth:
Calculate uv map
foreach pixel (i,j)  in depth frame:
 (k,l)=uv map(i,j)
 result(i,j)=color frame(k,l)
return result
```

Generating Depth-Aligned-to-Color is a bit trickier. Given pixel (i, j) inside the color image, there is no (easy) way to de-project it back to 3D space (Section 2.3). Instead, we can map all depth pixels to color coordinates. While doing so, it is important to always take the depth value closest to the camera, since more than one depth pixels may fall on the same color pixel.

```
Align Depth to Color:
Calculate uv map
result=zero(color frame size)
foreach pixel (i,j)  in depth frame:
 (k,l)=uv map(i,j)
 result(k,l)=min⁡(result(k,l),depth frame(i,j))
 return result
```

Finally, if the color sensor has higher pixel density than the depth sensor, some color pixels will remain blank, creating holes in the output image. To combat this, instead of copying single pixel at a time, each depth pixel is extended to a 2×2 patch.

## 4\. Occlusion Invalidation

## 4.1 Problem Statement

Let’s consider the following synthetic scene:

![{1196}](https://files.readme.io/011a602-fig12.png)

Figure 12. Setup for Occlusion demo – view from the color camera (left), depth-map (right)

If we apply Color-to-Depth Alignment or perform texture-mapping to Point-Cloud, you may notice a visible artifact in both outputs – part of the cone is projected to the cube and part of the cube was projected to the wall behind it.

![{1352}](https://files.readme.io/4faf963-fig13.png)

Figure 13. Point-cloud with texture (left), Color aligned to Depth (right)

Given this is an artificial setup, we know that intrinsic and extrinsic calibration is perfect, so it must be something else. In context of depth-cameras this effect is referred to as occlusion.

## 4.2 Understanding Occlusion

Let’s pick a single green pixel on the cube and troubleshoot step by step how it came to be. We start by de-projecting depth pixel to world coordinates; we move our origin to the position of the color camera (by applying extrinsic transform) and project the resulting point back to color camera coordinates.

![{1484}](https://files.readme.io/6829a54-fig14.png)

Figure 14. De-projecting pixel to point (left), re-projecting point to pixel with color as the origin (right)

When projecting back to the color camera, line segment from the 3D point to camera origin happens to intersect the scene second time, passing through the green cone. Since cone intersection was closer to the camera along this camera ray, its color was captured inside the color pixel. Another way to phrase it, is that color camera never had information about the color of this specific pixel, since it was occluded (by the cone) in color camera view.

![{949}](https://files.readme.io/154271e-fig15.png)

Figure 15. Occlusion recap – point on the cube is occluded from view in the color image

## 4.3 Occlusion Invalidation

While color information behind the cone is missing and cannot be reliably reconstructed from this data alone, it would be better to get no texture on the affected pixels instead of wrong texture.

This problem can be solved in general case by using additional projection and de-projection operations. However, for the special case of RealSense Depth Cameras the SDK is using significantly more efficient algorithm. To understand it, we will need to look closer at the uv-Map. We will separate the map into u(x,y) and v(y,y) components:

![{1225}](https://files.readme.io/b2f7a58-fig16.png)

Figure 16. Separated u and v components of a uv-Map

Let’s take a cross-section of u(x,y) at y=h/2 and plot the results. Within the bounds of shared field-of-view the graph is mostly monotonically increasing, except for couple of spots:

![{1013}](https://files.readme.io/f1ee012-fig17.png)

Figure 17. Cross-section of u(x,y) at y=h/2

If we overlay generated color-aligned-to-depth image on top of it, we see that occlusion area seem to begin exactly when u(x) graph decreases and disappears only when the graph recovers to its previous value.

![{1013}](https://files.readme.io/556f3a3-fig18.png)

Figure 18. Relation between occlusion and uv-Map

Intuitively, this makes sense – u(x) should be monotonically increasing. If more than one value of x corresponds to a certain u, this means same color pixel would be mapped to more than one depth pixels, resulting in a similar duplication artifact.

However, would this always work? Yes and no. The reason we are seeing only horizontal occlusion with RealSense D400 product-line is because in these cameras depth and color sensors are mounted horizontally next to each other. In the RealSense LiDAR Camera L515, for instance, you would see vertical occlusion since its color camera is mounted on top of the lidar receiver. In this case, we would have to look at v(y) function and not u(x).

| Invalidate Occlusion | Comments |
| --- | --- |
| *(R,t)=extrinsic between depth and color sensors* |  |
| *if t.x>t.y:* | Sensors are mounted horizontally? |
| *foreach y,foreach x:* | Scan depth frame horizontally |
| *a=uv map(x,y).u* |  |
| *for i=1..K:* |  |
| *b=uv map(x-i,y).u* |  |
| *if b>a:* |  |
| *uv map(x,y)=0* | Invalidate output pixel |
| *points(x,y)=0* |  |
| *else:* |  |
| *same,swap x↔y,u↔v* | Assume sensors are mounted vertically |

In theory max occlusion size can be unlimited but since we are dealing with limited resolution and range search window of 20 is sufficient.

RealSense SDK 2.35+ is automatically handling occlusion invalidation as part of point-cloud calculation. We provide open-source and reasonably optimized CPU and GPU versions of the algorithm:

• CPU implementation – [github.com/IntelRealSense/librealsense/blob/master/src/proc/occlusion-filter.cpp](https://github.com/IntelRealSense/librealsense/blob/master/src/proc/occlusion-filter.cpp#L66-L174)  
• GPU implementation – [github.com/IntelRealSense/librealsense/blob/master/src/gl/pointcloud-gl.cpp](https://github.com/IntelRealSense/librealsense/blob/master/src/gl/pointcloud-gl.cpp#L105-L204)

![{1344}](https://files.readme.io/f414055-fig19.png)

Figure 19. Occlusion Invalidation inside RealSense™ Viewer with L515 Lidar Camera\\ Left: Raw Point-cloud; Right: Point-cloud with occlusion invalidation enabled

## 5\. References

1. For D400 depth sensor, camera origin is not the center of physical sensor, but somewhere in between the front of the lens and the sensor. See D400 datasheet, section 4.8 Depth Start Point (Ground Zero Reference), reference 1. Similarly, L515 depth origin is inside the device, 4.5mm from the front glass. RealSense™ Product Family D400 Series Datasheet: [/docs/intel-realsense-d400-series-product-family-datasheet](https://dev.realsenseai.com/docs/intel-realsense-d400-series-product-family-datasheet)
2. Projection in RealSense SDK 2.0: [https://github.com/IntelRealSense/librealsense/wiki/Projection-in-RealSense-SDK-2.0](https://github.com/IntelRealSense/librealsense/wiki/Projection-in-RealSense-SDK-2.0)
3. Camera Calibration in OpenCV: [https://docs.opencv.org/2.4/modules/calib3d/doc/camera\_calibration\_and\_3d\_reconstruction.html](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html)
4. Multicamera stitching with ROS: [https://www.realsenseai.com/how-to-multiple-camera-setup-with-ros/](https://www.realsenseai.com/how-to-multiple-camera-setup-with-ros/)
5. Calibration Tools API: [https://downloadcenter.intel.com/download/29618/Intel-RealSense-D400-Series-Dynamic-Calibration-Tool](https://downloadcenter.intel.com/download/29618/Intel-RealSense-D400-Series-Dynamic-Calibration-Tool)

## 6\. Appendix 1 – Distortion Models

RealSense™ Depth Cameras are currently using the following distortion models:

| Model | Distortion Formula |
| --- | --- |
| None | D(x,y) = (x,y) |
| Brown Conrady | r = x <sup>2</sup> + y <sup>2</sup>   f = 1 + k <sub>1</sub> r + k <sub>2</sub> r <sup>2</sup> + k <sub>5</sub> r <sup>3</sup>   D(x,y) = (f·x + 2k <sub>3</sub> f <sup>2</sup> xy + k <sub>4</sub> (r + 2x <sup>2</sup> f <sup>2</sup>), f·y + 2k <sub>3</sub> f <sup>2</sup> xy + k <sub>4</sub> (r + 2y <sup>2</sup> f <sup>2</sup>)) |
| F-Theta | r = √(x <sup>2</sup> + y <sup>2</sup>)   d = (tan <sup>-1</sup> (2r·tan(k <sub>1</sub> /2))) / k <sub>1</sub>   D(x,y) = (d/r, d/r) |
| Kannala-Brandt | r = √(x <sup>2</sup> + y <sup>2</sup>)   θ = tan <sup>-1</sup> (r)   d = θ(1 + θ <sup>2</sup> (k <sub>1</sub> + θ <sup>2</sup> (k <sub>2</sub> + θ <sup>2</sup> (k <sub>3</sub> + θ <sup>2</sup> k <sub>4</sub>))))   D(x,y) = (d/r, d/r) |

*Table 2. Projection Distortion Models.*
