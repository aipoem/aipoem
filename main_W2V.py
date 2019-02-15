import spacy
import os
from Model import poema
import glob
import sys
import logging
import gensim
import yaml


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S%p')

    logger = logging.getLogger(__name__)

    logger.info('Loading configuration file')
    with open(os.path.join("config_file", "Model_params.yaml"), 'r') as stream:
        setting = yaml.load(stream)

    mymodel = poema(setting)
    modello = mymodel.train()

    logger.info("Let's check what our model learnt!")

    logger.info("TEST 1: find analogies of a given word")
    mymodel.nearest_neighbors('amore')

    logger.info("TEST 2: complete the analogy")
    mymodel.find_analogies('spada', 'cavalier', 'moro')
