import urllib.request
import logging
import os

logger = logging.getLogger(__name__)


class ETL():

    def __init__(self, params):

        self._poems = params['poems']
        self.path_out = self.select_or_create(params['path_out'])
        self.path_ready = self.select_or_create(params['path_ready'])

    @property
    def poems(self):
        return self._poems

    def download(self):

        for poem in self.poems:
            logger.info(f'Downloading {poem} with urllib2...')
            url = f"https://tools.wmflabs.org/wsexport/tool/book.php?lang=it&format=txt&page={poem}"
            urllib.request.urlretrieve(
                url, os.path.join(self.path_out, f'{poem}.txt'))

    def parse(self):
        # TODO lo script di parsing si potrebbe impacchettare quì dentro
        return None

    @staticmethod
    def select_or_create(path):
        try:
            os.stat(path)
        except:
            os.mkdir(path)
        return path
