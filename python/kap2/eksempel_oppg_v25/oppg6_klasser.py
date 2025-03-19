class Batteri:
  """
  Klasse for et batteri

  Parametre:
    batteri_id (int) - identifikasjon
    energi_niva (int) - nåværende energinivå
    energi_kapasitet (int) - maksimalt energinivå

  Metoder:
    lad_batteri(energi:int) - øk nåværende energinivå med angitt verdi
    bruk_energi(energi:int) - senk nåværende energinivå med angitt verdi
    vis_niva() (str) - returnerer en tekst med energinivået, kan brukes med print
  """
  def __init__(self,batteri_id:int,energi_niva:int,energi_kapasitet:int) -> None: 
    self.batteri_id = batteri_id
    self.energi_niva = energi_niva
    self.energi_kapasitet = energi_kapasitet

  def lad_batteri(self,energi:int) -> None:
    # Håndtering av unntak: sjekk input type
    if type(energi) == float or type(energi) == str:
      print("Angi energiladingen som heltall.")
    elif energi < 0:
      print("Angi energiladingen som positivt heltall.")
    else:
      # Håndtering av feil: sjekk at energien ikke overgår kapasiteten
      if self.energi_niva + energi <= self.energi_kapasitet:
        self.energi_niva += energi
      else:
        print(f"Du kan ikke lade over {self.energi_kapasitet} fra {self.energi_niva}")

  def bruk_energi(self,energi:int) -> None:
    # Håndtering av unntak: sjekk input type
    if type(energi) == float or type(energi) == str:
      print("Angi energibruken som heltall.")
    elif energi < 0:
      print("Angi energibruken som positivt heltall.")
    else:
      #Håndtering av feil: sjekk at energien ikke blir negativ
      if self.energi_niva - energi >= 0:
        self.energi_niva -= energi
      else:
        print(f"Du kan ikke bruke mer energi enn du har: {self.energi_niva}")

  def vis_niva(self) -> str:
    return "Energinivået er: " + str(self.energi_niva)