import sys

from src.predictcrypto.exception import CustomException
from src.predictcrypto.logger import logging


class BaseModel:
    def __init__(self):
        pass


class BestModel(BaseModel):
    def __init__(self):
        pass
    
    def model_training(self, X, y):
        pass
