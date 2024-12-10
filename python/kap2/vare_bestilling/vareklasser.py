import personklasser as pk
class Vare:
  __vare_nr = 0
  def __init__(self,varenavn:str,antall:int):
    Vare.__vare_nr += 1
    self.__vare_nr = Vare.__vare_nr
    self.varenavn = varenavn
    self.antall = antall

  def __str__(self):
    return str(self.__vare_nr) + " - " + self.varenavn + " : " + str(self.antall)
  
  def oppdater_antall(self,flere: int):
    self.antall += flere

class Bestilling:
  __bestilling_nr = 0
  def __init__(self):
    Bestilling.__bestilling_nr += 1
    self.__bestilling_nr = Bestilling.__bestilling_nr
    self.varer = []

  def legg_til_vare(self,vare:Vare):
    if vare.antall > 0:
      self.varer.append(vare)
      vare.antall -= 1
    else:
      print("Tomt for varen:",vare.varenavn)

  def legg_til_kunde(self,kunde:pk.Kunde):
    self.kunde = kunde

  def __str__(self):
    tekst = ""
    try:
      tekst += self.kunde.fornavn + " " + self.kunde.etternavn + ": "
    except:
      pass
    for x in self.varer:
      tekst += x.varenavn + " "
    return str(self.__bestilling_nr) + ": " + tekst  
  