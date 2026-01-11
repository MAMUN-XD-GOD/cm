import json, os

FILE = "data/session_stats.json"
os.makedirs("data", exist_ok=True)

def load_session():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_session(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def update_session(pair, timeframe, result, signal):
    data = load_session()
    key = f"{pair}_{timeframe}"
    if key not in data:
        data[key] = {"wins":0, "losses":0, "last_signal":None}
    if result == "WIN":
        data[key]["wins"] += 1
    elif result == "LOSS":
        data[key]["losses"] += 1
    data[key]["last_signal"] = signal
    save_session(data)
    return data[key]

def get_session_bias(pair, timeframe):
    data = load_session()
    key = f"{pair}_{timeframe}"
    if key not in data:
        return 0
    wins = data[key]["wins"]
    losses = data[key]["losses"]
    return max(min((wins - losses) * 2, 10), -10)  # bias adjustment
