import cv2
import numpy as np

def detect_candle_bias(img):
    h, w, _ = img.shape
    roi = img[int(h*0.25):int(h*0.75), int(w*0.6):int(w*0.9)]

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    green = cv2.inRange(hsv, (35, 40, 40), (85, 255, 255))
    red1 = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
    red2 = cv2.inRange(hsv, (170, 50, 50), (180, 255, 255))
    red = red1 + red2

    g_strength = cv2.countNonZero(green)
    r_strength = cv2.countNonZero(red)

    if abs(g_strength - r_strength) < 150:
        return "NEUTRAL"

    return "BULL" if g_strength > r_strength else "BEAR"
