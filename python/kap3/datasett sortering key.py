a = [
  [10,15,16],
  [40,2,12],
  [20,6,24],
  [10,13,32]
]

def sort_kol1(rad):
  return rad[1]

#a.sort() # kan bare brukes for første kolonne
a.sort(key=sort_kol1) # metode kan brukes for alle kolonner
#a.sort(key=lambda rad:rad[2]) # metode kan brukes for all kolonner
print(a)


liste = [6,1,-44,-7,-23,6,7,-9,344,-5,2,4,6]

def absoluttverdi(element):
  return abs(element)

liste.sort(key=absoluttverdi)

#liste.sort(key=lambda element:abs(element))

print(liste)



# Datasett
alt = [
  ["Nils","Hansen"],
  ["Kari","Johnsen"],
  ["Lise","Voll"],
  ["Inger","Selbakk"],
  ["Magnus","Kolstad"],
  ["Morten","Sletten"],
  ["Else","Kollen"],
  ["Ole","Gran"],
  ["Line","Ringen"]
]

def sort_kol1(rad):
  return rad[1]

alt.sort(key=sort_kol1)
for person in alt:
  print(person[0],person[1])
