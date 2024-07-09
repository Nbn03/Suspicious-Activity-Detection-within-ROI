
# Yolov5_Suspicious Activity Detection within ROI


https://github.com/Nbn03/Yolov5_Suspicious-Activity-Detection-within-ROI/assets/136473086/193a1b49-8b28-4a46-be07-9f2744d26d16



## Overview
This repository contains code for detecting suspicious activity within a specified Region of Interest (ROI) using Yolov5 and OpenCV. The model is trained to detect persons and cars, and it alerts when a person or car enters the ROI, highlighting the area with a masked red color.

## Main Functionalities
- **Suspicious Activity Detection:** Uses Yolov5 to detect persons and cars.
- **Region of Interest (ROI):** Monitors a static ROI in video frames for the presence of persons or cars.
- **Alert Mechanism:** Alerts with a message and masks the ROI in red when a person or car enters the region.
 
## OpenCV Library
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It contains more than 2500 optimized algorithms, which can be used for image processing, video capture and analysis, face detection, object identification, and more. In this project, OpenCV is utilized for drawing bounding boxes around detected objects and masking the ROI.

## YOLO Models and Yolov5 Version
YOLO (You Only Look Once) models are a family of convolutional neural networks designed for real-time object detection. They are known for their high speed and accuracy. Yolov5, the version used in this project, is highly efficient and easy to use for various object detection tasks.

## Model Details
- **Custom Weight File:** yolov5s.pt
- **Classes:** "Person" and "Car"
- **Region of Interest (ROI):** A static ROI is defined in the video frames to detect when a person or car enters this region.
- **Alert Mechanism:** When a person or car enters the ROI, an alert message is displayed on the video frames, and the ROI gets masked in red.

## Running the Code
### Points to Note
- Ensure all files in the repository are present in the folder where the main_roi.py file is running. If the video or weight file is in a different folder, provide the paths accordingly.
- Install the required dependencies using requirements.txt.
  
## Usage
1. Clone the repository:
```
git clone https://github.com/Nbn03/Yolov5_Suspicious-Activity-Detection-within-ROI.git
cd Yolov5_Suspicious-Activity-Detection-within-ROI
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

Run the main script:
```
python main_roi.py 
```
