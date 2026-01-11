from core.signal_filter import allow_trade
from core.expiry_engine import select_expiry
from core.confidence_engine import calculate_confidence

def decide(vision_result, momentum):
    allowed, reason = allow_trade(vision_result)

    if not allowed:
        return {
            "signal": "WAIT",
            "reason": reason
        }

    expiry = select_expiry(momentum)
    confidence = calculate_confidence(
        vision_result["confidence"], True
    )

    return {
        "signal": vision_result["signal"],
        "expiry": expiry,
        "confidence": confidence
    }
