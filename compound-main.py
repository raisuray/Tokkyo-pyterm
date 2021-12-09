import neologdn
from patent import PatentS
import pprint
import os 
import tools

import MeCab
import termextract.mecab
import termextract.core
from collections import Counter
import spacy
from IGNORE_WORDS import ig

###LOAD ALL TOKKYO BUNSHO
path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words)


### 特許文書の初期化 - 実施例の抽出 ###
patents_list = []
for patent in dict_eff_words.keys():
    file_path = path+patent
    new = PatentS(file_path)
    patents_list.append(new)

### TESTTING ###
pprint.pprint(patents_list[0].doc)

### 複合名詞の抽出 ###
m = MeCab.Tagger("-Ochasen")
nlp = spacy.load('ja_ginza')

for patent in patents_list:
    
    print(patent.name)
    ### MAKE LIST INTO ONE SENTENCE TEXT ###
    text = ''
    for i in range(len(patent.doc)):
        patent.doc[i] = neologdn.normalize(patent.doc[i])
        text += patent.doc[i]
    
    ### START PARSING THE TEXT ###
    tagged_text = ''
    node = m.parseToNode(text)    
    while node:
        if node.surface:
            tagged_text += node.surface + "\t" + node.feature + "\n"
            node = node.next
        else:
            node = node.next

    ### FINDING 複合名詞 ###
    frequency = termextract.mecab.cmp_noun_dict(tagged_text)
    lr = termextract.core.score_lr(
        frequency,
        ignore_words=termextract.mecab.IGNORE_WORDS,
        lr_mode=1, average_rate=1)

    term_imp = termextract.core.term_importance(frequency, lr)

    #### DELETE ALL SINGLE WORDS ####
    new_term_imp = Counter(term_imp)
    c = Counter()
    for cmp, value in term_imp.items():
        if len(cmp.split(' ')) != 1:
            c[termextract.core.modify_agglutinative_lang(cmp)] = value

    compound = c
    new = list(c.keys())
    dict_eff_words[patent.name] = new

    """
    ### DELETE ALL ASCII ###
    new_term_imp = {}
    for key in term_imp.keys():
        word = key.replace(' ', '')

        if(len(word) >= 2 and (word.isascii() == False)):
            new_term_imp[word] = term_imp[key]
    
    dict_eff_words[patent.name] = list(new_term_imp.keys())
    """

### DELETE IGNORE WORDS and SYMBOL ### 
for patname in dict_eff_words.keys():
    print("削除-"+patname)
    new = []
    for value in dict_eff_words[patname]:
        doc = nlp(value)
        found_symbol = 0
        for span in doc:
            if(span.pos_ == "SYM" or span.text in ig):
                found_symbol = 1
                break

        if(found_symbol != 1):
                new.append(value)
        dict_eff_words[patname] = new

tools.save_jsonfile('./out-compound-S.json', dict_eff_words)


