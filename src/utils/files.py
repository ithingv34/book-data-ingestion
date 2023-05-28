import os
import logging.config
import yaml

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

class FileUtils:

    logger = None

    @staticmethod
    def setup_logger(config_file_path: str):
        with open(config_file_path, "r") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        FileUtils.logger = logging.getLogger("logger")
        return FileUtils.logger

    @staticmethod
    def read_file(file_path: str) -> str:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    contents = file.read()
                    FileUtils.logger.info(f"File successfully loaded from {file_path}")
                    return contents
            except Exception as e:
                FileUtils.logger.error(f'Failed to read file: {file_path}. Error {str(e)}')
        else:
            FileUtils.logger.warning(f'File does not exists: {file_path}')
            raise FileNotFoundError     

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        
        directory = os.path.dirname(file_path)

        if not os.path.exists(directory):
                os.makedirs(directory)        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
                FileUtils.logger.info(f"File successfully saved to {file_path}")
        except Exception as e:
            FileUtils.logger.error(f"Failed to write file: {file_path}. Error: {str(e)}")
