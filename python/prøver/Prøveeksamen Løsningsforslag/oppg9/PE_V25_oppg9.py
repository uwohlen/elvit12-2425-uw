#########################
# IMPORT. START pygame  #
#########################

import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x)
import PE_V25_oppg9_klasser as pk
import random as rd

######################################
# KONSTANTER, VINDU og KLOKKE        #
######################################

VINDU_BREDDE = 240
VINDU_HOYDE = 480
ANTALL_X = 8
ANTALL_Y = 16
PLASS_SIDE = 30

vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
pg.display.set_caption("Oppg 9")
fonten = pg.font.SysFont("Arial",20)
klokke = pg.time.Clock()


###########################
# OBJEKTER, STARTVERDIER  #
###########################

klassen = pk.Klasserom(vindu)
klassen.lag_plassene()

klassen.timen_starter()
#print(klassen)

###########################
# WHILE                   #
###########################

tikk = 0

while True:

  #### BRUKER-INPUT ####
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()

  #### TEGN STATUS ####
  vindu.fill("bisque")

  for rad in klassen.plasser:
    for kol in rad:
      kol.tegn()


  #### OPPDATER læringsgrad ####
  
    #### OPPDATER VINDU ####
  if tikk < 90:
    klassen.kompetansen_gror()
    tikk += 1
  else:
    for rad in klassen.plasser:
      for kol in rad:
        if kol.lerer:
          kol.farge = "white"
    snitt = klassen.snitt()
    pg.draw.rect(vindu,"salmon",(20,100,200,40))
    pg.draw.rect(vindu,"black",(20,100,200,40),width=2)
    tekst = fonten.render("Gjennomsnitt: "+str(snitt),True,"black")
    vindu.blit(tekst,(30,107))

  pg.display.flip()
  klokke.tick(10)

