import sys
import pandas as pd

from predictcrypto.utils.datasource import ConnectionManager
from predictcrypto.logger import logging
from predictcrypto.exception import CustomException



class DataPipeline:
    def __init__(self):
        self.cmg = ConnectionManager()

    def build_base_data_pipeline(self) -> pd.DataFrame:
        try:
            
            logging.info("Building the data pipeline...")

            engine = self.cmg.establish_connection()

            with engine.connect() as conn, conn.begin():
                logging.info("Connection established...!!")
                raw = pd.read_sql_table(table_name="coinbasebtcpricerawdata", con=conn, schema="staging")

            logging.info("Data is retrieved from the source DB...!!")
            return raw
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def build_stream_data_pipeline(self):
        pass