import os
import sys
import numpy as np
import io
import re

path="txt_data/" ## adapt your path 
texts=list()
for filename in os.listdir(path):
    texts.append(filename)
print('list of texts')
print(texts)
#### check folders
new_folder="text_ready/"
try:
    os.stat(new_folder)
except:
    os.mkdir(new_folder)
### 
for f in texts:
    print(path+f)
    text=open(path+f,encoding="utf8")
    lines=text.readlines()
    print("i'm working")
    print(f)
    text.close()
    #################################### work on the single file
    new_file=open(new_folder+"ready_"+f,"w")
    i=False ## activator
    for l in lines: # TODO il codice si schianta quando trova il carattere '\u2032' (è come un apostrofo ma ha un codice unicode diverso. Per non impazzire metterei un controllo che per ogni carattere non riconosciuto sostituisce uno spazio)
        if l =="ARGOMENTO.\n" or i:
            i=True
            if len(l)<22:
                continue
            if len(l)>60:
                continue
            elif l[0].isdigit() : ## we can improve this part with a while o something like it
                lu=l[1:]
                if lu[0].isdigit() :                
                    lu=lu[1:]
                    if lu[0].isdigit() :
                        lu=lu[1:]               
                new_file.write(lu) ## lu.replace('\n',"") <-- use to create and unstructured text
            elif l[0]=="↑":
                    continue
            else:
                try:
                    new_file.write(l)
                except UnicodeEncodeError:
                    pass

    new_file.close()
            
    