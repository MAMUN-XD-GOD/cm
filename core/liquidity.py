def detect_liquidity(candles, sr_levels):
    last = candles[-1]

    for lvl in sr_levels:
        if abs((last["body"] + last["wick"]) - lvl) < 3:
            if last["rejection"]:
                return "LIQUIDITY_SWEEP"

    return "NO_SWEEP"
