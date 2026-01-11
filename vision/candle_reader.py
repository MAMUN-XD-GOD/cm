def candle_strength(body, wick):
    ratio = body / (wick + 1)

    if ratio > 2.5:
        return "STRONG"
    if ratio > 1.2:
        return "NORMAL"
    return "WEAK"
