import time
import os
from telegram import Bot
from config import ASSETS
from data_engine import analyze_candles
from signal_engine import generate_signal
from journal import log_signal

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def send_signal(asset, direction, payout, confidence):
    message = f"""
📊 OTC SIGNAL
Asset: {asset}
Direction: {direction}
Expiry: 1 Minute
Confidence: {confidence}
Payout: {int(payout * 100)}%
⏱ Enter NEXT candle only
"""
    bot.send_message(chat_id=CHAT_ID, text=message)
    log_signal(asset, direction, confidence, payout)

def get_mock_candles():
    # TEMPORARY mock candles for deployment test
    return [
        {"open":1,"high":2,"low":0.5,"close":1.5}
        for _ in range(210)
    ]

def run():
    bot.send_message(chat_id=CHAT_ID, text="🤖 OTC Sentinel Online – Signal Engine Active")

    while True:
        for asset in ASSETS:
            candles = get_mock_candles()
            obs = analyze_candles(candles)

            if not obs:
                continue

            payout = 0.87  # placeholder
            signal = generate_signal(asset, candles, obs, payout)

            if signal:
                confidence = "A+" if obs["wick_aggression"] > 0.7 else "A"
                send_signal(asset, signal, payout, confidence)

        time.sleep(60)

if __name__ == "__main__":
    run()
