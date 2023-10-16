import os
import pandas as pd
import numpy as np

from src.components.data_ingestion import data_ingestion

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass #type:ignore 

from src.utils import save_object

@dataclass
class preprocesser:
    ss = StandardScaler()
    ohe = OneHotEncoder()

class transformer:
    def __init__(self):
        obj_ingestion=data_ingestion()
        self.train_df,self.test_df = obj_ingestion.get_paths()
        self.preprocesser = preprocesser()
        
    
    def transform(self):
        train_data = pd.read_csv(self.train_df)
        test_data = pd.read_csv(self.test_df)

        x_train = train_data.drop(columns="math_score")
        y_train = train_data['math_score']

        x_test = test_data.drop(columns="math_score")
        y_test = test_data["math_score"]

        num_cols = x_train.select_dtypes(include="number").columns
        cat_cols = x_train.select_dtypes(exclude="number").columns

        num_pipeline = Pipeline(
            steps = [
                ("Number_Imputation",SimpleImputer(strategy="median")),
                ("Standardization",self.preprocesser.ss)
            ]
        )

        cat_pipeline = Pipeline(
            steps=[
                ("Categorical_Imputation",SimpleImputer(strategy="most_frequent")),
                ("OHE",self.preprocesser.ohe)
            ]
        )        

        preprocesser = ColumnTransformer([
            ("Numerical_Pipeline",num_pipeline,num_cols),
            ("Categorical_Pipeline",cat_pipeline,cat_cols)
        ])

        x_train_preprocessed = preprocesser.fit_transform(x_train)

        x_test_preprocessed = preprocesser.transform(x_test)

        # pd.DataFrame(x_train_preprocessed).to_csv(os.path.join("artifacts","xtrain.csv"),index=False)
        # pd.DataFrame(x_test_preprocessed).to_csv(os.path.join("artifacts","xtest.csv"),index=False)

        save_object(preprocesser,os.path.join("artifacts","preprocessor1.pkl"))

        return ((x_train_preprocessed,y_train,x_test_preprocessed,y_test))
    
    def get_processed_data(self):
        return(self.transform())


if __name__=="__main__":
    obj = transformer()
    obj.transform()
