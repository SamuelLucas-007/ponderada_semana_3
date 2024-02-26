from src.config.dev_config import Dev_Config
from src.config.production import Production_Config

class Config:
  def __init__(self):
    self.dev_config = Dev_Config()
    self.production_config = Production_Config()