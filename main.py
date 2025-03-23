from src.datascience_deployment import logger
from datascience_deployment.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from datascience_deployment.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from datascience_deployment.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "DATE INGESTION STAGE"



try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    raise e

logger.info("Welcome to our custom logging data science")




STAGE_NAME = "DATE VALIDATION STAGE"



try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    raise e

logger.info("Welcome to our custom logging data science")




STAGE_NAME = "DATE TRANSFORMATION STAGE"



try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    raise e

logger.info("Welcome to our custom logging data science")