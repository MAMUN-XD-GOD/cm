trade_history = []

def record_trade(result, confidence):
    trade_history.append({
        "result": result,  # WIN / LOSS
        "confidence": confidence
    })

    if len(trade_history) > 50:
        trade_history.pop(0)


def win_rate():
    if not trade_history:
        return 0.0

    wins = sum(1 for t in trade_history if t["result"] == "WIN")
    return wins / len(trade_history)
