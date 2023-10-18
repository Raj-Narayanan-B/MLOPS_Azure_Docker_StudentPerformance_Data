from flask import Flask, request, render_template
import os
import pandas as pd
from src.pipeline.predict_pipeline import prediction

application = Flask(__name__)

app = application

@app.route("/")
def index1():
    return render_template("index.html")

@app.route("/predict_data", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return render_template('home.html')
    else:
        data = {}
        columns = pd.read_csv("artifacts/data.csv").drop(columns="math_score").columns.tolist()
        for i in columns:
            data[i] = request.form[i]
        
        prediction_obj = prediction()

        result = prediction_obj.predict(data)

        return render_template('home.html', results = result)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)