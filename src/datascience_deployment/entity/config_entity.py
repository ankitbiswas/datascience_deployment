from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL:str 
    local_data_file: Path 
    unzip_dir: Path 


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path 
    STATUS_FILE: str
    all_schema: dict ## for the schema.yaml which has the column details 


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path 