import json

filnavn = "Datasett_fodselstall.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

#print(data)

datasett = data['dataset']
status = datasett['status']
dimension = datasett['dimension']
label = datasett['label']
"""

source
updated
value
"""

for key,value in label.items():
  print(key, value)



