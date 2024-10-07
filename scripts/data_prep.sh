#! /bin/bash

rm -rf downloads

echo "Downloading data...!!!"

product="BTC-USD"
start_date="20240101"
end_date="20241006"

python scripts/data_loader.py $product $start_date $end_date

sleep 2

rm -rf downloads

echo "Data loading completed...!!!"



