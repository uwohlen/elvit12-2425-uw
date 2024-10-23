# Funksjoner

def bytt(liste, fra_verdi, til_verdi):
  """
  Standardfunksjon for å bytte verdier i en liste-variabel
  Alle forekomster av fra_verdi i listen blir byttet til til_verdi
  """
  while fra_verdi in liste:
    indeks = liste.index(fra_verdi)
    liste[indeks] = til_verdi

import random as rd

tall = []
for i in range(10):
  tall.append(rd.randint(1,101))
  tall.append(200)

print(tall)

bytt(tall,200,0)

print(tall)


def gange_liste(liste,verdi):
  """
  Utfører et gangestykke på hvert element i en liste-variabel
  Faktoren i gangestykkene angis med verdi
  """
  dobbel = []
  for x in liste:
    dobbel.append(verdi*x)
  return dobbel


tall_liste = list(range(1,11))
print(tall_liste)
dobbel_liste = gange_liste(tall_liste,2)
print(dobbel_liste)
halv_liste = gange_liste(tall_liste,1/2)
print(halv_liste)