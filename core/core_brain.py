from vision.vision_core import analyze_screenshot
from core.decision_engine import decide
from core.learning_engine import adjust_confidence
from core.cooldown import in_cooldown

def analyze_trade(image_path, last_trade="WIN", amount=1):
    if in_cooldown(45):
        return {
            "direction": "WAIT",
            "expiry": "—",
            "confidence": 50,
            "note": "Cooldown active – avoid overtrading"
        }

    vision = analyze_screenshot(image_path)

    if vision["signal"] == "WAIT":
        return {
            "direction": "WAIT",
            "expiry": "—",
            "confidence": vision["confidence"],
            "note": vision.get("reason", "No trade")
        }

    momentum = "BUILDING" if vision["state"] == "TREND" else "NEUTRAL"
    decision = decide(vision, momentum)

    if decision["signal"] == "WAIT":
        return {
            "direction": "WAIT",
            "expiry": "—",
            "confidence": decision.get("confidence", 50),
            "note": decision.get("reason", "Filtered")
        }

    final_conf = adjust_confidence(decision["confidence"])

    return {
        "direction": decision["signal"],
        "expiry": decision["expiry"],
        "confidence": final_conf,
        "note": "Adaptive signal (learning enabled)"
    }
