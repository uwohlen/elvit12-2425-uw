import json

filnavn = "googleplaystore.json"

with open(filnavn, encoding="utf-8") as fil:
    innhold = json.load(fil)

for key,value in innhold[0].items():
    print(key," : ",value)

for app in innhold:
    if app["Category"] == "1.9":
        print(app)
    

