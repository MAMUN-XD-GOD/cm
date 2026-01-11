from core.timeframe_bias import higher_tf_bias

def confidence_score(candles, structure):
    score = 45
    htf = higher_tf_bias(candles)
    last = candles[-1]

    if htf != "NO_CLEAR_BIAS":
        score += 20

    if last["strong"]:
        score += 15

    if last["dominance"] < 0.8:
        score += 10

    return min(score, 99)
