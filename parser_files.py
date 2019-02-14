import os
import sys
import numpy as np
import io
import re

path = "txt_data/"  # adapt your path
texts = list()
for filename in os.listdir(path):
    texts.append(filename)
print('list of texts')
print(texts)
# check folders
new_folder = "text_ready/"
print("sono qui1")
try:
    os.stat(new_folder)
except:
    os.mkdir(new_folder)
###
regola_e=re.compile('é')# regola per cancellare numeri nel testo
regola_j=re.compile('j')# regola per cancellare numeri nel testo
regola_char=re.compile("(\.|\d|\!|\?|\,|\;|\à|\’|\:|\-|\))")## regola per cancellare caratteri strani #TODO check se ci sono tutti i necessari
for f in texts:
    print(path+f)
    text = open(path+f, encoding="utf8")
    lines = text.readlines()
    print("i'm working")
    print(f)
    text.close()
    #################################### work on the single file
    new_file=open(new_folder+"ready_"+f,"w")
    i=False ## activator
    for l in lines:
        if 22>len(l) or len(l)>60:
            continue
        elif l[0] == "↑":
            continue
        else:
            try:
                new_file.write(regola_char.sub("",regola_e.sub("è",regola_j.sub('i',l))).lower())
            except UnicodeEncodeError:
                pass

    new_file.close()
