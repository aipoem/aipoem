from hyphen import Hyphenator
from utils.constants import vocali, consonanti
import logging
# this function counts vowel and it checks if "u" or "i" is the tonal vocals

logger = logging.getLogger("__main__")

def tonale(word):
    """
    In this fuction we are assuming that the tonal vowel is the penultimate
    of the given word_list
    input: string 
    output: boolean 
    """
    tf = False
    lis = ["u", "i"]
    count = 0
    j = 0
    for i in word[::-1]:
        j+=1 
        if (i in vocali):
                count+=1
        if count==2 and j>=2: 
                if i in lis: tf=True
    return tf


def count_syllable(string):
    """
    This function counts the syllables of a given string 
    input : string  
    output: int
    """
    syl = syllable_division(string)
    counter = 0
    for i in syl:
        counter += len(i)
    return counter


# TODO: I WROTE IT WITHOUT REGRESSION TEST
def correction(list_of_syllables):
    """
    This function correct the syllables division merging
    the single letter (consonant) syllables, into the next one.
    """
    i = 0
    while True:
        # print(i)
        # print(len(a))
        if i > (len(list_of_syllables) - 1):
            break
        if len(list_of_syllables[i]) < 2 and i == (len(list_of_syllables) - 1):
            # print('qui')
            # print(a[i])
            list_of_syllables = list_of_syllables[:i]
            continue
        if len(list_of_syllables[i]) < 2:
            # print('qyui')
            # print(a[i])
            list_of_syllables[i + 1] = list_of_syllables[i] + list_of_syllables[i + 1]
            del list_of_syllables[i]
            if i == (len(list_of_syllables) - 1):
                break
            continue
        i += 1
    return list_of_syllables


def syllable_division(phrase):
    """
    this function will split in syllabs a given strig
    input: string
    output: list of list (list of word each one contains a list of syllables)  
    """
    h_it = Hyphenator('it_IT')
    word_list = phrase.split()
    if len(word_list) == 0:
        return []
    vocali_sill = ["a", "e", "o"]
    b_lis = ['u', 'i']
    sillabe_frase = []
    for w in word_list:
        ton = tonale(w)
        sillabe_custom = []
        if len(w) < 3:
            sillabe_custom.append(w)
        elif len(w) == 3:
            sy = w
            i = 0
            while True:
                if ((sy[i] in vocali_sill) and (sy[i + 1] in vocali_sill)) or (ton and (
                        ((sy[i] in b_lis) and (sy[i + 1] in vocali_sill)) or (
                        (sy[i] in vocali_sill) and (sy[i + 1] in b_lis)))):
                    sillabe_custom.append(sy[:i + 1])
                    sillabe_custom.append(sy[i + 1:])
                    break
                i += 1
                if i >= 2:
                    sillabe_custom.append(sy)
                    break
        else:
            if ((w[0] in vocali) and (w[1] in consonanti) and (w[2] in vocali)) or (
                    (w[0] in vocali) and (w[1] == "s") and (w[2] in consonanti)):
                sillabe_custom.append(w[0])
                w = w[1:]
            middle_division = h_it.syllables(w)
            if not middle_division:
                sillabe_custom.append(w)
            else:
                # control to recognize wrong syllables
                for sy in middle_division:
                    if len(sy) < 3:
                        sillabe_custom.append(sy)
                    else:
                        i = 0
                        while True:
                            if i >= (len(sy) - 1):
                                sillabe_custom.append(sy)
                                break
                            if ((sy[i] in vocali_sill) and (sy[i + 1] in vocali_sill)) or (ton and (
                                    ((sy[i] in b_lis) and (sy[i + 1] in vocali_sill)) or (
                                    (sy[i] in vocali_sill) and (sy[i + 1] in b_lis)))):
                                sillabe_custom.append(sy[:i + 1])
                                sillabe_custom.append(sy[i + 1:])
                                break
                            i += 1

        sillabe_frase.append(sillabe_custom)
       # else: sillabe_frase.append(h_it.syllables(w))
    return group_sy(sillabe_frase)

def group_sy(listt): 
    """
    This function groups wrong sillables, composed by just one or two consonant with the follow syllable.
    NB: this function doesn't control if the next syllable begin with a vowel ##TODO
    es: (l' , gl' , ..)
    Input: list
    Output: list 
    """
    flatten = lambda a: [item for sublist in a for item in sublist]
    a = flatten(listt)
    i=0
    while True:
        if i > (len(a)-1):
            break
        if len(a[i])<2 and i == (len(a)-1) and (a[i] in consonanti):
            #### cut the last false syllable
            a=a[:i]
            continue
        if (len(a[i])<2 and a[i][0] in consonanti) or (len(a[i])==2 and (a[i][0] in consonanti ) and (a[i][1] in consonanti)):
            try:
                a[i+1]=a[i]+a[i+1]
            except IndexError:
                logger.error(f"Unable to parse {a}, skipping")
                return []
            del a[i]
            if i ==(len(a)-1):
                break
            continue
        i+=1
    return a
