from core.market_shift import detect_bos_choch
from core.smc import detect_fvg, detect_order_block

def risk_check(candles, structure):
    shift = detect_bos_choch(candles)
    fvg = detect_fvg(candles)
    ob = detect_order_block(candles)
    last = candles[-1]

    # No confirmation
    if shift == "NO_SHIFT":
        return {"allow": False, "reason": "No market shift confirmation"}

    # Fake CHoCH without smart money
    if shift == "CHoCH" and not (fvg or ob):
        return {"allow": False, "reason": "Unconfirmed CHoCH"}

    # Weak reaction candle
    if not last["strong"]:
        return {"allow": False, "reason": "Weak BOS / CHoCH candle"}

    return {"allow": True}
