from core.patterns import detect_patterns
from core.smc import detect_fvg, detect_order_block, premium_discount

def generate_signal(candles, structure):
    patterns = detect_patterns(candles)
    fvg = detect_fvg(candles)
    ob = detect_order_block(candles)
    zone = premium_discount(candles)
    last = candles[-1]

    # BUY LOGIC
    if last["color"] == "bullish" and zone == "DISCOUNT":
        if "MOMENTUM" in patterns and (fvg or ob):
            return "CALL"

    # SELL LOGIC
    if last["color"] == "bearish" and zone == "PREMIUM":
        if "MOMENTUM" in patterns and (fvg or ob):
            return "PUT"

    return "WAIT"
