import os
import urllib.request as request
from src.DataScienceProject import logger
import zipfile
from src.DataScienceProject.entity.config_entity import (DataIngestionConfig)
from src.DataScienceProject.config.configuration import ConfigurationManager



class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        
    # Downloadig the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exists")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Functions returns None
        
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        
        # Check if the file is actually a zip file
        if str(self.config.local_data_file).endswith('.zip'):
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file to {unzip_path}")
        else:
            logger.info(f"File {self.config.local_data_file} is not a zip file, skipping extraction")
            # For non-zip files like CSV, just log that they're ready to use
            logger.info(f"Data file is ready at: {self.config.local_data_file}")