import os
from abc import abstractmethod, ABC

import requests

from utils.files import FileUtils
from utils.http_message import HTTPMessage

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)
CONFIG_FILE_PATH = os.path.join(PROJECT_PATH, 'config.yml')
TEMP_FOLDER_PATH = os.path.join(PROJECT_PATH, "temp")

class BaseScraper(ABC):
    def __init__(self):
        self.logger = FileUtils.setup_logger(CONFIG_FILE_PATH)

    def check_and_load_data(self, code:str, message: HTTPMessage) -> str:
        
        file_path = os.path.join(TEMP_FOLDER_PATH, f'{code}.txt')

        try:
            content = FileUtils.read_file(file_path)
        except FileNotFoundError:
            url, headers, params = message.__dict__.values()
            response = requests.get(url=url, headers=headers, params=params)
            response.raise_for_status()
            content = response.text
            FileUtils.write_file(file_path, content)

        return content
    
    
