def detect_bos_choch(candles):
    highs = [c["body"] + c["wick"] for c in candles]
    lows = [c["body"] - c["wick"] for c in candles]

    last_high = highs[-1]
    last_low = lows[-1]

    prev_high = max(highs[:-1])
    prev_low = min(lows[:-1])

    # Break of Structure
    if last_high > prev_high:
        return "BOS_BULLISH"

    if last_low < prev_low:
        return "BOS_BEARISH"

    # Change of Character
    if candles[-1]["color"] != candles[-2]["color"]:
        if abs(last_high - prev_high) < 5 or abs(last_low - prev_low) < 5:
            return "CHoCH"

    return "NO_SHIFT"
