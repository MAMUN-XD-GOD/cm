def higher_tf_bias(candles):
    bulls = sum(1 for c in candles if c["color"] == "bullish")
    bears = len(candles) - bulls

    if bulls > bears * 1.3:
        return "BULLISH_BIAS"
    if bears > bulls * 1.3:
        return "BEARISH_BIAS"

    return "NO_CLEAR_BIAS"


def lower_tf_entry(candles):
    last = candles[-1]

    if last["strong"] and not last["rejection"]:
        return "ENTRY_OK"

    return "ENTRY_WEAK"
