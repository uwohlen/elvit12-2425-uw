import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "fritidsaktiviteter_semikolondelt.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  tekst = next(filinnhold)
  #print(tekst)
  tekst2 = next(filinnhold)
  #print(tekst2)
  overskrifter = next(filinnhold)
  #print(overskrifter)

  for rad in filinnhold:
    #print(rad)
    innhold.append(rad)
    #print(len(rad))


print()
print("8A Deltakelse i ulike friluftsaktiviteter")
print("1000 spurte i Norges 14 fylker i 2024")
print()

tabell = []
for i in range(len(innhold)):
  rad = innhold[i].copy()
  aktivitet = rad[0]
  rad.pop(0)
  antall = 0
  for verdi in rad:
    antall += int(verdi)
  prosent = antall*100/14000
  tabell.append([aktivitet,antall,prosent])

print(f"Aktivitet                                                    | Antall (av 14000 spurte)   | Prosent")
print("____________________________________________________________________________________________________")
for rad in tabell:
  print(f"{rad[0]:60} | {rad[1]:24.0f}   | {rad[2]:7.1f}")
  print("____________________________________________________________________________________________________")

print()
print()

print("Velg et fylke for videre informasjon")
#print(overskrifter)
overskrifter.pop(0)
fylker = []
for fylke in overskrifter:
  fylke = fylke[23:]
  if "-" in fylke:
    til = fylke.index("-")
    fylke = fylke[:til]
  #print(fylke)
  fylker.append(fylke)

for i in range(len(fylker)):
  print(i+1,fylker[i])

fylke = int(input("Skriv nummeret til valgte fylke: "))
print(fylke)

fylkestabell = []
for rad in innhold:
  fylkestabell.append([int(rad[fylke]),rad[0]])

fylkestabell.sort(reverse=True)

print(f"Aktivitet                                                    | Antall (av 1000 spurte)    | Prosent")
print("____________________________________________________________________________________________________")
for rad in fylkestabell:
  print(f"{rad[1]:60} | {rad[0]:24.0f}   | {rad[0]/10:7.1f}")
  print("____________________________________________________________________________________________________")

print()
print()

x = []
y = []
for i in range(3):
  x.append(fylkestabell[i][1])
  y.append(fylkestabell[i][0])

plt.barh(x,y)
plt.subplots_adjust(left=0.5)

#plt.xticks(rotation='vertical')
plt.show()