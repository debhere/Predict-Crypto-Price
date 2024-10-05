import sys
import pandas as pd
from typing import Dict, Any

from prophet import Prophet # type: ignore

from predictcrypto.exception import CustomException
from predictcrypto.logger import logging


class BaseModel:
    def __init__(self, model_name="prophet"):
        self.name = model_name
    
    def model_list(self) -> Dict:
        try:
            logging.info("Loading list of base models")
            
            models = {
                "prophet": Prophet()
            }

            return models
        
        except Exception as e:
            raise CustomException(e, sys)


class BestModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def model_training(self, df) -> Any:
        try:
            model = self.model_list()[self.name]

            logging.info("invoking the base model")
            
            if self.name != "prophet":
                logging.info("Model not supported currently...!!")
                exit(1)

        except Exception as e:
            raise CustomException(e, sys)
        
        model.fit(df)

        return model
