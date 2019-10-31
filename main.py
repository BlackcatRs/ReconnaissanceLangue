var_a = "hello world"

#dictionnaire de la table d'occurance
dic1 = {}

#dictionnaire de la table de freqeuce
dic2 = {}

#get keys from dictionnaire
def getList(dict):
    return list(dict.keys())


#table de occurance
def de_str_a_table_doccurance():
    for element in var_a:
        if element in getList(dic1) :
            dic1[element] += 1
        else:
            dic1[element] = 1

#table de freqeuce
def de_str_a_table_de_frequece():
    for value in dic1:
        varLocal = dic1[value]
        dic2[value] =  (varLocal / len(dic1.keys()))


de_str_a_table_doccurance()
de_str_a_table_de_frequece()

print(dic2)
