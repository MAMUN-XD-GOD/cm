def smart_mtg(last_result, base_amount):
    if last_result == "LOSS":
        return round(base_amount * 1.8, 2)

    return base_amount
