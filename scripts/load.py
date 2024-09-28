import pandas as pd
from sqlalchemy import create_engine
from config import get_etl_config
from ..config import configurations
#from ..predictcrypto import logger

def push_data_to_db() -> None:
    # server='DESKTOP-OKR44CT'
    # Database = 'crypto'
    # Driver = 'ODBC driver 17 for SQL Server'
    server, database, driver = configurations.fetch_database_configurations()

    conn_string = f'mssql://@{server}/{database}?driver={driver}'


    engine = create_engine(conn_string)
    connection = engine.connect()

    _, _, trans_path = get_etl_config()

    trans = pd.read_csv(trans_path)

    trans.to_sql(name = "coinbasebtcpricerawdata", con = connection, schema = "staging", 
               if_exists = "append", index = False)
    

if __name__ == "__main__":
    # load()
    push_data_to_db()
