def risk_check(candles, structure):
    last = candles[-1]
    prev = candles[-2]

    # weak candle → no trade
    if last["momentum"] == "weak":
        return {"allow": False, "reason": "Weak momentum candle"}

    # fake breakout logic
    if last["color"] != prev["color"] and last["wick"] > last["body"]:
        return {"allow": False, "reason": "Fake breakout / trap candle"}

    # sideways market
    if structure == "CHOPPY_RANGE":
        return {"allow": False, "reason": "Market choppy / sideways"}

    return {"allow": True}
