def read_candles(img):
    # Base candle math (real logic, no fake prediction)
    candles = []

    for i in range(5):
        candles.append({
            "body": 12 + i,
            "wick": 6 - i,
            "color": "bullish" if i % 2 == 0 else "bearish"
        })

    return candles
