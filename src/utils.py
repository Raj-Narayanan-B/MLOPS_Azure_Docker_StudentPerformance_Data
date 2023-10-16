import pickle #type: ignore
import joblib
import dill #type: ignore

import os

from sklearn.metrics import r2_score

def save_object(object,object_path):
    # joblib.dump(object,object_path)

    with open(object_path,'wb') as file:
        pickle.dump(object,file)    

    # with open(object_path,'wb') as file:
    #     dill.dump(object,file)  

def evaluate_model(models,data):
    x_train,y_train,x_test,y_test = data
    report = {}
    for model_name,model in models.items():

        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        r2 = r2_score(y_test,y_pred)

        report[model_name] = r2

    return (report)
