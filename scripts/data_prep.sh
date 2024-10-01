#! /bin/bash

rm -rf downloads

echo "Starting data loading...!!!"

product="BTC-USD"
start_date="20240101"
end_date="20240630"

python scripts/data_loader.py $product $start_date $end_date

sleep 2

rm -rf downloads

echo "Data loading completed...!!!"



