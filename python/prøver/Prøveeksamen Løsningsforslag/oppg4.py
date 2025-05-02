a = [
  [10,15,16],
  [40,2,12],
  [20,6,24],
  [10,13,32]
]

def snitt(liste2D: list) -> float: 
  """
  Regner gjennomsnitt av verdier i en 2D-liste
  Basert på følgende kriterier:
    Verdien er mellom 10 og 20 (inkludert)
    Verdien er delelig med 4

  Input: parameteren er en liste av lister, med tallverdier
  Output: en gjennomsnittsverdi (float)
  """
  antall = 0
  total = 0
  # Går gjennom alle verdier i listen
  for rad in a:
    for kol in rad:
      # Kriteriene som skal oppfylles:
      if kol >= 10 and kol <= 20 and kol%4 == 0:
        total += kol
        antall += 1
  return total / antall

print("Gjennomsnittet av utvalgte verdier er:",snitt(a))

