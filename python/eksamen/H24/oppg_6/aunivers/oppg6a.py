# Oppgave 6a
class Batteri:
  def __init__(self, batteriID: str, energikapasitet: float):
    self.__batteriID = batteriID
    self.__energikapasitet = energikapasitet
    self.__energimengde = 0.0  # Starter med tomt batteri

  def ladOpp(self, energi: float) -> None:
    """Lader batteriet med en gitt mengde energi."""
    if energi < 0:
      raise ValueError("Energi som lades opp må være positiv.")
    self.__energimengde = min(self.__energimengde + energi, self.__energikapasitet)

  def brukEnergi(self, energi: float) -> None:
    """Bruker en gitt mengde energi fra batteriet."""
    if energi < 0:
      raise ValueError("Energiforbruk må være positivt.")
    if energi > self.__energimengde:
      raise ValueError("Ikke nok energi på batteriet.")
    self.__energimengde -= energi

  def visEnerginivå(self) -> float:
    """Viser hvor mye energi som er igjen i batteriet."""
    return self.__energimengde