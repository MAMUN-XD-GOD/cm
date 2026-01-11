def generate_signal(candles, structure):
    last = candles[-1]

    if structure == "UPTREND_CONTINUATION" and last["color"] == "bullish":
        return "CALL"

    if structure == "DOWNTREND_CONTINUATION" and last["color"] == "bearish":
        return "PUT"

    if structure == "POSSIBLE_REVERSAL":
        return "WAIT"

    return "WAIT"
