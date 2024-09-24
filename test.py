import requests
import pandas as pd
from datetime import datetime


def test():
    url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=3600&start=20240101&end=20240102"
    raw = requests.get(url)
    candles = raw.json()
    #df = pd.DataFrame(candles, columns = ['timestamp', 'low', 'high', 'open', 'close', 'volume'])
    #df.to_csv("btc.csv")
    #return df 
    # timestamps = [candle[0] for candle in candles]
    # datetimes = [datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M") for timestamp in timestamps]
    # return datetimes
    return candles

if __name__ == "__main__":
    # print(test())
    print(test())
    