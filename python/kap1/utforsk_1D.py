# testing

tall = [1,2,3]
bokstaver = ["a","b","c"]

# når ting skal skje basert på posisjon (eller verdi)
# og/eller vi ønsker å gjøre endringer i original-lista
for i in range(len(tall)):
  if (i == 0):
    tall[i] = tall[i] * 10
    print(tall[i],"første")
  elif (tall[i] == 3):
    print(tall[i],"her er 3'ern")
  else:
    print(tall[i])

print(tall)

# når ting skal skje basert på verdi
# og vi har ikke behov for å gjøre endringer i original-lista
for bokstav in bokstaver:
  if bokstav == "b":
    print(bokstav,"midten")
  else:
    bokstav = bokstav + "q"
    print(bokstav)

print(bokstaver)

highscores = [
  ["a",10],
  ["b",5],
  ["c",1]
]

for i in range(len(highscores)):
  for j in range(len(highscores[i])):
    print(highscores[i][j],end=" ")
  print()


for personer in highscores:
  for verdier in personer:
    print(verdier, end=" ")
  print()



# lage lister


antall = [0]*20
print(antall)

"""
import random as rd
tilfeldige_tall = [rd.randint(1,100)]*20
print(tilfeldige_tall)
# virker ikke, det blir 20 like tall. Trekker et tilfeldig tall bare EN gang.
"""


import random as rd

liste = []

for i in range(10):
  liste.append(rd.randint(1,101))
print(liste)

tilfeldige_tall = [rd.randint(1,101) for x in range(10)]
print(tilfeldige_tall)


partall = list(range(100,201,2))
print(partall)


x_verdier = list(range(1,11))
y_verdier = [(2*x+3) for x in x_verdier]


# denne ene linjen for y_verdier tilsvarer tre:
# valgfritt hvilken du bruker
"""
y_verdier = []
for x in x_verdier:
  y_verdier.append(2*x+3)
"""

for i in range(10):
  print(x_verdier[i],y_verdier[i])

"""
import matplotlib.pyplot as plt
plt.plot(x_verdier,y_verdier)
plt.show()
"""


navn = ["Anne","Berit","Unni","Lise","Cecilie"]
let_etter = "Unni"
indeks = "Ikke funnet"

if let_etter in navn:
  indeks = navn.index(let_etter)

print(let_etter,"har indeks:",indeks)


navn2 = navn.copy()
navn2.remove("Unni")

print("Innhold liste navn:",navn)
print("Innhold liste navn2:",navn2)

def lengde_funk(e):
  return len(e)

navn.sort(key=lengde_funk,reverse=True)
print(navn)


tall_liste = list(range(1,11))
print(tall_liste)
dobbel_liste = []
for x in tall_liste:
  dobbel_liste.append(2*x)
print(dobbel_liste)

import numpy as np
tall_array = np.array(range(1,11))
print(tall_array)
dobbel_array = tall_array*2
print(dobbel_array)


noen = tall_liste[3:7]
print(noen)

partall = tall_liste[3::2]
print(partall)
oddetall = tall_liste[4::2]
print(oddetall)
tregangen = tall_liste[2::3]
print(tregangen)

print(sorted(tilfeldige_tall))
print(tilfeldige_tall)
sortert_tall = sorted(tilfeldige_tall)
print(sortert_tall)
print(tilfeldige_tall)


blanding = ["hei","2","To","å","104","Æ","e","Trønder","æ"]
blanding.sort()
print(blanding)

tekst = "hei2Toå104ÆeTrønderæ"
print(sorted(tekst))


storst = tilfeldige_tall[0]
plass = 0

for i in range(1,len(tilfeldige_tall)):
  if tilfeldige_tall[i] > storst:
    storst = tilfeldige_tall[i]
    plass = i
    print("bytta til:",storst)

print("Indeks",plass,"Verdi",storst)