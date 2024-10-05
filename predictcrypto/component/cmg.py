import sys
#import fire # type: ignore
# import joblib

from predictcrypto.exception import CustomException
from predictcrypto.logger import logging

from predictcrypto.pipeline.data_pipeline import DataPipeline
from predictcrypto.pipeline.transformation_pipeline import TransformationPipeline

from predictcrypto.component.train import BestModel

# from exception import CustomException
# from logger import logging

# from pipeline.data_pipeline import DataPipeline
# from pipeline.transformation_pipeline import TransformationPipeline

# from train import BestModel

from prophet.serialize import model_to_json, model_from_json # type: ignore

def training_manager(modelname: str) -> None:
    try:
        logging.info("Invoking the data pipeline for training...")
        dp = DataPipeline()
        raw = dp.build_base_data_pipeline()
        
        logging.info("raw data fetched from data sources...!!")

        tp = TransformationPipeline()
        df = tp.make_transformation(raw)

        logging.info("raw data transformation completed...!!")
        logging.info("Getting ready for model ")
        
        logging.info("Initiating model invokation...!!")
        model = BestModel()
        estimator = model.model_training(df)
        
        if modelname == "prophet":
            with open('serialized_model.json', 'w') as fout:
                fout.write(model_to_json(estimator))  # Save model

            # with open('serialized_model.json', 'r') as fin:
            #     m = model_from_json(fin.read())  # Load model
        

    except Exception as e:
        raise CustomException(e, sys)