import cv2
import numpy as np

def load_image(file):
    try:
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return None

        h, w, _ = img.shape
        if w < 600 or h < 400:
            return None

        return img
    except:
        return None
