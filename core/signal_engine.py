from core.market_shift import detect_bos_choch
from core.smc import detect_fvg, detect_order_block, premium_discount
from core.patterns import detect_patterns

def generate_signal(candles, structure):
    shift = detect_bos_choch(candles)
    patterns = detect_patterns(candles)
    fvg = detect_fvg(candles)
    ob = detect_order_block(candles)
    zone = premium_discount(candles)
    last = candles[-1]

    # Continuation trades
    if shift == "BOS_BULLISH" and zone == "DISCOUNT":
        if "MOMENTUM" in patterns and (fvg or ob):
            return "CALL"

    if shift == "BOS_BEARISH" and zone == "PREMIUM":
        if "MOMENTUM" in patterns and (fvg or ob):
            return "PUT"

    # Reversal trades
    if shift == "CHoCH":
        if last["color"] == "bullish":
            return "CALL"
        if last["color"] == "bearish":
            return "PUT"

    return "WAIT"
