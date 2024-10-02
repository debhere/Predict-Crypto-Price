import fire
from extract import get_ohlc_data_from_coinbase
from transform import transform_ohlc_data
from load import push_data_to_db

def fetch_remote_data(product:str, from_date:str, to_date:str):
    try:
        from_date = str(from_date)
        to_date = str(to_date)

        get_ohlc_data_from_coinbase(product, from_date, to_date)
        transform_ohlc_data(product)
        push_data_to_db()

    except Exception as e:
        print("Error occured", e)


if __name__ == "__main__":
    fire.Fire(fetch_remote_data)