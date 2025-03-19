tall = [4,7,2,4,8,10,9,1]

# sortering

# standard funksjon
tall_kopi = sorted(tall)
print(tall_kopi)


# liste - metode
tall_kopi2 = tall.copy()
tall_kopi2.sort()
print(tall_kopi2)


# standard funksjon og liste-metode

tall_kopi3 = list(tall)
tall_kopi3.sort()
print(tall_kopi3)


# egen programmering av kopi og sortering, bruker noen andre liste-metoder (append og remove)

tall_kopi4 = []
for verdi in tall:
  tall_kopi4.append(verdi)

tall_kopi5 = []
for i in range(len(tall)):
  minst = tall_kopi4[0]
  for j in range(1,len(tall_kopi4)):
    if tall_kopi4[j] < minst:
      minst = tall_kopi4[j]
  tall_kopi5.append(minst)
  tall_kopi4.remove(minst)



print(tall_kopi5)

print(tall)


# standard funksjon gir feil resultat

tekst = ["b","u","æ","r","å","a","ø","f"]
tekst_kopi = sorted(tekst)
print(tekst_kopi)

# egen programmering for sortering (men fremdeles feil resultat)... dessuten er koden lite effektiv (bruker n! runder)
tekst_kopi2 = list(tekst)
tekst_kopi3 = []

for i in range(len(tekst)):
  minst = tekst_kopi2[0]
  for j in range(1,len(tekst_kopi2)):
    if tekst_kopi2[j] < minst:
      minst = tekst_kopi2[j]
  tekst_kopi3.append(minst)
  tekst_kopi2.remove(minst)

print(tekst_kopi3)

print(tekst)