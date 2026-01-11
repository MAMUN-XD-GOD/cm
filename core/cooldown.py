import time

_last_trade_time = 0

def in_cooldown(seconds=60):
    global _last_trade_time
    now = time.time()
    if now - _last_trade_time < seconds:
        return True
    _last_trade_time = now
    return False
