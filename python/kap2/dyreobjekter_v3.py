import dyreklasser as dk

mine_dyr = {
  "Heidi": dk.Hund("Heidi","Norsk buhund","Svart og hvit"),
  "Sniff": dk.Hund("Sniff","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Prikken": dk.Hund("Prikken","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Junior": dk.Hund("Junior","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Brumlemann": dk.Hund("Brumlemann","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Trulte": dk.Hund("Trulte","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Tott": dk.Hund("Tott","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Knoll": dk.Hund("Knoll","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Rita": dk.Hund("Rita","Schäferhund","Svart og brun"),
  "Silkesvarten": dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2),
  "Tigergutt": dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1),
  "Lillesvarten": dk.Katt("Mini","Katt med ukjent far","Svart"), 
  "Kaisa": dk.Hund("Kaisa","Labrador retriever","Svart")
}

nabo_dyr = {
  "Festus": dk.Hund("Festus","Norsk elghund","Grå-brun")
}

mine_dyr["Silkesvarten"].avkom("Lillesvarten")
print(mine_dyr["Silkesvarten"].barn)
mine_dyr["Lillesvarten"].sett_mor(mine_dyr["Silkesvarten"])
print(mine_dyr["Lillesvarten"].mor.navn)

# Heidis valper
valper = ["Sniff","Prikken","Junior","Brumlemann","Trulte","Tott","Knoll"]

for valp in valper:
  mine_dyr["Heidi"].avkom(valp)

print(mine_dyr["Heidi"].barn)

for valp in mine_dyr["Heidi"].barn:
  mine_dyr[valp].sett_mor(mine_dyr["Heidi"])
  mine_dyr[valp].sett_far(nabo_dyr["Festus"])

for valp in valper:
  print(valp,mine_dyr[valp].rase,mine_dyr[valp].mor.navn,mine_dyr[valp].mor.rase,mine_dyr[valp].far.navn,mine_dyr[valp].far.rase)

# hvordan gjøre det komplisert :D
valp1 = "Brumlemann"

print(valp1,"sine søsken er",end=" ")

for valp in mine_dyr[valp1].mor.barn:
  if valp != valp1:
    print(mine_dyr[valp].navn, end=" ")

print()