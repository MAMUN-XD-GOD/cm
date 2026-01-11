def risk_check(candles, structure):
    last = candles[-1]

    # No power
    if last["dominance"] < 0.45:
        return {"allow": False, "reason": "Low candle dominance"}

    # Trap candle
    if last["rejection"] and last["dominance"] < 0.35:
        return {"allow": False, "reason": "Rejection trap candle"}

    # Sideways protection
    if "RANGE" in structure or "CHOPPY" in structure:
        return {"allow": False, "reason": "Market indecision"}

    return {"allow": True}
