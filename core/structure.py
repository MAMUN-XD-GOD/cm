def analyze_structure(candles):
    bulls = sum(1 for c in candles if c["color"] == "bullish")
    bears = len(candles) - bulls

    if bulls >= 4:
        return "UPTREND"
    elif bears >= 4:
        return "DOWNTREND"
    else:
        return "RANGE"
