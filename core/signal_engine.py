def generate_signal(candles, structure):
    last = candles[-1]

    if structure == "UPTREND" and last["color"] == "bullish":
        return "CALL"

    if structure == "DOWNTREND" and last["color"] == "bearish":
        return "PUT"

    return "WAIT"
