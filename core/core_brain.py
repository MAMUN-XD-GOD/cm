from vision.vision_core import analyze_screenshot
from core.decision_engine import decide

def analyze_trade(image_path, last_trade="WIN", amount=1):
    vision = analyze_screenshot(image_path)

    momentum = "BUILDING" if vision["state"] == "CLEAN_TREND" else "NEUTRAL"

    decision = decide(vision, momentum)

    return {
        "pair": "Pocket Option",
        "market": "Binary",
        "direction": decision.get("signal"),
        "expiry": decision.get("expiry"),
        "confidence": decision.get("confidence"),
        "note": decision.get("reason", "AI validated setup")
    }
