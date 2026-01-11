from vision.image_loader import load_image
from vision.color_engine import detect_color
from vision.momentum_engine import momentum_sequence
from vision.market_state import market_state

def analyze_screenshot(path):
    img = load_image(path)

    # (simplified candle segmentation assumption)
    candles = img[400:650, 100:1100]
    segments = [candles[:, i:i+80] for i in range(0, 400, 80)]

    colors = [detect_color(seg) for seg in segments]

    momentum = momentum_sequence(colors)
    strength = "STRONG" if colors.count("GREEN") >= 3 else "WEAK"

    state = market_state(momentum, strength)

    if state == "CLEAN_TREND":
        direction = "CALL" if colors[-1] == "GREEN" else "PUT"
        return {
            "signal": direction,
            "confidence": 78,
            "state": state
        }

    return {
        "signal": "WAIT",
        "confidence": 40,
        "state": state
  }
