import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os

MODEL_PATH = "hand_landmarker.task"

class HandTracker:
    def __init__(self):
        # Download model if not present
        if not os.path.exists(MODEL_PATH):
            print("Downloading hand landmark model...")
            url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
            urllib.request.urlretrieve(url, MODEL_PATH)
            print("Model downloaded!")

        base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1,
            min_hand_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.results = None

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        self.results = self.detector.detect(mp_image)
        return self.results

    def draw_hands(self, frame):
        if self.results and self.results.hand_landmarks:
            h, w, _ = frame.shape
            for hand in self.results.hand_landmarks:
                points = [(int(lm.x * w), int(lm.y * h)) for lm in hand]
                for pt in points:
                    cv2.circle(frame, pt, 4, (0, 255, 0), -1)
                connections = [
                    (0,1),(1,2),(2,3),(3,4),
                    (0,5),(5,6),(6,7),(7,8),
                    (0,9),(9,10),(10,11),(11,12),
                    (0,13),(13,14),(14,15),(15,16),
                    (0,17),(17,18),(18,19),(19,20),
                    (5,9),(9,13),(13,17)
                ]
                for a, b in connections:
                    cv2.line(frame, points[a], points[b], (0, 200, 200), 2)
        return frame

    def get_landmarks(self, frame):
        landmarks = []
        if self.results and self.results.hand_landmarks:
            h, w, _ = frame.shape
            for hand in self.results.hand_landmarks:
                for lm in hand:
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
        return landmarks
