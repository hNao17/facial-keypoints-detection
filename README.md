## Overview
In this repository, I explore various CNN architectures that can be used to detect keypoints in an image. I worked with [Kaggle's Facial Keypoints](https://www.kaggle.com/c/facial-keypoints-detection) dataset. My choice of architectures and loss functions were based on methods developed in [1]-[3] for pose estimation and facial landmarks.

## Data
The original dataset consists of 7049 training images. Each image is grayscale and sized at a 96x96 resolution.
However, there is an uneven distribution of # keypoints / image throughout the training set, with images having either 4 or 15 keypoints per image. Specifically, 2140 images were annotated with 15 keypoints / image, while the remaining 4909 images had 4 keypoints per image.

I trained my models on the 15 keypoint subset of training images. The script [here] extracts each corresponding image from the full training set and saves it to a user-specified directory.

## Architecture

## Training

## Results

## References

[1]: Bulat, Adrian, and Georgios Tzimiropoulos. "Human pose estimation via convolutional part heatmap regression." European Conference on Computer Vision. Springer, Cham, 2016.

[2]: Newell, Alejandro, Kaiyu Yang, and Jia Deng. "Stacked hourglass networks for human pose estimation." European Conference on Computer Vision. Springer, Cham, 2016.

[3]: Merget, Daniel, Matthias Rock, and Gerhard Rigoll. "Robust Facial Landmark Detection via a Fully-Convolutional Local-Global Context Network." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.
