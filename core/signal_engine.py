from core.patterns import detect_patterns
from core.sr_engine import detect_sr
from core.liquidity import detect_liquidity

def generate_signal(candles, structure):
    patterns = detect_patterns(candles)
    sr = detect_sr(candles)
    liquidity = detect_liquidity(candles, sr)
    last = candles[-1]

    # BREAK & HOLD continuation
    if structure == "UPTREND_BREAK_HOLD" and last["color"] == "bullish":
        if "MOMENTUM" in patterns:
            return "CALL"

    if structure == "DOWNTREND_BREAK_HOLD" and last["color"] == "bearish":
        if "MOMENTUM" in patterns:
            return "PUT"

    # LIQUIDITY REVERSAL
    if liquidity == "LIQUIDITY_SWEEP":
        if last["color"] == "bullish":
            return "CALL"
        if last["color"] == "bearish":
            return "PUT"

    return "WAIT"
