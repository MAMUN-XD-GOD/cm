def detect_patterns(candles):
    patterns = []

    last = candles[-1]
    prev = candles[-2]

    # ENGULFING
    if last["body"] > prev["body"] * 1.4:
        if last["color"] != prev["color"]:
            patterns.append("ENGULFING")

    # PIN BAR
    if last["rejection"] and last["dominance"] < 0.4:
        patterns.append("PIN_BAR")

    # MOMENTUM CANDLE
    if last["strong"] and not last["rejection"]:
        patterns.append("MOMENTUM")

    return patterns
