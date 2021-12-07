import spacy as spacy
import json as json 
import tools

files = tools.load_jsonfile("out-compound.json")
nlp = spacy.load("ja_ginza")

patent_noun = files["1992242233.txt"]
res = []

for noun in patent_noun:
    doc = nlp(noun)
    for ent in doc.ents:
        print(ent.text + " " + ent.label_)
        res.append(ent.text)
    
temp3 = set(patent_noun) - set(res)
print(temp3)