#!/usr/bin/env python3
from langues import *
from math import *

#my text
var_a = "hello world"

#dictionnaire de la table d'occurance utilise par de_str_a_table_doccurance(textLocal)
dic1 = {}

#dictionnaire de la table de freqeuce utlise par de_str_a_table_de_frequece(localDic)
dic2 = {}

#get keys from dictionnaire
def getList(dict):
    return list(dict.keys())

#calculer le nombre total des caractere contient un dictionnaire
def lenOfDic(localDic):
    len = 0
    for keys in localDic:
        len += localDic[keys]
    return len

#table d'occurance
def de_str_a_table_doccurance(textLocal):
    for element in textLocal:
        if element in getList(dic1) :
            dic1[element] += 1
        else:
            dic1[element] = 1

#table de freqeuce
def de_str_a_table_de_frequece(localDic):
    for value in localDic:
        dic2[value] = dic1[value]
        dic2[value] /= lenOfDic(dic1)



#fonction permet de calculer la distance entre la langue ecrit par utilisateur et
#langue definie dans la fichier langues.py

# si tu trouve caractere dans la table de freqeuce
    #calcule
#sinon
    #fo = 0 et calcule





de_str_a_table_doccurance(var_a)
de_str_a_table_de_frequece(dic1)

print(dic1)
