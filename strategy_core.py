def false_breakout(candles, obs):
    last = candles[-1]
    recent_high = max(c["high"] for c in candles[-6:-1])
    recent_low = min(c["low"] for c in candles[-6:-1])

    breakout_up = last["high"] > recent_high
    breakout_down = last["low"] < recent_low

    candle_range = last["high"] - last["low"]
    if candle_range == 0:
        return None

    close_strength = (last["close"] - last["low"]) / candle_range

    if breakout_up and close_strength < 0.4 and obs["wick_aggression"] > 0.6:
        return "PUT"

    if breakout_down and close_strength > 0.6 and obs["wick_aggression"] > 0.6:
        return "CALL"

    return None


def micro_trend_exhaustion(candles):
    recent = candles[-4:]

    directions = [(c["close"] > c["open"]) for c in recent]
    if not all(d == directions[0] for d in directions):
        return None

    bodies = [abs(c["close"] - c["open"]) for c in recent]

    if bodies[0] > bodies[1] > bodies[2] > bodies[3]:
        return "PUT" if directions[0] else "CALL"

    return None
