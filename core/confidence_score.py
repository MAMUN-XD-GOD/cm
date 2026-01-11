def calculate_confidence(vision_conf, filters_passed):
    base = vision_conf

    if filters_passed:
        base += 7

    return min(base, 92)
