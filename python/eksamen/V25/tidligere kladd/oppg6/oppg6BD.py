# oppgaven ber om Låner etc. med å, så da bruker jeg æøå i klassenavn og variabelnavn, ellers ville jeg unngått det
# oppgaven bruker kamelSkrift, så da skriver jeg det, ellers ville jeg brukt under_strek i python


# Klasse Bok

class Bok:
  """
  Klasse for en bok på biblioteket

  Parametre:
    tittel (str): bokens tittel
    forfatter (str): bokens forfatter

  Intern variabel
    utlånt: objekt av klassen Låner, eller verdien False (boolsk)
  """
  def __init__(self, tittel:str, forfatter:str):
    """
    Konstruktør: tittel, forfatter, utlånt
    """
    self.tittel = tittel
    self.forfatter = forfatter
    self.utlånt = False
    
  def visInfo(self):
    """
    Returnerer en setning med verdiene til boken
    """
    if type(self.utlånt) == bool:
      lånt = ", er ikke utlånt"
    else:
      lånt = ", er lånt av " + str(self.utlånt.lånerID)
    return self.tittel + ": " + self.forfatter + lånt

  def lånUt(self, person):
    """
    Metode for å låne ut boken
      self = boken man skal låne ut
      person = låneren boken skal lånes ut til
      Boken får låneren lagt inn under self.utlånt. Låneren får boken lagt til i sin liste lånteBøker.
    """
    if type(self.utlånt) == bool:
      self.utlånt = person
      person.lånteBøker.append(self)
      print("Boklån registrert:",self.tittel)
    else:
      print(f"Boken: '{self.tittel}' er allerede utlånt. Velg en annen bok.")


  def leverTilbake(self):
    """
    Metode for å levere tilbake boken
      self.utlånt = False
      person får boken fjernet fra lånteBøker
    """
    if type(self.utlånt) != bool: # 6D - sjekker at boken er lånt ut før levering
      self.utlånt.lånteBøker.remove(self)
      self.utlånt = False
      print("Boken er levert tilbake:",self.tittel)
    else:
      print(f"Boken '{self.tittel}' er ikke lånt ut. Velg en annen bok.")

# Klasse Låner

class Låner:
  """
  Klasse for en person som låner bøker
  
  Intern variabel
    lånteBøker (list): liste med Bok-objekter som personen har lånt

  Klassevariabel:
    lånerID (int): unikt id-nummer for hver lånetaker
  """
  lånerID = 0
  def __init__(self):
    """ 
    Konstruktør: lånerID, lånteBøker
    """
    self.lånerID = Låner.lånerID
    Låner.lånerID += 1
    self.lånteBøker = []

  def __str__(self):
    """
    print(låner) vil skrive en setning med personens registrerte verdier
    """
    if len(self.lånteBøker) == 0:
      bøker = " har ikke lånt noen bøker akkurat nå."
    else:
      bøker = " har lånt \n"
      for bok in self.lånteBøker:
        bøker += bok.tittel + "\n"
    return "Låner ID " + str(self.lånerID) + bøker

  def lånBok(self,lånebok):
    """
    Metode for å låne en bok
      self = personen som skal låne boka, boka blir lagt til self.lånteBøker
      lånebok = boken som skal lånes, personen blir lagt til lånebok.utlånt
    """
    if type(lånebok.utlånt) == bool:
      lånebok.utlånt = self
      self.lånteBøker.append(lånebok)
      print("Boklån registrert:",lånebok.tittel)
    else:
      print(f"Boken '{lånebok.tittel}' er allerede utlånt. Velg en annen bok.")

  def leverTilbakeBok(self,lånebok):
    """ 
    Metode for å levere tilbake en bok
      self = personen som skal levere boka, boka blir fjernet fra self.lånteBøker
      lånebok = boken som skal leveres, lånebok.utlånt = False
    """
    if lånebok in self.lånteBøker: # 6D - sjekker at personen har lånt boken før levering
      self.lånteBøker.remove(lånebok)
      lånebok.utlånt = False
      print("Boken er levert tilbake:",lånebok.tittel)
    else:
      print(f"Låner nr. {self.lånerID} har ikke lånt boken '{lånebok.tittel}'. Velg en annen bok.")