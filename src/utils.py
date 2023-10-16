import pickle #type: ignore
import joblib
import dill #type: ignore
import os
import yaml

from sklearn.model_selection import GridSearchCV



from sklearn.metrics import r2_score

def save_object(object,object_path):
    with open(object_path,'wb') as file:
        pickle.dump(object,file)    

    #             OR

    # with open(object_path,'wb') as file:
    #     dill.dump(object,file)  

    #             OR

    # joblib.dump(object,object_path)


def evaluate_model(models,data):
    x_train,y_train,x_test,y_test = data
    report = {}
    for model_name,model in models.items():
        if model_name != "Linear_Regression":
            best_params = hyper_parameter_tuning(model_name,model,data)
            model.set_params(**best_params)
            model.fit(x_train,y_train)
            y_pred = model.predict(x_test)
            r2 = r2_score(y_test,y_pred)
            report[model_name] = r2
        else:
            model.fit(x_train,y_train)
            y_pred = model.predict(x_test)
            r2 = r2_score(y_test,y_pred)
            report[model_name] = r2
    return (report)

def hyper_parameter_tuning(model_name,model,data):
    x_train,y_train,x_test,y_test = data
    config=get_config()
    param_grid = {}
    for i in config["params"]:
        if i == model_name:
            param_grid = config["params"][i]
            break
    
    gs = GridSearchCV(estimator=model,
                      param_grid=param_grid,
                      scoring = "r2")
    gs.fit(x_train,y_train)
    print (model)
    print (gs.best_params_,"\n")
    
    return(gs.best_params_)
    
                              

def get_config():
    with open("params.yaml") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return (config)