import pygame as pg

class Firkant:
  """
  Firkanter blir objekter og kan tegnes

    Egenskaper
      plassering: x,y i vindu
      størrelse:  bredde, høyde
      farge:      fargekode eller fargenavn
      objekt:     obj

    Metoder
      tegn: bredde: angis om det er kantstrek, ellers blir det heldekkende farge
            farge:  kan angi nye farger
            radius: kan angi runde hjørner
      
      __str__: for utskrift av egenskaper
  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,farge):
    self.vindu = vindu
    self.x = x
    self.y = y
    self.bredde = bredde
    self.hoyde = hoyde
    self.farge = farge
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def tegn(self,bredde:int=0,farge="",radius:int=-1):
    # tegn firkanten
    if bredde == 0:
      # heldekkende farge
      if farge == "":
        # bruk firkantens farge
        pg.draw.rect(self.vindu, self.farge, self.obj, bredde, radius)
      else: 
        # bruk en annen farge
        pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)
    else:
      # tegn omriss
      if farge == "":
        # hvis angitt farge mangler, så settes det til svart omriss
        farge = "black"
      pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)
      

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"


class Person(Firkant):
  """
  Personer er firkanter med varierende grafikk, arver fra klassen Firkant

    Nye egenskaper
      helsetilstand: tilstand
      smitte rundt person: naboer

    Redigert metode:
      tegn: verdi av tilstand påvirker grafikken
      
  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,tilstand,naboer,farge="gray"):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tilstand = tilstand
    self.naboer = naboer

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nTilstand: {self.tilstand}\nNaboer: {self.naboer}"

  def tegn(self):
    pass