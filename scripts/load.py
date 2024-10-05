import pandas as pd
from sqlalchemy import create_engine # type: ignore
from config import get_etl_config, fetch_database_configurations


def push_data_to_db() -> None:

    server, database, driver = fetch_database_configurations()
    conn_string = f'mssql://@{server}/{database}?driver={driver}'

    engine = create_engine(conn_string)
    connection = engine.connect()

    _, _, trans_path = get_etl_config()

    trans = pd.read_csv(trans_path)

    trans.to_sql(name = "coinbasebtcpricerawdata", con = connection, schema = "staging", 
               if_exists = "append", index = False)
