import matplotlib.pyplot as plt

fortsett = True
tall = []

def beregn(liste):
  print(liste)
  listesum = 0
  antall = 0
  x = []
  
  for i in range(len(liste)):
    listesum += liste[i]
    antall += 1
    x.append(i)

  print("Sum: ",listesum)
  print("Sum: ",sum(liste))
  print("Gjennomsnitt: ",listesum/antall)
  print("Gjennomsnitt: ",sum(liste)/len(liste))

  plt.plot(x,liste)
  plt.scatter(x,liste)
  plt.show()
  
while fortsett:
  a = input("Skriv inn et tall: ")
  if a == "q":
    beregn(tall)
    fortsett = False
  else:
    tall.append(float(a))

