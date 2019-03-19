import urllib.request
import logging
import os
import re
from pathlib import Path
from hyphen import Hyphenator
import syllable_func as sf


logger = logging.getLogger("__main__")


class ETL:

    def __init__(self, params):

        self._poems = params['poems']
        self.path_out = self.select_or_create(params['path_out'])
        self.path_word = self.select_or_create(params['path_word'])

    @property
    def poems(self):
        return self._poems

    def download(self):

        for poem in self.poems:
            txt_out = os.path.join(self.path_out, f'{poem}.txt')
            if Path(txt_out).exists():
                logger.info(
                    f"Skipping {poem} as it's already found in the local folder...")
            else:
                logger.info(f'Downloading {poem} with urllib2...')
                url = f"https://tools.wmflabs.org/wsexport/tool/book.php?lang=it&format=txt&page={poem}"
                try:
                    urllib.request.urlretrieve(url, txt_out)
                except urllib.error.HTTPError:
                    logger.error(f"{poem} not downloaded due to an HTTP error")

    def parse(self, verbose=False):
        texts = list()
        for filename in os.listdir(self.path_out):
            texts.append(filename)
        logger.info(f'Found {len(texts)} .txt files:')
        logger.info(texts)

        # regola per sostituire le grafie particolari della e
        regola_e = re.compile("[êë]")
        regola_eacc = re.compile("é")  # regola per uniformare gli accenti

        regola_i = re.compile("[ïjî]")
        regola_iacc = re.compile("í")

        regola_a = re.compile("[âǻä]")
        regola_aacc = re.compile('á')

        regola_o = re.compile('ô')
        regola_oacc = re.compile('ò')

        regola_u = re.compile('ü')
        regola_uacc = re.compile("ú")

        # regola per cancellare punteggiatura e caratteri non validi
        regola_char = re.compile(
            "[©°―\-/“„=ª\{\}\[\]\\/|&><\*\(.\d!?\,\;\:\-\)\"\,\«\»ωεἠγήρτφὃνἄἀάὸσἢκαμῦςοιὶἱθᾶέπληῶό—('ǻ')]")
        regola_space = re.compile("[’\']")

        for f in texts:
            if os.path.isfile(os.path.join(self.path_word, f'ready_{f}')):
                logger.info(f'File {f} already parsed, skipping...')
            else:
                logger.info(f'Parsing file {os.path.join(self.path_out, f)}...')
                text = open(os.path.join(self.path_out, f), encoding="utf8")
                lines = text.readlines()
                text.close()
                # work on the single file
                new_file = open(os.path.join(self.path_word, "ready_" + f), "w", encoding='utf8')
                i = False  # activator
                for l in lines:
                    if len(l) < 22 or len(l) > 60:
                        continue
                    elif l[0] == "↑":
                        continue
                    elif 'Informazioni su questa edizione elettronica:' in l:
                        break
                    else:
                        line = regola_char.sub(
                            "", regola_eacc.sub(
                                "è", regola_i.sub(
                                    "i", regola_a.sub(
                                        'a', regola_space.sub(
                                            " ", regola_e.sub(
                                                "e", regola_o.sub(
                                                    "o", regola_oacc.sub(
                                                        "ó", regola_u.sub(
                                                            "u", regola_iacc.sub(
                                                                "ì", regola_aacc.sub(
                                                                    "à", regola_uacc.sub(
                                                                        "ù", l)))))))))))).lower()
                        if verbose:
                            print(line)
                            print(sf.syllable_division(line))
                            print(sf.count_syllable(line))
                            print("________________________")
                        # TODO check if this interval is ok
                        if 10<=len(sf.syllable_division(line))<15 ## this function, due to this control, will be slower than before #CHECK if it improves the performances or delete it
                        new_file.write(line)
                new_file.close()
        return True

    def parse_syllables(self):
        # TODO lo script di parsing si potrebbe impacchettare quì dentro
        return None

    @staticmethod
    def select_or_create(path):
        try:
            os.stat(path)
        except FileNotFoundError:
            os.mkdir(path)
        return path
