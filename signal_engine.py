from strategy_core import false_breakout, micro_trend_exhaustion
from learning_engine import is_asset_dirty
from sentiment_filter import crowd_bias_detected

def generate_signal(asset, candles, obs, payout):
    if payout < 0.80:
        return None

    if is_asset_dirty(asset):
        return None

    if crowd_bias_detected(asset):
        return None

    signal = false_breakout(candles, obs)
    if signal:
        return signal

    return micro_trend_exhaustion(candles)
