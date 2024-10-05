import sys
#import requests
import pandas as pd
from datetime import datetime
from predictcrypto.exception import CustomException
from predictcrypto.pipeline.data_pipeline import DataPipeline
from predictcrypto.pipeline.transformation_pipeline import TransformationPipeline

from predictcrypto.component.train import BestModel
from predictcrypto.component.cmg import training_manager

if __name__ == "__main__":
    training_manager("prophet")
    