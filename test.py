import http.client
import requests
import pandas as pd

def test():
    url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=3600&start=20240101&end=20240102"
    raw = requests.get(url)
    candles = raw.json()
    df = pd.DataFrame(candles, columns = ['tiemstamp', 'low', 'high', 'open', 'close', 'volume'])
    df.to_csv("btc.csv")
    #pd.to_csv("cryptodata.csv", df)
    return df 

if __name__ == "__main__":
    # print(test())
    print(test())
    