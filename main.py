from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    object = DataIngestionTrainingPipeline()
    object.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e