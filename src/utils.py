import logging

class Logging:
  def __init__(self, log_file='app.log'):
    self.log_file = log_file
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Configuration of manipluation of logs in file
    file_handler = logging.FileHandler(self.log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)
    
    # Configuration of manipulation of logs in console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    self.logger.addHandler(console_handler)
    
  def log_info(self, message):
    self.logger.info(message)
    
  def log_debug(self, message):
    self.logger.debug(message)
    
  def log_warning(self, message):
    self.logger.warning(message)
    
  def log_error(self, message):
    self.logger.error(message)
    
  def log_critical(self, message):
    self.logger.critical(message)
  
  