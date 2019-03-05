import os
import sys
import numpy as np
import io
import re
import syllable_func as sf
path = "txt_data/"  # adapt your path
texts = list()
for filename in os.listdir(path):
    texts.append(filename)
print('list of texts')
print(texts)
# check folders
new_folder = "text_ready/"
try:
    os.stat(new_folder)
except:
    os.mkdir(new_folder)
###

regola_e = re.compile("[ëêë]")# regola per sostituire le grafie particolari della e
regola_eacc = re.compile("é") # regola per uniformare gli accenti

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
    print(path+f)
    text = open(path+f, encoding="utf8")
    lines = text.readlines()
    text.close()
    # work on the single file
    new_file = open(new_folder+"ready_"+f, "w")
    i = False  # activator
    for l in lines:
        if 22 > len(l) or len(l) > 60:
            continue
        elif l[0] == "↑":
            continue
        else:
            """
            new_file.write(regola_char.sub("", 
                           regola_eacc.sub("è",
                           regola_i.sub("i", 
                           regola_a.sub('a', 
                           regola_space.sub(" ", 
                           regola_e.sub("e", 
                           regola_o.sub("o", 
                           regola_oacc.sub("ó",
                           regola_u.sub("u", 
                           regola_iacc.sub("ì", 
                           regola_aacc.sub("à", 
                           regola_uacc.sub("ù", l)))))))))))).lower())
            """
            line=regola_char.sub("", 
                           regola_eacc.sub("è",
                           regola_i.sub("i", 
                           regola_a.sub('a', 
                           regola_space.sub(" ", 
                           regola_e.sub("e", 
                           regola_o.sub("o", 
                           regola_oacc.sub("ó",
                           regola_u.sub("u", 
                           regola_iacc.sub("ì", 
                           regola_aacc.sub("à", 
                           regola_uacc.sub("ù", l)))))))))))).lower()
            #### list of print to check the code performance
            print(line)
            print(sf.syllable_division(line))
            print(sf.count_syllable(line))
            print("________________________")
            ####
            if 9 < sf.count_syllable(line) < 12: #TODO check if this interval 
                new_file.write(line)
    new_file.close()
