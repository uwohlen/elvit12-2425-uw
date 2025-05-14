class Dag_info:
  """
  Objekter av denne klassen inneholder
    ukedag (tekst)
    mm nedbør (float)

  Verdier settes (eller endres) og hentes ved hjelp av metodene
    set_ukedag(dag)
    get_ukedag()
    set_mm(verdi)
    get_mm()
  """
  def __init__(self) -> None:
    # Verdier settes inn ved metoder
    self.__ukedag:str
    self.__mm:float

  def set_ukedag(self,dag:str) -> None:
    self.__ukedag = dag
  
  def get_ukedag(self) -> str:
    return self.__ukedag
  
  def set_mm(self,mm:float) -> str:
    """
    Sjekker input-data før verdien lagres
    Gir feilmelding om verdien:
    -er negativ
    -er for stor > 250 mm
    -er av feil format (ikke int, float)
    """
    if type(mm) == str or type(mm) == float or type(mm) == int:
      try:
        mm = float(mm)
        if mm < 0:
          return "Nedbørsmengde må angis som et positivt tall."
        elif mm > 250:
          return "Største tillatte verdi er 250 mm. Hvis nedbøren virkelig er høyere: kontakt programmereren for redigering av metoden."
        else:
          self.__mm = mm
          return "Nedbør lagret"
      except:
        return "Tekstverdien kan ikke gjøres om til tall. Skriv inn et ekte tall."
    else:
      return "Nedbørsmengden må være et tall av typen int eller float."

  def get_mm(self) -> float:
    return self.__mm
  

class Registrering:
  """
  Objekter av denne klassen inneholder en liste
    Listen inneholder objekter av klassen Dag_info

  Verdier legges til i listen og hentes ved metodene
    lett_til_en(mm)
    get_liste()
  
  Total mm nedbør siden starten av registreringen
    total()

  """
  def __init__(self) -> None:
    # Starter med en tom liste, verdier settes inn ved metoder
    self.__liste:list[Dag_info] = []

  def get_liste(self) -> list[Dag_info]:
    return self.__liste
  
  def legg_til_en(self,mm:float) -> str:
    # Lag objekt
    ny_dag_for_test = Dag_info()
    
    # Sjekk antall mm nedbør
    sjekk = ny_dag_for_test.set_mm(mm)
    if sjekk == "Nedbør lagret":
      # Ukedager
      uke = ["Ma","Ti","On","To","Fr","Lø","Sø"]
      # Starter med mandag, går gjennom listen
      # Etter søndag kommer mandag igjen
      # Indeks for uke-listen basert på 
      # hvor mange verdier vi har registrert så langt:
      n = len(self.__liste) % len(uke)
      # Legg inn riktig dag
      ny_dag_for_test.set_ukedag(uke[n])

      # Utvid listen
      self.__liste.append(ny_dag_for_test)
    return sjekk

  def total(self) -> float:
    total = 0
    for info in self.__liste:
      total += info.get_mm()
    return total

  
