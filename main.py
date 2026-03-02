import time
from telegram import Bot
from data_engine import analyze_candles
from strategy_core import false_breakout, micro_trend_exhaustion
from utils import get_mock_candles

TOKEN = "8649619777:AAEpJiftucXeViN1zR75s2z-9GrJ7lKtb2k"
CHAT_ID = "1781713201"

bot = Bot(token=TOKEN)

ASSETS = [
    "FACEBOOK INC OTC",
    "American Express OTC",
    "Microsoft OTC",
    "Tesla OTC",
    "Apple OTC",
    "Bitcoin OTC",
    "Polygon OTC",
    "Chainlink OTC",
    "Polkadot OTC",
    "Cardano OTC",
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/CAD OTC",
    "USD/JPY OTC",
    "AUD/USD OTC"
]

def send(msg):
    try:
        bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print("Telegram error:", e)

send("🤖 OTC Sentinel Online – Signal Engine Active")

while True:
    for asset in ASSETS:
        try:
            candles = get_mock_candles(asset)

            # 🔒 HARD GUARD 1
            if candles is None or len(candles) < 30:
                continue

            obs = analyze_candles(candles)

            # 🔒 HARD GUARD 2
            if obs is None:
                continue

            direction = None

            fb = false_breakout(candles, obs)
            mt = micro_trend_exhaustion(candles)

            if fb:
                direction = fb
                reason = "False Breakout"

            elif mt:
                direction = mt
                reason = "Micro-Trend Exhaustion"

            # 🔒 HARD GUARD 3
            if direction is None:
                continue

            message = (
                f"📊 OTC SIGNAL\n"
                f"Asset: {asset}\n"
                f"Direction: {direction}\n"
                f"Expiry: 1 Minute\n"
                f"Reason: {reason}\n"
                f"Confidence: MEDIUM\n"
            )

            send(message)
            time.sleep(3)

        except Exception as e:
            print(f"Skipped {asset} due to error:", e)

    time.sleep(20)