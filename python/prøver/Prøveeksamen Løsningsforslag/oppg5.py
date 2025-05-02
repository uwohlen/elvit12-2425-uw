a = [
  [10,15,16],
  [40,2,12],
  [20,6,24],
  [10,13,32]
]

# a)
def snitt_rad(liste2D):
  antall = []
  total = []
  snitt = []

  for rad in liste2D:
    antall.append(0)
    total.append(0)
    for kol in rad:
      total[-1] += kol
      antall[-1] += 1
    snitt.append(total[-1]/antall[-1])

  return snitt

print(snitt_rad(a))

# b)
def snitt_kol(liste2D:list) -> list:
  """
  Regner gjennomsnitt av verdiene i hver kolonne i en liste av lister med tall

  Innput: parameteren er en liste av lister, med tallverdier
  Output: en liste med gjennomsnittsverdier (list)
  
  """
  antall = []
  total = []
  snitt = []

  # For hver verdi i lista
  for i in range(len(liste2D)):
    for j in range(len(liste2D[i])):
      # Listene utvides med et nytt tall for hver kolonne,
      # for regning av gjennomsnitt for denne kolonnen
      # Gjøres bare for første rad
      if i == 0:
        antall.append(0)
        total.append(0)
      # Tell antall verdier, legg til summen av verdier
      antall[j] += 1
      total[j] += liste2D[i][j]
  # Regn ut snitt for alle kolonner som sum/antall
  for i in range(len(total)):
    snitt.append(total[i]/antall[i])

  return snitt

print("Gjennomsnitt av kolonnene er:",snitt_kol(a))
