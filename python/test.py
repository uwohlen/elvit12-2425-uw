fortsett = True

while fortsett:
  svar = input("Skriv inn et heltall: ")
  try:
    tall = int(svar)
    fortsett = False
  except:
    print("Du må faktisk skrive et heltall!")

print("Løkke ferdig.")
print(tall)


meny = True
while meny:
  print()
  print("Meny")
  print("A - riktig valg")
  print("B - ikke et godt valg")
  svar = input("Velg: ")
  if (svar == "A"):
    print("wow")
    meny = False
  elif (svar == "B"):
    print("fortsett")
  else:
    print("invalid, prøv igjen")