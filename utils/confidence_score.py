def confidence_score(candles, structure):
    score = 50

    if structure != "RANGE":
        score += 20

    if candles[-1]["body"] > 12:
        score += 15

    return min(score, 95)
