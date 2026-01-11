def momentum_sequence(colors):
    streak = 1
    for i in range(1, len(colors)):
        if colors[i] == colors[i-1]:
            streak += 1
        else:
            break

    if streak >= 4:
        return "OVEREXTENDED"
    if streak >= 2:
        return "BUILDING"
    return "NEUTRAL"
