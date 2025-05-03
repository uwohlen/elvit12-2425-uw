import pygame as pg
import random as rd
import math

class Plass:
  """
  Plassering i klasserommet
    
  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,side:int=30,farge:str="brown") -> None:
    self.vindu = vindu
    self.x = x
    self.y = y
    self.side = side
    self.farge = farge
    self.elev: bool = False
    self.lerer:bool = False
    self.grad:bool = 0
    self.grit = 0
    self.minutt = 0
    self.obj:pg.rect.Rect = pg.Rect(self.x, self.y, self.side, self.side)

  def __str__(self) -> str:
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: {self.side}\nFarge: {self.farge}\nElev: {self.elev}\nLærer: {self.lerer}\nGrad: {self.grad}"

  def tegn(self) -> None:
    """
    Tegner firkanten i vinduet

    """
    karakter = ["white","yellow","orange","green","blue","purple","brown"]

    if self.elev:
      bordfarge = "gray" + str(self.grit*3)
      pg.draw.rect(self.vindu, bordfarge, self.obj)
      pg.draw.rect(self.vindu, "black", self.obj,width=1)
      farge = karakter[math.floor(self.grad)]
      pg.draw.circle(self.vindu, farge, (self.x+15,self.y+15),10)
      pg.draw.circle(self.vindu, "black", (self.x+15,self.y+15),10, width=1)
    else:
      pg.draw.rect(self.vindu, "black", self.obj,width=1)
      if self.lerer:
        pg.draw.circle(self.vindu,self.farge,(self.x+15,self.y+15),10)
        pg.draw.circle(self.vindu, "black",(self.x+15,self.y+15),10,width=1)

      

class Klasserom:
  """
  Et klasserom inneholder en 2D-liste med 8x16 plasseringer
    32 elever sitter ved 8 firer-bord slik som illustrert
    posisjon (1,1), ...
    Læreren kan bevege seg til alle posisjoner som ikke er opptatt av en elev
  """
  def __init__(self,vindu:pg.surface.Surface,antall_x:int=8,antall_y:int = 16,plass_side = 30) -> None:
    self.vindu = vindu
    self.antall_x = antall_x
    self.antall_y = antall_y
    self.plass_side = plass_side
    self.plasser:list[Plass] = []
  
  def __str__(self) -> str:
      return f"Antall: ({self.antall_x},{self.antall_y})\nSide: {self.plass_side}\nPlasser: {len(self.plasser)}"

  def lag_plassene(self) -> None:
    """
    Sett plasser inn i lista med plasser i klasserommet
      
    """
    for i in range(self.antall_y): # rader
      self.plasser.append([])
      for j in range(self.antall_x): # kolonner
        self.plasser[i].append(Plass(self.vindu,j*self.plass_side,i*self.plass_side,self.plass_side))

  def timen_starter(self) -> None:
    """
    Elever og lærer kommer med tidligere kunnskaper
    
    Sett elever på faste plasser i klasserommet
    Læreren går rundt 

    """
    for i in range(len(self.plasser)):
      for j in range(len(self.plasser[i])):
        if i in [1,2,5,6,9,10,13,14] and j in [1,2,5,6]:
          self.plasser[i][j].elev = True
          self.plasser[i][j].grit = rd.randint(0,33)

    self.plasser[0][0].lerer = True

  def kompetansen_gror(self) -> None:
    """
    Læreren går rundt og lærer bort ting
    """

    # Finn et nytt sted
    finn_ny_plass = True
    while finn_ny_plass:
      ry = rd.randint(0,self.antall_y-1)
      rx = rd.randint(0,self.antall_x-1)
      if not self.plasser[ry][rx].elev: 
        finn_ny_plass = False

    # Gå til det nye stedet
    for i in range(len(self.plasser)):
      for j in range(len(self.plasser[i])):
        if self.plasser[i][j].lerer:
          self.plasser[i][j].lerer = False 
        if i == ry and j == rx:
          self.plasser[i][j].lerer = True

    #Lær bort noe
    for i in range(len(self.plasser)):
      for j in range(len(self.plasser[i])):
        if self.plasser[i][j].elev and self.plasser[i][j].grad < 6: 
          if abs(i-ry)<2 and abs(j-rx)<2:
            self.plasser[i][j].minutt = 0.3
          else:
            if rd.random() < self.plasser[i][j].grit/100:
              bordet = 0
              for m in range(-1,2):
                for n in range(-1,2):
                  bordet += self.plasser[i+m][j+n].grad
              self.plasser[i][j].minutt = bordet/80 + 0.2

    for rad in self.plasser:
      for kol in rad:
        kol.grad += kol.minutt
        kol.minutt = 0

  def snitt(self) -> float:
    """ 
    Gjennomsnittskarakter i klassen
    """
    snitt = 0
    for rad in self.plasser:
      for kol in rad:
        snitt += kol.grad
    snitt = snitt / 32
    return round(snitt,1)
