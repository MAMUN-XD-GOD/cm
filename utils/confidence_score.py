def confidence_score(candles, structure):
    score = 40
    last = candles[-1]

    if structure in ["UPTREND_CONTINUATION", "DOWNTREND_CONTINUATION"]:
        score += 25

    if last["momentum"] == "strong":
        score += 20

    if last["wick"] < last["body"]:
        score += 10

    return min(score, 95)
