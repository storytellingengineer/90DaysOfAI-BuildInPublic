# 🧍‍♂️ Pose Estimation Using MediaPipe

## 📌 Project Overview

Pose Estimation refers to identifying key body landmarks (like shoulders, knees, elbows) from an image or video. It’s a foundational technique for building AI systems that understand human posture and movement.

In this project, I used **MediaPipe**, a Google framework, to implement real-time pose detection using a webcam. It tracks 33 key points and is efficient enough to run even on a CPU, making it a great option for lightweight applications and prototypes.

---

## 🎯 Why Pose Estimation?

Pose estimation is used in:
- 👟 Fitness applications for posture analysis
- 🧠 Physiotherapy & rehabilitation
- 🎮 AR/VR and gesture control
- 📊 Sports analytics
- 🕹️ Human-computer interaction systems

Understanding body posture adds depth to how AI systems interact with humans.

---

## 🛠️ Tools Used

- Python
- OpenCV
- MediaPipe
- Google Colab / Jupyter Notebook

---

## ⚙️ How to Run

Install dependencies:
```bash
pip install mediapipe opencv-python
```

---

## 📚 Learning & Reflections

**Why I chose MediaPipe over OpenPose/BlazePose:**

| Model      | Pros                                    | Cons                                 |
|------------|-----------------------------------------|--------------------------------------|
| **MediaPipe** | ✅ Lightweight, easy to use, CPU-friendly  | ❌ Only single-person detection      |
| **OpenPose**  | ✅ Multi-person tracking, very accurate    | ❌ Requires GPU, heavy setup        |
| **BlazePose** | ✅ Great for mobile/AR, fast             | ❌ Not fully open source outside MediaPipe |


## Reflection:
While OpenPose is more powerful, MediaPipe was chosen because of its quick setup, lightweight nature, and ease of experimentation. For large-scale or multi-person projects, transitioning to OpenPose or MoveNet can be the next step.

---

## 🧩 Issues Faced
- `cv2.imshow()` not working in Google Colab
- Replaced with `cv2_imshow()` using `google.colab.patches`.
- Camera not opening by default
- Had to handle webcam stream explicitly with `cv2.VideoCapture(0)` and ensure permissions were granted.
- Pose landmarks jittering
- Inconsistent detection under poor lighting or fast movement. Can be improved with better lighting or smoothing techniques.

---

## 🧪 Output
- Detected and rendered 33 body landmarks on live webcam stream.
- Displayed real-time body posture visualization.
- Great FPS and performance on CPU.

---

## 🔮 Future Scope
- Add rep counters for exercises (e.g. push-ups/squats)
- Calculate joint angles and symmetry for form correction
- Extend to multi-person tracking using OpenPose
- Integrate with voice feedback or alerts
