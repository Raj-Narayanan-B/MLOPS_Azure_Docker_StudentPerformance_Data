import os
import sys

from src.exception import CustomException
from src.components.data_transformer import transformer
from src.utils import evaluate_model,save_object
from dataclasses import dataclass #type: ignore

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

@dataclass
class modelconfig_path:
    model_path = os.path.join("artifacts","model.pkl")

class model_trainer:
    try:
        def __init__(self):
            self.model_config = modelconfig_path()

        def train_model(self):
            transformer_object = transformer()
            x_train, y_train, x_test, y_test = transformer_object.get_processed_data()

            models = {
                "Decision_Tree": DecisionTreeRegressor(),
                "Random_Forest": RandomForestRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                "GradientBoost": GradientBoostingRegressor(),
                # "XGBoost": XGBRegressor(),
                "CatBoost": CatBoostRegressor(silent=True),
                "Linear_Regression": LinearRegression()
            }

            data=list((x_train,y_train,x_test,y_test))

            report = evaluate_model(models,data)

            # best_model = max(report, key = report.get)

            best_score = max(report.values())

            for i,j in report.items():
                if j==best_score:
                    best_model = i

            save_object(object = models[best_model], object_path=self.model_config.model_path)
            
            print(report)
            print (best_model)
            print (best_score)
    
    except Exception as e:
        raise CustomException(e,sys)


if __name__=="__main__":
    obj_model_trainer = model_trainer()
    obj_model_trainer.train_model()
        