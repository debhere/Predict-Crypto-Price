#! /bin/bash

rm -rf downloads

echo "Downloading data...!!!"

#products=("BTC-USD", "ETH-USD", "DOGE-USD", "LTC-USD", "USDT-USD")
#product="BTC-USD"
start_date="20240101"
end_date="20241014"

#python scripts/data_loader.py $product $start_date $end_date

python scripts/data_loader.py $start_date $end_date

sleep 2

rm -rf downloads

echo "Data loading completed...!!!"



