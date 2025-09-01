import os
from src.DataScienceProject import logger
from sklearn.model_selection import train_test_split
from src.DataScienceProject.entity.config_entity import (DataTransformationConfig)
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # Note you can add different data transformation techniques such as Scaler, PCA and all
    
    def train_test_splitting(self):
        # Read CSV with semicolon separator (like your wine dataset)
        data = pd.read_csv(self.config.data_path, sep=';')
        
        # Split the data into train and test sets
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")
        
        print(f"Train shape: {train.shape}")            
        print(f"Test shape: {test.shape}")