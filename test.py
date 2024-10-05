import sys
import requests
import pandas as pd
from datetime import datetime
from predictcrypto.exception import CustomException
from predictcrypto.pipeline.data_pipeline import DataPipeline
from predictcrypto.pipeline.transformation_pipeline import TransformationPipeline


if __name__ == "__main__":
    dp = DataPipeline()
    df = dp.build_static_data_pipeline()

    tp = TransformationPipeline()
    df_ = tp.make_transformation(df)
    print(df_.head())
    