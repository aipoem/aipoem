import logging
import os
import glob
import gensim
from multiprocessing import cpu_count
import matplotlib.pyplot as plt
import numpy as np

from gensim.test.utils import get_tmpfile
from gensim.models.callbacks import CallbackAny2Vec

logger = logging.getLogger(__name__)


class TrainLogger(CallbackAny2Vec):
    """
    Callback to log information about training
    """

    def __init__(self):
        self.epoch = 0
        self.losses = []

    def on_epoch_end(self, model):
        self.losses.append(model.get_latest_training_loss())
        self.epoch += 1

    def on_train_end(self, model):
        plt.plot(np.array(self.losses[1:]) - np.array(self.losses[0:-1]))
        plt.ylabel("Loss")
        plt.xlabel("Epochs")
        plt.grid(b=True)
        plt.show()


class Poema:

    def __init__(self, params):
        self.path_in = params['path_in']
        self.model = None
        self._epochs = params['model_params']['epochs']
        self.model_params = params['model_params']
        self._losses = []

    @property
    def epochs(self):
        return self._epochs

    @staticmethod
    def read_poem(text):
        f = open(os.path.join(text), "r")
        return f.read()

    def train(self):
        # At each loop, the loaded poem is appended to the string txt
        versi = Verso(self.path_in)
        self.model = gensim.models.Word2Vec(
            versi, min_count=self.model_params["min_count"], size=self.model_params["size"], workers=cpu_count())
        return self.model.train(versi, total_examples=self.model.corpus_count, epochs=self.epochs, compute_loss=True,
                                callbacks=[TrainLogger()])

    def save_model(self):
        self.model.save(self.model_params['filename'])

    @property
    def vectors(self):
        return self.model.wv

    def save_vectors(self, filename):
        fname = get_tmpfile(filename)
        self.model.wv.save(fname)
        return None

    def find_analogies(self, w1, w2, w3):
        r = self.vectors.most_similar(positive=[w1, w3], negative=[w2])
        print("%s - %s = %s - %s" % (w1, w2, r[0][0], w3))

    def nearest_neighbors(self, w):
        r = self.vectors.most_similar(positive=[w])
        print(f"Neighbors of {w}:")
        for word, score in r:
            print("\t%s" % word)


class Verso:
    def __init__(self, path):

        self.path_in = path

    def __iter__(self):  # TODO lo script di parsing si potrebbe impacchettare quì dentro
        for text in glob.glob(os.path.join(self.path_in, '*.txt')):
            for line in open(text):
                yield line.split()
