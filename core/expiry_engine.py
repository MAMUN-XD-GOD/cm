def suggest_expiry(candles):
    last = candles[-1]

    if last["strong"] and last["dominance"] > 0.7:
        return "1 MIN"

    if last["dominance"] > 0.55:
        return "2 MIN"

    return "3 MIN"
