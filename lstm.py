import numpy as np
import pandas as pd
import glob
import yaml
import os

import gensim

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
# TODO: controllare np_utils

from Model_syl import Verso


def unique_poem(path):
    poem = []
    for _text in glob.glob(os.path.join(path, '*.txt')):
        for line in open(_text):
            poem.append(line.split())
    return poem


with open(os.path.join("config_file", "Model_syl_params.yaml"), 'r') as stream:
    setting = yaml.load(stream)

# load del modello w2v allenato sulle sillabe
mymodel = gensim.models.Word2Vec.load('w2v_syllable.model')

path_in = setting['path_in']

# rendo i testi un unico "poema" lunghissimo
text_list2d = unique_poem(path_in)
# il testo è una lista 2d -> la appiattisco (per poter allenare la rete lstm)
text = [j for sub in text_list2d for j in sub]

X = []
Y = []
# X_word = []
# Y_word = []
length = len(text)
seq_length = 5
for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label = text[i + seq_length]
    # X_word.append([char for char in sequence])
    # Y_word.append(label)

    # transform syllables in w2v vectors through the trained model
    X.append([mymodel.wv.get_vector(char) for char in sequence])
    Y.append(mymodel.wv.get_vector(label))

