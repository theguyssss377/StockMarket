import alpaca_trade_api as tradeapi
import time
import os
from datetime import datetime
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

SYMBOL = "AAPL"
QTY = 1

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

def market_is_open():
    clock = api.get_clock()
    return clock.is_open


def trade():
    if market_is_open():
        api.submit_order(
            symbol=SYMBOL,
            qty=QTY,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        print("Bought {QTY} {SYMBOL} at {datetime.now()}")
    else:
        print("Market closed — no trade executed")

if __name__ == "__main__":
    trade()
