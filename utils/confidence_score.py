def confidence_score(candles, structure):
    score = 30
    last = candles[-1]

    if last["strong"]:
        score += 20

    if not last["rejection"]:
        score += 15

    if "BREAK_HOLD" in structure:
        score += 25

    return min(score, 97)
