def detect_fvg(candles):
    gaps = []
    for i in range(1, len(candles)-1):
        prev = candles[i-1]
        curr = candles[i]
        nxt = candles[i+1]

        if curr["body"] > prev["body"] and curr["body"] > nxt["body"]:
            gaps.append("FVG")

    return gaps


def detect_order_block(candles):
    last = candles[-1]
    prev = candles[-2]

    if prev["color"] != last["color"] and prev["strong"]:
        return "ORDER_BLOCK"

    return None


def premium_discount(candles):
    highs = [c["body"] + c["wick"] for c in candles]
    lows = [c["body"] - c["wick"] for c in candles]

    mid = (max(highs) + min(lows)) / 2
    last_price = candles[-1]["body"]

    if last_price < mid:
        return "DISCOUNT"
    return "PREMIUM"
