# -*- coding: utf-8 -*-
"""pose_estimation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mP7vu4_u1Rfw7D9VKGORFBzM2fv8MMw0
"""

!pip uninstall -y numpy
!pip install numpy==1.23.5
!pip install mediapipe --upgrade

import cv2
import mediapipe as mp
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import files
from PIL import Image
import io

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Upload image
uploaded = files.upload()

for file_name in uploaded.keys():
    # Read the uploaded image
    image = Image.open(io.BytesIO(uploaded[file_name]))
    image_np = np.array(image.convert('RGB'))

    # Convert to BGR for OpenCV
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Process the image and detect poses
    results = pose.process(image_np)

    # Draw the pose annotation on the image
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image=image_bgr, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS)
        print("Pose detected!")
    else:
        print("No pose detected.")

    # Display the annotated image
    cv2_imshow(image_bgr)

