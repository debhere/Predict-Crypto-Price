import os
from pathlib import Path
from typing import Tuple
import yaml

CURR_DIR = "scripts"
CONFIG_FILENAME = "source.yaml"
CONFIG_FOLDERNAME = "_config"
DB_CONFIG = "database.yaml"

def get_etl_config() -> Tuple:
    
    try:
        interim_path, raw_path, trans_path = None, None, None
        CONFIG_FILE_PATH = Path(os.path.join(CURR_DIR, CONFIG_FOLDERNAME, CONFIG_FILENAME))
            
        with open(CONFIG_FILE_PATH) as ds:
            all_config:dict = yaml.safe_load(ds)
            
            ROOT_FOLDER = all_config["folder"]
            RAW_FILENAME = all_config["raw"]
            TRANS_FILENAME = all_config["transform"]
            INTERIM_FILENAME = all_config["interim"]

            os.makedirs(ROOT_FOLDER, exist_ok=True)

            raw_path = os.path.join(ROOT_FOLDER, RAW_FILENAME)
            interim_path = Path(os.path.join(ROOT_FOLDER, INTERIM_FILENAME))
            trans_path = Path(os.path.join(ROOT_FOLDER, TRANS_FILENAME))

    except Exception as e:
        print(e)

    return raw_path, interim_path, trans_path


def fetch_database_configurations() -> Tuple:

    CONFIG_FILE_PATH = Path(os.path.join(CURR_DIR, CONFIG_FOLDERNAME, DB_CONFIG))

    with open(CONFIG_FILE_PATH) as cfg:
        all_config:dict = yaml.safe_load(cfg)

        SERVER:str = all_config["SERVER"]
        DATABASE: str = all_config["DATABASE"]
        DRIVER:str = all_config["DRIVER"]

    return SERVER, DATABASE, DRIVER