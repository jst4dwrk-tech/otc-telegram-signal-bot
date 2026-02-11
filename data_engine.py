import statistics

def analyze_candles(candles):
    bodies = []
    wicks = []

    for c in candles:
        body = abs(c["close"] - c["open"])
        wick = (c["high"] - c["low"]) - body
        bodies.append(body)
        wicks.append(wick)

    if len(bodies) < 20:
        return None

    volatility = statistics.stdev(bodies[-20:])
    wick_aggression = sum(wicks[-5:]) / (sum(bodies[-5:]) + 0.0001)

    compression = volatility < (sum(bodies) / len(bodies)) * 0.7

    return {
        "volatility": volatility,
        "wick_aggression": wick_aggression,
        "compression": compression,
        "last_candle": candles[-1]
    }
