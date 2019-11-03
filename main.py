#!/usr/bin/env python3
from langues import *
from math import *

#my text
var_a = "hello world"

#get keys from dictionnaire
def getList(dict):
    return list(dict.keys())

#calculer le nombre total des caractere contient un dictionnaire
def lenOfDic(localDic):
    len = 0
    for keys in localDic:
        len += localDic[keys]
    return len

#fonction return un dictionnaire de table d'occurance
def de_str_a_table_doccurance(textLocal):
    dicTableOccurance = {}
    for element in textLocal:
        if element in getList(dicTableOccurance) :
            dicTableOccurance[element] += 1
        else:
            dicTableOccurance[element] = 1
    return dicTableOccurance

#fonction returne un dictionnaire de table de freqeuce
def de_str_a_table_de_frequece(localDic):
    dicTableDeFrequece = {}
    for value in localDic:
        dicTableDeFrequece[value] = localDic[value]
        dicTableDeFrequece[value] /= lenOfDic(localDic)
    return dicTableDeFrequece



def calcule():
    dicTableDeFrequeceMyText = {}
    dicTableDeFrequeceMyText = de_str_a_table_de_frequece(de_str_a_table_doccurance(var_a)) #my text

    dicDistance = {}

    for element in language_name_to_text:
        result = 0
        dicTableDeFrequeceLangue = {}
        dicTableDeFrequeceLangue = de_str_a_table_de_frequece(de_str_a_table_doccurance(language_name_to_text[element]))
        for key in dicTableDeFrequeceMyText:
            if key in getList(dicTableDeFrequeceLangue):
                result += (dicTableDeFrequeceMyText[key] - dicTableDeFrequeceLangue[key])**2
            else :
                result += (dicTableDeFrequeceMyText[key] - 0)**2

        dicDistance[element] = sqrt(result)
    return dicDistance

def smallNum(dic):
    list = []
    for value in dic:
        list.append(dic[value])

    list.sort()

    for value in dic:
        if list[0] == dic[value]:
            print(value)

smallNum(calcule())
