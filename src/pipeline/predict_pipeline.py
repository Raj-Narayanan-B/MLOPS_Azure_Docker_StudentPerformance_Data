import pandas as pd
from src.utils import load_object,get_config

class prediction:
    def __init__(self):
        self.config = get_config()
        self.preprocessor_path = self.config["preprocesser"]
        self.model_path = self.config["model"]
        self.preprocessor = load_object(self.preprocessor_path)
        self.model = load_object(self.model_path)

    def predict(self,data):
        df = pd.DataFrame(data, index = [0])

        df_preprocessed = self.preprocessor.transform(df)

        pred = self.model.predict(df_preprocessed)

        return (pred)



