from core.trade_memory import win_rate

def feedback_adjustment():
    wr = win_rate()

    if wr >= 0.75:
        return {"mode": "AGGRESSIVE", "confidence_boost": 10}

    if wr >= 0.6:
        return {"mode": "NORMAL", "confidence_boost": 0}

    return {"mode": "DEFENSIVE", "confidence_boost": -10}
