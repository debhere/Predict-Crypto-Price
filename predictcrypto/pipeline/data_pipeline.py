import sys
import pandas as pd
from dataclasses import dataclass
from predictcrypto.utils.configurations import fetch_database_configurations
from predictcrypto.logger import logging
from predictcrypto.exception import CustomException
from sqlalchemy import create_engine

@dataclass
class DataPipelineConfig:
    server, db, driver = fetch_database_configurations()  

class DataPipeline:
    def __init__(self):
        self.configs = DataPipelineConfig()
    def initiate_data_collection(self):
        try:
            db = self.configs.db
            server = self.configs.server
            driver = self.configs.driver

            logging.info("Retrieving database connection details")

            conn_string = f'mssql://@{server}/{db}?driver={driver}'
            engine = create_engine(conn_string)

            logging.info("Establishing database connection")

            with engine.connect() as conn, conn.begin():
                data = pd.read_sql_table("staging.coinbasebtcpricerawdata", conn)
                logging.info("Connection successful...!!!")

            return data
        except Exception as e:
            raise CustomException(e, sys)