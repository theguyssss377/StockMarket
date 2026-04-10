import alpaca_trade_api as tradeapi
import time
API_KEY = "PKCTPB3AWDM2UHCV7JATMHRAJB"
API_SECRET = "HUr2U5YzBDg2zNC2BXk7vkB2XfzZGkKPfTDsstcnzsRo"
BASE_URL = "https://paper-api.alpaca.markets"

SYMBOL = "AAPL"
QTY = 1

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

while True:
    api.submit_order(
symbol=SYMBOL,
qty=QTY,
side="buy",
type="market",
time_in_force="gtc"
    )

    print("Bought", QTY, SYMBOL)
    time.sleep(28800)