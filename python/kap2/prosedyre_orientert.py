person1 = ["Unni",54,175,2007,2003]

person2 = {
  "navn" : "Unni",
  "alder" : 54,
  "hoyde" : 175,
  "ansatt" : 2007,
  "klatret_siden" : 2003
}



katt1 = {
  "navn" : "Silkesvarten",
  "type" : "Norsk skogkatt",
  "farge" : "Svart"
}

katt2 = {
  "navn" : "Tigergutt",
  "rase" : "Norsk skogkatt",
  "farge" : "Stripete grå-svart"
}

hund1 = {
  "navn" : "Kaisa",
  "rase" : "Labrador retriever",
  "farge" : "Svart"
}

mine_dyr = [katt1, katt2, hund1]

def snakk_katt(dyr):
  print(dyr["navn"],'sier "Mjau"')

def snakk_hund(dyr):
  print(dyr["navn"],'sier "Voff"')

def dyr_info(dyr):
  print(dyr["navn"],"er en",dyr["farge"].lower(),dyr["rase"].lower())

snakk_katt(mine_dyr[0])
snakk_hund(mine_dyr[2])
dyr_info(mine_dyr[1])