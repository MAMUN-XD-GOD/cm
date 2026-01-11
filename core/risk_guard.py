from core.smc import detect_fvg, detect_order_block, premium_discount

def risk_check(candles, structure):
    fvg = detect_fvg(candles)
    ob = detect_order_block(candles)
    zone = premium_discount(candles)
    last = candles[-1]

    # No smart money context
    if not fvg and not ob:
        return {"allow": False, "reason": "No smart money zone"}

    # Wrong zone entry
    if last["color"] == "bullish" and zone == "PREMIUM":
        return {"allow": False, "reason": "Bullish entry in premium zone"}

    if last["color"] == "bearish" and zone == "DISCOUNT":
        return {"allow": False, "reason": "Bearish entry in discount zone"}

    # Weak candle
    if not last["strong"]:
        return {"allow": False, "reason": "Weak smart money reaction"}

    return {"allow": True}
