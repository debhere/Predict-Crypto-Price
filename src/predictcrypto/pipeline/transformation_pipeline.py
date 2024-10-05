import sys
import pandas as pd
from src.predictcrypto.exception import CustomException
from src.predictcrypto.logger import logging


class TransformationPipeline:
    
    def make_transformation(self, df) -> pd.DataFrame:
        try:
            logging.info("Inside Transformation Pipeline")
            #df = self.dp.build_pipeline()
            df["tot"] = df["lowprice"] + df["highprice"] + df["openprice"] + df["closeprice"]
            df["twap"] = df["tot"] / 4

            df["trademonth"] = df["tickdatetime"].dt.month
            df["tradeday"] = df["tickdatetime"].dt.day
            df["tradehour"] = df["tickdatetime"].dt.hour
            df["trademin"] = df["tickdatetime"].dt.minute

            df.index = df["tickdatetime"]

            df_ = df.drop(columns=["tot", "lowprice", "highprice", "openprice", "closeprice", "ticktimestamp", "product", "tickdatetime"])

            logging.info("Transformation complete for training data.")
            return df_
        except Exception as e:
            raise CustomException(e, sys)