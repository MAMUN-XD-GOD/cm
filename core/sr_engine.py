def detect_sr(candles):
    levels = []

    for c in candles:
        levels.append(round((c["body"] + c["wick"]) / 10) * 10)
        levels.append(round((c["body"] - c["wick"]) / 10) * 10)

    return list(set(levels))
