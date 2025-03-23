## component - Data Ingestion 
import urllib.request as request 
from src.datascience_deployment import logger
import zipfile 
import os 
import shutil
from src.datascience_deployment.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config

    ## Download the zip file 
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n {headers}")
        
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        """
        zip_file_path:str 
        Extracts the zip file into data directory 
        Function returns none
        
        """
        unzip_path = self.config.unzip_dir
        zip_file = self.config.local_data_file

        os.makedirs(unzip_path,exist_ok=True)
        zip_file = os.path.join(self.config.local_data_file)

        try:
            shutil.unpack_archive(zip_file, unzip_path)
            print("Extraction successful!")
        except shutil.ReadError:
            print("Unknown format or corrupted file.")