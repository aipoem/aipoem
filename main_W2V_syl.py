import os
from Model_syl import Poema
import sys
import logging
import yaml

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S%p')

    logger = logging.getLogger(__name__)

    logger.info('Loading configuration file')
    with open(os.path.join("config_file", "Model_syl_params.yaml"), 'r') as stream:
        setting = yaml.load(stream)

    mymodel = Poema(setting)
    modello = mymodel.train()

    if setting['save']:
        logger.info("Let's check what our model learnt!")
        mymodel.save_model()
