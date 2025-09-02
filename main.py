from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.Data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DataScienceProject.pipeline.Data_validation_pipeline import DataValidationTrainingPipeline
from src.DataScienceProject.pipeline.Data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DataScienceProject.pipeline.Model_trainer_pipeline import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj_ingestion = DataIngestionTrainingPipeline()
        obj_ingestion.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Data Validation Stage"
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj_validation = DataValidationTrainingPipeline()
        obj_validation.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    STAGE_NAME = "Data Transformation Stage"
    
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj_transformation = DataTransformationTrainingPipeline()
        obj_transformation.initiate_data_transformation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    STAGE_NAME = "Model Trainer Stage"
    
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj_training = ModelTrainerTrainingPipeline()
        obj_training.initiate_model_training()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e