# Oppgave 6b og c
from oppg6a import Batteri
def testBatteri():
  # Opprett et batteri
  batteri = Batteri("BAT123", 100.0)
 
  # Test lading
  print("Lader batteriet med 50 enheter...")
  batteri.ladOpp(50.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 50.0)")
 
  # Test overfylling
  print("Lader batteriet med 60 enheter (over maks kapasitet)...")
  batteri.ladOpp(60.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 100.0)")
 
  # Test forbruk av energi
  print("Bruker 30 enheter energi...")
  batteri.brukEnergi(30.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 70.0)")
 
  # Test overforbruk
  try:
    print("Prøver å bruke 80 enheter energi (mer enn tilgjengelig)...")
    batteri.brukEnergi(80.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")

  # Test negativ lading
  try:
    print("Prøver å lade med -10 enheter...")
    batteri.ladOpp(-10.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")
 
  # Test negativt energiforbruk
  try:
    print("Prøver å bruke -5 enheter energi...")
    batteri.brukEnergi(-5.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")

# Kjør testprogrammet
testBatteri()