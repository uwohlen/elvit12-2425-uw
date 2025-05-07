# Datasett

alt = [
  ["Nils","Hansen",17183423,[44,25,46,65,96,73,65]],
  ["Kari","Johnsen",18234223,[46,42,13,39,64,35,36]],
  ["Lise","Voll",19123563,[13,34,63,93,84,66,35]],
  ["Inger","Selbakk",17214334,[65,44,36,53,94,65,13]],
  ["Magnus","Kolstad",18133265,[22,55,6,15,26,33,5]],
  ["Morten","Sletten",17233123,[54,64,48,46,59,46,24]],
  ["Else","Kollen",16123141,[41,43,26,38,50,56,54]],
  ["Ole","Gran",18144235,[52,26,19,26,22,16,61]],
  ["Line","Ringen",17122345,[43,25,18,33,61,45,58]]
]

#Oppgave: hvem har størst variasjonsbredde?

# Eksempel 1
variasjon = []

for person in alt:
  vb = max(person[3]) - min(person[3]) 
  variasjon.append([vb,person]) # setter tallene først for enkel sortering

variasjon.sort()
print(variasjon[-1])

# Eksempel 2

def variasjonsbredde(rad):
  vb = max(rad[3]) - min(rad[3])
  rad.append(vb)
  rad.append(round(sum(rad[3])/len(rad[3]),1))
  return vb

resultat = sorted(alt,key=variasjonsbredde, reverse=True)
print(resultat[0])