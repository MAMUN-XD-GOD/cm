def smart_mtg(last_result):
    if last_result == "LOSS":
        return "Reduce lot, wait confirmation"
    return "Normal risk"
