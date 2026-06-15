from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger

STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()

    def initiate_data_validation(self):
        data_validation_config = self.config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)

        return data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        pipeline = DataValidationTrainingPipeline()
        result = pipeline.initiate_data_validation()

        if not result:
            raise ValueError("Data validation failed")

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception:
        logger.exception("Error occurred during data validation stage")
        raise