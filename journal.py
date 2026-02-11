import csv
from datetime import datetime

def log_signal(asset, direction, confidence, payout):
    with open("trade_journal.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            asset,
            direction,
            confidence,
            payout
        ])
