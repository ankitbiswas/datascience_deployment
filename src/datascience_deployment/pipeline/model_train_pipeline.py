from src.datascience_deployment.config.configuration import ConfigurationManager
from src.datascience_deployment.entity.config_entity import DataValidationConfig
from src.datascience_deployment.components.data_validation import DataValidation
from src.datascience_deployment.components.model_train import ModelTrain
from src.datascience_deployment import logger 


STAGE_NAME = "DATE TRAIN STAGE"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_train(self):
        try:
            config=ConfigurationManager()
            model_train_config = config.get_model_train_config()
            model_train = ModelTrain(config=model_train_config)
            model_train.train()

        except Exception as e:
            raise e 
        

if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_train()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        raise e