# 
# testing
#
"""
for i in range(1,20,2):
  print(i,"hei")

print(i)

for i in range(10):
  print(i)
print(i)


i = 0
while i < 10:
  print("Starten av løkka:",i,end=" - ")
  i += 1
  print("Slutten av løkka:",i)

print(i)


tekst = "May the force be with you!"

for verdi in tekst:
  print(verdi,end="-")
print()
print(verdi)

for i in range(len(tekst)):
  if i == len(tekst)-1:
    print(tekst[i])
  else:
    print(tekst[i],end="-")
print(i)

tekst = "May the force be with you!"

for verdi in tekst:
  if verdi == "!":
    break
  print(verdi,end="-")
print(", Luke!")


import random as rd
navn = input("Navn: ")

spill = True
totalsum = 0
antall = 0

while spill:
  if totalsum >= 50:
    break
  antall += 1
  delsum = 0
  fortsett = True
  while fortsett:
    valg = input("Kast (K) eller Lagre (L): ")
    if valg == "k" or valg == "K" or valg == "Kast" or valg == "kast":
      resultat = rd.randint(1,6)
      if resultat == 1:
        print("Omgangen",antall,"gikk tapt, du fikk: ", resultat)
        print()
        fortsett = False
      else:
        delsum += resultat
        print("Omgangen",antall,"Du fikk: ", resultat, "og har nå",delsum,"i denne omgangen.")
        print()
    elif valg == "l" or valg == "L" or valg == "Lagre" or valg == "lagre":
      fortsett = False
      totalsum += delsum
      print("Omgangen",antall,"Du har nå: ", totalsum, "totalt.")
print("Antall omganger:",antall)



import random as rd

liste = []
for i in range(30):
  gender = rd.randint(1,2)
  if gender == 1: 
    kjonn = "M"
    verdi = rd.randint(167,210)
  else:
    kjonn = "K"
    verdi = rd.randint(160,182)
  liste.append([kjonn,verdi])
print(liste)
  

"""
i = 0
while i < 10:
  print(i)
  if i+1 == 10:
    break
  i += 1
print(i)

