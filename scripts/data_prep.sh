#! /bin/bash

rm -rf downloads

echo "Downloading data...!!!"

#products=("BTC-USD", "ETH-USD", "DOGE-USD", "LTC-USD", "USDT-USD")

end_date="$(date --date="yesterday" "+%Y%m%d")"

if [ "$1" != "y" ]
then 
    start_date="$(date --date="-2 days" "+%Y%m%d")"
else
    start_date="20240101"
fi


python scripts/data_loader.py $start_date $end_date

sleep 2

rm -rf downloads

echo "Data loading completed...!!!"



