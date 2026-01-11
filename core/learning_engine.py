from core.session_memory import get_session_bias, update_session
import json, os

STATS_FILE = "data/stats.json"
os.makedirs("data", exist_ok=True)

def adjust_confidence(base_conf, pair=None, timeframe=None):
    bias = 0
    if pair and timeframe:
        bias = get_session_bias(pair, timeframe)
    adj = max(min(bias, 10), -10)
    return max(min(base_conf + adj, 95), 50)

def feedback(result, signal, pair=None, timeframe=None):
    # update global stats
    stats = load_stats()
    if result == "WIN":
        stats["wins"] += 1
    elif result == "LOSS":
        stats["losses"] += 1
    save_stats(stats)

    # update session memory
    if pair and timeframe:
        update_session(pair, timeframe, result, signal)

    return stats
