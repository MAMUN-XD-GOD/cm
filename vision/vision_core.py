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
import cv2
from vision.candle_detector import detect_candle_bias
from vision.market_state import detect_market_state
from vision.validator import validate_signal

def analyze_screenshot(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    candle_bias = detect_candle_bias(img)
    market_state = detect_market_state(gray)

    if candle_bias == "NEUTRAL":
        return {
            "signal": "WAIT",
            "confidence": 55,
            "state": market_state,
            "reason": "Indecision candle"
        }

    signal = "CALL" if candle_bias == "BULL" else "PUT"
    valid, reason = validate_signal(signal, candle_bias, market_state)

    if not valid:
        return {
            "signal": "WAIT",
            "confidence": 52,
            "state": market_state,
            "reason": reason
        }

    base_conf = 72 if market_state == "TREND" else 60

    return {
        "signal": signal,
        "confidence": base_conf,
        "state": market_state,
        "reason": "Trend + candle confirmation"
        }
