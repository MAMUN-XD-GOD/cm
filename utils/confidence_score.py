from core.market_shift import detect_bos_choch

def confidence_score(candles, structure):
    score = 40
    shift = detect_bos_choch(candles)
    last = candles[-1]

    if "BOS" in shift:
        score += 25

    if shift == "CHoCH":
        score += 15

    if last["strong"]:
        score += 15

    return min(score, 99)
