---
source_id: "SRC-ai-074"
title: "MediaPipe Android setup guide"
source_type: "product_documentation"
publisher: "Google AI Edge"
source_date: "2026-05-28"
url: "https://developers.google.com/edge/mediapipe/solutions/setup_android"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:10:12+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-ai-074
---
# MediaPipe Android setup guide

This page shows you how to set up your development environment to use MediaPipe Tasks in your Android applications.

## Supported devices and platforms

To create Android applications with MediaPipe Tasks, your development environment requires the following:

- [Android Studio](https://developer.android.com/studio/index.html) with a recommended version of at least 2021.1.1 (Bumblebee), or another compatible IDE.
- Android SDK version 24 or higher
- Android device with at least the minimum SDK version. An Android emulator may not work for all tasks.

## Developer environment setup

Before running a MediaPipe task on an Android application, you must either have an existing app or create a new Android Studio project on your local machine. MediaPipe fits into the [Data layer](https://developer.android.com/topic/architecture/data-layer) of your app, which contains the application data and business logic. For more information on Android app architecture, refer to [Guide to app architecture](https://developer.android.com/topic/architecture).

## Android device setup

You must enable Developer options and USB debugging on a physical Android device before using it to test your application. For instructions on configuring your device with Developer options, refer to [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options).

For tasks that do not require a device camera or microphone, you can use an Android device emulator instead of a physical Android device. For instructions on setting up an Android Emulator, refer to [Run apps on the Android Emulator](https://developer.android.com/studio/run/emulator).

## Example code setup

The [MediaPipe Examples](https://github.com/googlesamples/mediapipe/tree/main/examples) repository contains example Android applications for each MediaPipe task. You can create a project from the example code, build the project, and then run it.

To import and build the example code project:

1. Start [Android Studio](https://developer.android.com/studio).
2. From the Android Studio, select **File > New > Import Project**.
3. Navigate to the example code directory containing the `build.gradle` file and select that directory, for example: `.../mediapipe/examples/text_classification/android/build.gradle`
4. If Android Studio requests a Gradle Sync, choose **OK**.
5. Ensure that your Android device is connected to your computer and developer mode is enabled. Click the green `Run` arrow.

If you select the correct directory, Android Studio creates a new project and builds it. This process can take a few minutes, depending on the speed of your computer and if you have used Android Studio for other projects. When the build completes, the Android Studio displays a `BUILD SUCCESSFUL` message in the **Build Output** status panel.

To run the project:

1. From Android Studio, run the project by selecting **Run > Run…**.
2. Select an attached Android device (or emulator) to test the app.

## MediaPipe Tasks dependencies

MediaPipe Tasks provides three prebuilt libraries for vision, text, audio. The `.tflite` model file must be located in the assets directory of the Android module that uses the model. Depending on the MediaPipe Task used by the app, add the vision, text, or audio library to the list of dependencies within the `build.gradle` file.

### Generative AI tasks

The MediaPipe Tasks Generative AI libraries contain tasks that handle image or text generation. To import the MediaPipe Tasks Generative AI libraries in Android Studio, add the dependencies to your `build.gradle` file.

#### Image Generator

The MediaPipe Image Generator task is contained within the `tasks-vision-image-generator` library. Add the dependency to your `build.gradle` file:

```
dependencies {
    implementation 'com.google.mediapipe:tasks-vision-image-generator:latest.release'
}
```

#### LLM Inference API

The MediaPipe LLM Inference task is contained within the `tasks-genai` library. Add the dependency to your `build.gradle` file:

```
dependencies {
    implementation 'com.google.mediapipe:tasks-genai:latest.release'
}
```

### Vision tasks

The MediaPipe Tasks vision library contains tasks that handle image or video inputs. To import the MediaPipe Tasks vision library in Android Studio, add the following dependencies to your `build.gradle` file:

```
dependencies {
    implementation 'com.google.mediapipe:tasks-vision:latest.release'
}
```

### Text tasks

The MediaPipe Tasks text library contains tasks that handle language data in text format. To import the MediaPipe Tasks text library in Android Studio, add the following dependencies to your `build.gradle` file:

```
dependencies {
    implementation 'com.google.mediapipe:tasks-text:latest.release'
}
```

### Audio tasks

The MediaPipe Tasks audio library contains tasks that handle sound inputs. To import the MediaPipe Tasks audio library in Android Studio, add the following dependencies to your `build.gradle` file:

```
dependencies {
    implementation 'com.google.mediapipe:tasks-audio:latest.release'
}
```

## BaseOptions configuration

The `BaseOptions` allow for general configuration of MediaPipe Task APIs.

| Option name | Description | Accepted values |
| --- | --- | --- |
| `modelAssetBuffer` | The model asset file contents as a direct `ByteBuffer` or a `MappedByteBuffer`. | `ByteBuffer` or `MappedByteBuffer` as a string |
| `modelAssetPath` | The model path to a model asset file in the Android app assets folder. | File path as a string |
| `modelAssetFileDescriptor` | The native file descriptor integer of a model asset file. | Integer specifying the file descriptor |
| `Delegate` | Enables hardware acceleration through a device delegate to run the MediaPipe pipeline. Default value: `CPU`. | \[`CPU`,   `GPU`\] |

## Hardware acceleration

MediaPipe Tasks supports the use of graphics processing units (GPUs) to run machine learning models. On Android devices, you can enable use of GPU-accelerated execution of your models using a delegate. Delegates act as hardware drivers for MediaPipe, allowing you to run your models on GPU processors instead of the standard CPU processors.

Configure GPU delegate in the task options through `BaseOptions`:

```
BaseOptions baseOptions = BaseOptions.builder().useGpu().build();
```

## Troubleshooting

For help with technical questions related to MediaPipe, visit the [discussion group](https://groups.google.com/forum/#!forum/mediapipe) or [Stack Overflow](https://stackoverflow.com/questions/tagged/mediapipe) for support from the community. To report bugs or make feature requests, [file an issue on GitHub](https://github.com/google/mediapipe/issues).

For help setting up your Android development environment, visit the [Android developer documentation](https://developer.android.com/guide).
