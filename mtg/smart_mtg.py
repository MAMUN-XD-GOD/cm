def smart_mtg(balance, confidence, mode):
    if mode == "DEFENSIVE":
        return round(balance * 0.005, 2)

    if confidence >= 80:
        return round(balance * 0.02, 2)

    if confidence >= 65:
        return round(balance * 0.01, 2)

    return round(balance * 0.007, 2)
