from core.smc import detect_fvg, detect_order_block

def confidence_score(candles, structure):
    score = 35
    last = candles[-1]

    if detect_fvg(candles):
        score += 20

    if detect_order_block(candles):
        score += 20

    if last["strong"]:
        score += 15

    return min(score, 98)
