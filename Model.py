import spacy
import logging
import os
import glob
import gensim
from multiprocessing import cpu_count

from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors

logger = logging.getLogger(__name__)


class poema():

    def __init__(self, params):

        self.path_in = params['path_in']
        self.model = None
        self.model_params = params['model_params']

    def read_poem(self, text):
        f = open(os.path.join(text), "r")
        return f.read()

    def train(self):
        # At each loop, the loaded poem is appended to the string txt
        versi = verso(self.path_in)
        self.model = gensim.models.Word2Vec(
            versi, min_count=self.model_params["min_count"], size=self.model_params["size"], workers=cpu_count())
        self.model.save(self.model_params['filename'])
        return self.model

    @property
    def vectors(self):
        return self.model.wv

    def save_vectors(self, filename):
        fname = get_tmpfile(filename)
        self.model.wv.save(fname)
        return None

    @staticmethod
    def load_if_exists(model_name):
        # TODO to be implemented (se trova un modello pretrainato al percorso lo deve caricare)
        return None

    def find_analogies(self, w1, w2, w3):
        r = self.vectors.most_similar(positive=[w1, w3], negative=[w2])
        print("%s - %s = %s - %s" % (w1, w2, r[0][0], w3))

    def nearest_neighbors(self, w):
        r = self.vectors.most_similar(positive=[w])
        print(f"Neighbors of {w}:")
        for word, score in r:
            print("\t%s" % word)


class verso():
    def __init__(self, path):

        self.path_in = path

    def __iter__(self):
        for text in glob.glob(os.path.join(self.path_in, '*.txt')):
            for line in open(text):
                yield line.split()
