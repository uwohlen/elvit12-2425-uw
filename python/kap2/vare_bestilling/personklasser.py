class Person:
  def __init__(self, fornavn:str, etternavn:str, mobil:str):
    self.fornavn = fornavn
    self.etternavn = etternavn
    self.mobil = str(mobil)
  
  def __str__(self):
    return self.fornavn + " " + self.etternavn + ", " + self.mobil
  
class Ansatt(Person):
  __ansatt_nr = 0
  def __init__(self, fornavn, etternavn, mobil, stilling:str):
    super().__init__(fornavn, etternavn, mobil)
    self.stilling = stilling
    Ansatt.__ansatt_nr += 1
    self.__ansatt_nr = Ansatt.__ansatt_nr

  def __str__(self):
    return str(self.__ansatt_nr) + ": " + self.fornavn + " " + self.etternavn + ", " + self.mobil + ": " + self.stilling

class Kunde(Person):
  __kunde_nr = 0
  def __init__(self, fornavn, etternavn, mobil, adresse:str, postnr:str):
    super().__init__(fornavn, etternavn, mobil)
    Kunde.__kunde_nr += 1
    self.__kunde_nr = Kunde.__kunde_nr
    self.adresse = adresse
    self.postnr = str(postnr)

  def __str__(self):
    return str(self.__kunde_nr) + ": " + self.fornavn + " " + self.etternavn + ", " + self.mobil + ": " + self.adresse + " " + self.postnr
