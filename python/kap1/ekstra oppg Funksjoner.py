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

