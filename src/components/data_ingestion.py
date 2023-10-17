import os
import sys # type: ignore
import pandas as pd
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass # type: ignore

@dataclass
class data_path:
    train_data_path = os.path.join("artifacts","train.csv")
    test_data_path = os.path.join("artifacts","test.csv")
    
class data_ingestion:
    def __init__(self):
        self.train_path = data_path.train_data_path
        self.test_path = data_path.test_data_path
        logging.info("Train-Test paths created")

    def data_load(self):
        try:    
            data_path = os.path.join("artifacts","data.csv")
            df = pd.read_csv(data_path)
            logging.info("Data loaded")

            train_data,test_data = train_test_split(df,test_size=.25,random_state=8)
            logging.info("Train_data, Test_data split successful")

            train_data.to_csv(self.train_path,index=False)
            test_data.to_csv(self.test_path,index=False)
            logging.info("Train_data, Test_data loaded")

            return (train_data,test_data)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_paths(self):
        return (self.train_path,self.test_path)
        
if __name__=="__main__":
    obj=data_ingestion()
    train_data,test_data = obj.data_load()
