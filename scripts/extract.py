import sys
sys.path.append('../')

import requests
from datetime import datetime
import pandas as pd
from pathlib import Path
from typing import Optional
from ..predictcrypto.logger import logging
from ..predictcrypto.exception import CustomException

def get_ohlc_data_from_coinbase(
        product: Optional[str] = "BTC-USD",
        start: Optional[str] = "20240101",
        days: Optional[int] = 180
) :#-> Path:
    try:
        logging.info("Initiating download...")
        end = datetime.strptime(start, "%Y%m%d") + days
        print(end)
    except Exception as e:
        raise CustomException(e, sys)


def pull_data(
        product: Optional[str] = "BTC-USD", 
        start: Optional[str] = "20240101", 
        end: Optional[str] = "20240102"
): #-> pd.DataFrame:
    
    url = f"https://api.exchange.coinbase.com/products/{product}/candles?granularity=3600&start={start}&end={end}"
    btc = requests.get(url)
    raw = btc.json()
    #df = pd.DataFrame(raw, columns = ["timestamp", "low", "high", "open", "close", "volume"])
    # df.to_csv("btc.csv")
    # return df
    #print(raw)
    return raw

if __name__ == "__main__":
    pull_data()
    get_ohlc_data_from_coinbase()