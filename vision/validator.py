def validate_signal(signal, candle_bias, market_state):
    if market_state != "TREND":
        return False, "Market not trending"

    if signal == "CALL" and candle_bias != "BULL":
        return False, "Bull bias missing"

    if signal == "PUT" and candle_bias != "BEAR":
        return False, "Bear bias missing"

    return True, "Valid setup"
