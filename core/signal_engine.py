from core.market_shift import detect_bos_choch
from core.timeframe_bias import higher_tf_bias
from core.patterns import detect_patterns
from core.smc import detect_fvg, detect_order_block, premium_discount
from core.feedback_loop import feedback_adjustment

def generate_signal(candles, structure):
    htf = higher_tf_bias(candles)
    shift = detect_bos_choch(candles)
    patterns = detect_patterns(candles)
    fvg = detect_fvg(candles)
    ob = detect_order_block(candles)
    zone = premium_discount(candles)

    feedback = feedback_adjustment()
    last = candles[-1]

    if htf == "BULLISH_BIAS":
        if shift == "BOS_BULLISH" and zone == "DISCOUNT":
            if "MOMENTUM" in patterns and (fvg or ob):
                return {
                    "signal": "CALL",
                    "mode": feedback["mode"]
                }

    if htf == "BEARISH_BIAS":
        if shift == "BOS_BEARISH" and zone == "PREMIUM":
            if "MOMENTUM" in patterns and (fvg or ob):
                return {
                    "signal": "PUT",
                    "mode": feedback["mode"]
                }

    return {"signal": "WAIT", "mode": "SAFE"}
