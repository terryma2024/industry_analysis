---
source_id: "SRC-ai-069"
title: "MediaPipe Model Maker overview"
source_type: "product_documentation"
publisher: "Google AI Edge"
source_date: "2026-06-05"
url: "https://developers.google.com/edge/mediapipe/solutions/model_maker"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:10:12+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-ai-069
---
# MediaPipe Model Maker overview

MediaPipe Model Maker is a tool for customizing existing machine learning (ML) models to work with your data and applications. You can use this tool as a faster alternative to building and training a new ML model. Model Maker uses an ML training technique called [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning) which retrains existing models with new data. This technique re-uses a significant portion of the existing model logic, which means training takes less time than training a new model, and can be done with less data.

Model Maker works on various types of models including, object detection, gesture recognition, or classifiers for images, text, or audio data. The tool retrains models by removing the last few layers of the model that classify data into specific categories, and rebuilds those layers using new data you provide. Model Maker also supports some option to fine tune model layers to improve accuracy and performance.

![Machine learning model showing classification layers being removed and replaced](https://developers.google.com/static/edge/mediapipe/images/solutions/mm-transfer-learning.svg)

**Figure 1. Model Maker removes the final layers of an existing model and rebuilds them with new data.**

Retraining a model using Model Maker generally makes the model smaller, particularly if you retrain the new model to recognize fewer things. This means you can use Model Maker to create more focused models that work better for your application. The tool can also help you apply ML techniques like quantization so your model uses less resources and runs more efficiently.

## Training data requirements

You can use Model Maker to retrain models with significantly less data than training a new model. When retraining a model with new data, you should aim to have approximately 100 data samples for each trained class. For example, if you are retraining an image classification model to recognize cats, dogs, and parrots, you should have around 100 images of cats, 100 images of dogs, and 100 images of parrots. Depending on your application, you may be able to retrain a useful model with even less data per category, although a larger dataset generally improves the accuracy of your model. When creating your training dataset, remember that your training data gets split up during the retraining process, typically 80% for training, 10% for testing, and the remainder for validation.

## Limitations of customization

Since the retraining process removes the previous classification layers, the resulting model can only recognize items, or classes, provided in the new data. If the old model was trained to recognize 30 different item classes, and you use Model Maker to retrain with data for 10 different items, the resulting model is only able to recognize those 10 new items.

Retraining a model with Model Maker cannot change what the original ML model was built to solve, even if those jobs are similar. For example, you can't use the tool to make an image classification model perform object detection, even though those tasks share some similarity.

## Get started

You can start using MediaPipe Model Maker by running one of the solution Customization tutorials for MediaPipe Solutions, such as [Image Classification](https://developers.google.com/edge/mediapipe/solutions/customization/image_classifier)
