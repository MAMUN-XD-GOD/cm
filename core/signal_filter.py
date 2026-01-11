def allow_trade(vision_result):
    if vision_result["signal"] == "WAIT":
        return False, "Market unclear"

    if vision_result["confidence"] < 65:
        return False, "Low confidence"

    if vision_result["state"] == "EXHAUSTION":
        return False, "Exhausted move"

    return True, "Trade allowed"
