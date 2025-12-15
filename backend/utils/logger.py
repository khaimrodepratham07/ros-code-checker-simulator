import logging
import os


def setup_logger(name, log_file):
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logger = logging.getLogger(name)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
return logger