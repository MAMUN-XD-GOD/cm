def detect_pair(text):
    known = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "XAUUSD"]
    for p in known:
        if p in text.replace("/", ""):
            return p
    return "UNKNOWN"
