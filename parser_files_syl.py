import os
import re
import syllable_func as sf
from utils.utils_functions import intersperse

path = "txt_data/"  # adapt your path
texts = list()
for filename in os.listdir(path):
    texts.append(filename)
print('list of texts')
print(texts)
# check folders
new_folder = "text_ready_syl/"
try:
    os.stat(new_folder)
except FileNotFoundError:
    os.mkdir(new_folder)

# regola per sostituire le grafie particolari della e
regola_e = re.compile("[ëê]")
# regola per uniformare gli accenti
regola_eacc = re.compile("é")

regola_i = re.compile("[ïjî]")
regola_iacc = re.compile("í")

regola_a = re.compile('[âä]')
regola_aacc = re.compile('á')

regola_o = re.compile('ô')
regola_oacc = re.compile('ò')

regola_u = re.compile('ü')
regola_uacc = re.compile("ú")

# regola per cancellare punteggiatura e caratteri non validi
regola_char = re.compile(
    "[©°\―\-\/“„=ª\{\[\]\\/|&><\*\(.\d!?\,\;\:\-\)\"\,\«\»ωεἠγήρτφὃνἄἀάὸσἢκαμῦςοιὶἱθᾶέπληῶό]")
regola_space = re.compile("[’\']")

for f in texts:
    if os.path.isfile(os.path.join(new_folder, f'ready_{f}')):
        print(f'File {f} already parsed')
    else:
        print('Processing file ', path + f)
        text = open(path + f, encoding="utf8")
        lines = text.readlines()
        text.close()
        # work on the single file
        new_file = open(new_folder + "ready_" + f, "w")
        i = False  # activator
        for l in lines:
            if len(l) < 22 or len(l) > 60:
                continue
            elif l[0] == "↑":
                continue
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
                # print(line)
                # print(sf.syllable_division(line))
                # print(sf.count_syllable(line))
                # print("________________________")
                # TODO check if this interval is ok
                syl_line = sf.syllable_division(line)
                if 10 < len(syl_line) < 15:
                    #syl_line = sf.syllable_division(line)
                    space_separator = [' - ']
                    syl_line = intersperse(syl_line, space_separator)
                    new_line_separator = [' -n-\n']
                    syl_line.append(new_line_separator)
                    parsed_line = ' '.join(
                        [j for sub in syl_line for j in sub])
                   # print('')
                   # print(line)
                   # print(parsed_line)
                   # print('_______________________________')
                    new_file.write(parsed_line)
        new_file.close()
