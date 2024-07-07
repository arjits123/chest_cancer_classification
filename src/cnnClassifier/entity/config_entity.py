from dataclasses import dataclass
from pathlib import Path


# Entity is created here
@dataclass(frozen=True)
class DataIngestionConfig:
  """Data Ingestion Config Class"""
  root_dir: Path
  source_URL: str
  local_data_file: Path
  unzip_dir: Path