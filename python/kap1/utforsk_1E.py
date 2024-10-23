"""
svar = input("Regnestykke: ")
print(svar)
print(eval(svar))
"""

liste = [1,2,3,4,5]

def sjekk(liste,indeks):
  i = 1
  j = 2
  return liste[eval(indeks)]

print(sjekk(liste,"i+j"))
print(sjekk(liste,"j-i"))
print(sjekk(liste,"4"))