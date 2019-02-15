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
regola_e2 = re.compile('ë')
regola_j=re.compile('ï|j')# regola per cancellare numeri nel testo
regola_a = re.compile('â')
regola_char=re.compile("(\.|\d|\!|\?|\,|\;|\à|\:|\-|\)|\"|\,|\«|\»)")
regola_space = re.compile("\’|\'")

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
                new_file.write(regola_char.sub("",regola_e.sub("è",regola_j.sub('i',regola_a.sub('a',regola_space.sub(" ", regola_e2.sub("e", l)) )))).lower())
            except UnicodeEncodeError: #TODO capire esattamente quali sono i caratteri che danno errore e gestirli correttamente
                pass        
    new_file.close()
