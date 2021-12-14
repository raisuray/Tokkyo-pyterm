import json
import tools
import pprint
import re
import numpy as np
from IGNORE_WORDS import get_regex

"""
fileF = open("out-compound-FILTERED.json", "r")
Fil = json.load(fileF)
fileF.close()

p = get_regex()

list_of_kanji = dict()

patent_files = Fil.keys()

new_compound_list = dict.fromkeys(patent_files)


for patent in patent_files:
    new_list_word = []
    lst_of_words = Fil[patent]
    

    for word in lst_of_words:
        flagascii = 0
        for kanji in word:
            
            if len(p.findall(kanji)) >= 1:
                flagascii = 1
                continue

            if kanji.isascii():
                flagascii = 1
                continue

            if(kanji not in list_of_kanji.keys()):
                list_of_kanji[kanji] = 1
            else:
                list_of_kanji[kanji] += 1

        if(flagascii == 0):
            new_list_word.append(word)
    
    new_compound_list[patent] = new_list_word


top_kanji = dict()

for key in list_of_kanji.keys():
    if (list_of_kanji[key] <= 600 and list_of_kanji[key] >= 200):
        top_kanji[key] = list_of_kanji[key]


tools.save_jsonfile("list_of_kanji.json", list_of_kanji)
tools.save_jsonfile("top_kanji_list.json", top_kanji)
tools.save_jsonfile("out-compound-FILTERED-noascii.json", new_compound_list)
"""



def initialize_dict_to_list(dit):
    for key in dit.keys():
        dit[key] = []
    return dit 


###FIND THE TOP PAIR WORD BASED 発明の効果 ###

hatsumei = tools.load_jsonfile("result_02.json")
#print(hatsumei["1992073168.txt"][0]["発明の効果"])
patent_files = list(hatsumei.keys())
distance = tools.load_jsonfile("distance.json")
#print(distance[patent_files[0]])

for patent in patent_files:
    
    word_list = hatsumei[patent][0]["発明の効果"]
    

    ### 初期化辞書 ###
    res = dict.fromkeys(word_list)
    res = initialize_dict_to_list(res)

    top_total = len(word_list)

    ### FLAG vector for total word ###
    flag = np.zeros(top_total)
    flag += top_total

    for expword, invword, distance in distance[patent]:
        index = word_list.index(invword)
        if(flag[index] != 0):
            res[invword].append((expword, invword, distance))
            flag[index] -= 1
        else:
            min = res[invword][0][2]
            indextochange = 0

            for i in range(len(res[invword])):
                if(res[invword][i][2] >= distance):
                    min = distance        
        
    print(res)
    
    break
