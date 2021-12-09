import json
import tools
import pprint
import re
from IGNORE_WORDS import get_regex

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
