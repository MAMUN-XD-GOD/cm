def risk_check(candles, structure):
    last = candles[-1]

    if last["body"] < 5:
        return {"allow": False, "reason": "Weak candle / no momentum"}

    if structure == "RANGE":
        return {"allow": False, "reason": "Sideways market"}

    return {"allow": True}
