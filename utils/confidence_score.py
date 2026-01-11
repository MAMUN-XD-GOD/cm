def confidence_score(candles, structure):
    score = 35
    last = candles[-1]

    if last["strong"]:
        score += 20

    if not last["rejection"]:
        score += 15

    if structure.startswith("UPTREND") or structure.startswith("DOWNTREND"):
        score += 20

    return min(score, 96)
