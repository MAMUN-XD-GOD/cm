def suggest_expiry(candles):
    avg_body = sum(c["body"] for c in candles) / len(candles)

    if avg_body > 15:
        return "1 MIN"
    elif avg_body > 10:
        return "2 MIN"
    else:
        return "3 MIN"
