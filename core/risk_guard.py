from core.sr_engine import detect_sr
from core.liquidity import detect_liquidity

def risk_check(candles, structure):
    sr = detect_sr(candles)
    liquidity = detect_liquidity(candles, sr)
    last = candles[-1]

    if liquidity == "LIQUIDITY_SWEEP" and not last["strong"]:
        return {"allow": False, "reason": "Liquidity sweep trap"}

    if structure == "RANGE_STRUCTURE":
        return {"allow": False, "reason": "Range market – no edge"}

    if last["rejection"] and last["dominance"] < 0.4:
        return {"allow": False, "reason": "Rejection near key level"}

    return {"allow": True}
