import json

with open("distance.json", "r") as f:
    res = json.load(f)

patent_files = list(res.keys())
#print(patent_files)

top3 = []

for patent in patent_files:
    for myword, hisword, distance in res[patent]:
        print(myword, hisword, distance)
        
