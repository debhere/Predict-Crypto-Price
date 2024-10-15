import requests # type: ignore
import pandas as pd
from typing import Optional
from config import get_etl_config


#BTC-USD: Bitcoin, ETH-USD: Ethereum, DOGE-USD: Dogecoin, LTC-USD:Litcoin, USDT-USD: Tether
def get_ohlc_data_from_coinbase(
        product: Optional[str] = "BTC-USD",
        start_date: Optional[str] = "20240101",
        end_date: Optional[str] = "20240630"
) -> None:
    
    try:
        
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

    except Exception as e:
        print("Error occured", e)
        exit(1)

def get_ohlc_data_for_one_day(product, fromDate, toDate) -> pd.DataFrame:
    url = f"https://api.exchange.coinbase.com/products/{product}/candles?granularity=300&start={fromDate}&end={toDate}"
    
    try:
        btc = requests.get(url)
        raw = btc.json()
        df = pd.DataFrame(raw, columns = ["ticktimestamp", "lowprice", "highprice", "openprice", "closeprice", "volume"])
        return df
    except Exception as e:
        print("Error occured", e)