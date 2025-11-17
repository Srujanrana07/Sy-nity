import cv2
import os

class IdentityVerifier:
    def __init__(self, cascade_path=None):
        if cascade_path is None:
            # Default Haarcascade shipped with OpenCV
            cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

        if not os.path.exists(cascade_path):
            raise FileNotFoundError("Haarcascade file not found.")

        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def verify(self, image_path):
        if not os.path.exists(image_path):
            return {"status": "error", "message": "Image not found."}

        img = cv2.imread(image_path)

        if img is None:
            return {"status": "error", "message": "Invalid image file."}

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            return {"status": "failed", "faces": 0}
        else:
            return {"status": "verified", "faces": len(faces)}
