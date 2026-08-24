import os
import sys
import pandas as pd
import numpy as np

"""
Defining common constant variables for training pipeline
"""
TARGET_COLUMN = 'Result'
PIPELINE_NAME: str= 'NetworkSecurity'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME:str = 'phisingData.csv'

TRAIN_FILE_NAME : str='train.csv'
TEST_FILE_NAME : str = 'test.csv'

"""
Data injection related constants
"""
DATA_INJECTION_COLLECTION_NAME : str= 'NetworkData'
DATA_INJECTION_DATABASE_NAME : str = 'Nithin_Data_Science'
DATA_INJECTION_DIR_NAME : str= 'data_injection'
DATA_INJECTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INJECTION_INJESTED_DIR: str= 'ingested'
DATA_INJECTION_TRAIN_TEST_SPLIT_RATIO: float=0.2

