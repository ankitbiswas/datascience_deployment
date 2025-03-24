import pandas as pd
import os 
from src.datascience_deployment import logger
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.datascience_deployment.entity.config_entity import ModelEvaluationConfig
from src.datascience_deployment.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.datascience_deployment.utils.common import read_yaml,create_directories,save_json

os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/ankitbiswas008/datascience_deployment.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME']='ankitbiswas008'
os.environ['MLFLOW_TRACKING_PASSWORD']='eb9fc481646c52c5e2740778b48ba9d38d70f9a5'

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config

    def evaluation_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse, mae, r2 
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme 
        print(tracking_url_type_store)

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.evaluation_metrics(test_y,predicted_qualities)

            # Saving metrics in local 
            scores = {"rmse":rmse,"mae":mae,"r2":r2}
            # save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("r2",r2)
            mlflow.log_metric("mae",mae)

            #Model registry does not work with file store
            if tracking_url_type_store!="file":
                print(model)
                mlflow.sklearn.log_model(model,"model", registered_model_name = "ElasticModel")

            else:
                mlflow.sklearn.log_model(model,"model")
