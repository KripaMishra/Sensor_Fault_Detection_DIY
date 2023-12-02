import os 
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


SAVED_MODEL_DIR = os.path.join("saved_models")

#training pipeline variables

# prerpocessing constants
TARGET_COLUMN= "class"
PIPELINE_NAME:str = "sensor"
ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "sensor.csv"

#train,test constants
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
PREPROCESSING_OBJECT_FILE_NAME: str= "preprocessor.pkl"

#model training constants

MODEL_FILE_NAME:str = "model.pkl"
SCHEMA_FILE_PATH= os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS= "drop_columns"

"""
Data Ingestion Constants
"""
DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2