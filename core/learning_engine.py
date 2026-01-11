import json
import os

STATS_FILE = "data/stats.json"
os.makedirs("data", exist_ok=True)

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"wins": 0, "losses": 0, "bias": 0}
    with open(STATS_FILE, "r") as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)

def update_stats(result):
    stats = load_stats()
    if result == "WIN":
        stats["wins"] += 1
        stats["bias"] += 1
    elif result == "LOSS":
        stats["losses"] += 1
        stats["bias"] -= 1
    save_stats(stats)
    return stats

def adjust_confidence(base_conf):
    stats = load_stats()
    bias = stats.get("bias", 0)

    # clamp bias effect
    adj = max(min(bias * 2, 8), -8)
    return max(min(base_conf + adj, 90), 50)
