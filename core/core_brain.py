from vision.vision_core import analyze_screenshot
from core.decision_engine import decide

def analyze_trade(image_path, last_trade="WIN", amount=1):
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
            "note": decision.get("reason", "Filtered out")
        }

    return {
        "direction": decision["signal"],
        "expiry": decision["expiry"],
        "confidence": decision["confidence"],
        "note": vision["reason"]
    }
