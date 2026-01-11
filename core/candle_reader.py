def read_candles(img):
    candles = []

    # dynamic candle logic placeholder (image parsing will come later)
    raw = [
        (18, 6, "bullish"),
        (15, 4, "bullish"),
        (10, 8, "bearish"),
        (20, 5, "bullish"),
        (22, 4, "bullish"),
    ]

    for body, wick, color in raw:
        strength = body - wick
        momentum = "strong" if strength > 10 else "weak"

        candles.append({
            "body": body,
            "wick": wick,
            "color": color,
            "strength": strength,
            "momentum": momentum
        })

    return candles
