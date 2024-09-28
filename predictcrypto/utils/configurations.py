import sys
from . import *
import os
import yaml
from pathlib import Path
from typing import Tuple

from predictcrypto.exception import CustomException
from predictcrypto.logger import logging

def fetch_database_configurations() -> Tuple:
    try:
        logging.info("Getting the configurations")
        CONFIG_PATH:Path = Path(os.path.join(CONFIG_FOLDER, CONFIG_FILENAME))

        with open(CONFIG_PATH) as cfg:
            all_config:dict = yaml.safe_load(cfg)

            SERVER:str = all_config["SERVER"]
            DATABASE: str = all_config["DATABASE"]
            DRIVER:str = all_config["DRIVER"]

            logging.info("DB Configurations are ready..!!!")

        return SERVER, DATABASE, DRIVER
    except Exception as e:
        raise CustomException(e, sys)