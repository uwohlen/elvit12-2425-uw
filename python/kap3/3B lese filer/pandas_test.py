import pandas as pd

liste = ["Espen","Askeladd",23]

overskrifter = ["Fornavn","Etternavn","Alder"]


alternativ_ordbok = {
  "Fornavn": "Espen",
  "Etternavn": "Askeladd",
  "Alder": 23
}

#info = pd.Series(liste,index=overskrifter)
info = pd.Series(alternativ_ordbok)

print(info)
print(info[0]) # ikke likt med index-nummer, bedre med index-navn under:
print(info["Etternavn"])

# UTVALG

deler_av_info = pd.Series(alternativ_ordbok, index=["Fornavn","Alder"])

print(deler_av_info)

"""
data = [
  [420, 234, 390],
  [50, 40, 45]
  ]

overskrifter = ["a","b","c"]
kategorier = ["Per","Pål"]

#load data into a DataFrame object:
df = pd.DataFrame(data,index=kategorier,columns=overskrifter)

print(df) 
"
"""