def select_expiry(momentum):
    if momentum == "BUILDING":
        return "1 MIN"

    if momentum == "OVEREXTENDED":
        return "30 SEC"

    return "NO_TRADE"
