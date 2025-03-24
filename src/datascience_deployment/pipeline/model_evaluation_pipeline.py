from src.datascience_deployment.config.configuration import ConfigurationManager
from src.datascience_deployment.entity.config_entity import DataValidationConfig
from src.datascience_deployment.components.data_validation import DataValidation
from src.datascience_deployment.components.model_evaluation import ModelEvaluation
from src.datascience_deployment import logger 


STAGE_NAME = "MODEL EVALUATION STAGE"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config=ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()

        except Exception as e:
            raise e 
        

if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        raise e