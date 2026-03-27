# utils.py

import os
import datetime
import logging
import json
from typing import Dict, List

def get_current_time() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_data_to_file(file_path: str, data: Dict) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_data_from_file(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_log_file_path() -> str:
    return os.path.join(os.path.dirname(__file__), '../logs', 'app.log')

def configure_logging(log_file_path: str = None) -> None:
    if log_file_path is None:
        log_file_path = get_log_file_path()
    logging.basicConfig(filename=log_file_path, level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger

def get_config() -> Dict:
    try:
        with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}