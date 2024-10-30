class Dyr:
  """
  Klasse for å lage dyr
  Parametre:
    navn (str): Dyrets personlige navn
    rase (str): Dyrets rase
    farge (str): Dyrets farge
    hale="Lang" (str): Beskrivelse av dyrets hale

  Intern variabel
    alder=0 (int): Dyrets alder i antall år. Endres med metoden aldring()
  """
  def __init__(self,navn:str,rase:str,farge:str,hale:str="Lang"):
    """
    Konstruktør
    """
    self.navn = navn
    self.rase = rase
    self.farge = farge
    self.hale = hale
    self.alder = 0 

  def dyr_info(self):
    """
    Metode for utskrift
    """
    print(f"{self.navn} er en {self.farge.lower()} {self.rase.lower()}")

  def aldring(self,antall:int):
    """
    Metode for å øke dyrets alder med et gitt antall år
    Parametre:
      antall (int): Antall år som har gått siden siste oppdatering
    Output:
      Skriver ut ny beregnet alder
    """
    self.alder += antall
    print(f"{self.navn} er nå {self.alder} år")




class Katt(Dyr):
  """
  Klasse for å lage katter
  Parametre:
    navn (str): Kattens personlige navn
    rase (str): Kattens rase
    farge (str): Kattens farge
    hale="Lang" (str): Beskrivelse av kattens hale
    liv=0 (int): Antall liv katten har brukt (av 9). Endres med metoden antall_liv()

  Intern variabel
    alder=0 (int): Kattens alder i antall år. Endres med metoden aldring()
  """ 
  def __init__(self,navn,rase,farge,hale="Lang",liv=0):
    """
    Konstruktør
    """
    super().__init__(navn,rase,farge,hale)
    self.liv = liv                        
  
  def snakk(self):
    """
    Metode for at katten snakker
    Output:
      Skriver ut at katten sier Mjau
    """
    print(f'{self.navn} sier "Mjau"')

  def antall_liv(self):
    """
    Metode for å øke antall brukte liv med 1.
    Output:
      Skriver ut hvor mange liv som er brukt. Eller at det er alle hvis antallet er 9 eller mer.
    """
    self.liv += 1
    if self.liv >= 9:
      print(f"{self.navn} har nå brukt alle sine liv :(")
    else:
      print(f"{self.navn} har nå brukt {self.liv} liv.")


class Hund(Dyr):
  """
  Klasse for å lage hunder
  Parametre:
    navn (str): Hundens personlige navn
    rase (str): Hundens rase
    farge (str): Hundens farge
    hale="Lang" (str): Beskrivelse av hundens hale

  Intern variabel
    alder=0 (int): Hundens alder i antall år. Endres med metoden aldring()
  """ 
  def __init__(self,navn,rase,farge,hale="Lang"):
    """
    Konstruktør
    """
    super().__init__(navn,rase,farge,hale)
  
  def snakk(self):
    """
    Metode for at hunden snakker
    Output:
      Skriver ut at hunden sier Voff
    """
    print(f'{self.navn} sier "Voff"')
