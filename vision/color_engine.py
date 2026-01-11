import numpy as np

def detect_color(candle_img):
    avg = np.mean(candle_img, axis=(0, 1))
    r, g, b = avg

    if g > r + 20:
        return "GREEN"
    if r > g + 20:
        return "RED"
    return "NEUTRAL"
