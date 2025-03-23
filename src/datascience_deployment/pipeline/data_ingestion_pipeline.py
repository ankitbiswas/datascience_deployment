from src.datascience_deployment.config.configuration import ConfigurationManager
from src.datascience_deployment.entity.config_entity import DataIngestionConfig
from src.datascience_deployment.components.data_ingestion import DataIngestion
from src.datascience_deployment import logger 


STAGE_NAME = "DATE INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e 
        

if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        raise e