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
  
  def set_mm(self,verdi:float) -> None:
    self.__mm = verdi

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
  
  def legg_til_en(self,mm:float) -> None:
      # Ukedager
      uke = ["Ma","Ti","On","To","Fr","Lø","Sø"]
      # Starter med mandag, går gjennom listen
      # Etter søndag kommer mandag igjen
      # Indeks for uke-listen basert på 
      # hvor mange verdier vi har registrert så langt:
      n = len(self.__liste) % len(uke)
      # Utvid listen
      self.__liste.append(Dag_info())
      # Legg inn riktig dag
      self.__liste[-1].set_ukedag(uke[n])
      # Legg inn antall mm nedbør
      self.__liste[-1].set_mm(mm)

  def total(self) -> float:
    total = 0
    for info in self.__liste:
      total += info.get_mm()
    return total

  
