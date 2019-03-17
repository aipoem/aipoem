import yaml
import sys
import os
from ETL import ETL
import logging

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S%p')

    logger = logging.getLogger(__name__)

    logger.info('Loading configuration file')
    with open(os.path.join("config_file", "ETL_params.yaml"), 'r') as stream:
        setting = yaml.load(stream)

    my_etl = ETL(setting)
    my_etl.parse()
    my_etl.download()
