def market_state(momentum, strength):
    if momentum == "OVEREXTENDED" and strength == "WEAK":
        return "EXHAUSTION"

    if momentum == "BUILDING" and strength == "STRONG":
        return "CLEAN_TREND"

    return "NO_TRADE"
