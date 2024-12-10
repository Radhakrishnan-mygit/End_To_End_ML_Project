import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
   train_data_path:str=os.path.join("artifacts","train_data.csv")
   test_data_path:str=os.path.join("artifacts","test_data.csv")
   raw_data_path:str=os.path.join("artifacts","raw_data.csv")

class DataIngestion:
   def __init__(self):
      self.ingestion_config=DataIngestionConfig()

   def initiate_data_ingestion(self):
      logging.info("Entered Data Ingestion module")
      try:
         df=pd.read_csv(r"notebook\data\stud.csv")
         logging.info("read dataset..")

         os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
         df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

         train_data,test_data=train_test_split(df,test_size=.2,random_state=42)

         train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
         test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
         logging.info("Data Ingestion is completed...")

         return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
         )
      except Exception as e:
         logging.error("Error in reading dataset")
         raise CustomException(e,sys)
   
if __name__=="__main__":
   obj=DataIngestion()
   obj.initiate_data_ingestion()