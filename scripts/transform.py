import pandas as pd
from extract import pull_data
from datetime import datetime

def transform():
    batches = pull_data()
    df = pd.DataFrame(batches, columns = ["ticktimestamp", "lowprice", "highprice", "openprice", "closeprice", "volume"])
    timestamps = [batch[0] for batch in batches]
    tickdatetime = [datetime.fromtimestamp(timestamp).strftime('%Y%m%d %H:%M') for timestamp in timestamps]
    df["tickdatetime"] = tickdatetime
    #print(df)
    return df

if __name__ == "__main__":
    transform()