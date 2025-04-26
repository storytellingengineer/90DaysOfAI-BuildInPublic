# Day 8 – Face Detection + Emotion Recognition 🎭

As part of my "90 Days of AI" journey, today’s project focuses on giving computers the ability to not just see faces but also feel human emotions — an important bridge between visual understanding and emotional intelligence.

---

## 🛠️ Problem Statement

Design a simple AI tool that can:
- Detect faces in an image
- Predict the dominant emotion for each detected face

---

## 🔍 Approach

1. **Face Detection** using OpenCV’s Haar Cascade Classifier
2. **Emotion Recognition** using DeepFace (pre-trained on thousands of facial emotion datasets)
3. **Visualization** by drawing bounding boxes and labeling detected emotions over the faces

---

## ⚙️ Setup Instructions

1. Install the required libraries:
```bash
pip install opencv-python deepface
