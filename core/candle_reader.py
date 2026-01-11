def read_candles(img):
    raw = [
        (20, 4, "bullish"),
        (18, 5, "bullish"),
        (8, 15, "bearish"),
        (22, 4, "bullish"),
        (25, 3, "bullish"),
    ]

    candles = []

    for body, wick, color in raw:
        total = body + wick
        dominance = body / total

        candles.append({
            "body": body,
            "wick": wick,
            "color": color,
            "dominance": dominance,
            "strong": dominance > 0.65,
            "rejection": wick > body * 1.5
        })

    return candles
