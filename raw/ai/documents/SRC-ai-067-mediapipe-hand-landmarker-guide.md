---
source_id: "SRC-ai-067"
title: "MediaPipe Hand Landmarker guide"
source_type: "product_documentation"
publisher: "Google AI Edge"
source_date: "2026-05-28"
url: "https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:10:12+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-ai-067
---
# MediaPipe Hand Landmarker guide

![A hand holding an egg. The shape of the hand is marked with a wireframe that
indicates the identified
structure](https://developers.google.com/static/mediapipe/images/solutions/examples/hand_landmark.png)

The MediaPipe Hand Landmarker task lets you detect the landmarks of the hands in an image. You can use this task to locate key points of hands and render visual effects on them. This task operates on image data with a machine learning (ML) model as static data or a continuous stream and outputs hand landmarks in image coordinates, hand landmarks in world coordinates and handedness(left/right hand) of multiple detected hands.

[Try it!](https://google-ai-edge.github.io/mediapipe-samples-web/#/vision/hand_landmarker)

## Get Started

Start using this task by following one of these implementation guides for your target platform. These platform-specific guides walk you through a basic implementation of this task, including a recommended model, and code example with recommended configuration options:

- **Android** - [Code example](https://github.com/google-ai-edge/mediapipe-samples/tree/main/examples/hand_landmarker/android)
	- [Guide](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/android)
- **Python** - [Code example](https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/hand_landmarker/python/hand_landmarker.ipynb)
	- [Guide](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/python)
- **Web** - [Code example](https://github.com/google-ai-edge/mediapipe-samples-web/blob/main/src/tasks/hand-landmarker.ts) - [Guide](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/web_js)

## Task details

This section describes the capabilities, inputs, outputs, and configuration options of this task.

### Features

- **Input image processing** - Processing includes image rotation, resizing, normalization, and color space conversion.
- **Score threshold** - Filter results based on prediction scores.

| Task inputs | Task outputs |
| --- | --- |
| The Hand Landmarker accepts an input of one of the following data types:   - Still images - Decoded video frames - Live video feed | The Hand Landmarker outputs the following results:   - Handedness of detected hands - Landmarks of detected hands in image coordinates - Landmarks of detected hands in world coordinates |

### Configurations options

This task has the following configuration options:

| Option Name | Description | Value Range | Default Value |
| --- | --- | --- | --- |
| `running_mode` | Sets the running mode for the task. There are three modes:      IMAGE: The mode for single image inputs.      VIDEO: The mode for decoded frames of a video.      LIVE\_STREAM: The mode for a livestream of input data, such as from a camera. In this mode, resultListener must be called to set up a listener to receive results asynchronously. | { `IMAGE, VIDEO, LIVE_STREAM` } | `IMAGE` |
| `num_hands` | The maximum number of hands detected by the Hand landmark detector. | `Any integer > 0` | `1` |
| `min_hand_detection_confidence` | The minimum confidence score for the hand detection to be considered successful in palm detection model. | `0.0 - 1.0` | `0.5` |
| `min_hand_presence_confidence` | The minimum confidence score for the hand presence score in the hand landmark detection model. In Video mode and Live stream mode, if the hand presence confidence score from the hand landmark model is below this threshold, Hand Landmarker triggers the palm detection model. Otherwise, a lightweight hand tracking algorithm determines the location of the hand(s) for subsequent landmark detections. | `0.0 - 1.0` | `0.5` |
| `min_tracking_confidence` | The minimum confidence score for the hand tracking to be considered successful. This is the bounding box IoU threshold between hands in the current frame and the last frame. In Video mode and Stream mode of Hand Landmarker, if the tracking fails, Hand Landmarker triggers hand detection. Otherwise, it skips the hand detection. | `0.0 - 1.0` | `0.5` |
| `result_callback` | Sets the result listener to receive the detection results asynchronously when the hand landmarker is in live stream mode. Only applicable when running mode is set to `LIVE_STREAM` | N/A | N/A |

## Models

The Hand Landmarker uses a model bundle with two packaged models: a palm detection model and a hand landmarks detection model. You need a model bundle that contains both these models to run this task.

| Model name | Input shape | Quantization type | Model Card | Versions |
| --- | --- | --- | --- | --- |
| [HandLandmarker (full)](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task) | 192 x 192, 224 x 224 | float 16 | [info](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20Hand%20Tracking%20\(Lite_Full\)%20with%20Fairness%20Oct%202021.pdf) | [Latest](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task) |

The hand landmark model bundle detects the keypoint localization of 21 hand-knuckle coordinates within the detected hand regions. The model was trained on approximately 30K real-world images, as well as several rendered synthetic hand models imposed over various backgrounds.

![](https://developers.google.com/static/mediapipe/images/solutions/hand-landmarks.png)

The hand landmarker model bundle contains a palm detection model and a hand landmarks detection model. The Palm detection model locates hands within the input image, and the hand landmarks detection model identifies specific hand landmarks on the cropped hand image defined by the palm detection model.

Since running the palm detection model is time consuming, when in video or live stream running mode, Hand Landmarker uses the bounding box defined by the hand landmarks model in one frame to localize the region of hands for subsequent frames. Hand Landmarker only re-triggers the palm detection model if the hand landmarks model no longer identifies the presence of hands or fails to track the hands within the frame. This reduces the number of times Hand Landmarker tiggers the palm detection model.

## Task benchmarks

Here's the task benchmarks for the whole pipeline based on the above pre-trained models. The latency result is the average latency on Pixel 6 using CPU / GPU.

| Model Name | CPU Latency | GPU Latency |
| --- | --- | --- |
| HandLandmarker (full) | 17.12ms | 12.27ms |
