from src.datascience_deployment import logger
from datascience_deployment.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from datascience_deployment.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from datascience_deployment.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from datascience_deployment.pipeline.model_train_pipeline import ModelTrainingPipeline
from datascience_deployment.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
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



STAGE_NAME = "MODEL TRAIN STAGE"



try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_train = ModelTrainingPipeline()
    model_train.initiate_model_train()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    raise e





STAGE_NAME = "MODEL EVALUATION STAGE"



try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    raise e
