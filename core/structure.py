from core.market_shift import detect_bos_choch

def analyze_structure(candles):
    shift = detect_bos_choch(candles)

    if shift == "BOS_BULLISH":
        return "BULLISH_CONTINUATION"

    if shift == "BOS_BEARISH":
        return "BEARISH_CONTINUATION"

    if shift == "CHoCH":
        return "POTENTIAL_REVERSAL"

    return "NO_CLEAR_STRUCTURE"
