import pandas as pd
from datetime import datetime
from config import get_etl_config


def transform_ohlc_data(product:str = "BTC-USD") -> None:
    _, interim_path, trans_path = get_etl_config()
    trans = pd.read_csv(interim_path)
    idx = trans[trans["ticktimestamp"].isna()].index
    trans.drop(idx, inplace=True)
    
    trans["ticktimestamp"] = trans["ticktimestamp"].astype("int64")
    trans["TickDatetime"] = trans["ticktimestamp"].apply(lambda x: datetime.fromtimestamp(x))
    trans["product"] = product

    trans.to_csv(trans_path, index=False)
    
if __name__ == "__main__":
    #transform()
    transform_ohlc_data()