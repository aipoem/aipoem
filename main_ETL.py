import yaml
import sys
import os
from ETL import ETL
import logging

def load_yaml(filename: str) -> dict:
    """
    Utility function to load a yaml file into a pyhon dict
    Parameters:
    - filename: str -> fullpath of the yaml file
    """
    assert (filename.endswith("yaml") or filename.endswith("yml")), "Not a yaml extention!"
    with open(filename, 'r', encoding="utf-8") as handler:
        return yaml.load(handler, Loader=yaml.FullLoader)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S%p')

    logger = logging.getLogger(__name__)

    logger.info('Loading configuration file')
    setting = load_yaml(os.path.join("config_file", "ETL_params.yaml"))

    my_etl = ETL(setting)
    my_etl.download()
    my_etl.parse(verbose=False)
