#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from langues import *
from math import *

#extraire les lettre de la table d'occurance
def lettres_de_table_doccurance(table_occurance):
    table_occurance_keys_list = []
    for key in table_occurance:
        table_occurance_keys_list.append(key)
    return table_occurance_keys_list

#calculer la longeur de text
def len_of_unknown_language_text(unknown_language_text):
    unknown_language_text_len = 0

    for letter in unknown_language_text:
        unknown_language_text_len += 1

    return unknown_language_text_len

#fonction return un dictionnaire de table d'occurance
def de_str_a_table_doccurance(unknown_language_text):
    table_occurance = {}
    for letter in unknown_language_text:
        if letter in lettres_de_table_doccurance(table_occurance) :
            table_occurance[letter] += 1
        else:
            table_occurance[letter] = 1
    return table_occurance

#fonction retourne une table de freqeuce sous forme d'un dictionnaire
def de_str_a_table_de_frequece(table_occurance, unknown_language_text_len):
    table_de_frequence = {}
    for letter in table_occurance:
        table_de_frequence[letter] = table_occurance[letter]
        table_de_frequence[letter] /= unknown_language_text_len
    return table_de_frequence

# fonction calcule la distance entre la langue inconnue et connue
def distance_entre_langue_inconnue_connue(table_de_frequence_langue_inconnue, unknown_language_text_len):
    distance_entre_langue_inconnue_connue = {}

    for nom_de_langue in language_name_to_text:
        result = 0
        len_langue_connue = len_of_unknown_language_text(language_name_to_text[nom_de_langue])
        table_occurance_langue_connue = de_str_a_table_doccurance(language_name_to_text[nom_de_langue])
        table_de_frequence_langue_connue = de_str_a_table_de_frequece(table_occurance_langue_connue, len_langue_connue)

        for lettre in table_de_frequence_langue_inconnue:
            if lettre in lettres_de_table_doccurance(table_de_frequence_langue_connue):
                result += (table_de_frequence_langue_inconnue[lettre] - table_de_frequence_langue_connue[lettre])**2
            else :
                result += (table_de_frequence_langue_inconnue[lettre] - 0)**2


        distance_entre_langue_inconnue_connue[nom_de_langue] = sqrt(result)

    return distance_entre_langue_inconnue_connue

# fonction retourne la langue correspond a la plus petite distance
def plus_petit_distance(table_de_distance):
    list_of_sorted_distance = []
    for nom_de_langue in table_de_distance:
        list_of_sorted_distance.append(table_de_distance[nom_de_langue])

    list_of_sorted_distance.sort()

    for nom_de_langue in table_de_distance:
        if list_of_sorted_distance[0] == table_de_distance[nom_de_langue]:
            return nom_de_langue


def main():
    user_text = input("Enter your text :  ")

    len_of_user_text = len_of_unknown_language_text(user_text)
    table_occurance = de_str_a_table_doccurance(user_text)
    table_de_frequence = de_str_a_table_de_frequece(table_occurance, len_of_user_text)

    distance = distance_entre_langue_inconnue_connue(table_de_frequence, len_of_user_text)

    print(plus_petit_distance(distance))

if __name__ == "__main__":
    main()
