import cv2
import numpy as np

def analyze_screenshot(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)
    edge_strength = np.mean(edges)

    if edge_strength < 20:
        return {
            "signal": "WAIT",
            "confidence": 50,
            "state": "SIDEWAYS"
        }

    # Simplified directional bias
    h, w = gray.shape
    left = np.mean(gray[:, :w//2])
    right = np.mean(gray[:, w//2:])

    if right > left:
        signal = "CALL"
    else:
        signal = "PUT"

    return {
        "signal": signal,
        "confidence": min(80, int(edge_strength)),
        "state": "CLEAN_TREND"
    }
