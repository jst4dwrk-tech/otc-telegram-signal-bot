import random
import time

def get_mock_candles(asset, count=60):
    candles = []
    price = random.uniform(100, 200)

    for _ in range(count):
        open_price = price
        close_price = open_price + random.uniform(-2, 2)
        high = max(open_price, close_price) + random.uniform(0, 1)
        low = min(open_price, close_price) - random.uniform(0, 1)

        candles.append({
            "open": open_price,
            "close": close_price,
            "high": high,
            "low": low,
            "timestamp": int(time.time())
        })

        price = close_price

    return candles