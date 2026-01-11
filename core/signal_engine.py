from core.patterns import detect_patterns

def generate_signal(candles, structure):
    patterns = detect_patterns(candles)
    last = candles[-1]

    # CONTINUATION
    if "MOMENTUM" in patterns:
        if structure.startswith("UPTREND") and last["color"] == "bullish":
            return "CALL"
        if structure.startswith("DOWNTREND") and last["color"] == "bearish":
            return "PUT"

    # REVERSAL CONFIRMATION
    if "ENGULFING" in patterns or "PIN_BAR" in patterns:
        if last["color"] == "bullish":
            return "CALL"
        if last["color"] == "bearish":
            return "PUT"

    return "WAIT"
