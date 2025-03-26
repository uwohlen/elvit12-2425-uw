##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q,K_RETURN)

########################
# KONSTANTER           #
########################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 600
VINDU_HOYDE  = 600



########################
# VINDU og FONT        #
########################

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)


###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet
enter = False # Har brukeren trykket Enter-tasten?
klikk = False # Har brukeren klikket med musepekeren?

while True:

  #### BRUKER-INPUT ####
  for event in pg.event.get():
    # Sjekker om brukeren har lukket vinduet (X i øvre høyre hjørne)
    if event.type == pg.QUIT:
      pg.quit() # avslutter med en gang
      sys.exit()
    # Sjekker om brukeren har klikket med musepekeren
    elif event.type == pg.MOUSEBUTTONDOWN:
      x, y = pg.mouse.get_pos() # får tak i posisjonen
      klikk = True

  # Henter en liste med status for alle tastatur-taster
  trykkede_taster = pg.key.get_pressed()
  # Sjekker om brukeren har trykket på tastaturet siden forrige runde 
  # Behandler forskjellige taster (flere kan være brukt):
  if trykkede_taster[K_q]: # q for quit
    pg.quit()
    sys.exit()
  if trykkede_taster[K_RETURN]: # Enter-tasten for f.eks. å velge "OK-knappen"
    enter = True

  # Kontinuerlig innhentig av museposisjon
  muspos = pg.mouse.get_pos() # ikke avhengig av klikk
  

  #### BAKGRUNN ####
  # Farger bakgrunnen hvit
  vindu.fill("white")



  #### FIGURER OG TEKST ####
  # Det som er tegnet sist vil vises, pixel for pixel

  # Hva skjer om Enter-tasten er trykket på en gang
  if enter:
    firkant_farge = "green"
  else:
    firkant_farge = "magenta"
  
  # Lager et OBJEKT som man kan "kollidere" med
  knapp = pg.Rect(10,10,100,50) 
  # Tegner et rektangel samme sted pg.draw.rect(vindu,farge,(x,y,b,h))
  if knapp.collidepoint(muspos): # hover
    pg.draw.rect(vindu, "deeppink4", knapp)
  else:
    pg.draw.rect(vindu,firkant_farge,knapp)

  
  # Lager en tekst i form av et bilde og legger til bildet i vinduet
  # bilde = font.render(tekst, True, farge)
  # vindu.blit(bilde, (x, y)) for øvre venstre hjørne av teksten
  # teksten legger seg over firkanten

  bilde = font.render("OK", True, "black")
  vindu.blit(bilde, (20, 20))

  # Tegner en sirkel der man klikker, men bare på knappen, ikke utenfor
  if klikk and knapp.collidepoint((x,y)):
      # pg.draw.circle(vindu,farge,(x,y) for sirkelsentrum,radius)
      pg.draw.circle(vindu,"purple",(x,y),5)
  


  #### OPPDATER VINDU ####
  pg.display.flip()
