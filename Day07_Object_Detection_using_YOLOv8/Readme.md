# Day 7 – Object Detection with YOLOv8 🚀

Welcome to Day 7 of my **#90DaysOfAI** challenge! Today, I explored object detection using **YOLOv8**, the latest from Ultralytics.

## 🔍 What I Did

- Loaded the pre-trained `yolov8n.pt` model (Nano = faster & lightweight)
- Ran object detection on sample images
- Visualized the results using OpenCV

![image](https://github.com/user-attachments/assets/6150bf49-41fd-4071-9c31-c468a5695c2b)

## 🧠 Learnings

- How object detection models return bounding boxes, confidence scores, and class labels
- Difference between YOLO versions (v5, v8) and how YOLOv8 improves ease of use
- The `.plot()` method in Ultralytics is super handy for visualizations

## ⚠️ Issues Faced

- Older Python versions had OpenCV compatibility issues — fixed by using Python 3.10+
- Some confusion between `.show()` and `.plot()` methods in YOLO API

## 🛠️ Installation

```bash
pip install ultralytics opencv-python
