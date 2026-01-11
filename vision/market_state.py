def market_state(momentum, strength):
    if momentum == "OVEREXTENDED" and strength == "WEAK":
        return "EXHAUSTION"

    if momentum == "BUILDING" and strength == "STRONG":
        return "CLEAN_TREND"

    return "NO_TRADE"
import cv2
import numpy as np

def detect_market_state(gray):
    edges = cv2.Canny(gray, 40, 120)
    density = edges.mean()

    if density < 12:
        return "RANGE"

    if density > 40:
        return "CHAOS"

    return "TREND"
