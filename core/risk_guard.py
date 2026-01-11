from core.timeframe_bias import higher_tf_bias, lower_tf_entry

def risk_check(candles, structure):
    htf = higher_tf_bias(candles)
    ltf = lower_tf_entry(candles)
    last = candles[-1]

    # No higher timeframe bias
    if htf == "NO_CLEAR_BIAS":
        return {"allow": False, "reason": "No HTF bias"}

    # Late / weak entry
    if ltf == "ENTRY_WEAK":
        return {"allow": False, "reason": "Late or weak entry"}

    # Exhausted candle
    if last["dominance"] > 0.85:
        return {"allow": False, "reason": "Move already extended"}

    return {"allow": True}
