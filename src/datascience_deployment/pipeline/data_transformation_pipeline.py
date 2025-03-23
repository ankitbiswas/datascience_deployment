from src.datascience_deployment.config.configuration import ConfigurationManager
from src.datascience_deployment.entity.config_entity import DataTransformationConfig
from src.datascience_deployment.components.data_transformation import DataTransformation
from src.datascience_deployment import logger 
from pathlib import Path


STAGE_NAME = "DATE TRANSFORMATION STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            config=ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)

            data_transformation.train_test_splitting()

        except Exception as e:
            raise e 
        

if __name__ =="__main__":
    try:
        with open(Path("artifacts/data_validation/status.txt"),'r') as f:
            status=f.read().split(" ")[-1]
        if status=="True":
            logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
            obj = DataTransformationTrainingPipeline()
            obj.initiate_data_transformation()
            logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
        else:
            raise Exception("your data schema is not valid")
    except Exception as e:
        print(e)