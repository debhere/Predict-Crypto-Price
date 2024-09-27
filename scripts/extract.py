import os
import requests
from datetime import datetime, timedelta
import pandas as pd
from typing import Optional
from config import get_etl_config


#BTC-USD: Bitcoin, ETH-USD: Ethereum, DOGE-USD: Dogecoin, LTC-USD:Litcoin, USDT-USD: Tether
def get_ohlc_data_from_coinbase(
        product: Optional[str] = "BTC-USD",
        start_date: Optional[str] = "20240101",
        end_date: Optional[int] = "20240630"
) -> None:
        
    # end_dt = datetime.strptime(start, '%Y%m%d') + timedelta(days=days)
    # end = end_dt.strftime('%Y%m%d')
    #print(end_dt, type(end_dt))
    
    dates = pd.date_range(start = start_date, end = end_date)
    dates = [day.strftime("%Y%m%d") for day in dates]

    raw_path, interim_path, _ = get_etl_config()
    
    next_day = dates[1]
    for i, day in enumerate(dates):
        if day == dates[-1]:
            break
        next_day = dates[i + 1]
        df = get_ohlc_data_for_one_day(product, day, next_day)
        
        df.to_csv(raw_path, index=False)

        if not interim_path.is_file():
            interim = pd.DataFrame(list(), df.columns)
            interim.to_csv(interim_path, index=False)
        else:
            interim = pd.read_csv(interim_path)

        interim = pd.concat([df, interim], axis = 0)
        interim.to_csv(interim_path, index=False)
    
    # df_ = pd.read_csv(interim_path)
    # print(df_.head(10))
    print(interim.head())

def get_ohlc_data_for_one_day(product, fromDate, toDate) -> pd.DataFrame:
    url = f"https://api.exchange.coinbase.com/products/{product}/candles?granularity=3600&start={fromDate}&end={toDate}"
    btc = requests.get(url)
    raw = btc.json()
    df = pd.DataFrame(raw, columns = ["ticktimestamp", "lowprice", "highprice", "openprice", "closeprice", "volume"])
    return df

if __name__ == "__main__":
    #pull_data()
    get_ohlc_data_from_coinbase()