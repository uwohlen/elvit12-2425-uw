# testing

tall = [1,2,3]
bokstaver = ["a","b","c"]

# når ting skal skje basert på posisjon
for i in range(len(tall)):
  if (i == 0):
    print(tall[i],"første")
  elif (i == len(tall)-1):
    print(tall[i],"siste")
  else:
    print(tall[i])

# når ting skal skje basert på verdi
for bokstav in bokstaver:
  if bokstav == "b":
    print(bokstav,"midten")
  else:
    print(bokstav)

highscores = [
  ["a",10],
  ["b",5],
  ["c",1]
]

for i in range(len(highscores)):
  for j in range(len(highscores[i])):
    print(highscores[i][j],end=" ")
  print()





# lage lister


antall = [0]*20
print(antall)


import random as rd

liste = []

for i in range(10):
  liste.append(rd.randint(1,100))
print(liste)

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
