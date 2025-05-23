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


class Knapp(Firkant):
  """
  Knapper er firkanter med tekst, arver fra klassen Firkant

    Nye egenskaper
      betydning: tekst, font

    Nye metoder:
      vis_tekst: setter teksten venstrestilt, sentrert i høyden

  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,farge,tekst:str,font):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tekst = tekst
    self.font = font

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}\nTekst: {self.tekst}"

  def vis_tekst(self,align="v"):
    # sett teksten sentrert i høyden
    # hvis align = "v": venstrestilt. Ellers høyrestilt.
    knapp_tekst = self.font.render(str(self.tekst),True, "black")
    tekst_hoyde = knapp_tekst.get_height()
    tekst_bredde = knapp_tekst.get_width()
    forskyvning_y = (self.hoyde - tekst_hoyde)/2
    if align == "v": # venstrestilt
      forskyvning_x = forskyvning_y + 5 # juster etter behov
    else: # høyrestilt
      forskyvning_x = self.bredde - tekst_bredde - 5 # juster etter behov
    self.vindu.blit(knapp_tekst,(self.x+forskyvning_x,self.y + forskyvning_y))




class Nedtrekk(Knapp):
  """
  Nedtrekksmenyer er Knapper med en tilhørende liste med knapper for alternativer
                  arver fra klassen Knapp

    Nye egenskaper
      alternativer:     liste med alternativer for nedtrekksmenyen
      alternativ_farge: farge til bruk på alternativene
      alt_obj:          liste med objekter for alternativene
      vis:              True / False for visning av alternativene
                        alternativene kan trykkes på når vis er True

    Nye metoder
      lag_alt_obj:      fyll listen alt_obj med objekter for alternativene
                        Ting som kan være annerledes enn hovedknappen:
                        bredde, hoyde:  størrelse på nedtrekksalternativene
                        font
                        skift:          antall alternativer i høyden (lager
                                        flere kolonner med alternativer)

  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,farge,tekst:str,font,alternativer:list,alt_farge,vis:bool=False):
    super().__init__(vindu,x,y,bredde,hoyde,farge,tekst,font)
    self.alternativer = alternativer
    self.alt_farge = alt_farge
    self.alt_obj = [] 
    self.vis = vis
  
  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}\nTekst: {self.tekst}\nAlternativer: {self.alternativer}\nFarge: {self.alt_farge}"

  def lag_alt_obj(self,bredde:int,hoyde:int,font,skift:int=0):
    # lag liste med objekter, ett objekt for hvert alternativ
    skift_x = 0
    skift_y = 0
    for i in range(len(self.alternativer)):
      if skift == 0:
        self.alt_obj.append(Knapp(self.vindu,self.x,self.y+self.hoyde+i*hoyde,bredde,hoyde,self.alt_farge,self.alternativer[i],font))
      else:
        self.alt_obj.append(Knapp(self.vindu,self.x+skift_x*bredde,self.y+self.hoyde+skift_y*hoyde,bredde,hoyde,self.alt_farge,self.alternativer[i],font))
        skift_y += 1
        if skift_y % skift == 0:
          skift_x += 1
          skift_y = 0

