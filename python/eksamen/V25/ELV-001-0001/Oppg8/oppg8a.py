import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "friluftsaktiviteter.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  overskrifter = next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    print(rad)
    innhold.append(rad)
    print(len(rad))


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
