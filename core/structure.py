def analyze_structure(candles):
    highs = [c["body"] + c["wick"] for c in candles]
    lows = [c["body"] - c["wick"] for c in candles]

    hh = highs[-1] > max(highs[:-1])
    ll = lows[-1] < min(lows[:-1])

    if hh and candles[-1]["strong"]:
        return "UPTREND_BREAK_HOLD"

    if ll and candles[-1]["strong"]:
        return "DOWNTREND_BREAK_HOLD"

    if hh or ll:
        return "BREAK_NO_HOLD"

    return "RANGE_STRUCTURE"
