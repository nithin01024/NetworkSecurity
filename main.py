from networksecurity.components.data_injection import DataInjection
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import CoustomException
from networksecurity.logging.logging import logging
import sys
from networksecurity.entity.confi_entity import DataInjectionConfig,DataValidationConfig
from networksecurity.entity.confi_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        datainjectionconfig = DataInjectionConfig(trainingpipelineconfig)
        data_injection = DataInjection(datainjectionconfig)
        logging.info('initiate the data injection')
        datainjectionartifact=data_injection.initiate_data_ingestion()
        logging.info('data injection completed')
        print(datainjectionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)

        data_validation = DataValidation(datainjectionartifact,data_validation_config)
        logging.info('initiate the data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('data validation completed')
        print(data_validation_artifact)
        
    except Exception as e:
        raise CoustomException(e,sys)