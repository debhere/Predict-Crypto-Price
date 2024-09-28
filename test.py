import sys
import requests
import pandas as pd
from datetime import datetime
from predictcrypto.exception import CustomException

def test():
    start = "20240101"
    end = "20240831"

    days = pd.date_range(start=start, end=end)
    days = [day.strftime('%Y%m%d') for day in days]
    print(days)

if __name__ == "__main__":
    test()
    