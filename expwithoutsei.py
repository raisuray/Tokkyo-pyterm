import json
import tools
import pprint

fileE = open("out-compound.json", "r")
fileS = open("out-compound-S.json", "r")

Exp = json.load(fileE)
Sei = json.load(fileS)

print(len(Exp) == len(Sei))

print(Exp.keys() == Sei.keys())

patent_files = Exp.keys()

new_CW_wordlist = dict.fromkeys(patent_files)

for patent in patent_files:

    word_setExp = set(Exp[patent])
    word_setSei = set(Sei[patent])

    res1 = word_setSei - word_setExp
    res2 = word_setExp - word_setSei
    res = res1 | res2

    new_CW_wordlist[patent] = list(res)

tools.save_jsonfile("out-compound-FILTERED.json", new_CW_wordlist)



