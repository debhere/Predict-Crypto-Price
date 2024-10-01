import sys

from dataclasses import dataclass
from typing import Any
from sqlalchemy import create_engine

from predictcrypto.exception import CustomException
from predictcrypto.logger import logging

from predictcrypto.utils.config_manager import fetch_database_configurations



@dataclass
class DataSourceConfig:
    server, db, driver = fetch_database_configurations() 

class ConnectionManager:
    def __init__(self):
        self.configs = DataSourceConfig()

    def establish_connection(self) -> Any:
        try:
            server = self.configs.server
            db = self.configs.db
            driver = self.configs.driver

            logging.info("Retrieving database connection details")

            conn_string = f'mssql://@{server}/{db}?driver={driver}'
            engine = create_engine(conn_string)
            
            logging.info("Establishing database connection")

            return engine

        except Exception as e:
            raise CustomException(e, sys)


