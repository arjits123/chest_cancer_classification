from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data ingestion Stage"

try:
    logger.info(f'>>> stage {STAGE_NAME} has started <<<<')
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f'>>> stage {STAGE_NAME} has completed <<<<')
except Exception as e:
    logger.exception(e)
    raise e