def analyze_structure(candles):
    bull_power = sum(c["strength"] for c in candles if c["color"] == "bullish")
    bear_power = sum(c["strength"] for c in candles if c["color"] == "bearish")

    if bull_power > bear_power * 1.4:
        return "UPTREND_CONTINUATION"

    if bear_power > bull_power * 1.4:
        return "DOWNTREND_CONTINUATION"

    if abs(bull_power - bear_power) < 10:
        return "CHOPPY_RANGE"

    return "POSSIBLE_REVERSAL"
