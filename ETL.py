import urllib.request
import logging
import os

logger = logging.getLogger(__name__)


class ETL():

    def __init__(self, params):

        self._poems = params['poems']
        self.path_out = params['path_out']

    @property
    def poems(self):
        return self._poems

    def download(self):

        for poem in self.poems:
            logger.info(f'Downloading {poem} with urllib2...')
            url = f"https://tools.wmflabs.org/wsexport/tool/book.php?lang=it&format=txt&page={poem}"
            urllib.request.urlretrieve(
                url, os.path.join(self.path_out, f'{poem}.txt'))