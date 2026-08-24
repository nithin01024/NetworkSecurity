from networksecurity.components.data_injection import DataInjection
from networksecurity.exception.exception import CoustomException
from networksecurity.logging.logging import logging
import sys
from networksecurity.entity.confi_entity import DataInjectionConfig
from networksecurity.entity.confi_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        datainjectionconfig = DataInjectionConfig(trainingpipelineconfig)
        data_injection = DataInjection(datainjectionconfig)
        logging.info('initiate the data injection')
        datainjectionartifact=data_injection.initiate_data_ingestion()
        print(datainjectionartifact)
    except Exception as e:
        raise CoustomException(e,sys)