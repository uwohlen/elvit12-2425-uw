##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# For grafer inn i pygame
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
# Sett Matplotlib til ikke-interaktiv modus med "Agg" som backend
matplotlib.use("Agg")

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q,K_RETURN)

########################
# KONSTANTER           #
########################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 1000
VINDU_HOYDE  = 700



########################
# VINDU og FONT        #
########################

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)


##########################
# DATASETT og GRAF       #
##########################

x_verdier = ["A","B","C","D"]
y_verdier = [10,15,13,8]

# Lag en figur-variabel, og putt grafen inn i den
fig, ax = plt.subplots()
ax.bar(x_verdier, y_verdier)

# Lagre diagrammet som en bildebuffer
buf = BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
plt.close(fig) # Putter figurvariabelen inn i png-filen
bilde_av_graf = pg.image.load(buf)

# Skalerer bildet til å passe til vinduet.
bilde_skalert = pg.transform.scale(bilde_av_graf,(600,500))


###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet

# Globale variabler - status-sjekk
enter = False # Har brukeren trykket Enter-tasten?
klikk = False # Har brukeren klikket med musepekeren?
skjult = True # Har brukeren åpnet nedtrekksmenyen?
valg_objekter = [] # objekter for "kollisjon" av alternativene
valgt = ""    # Har brukeren valgt noe fra nedtrekksmenyen?
  
while True:

  ###################
  # BRUKER-INPUT    #
  ###################

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
  
  

  ###############################
  # OBJEKTER, FIGURER og TEKST  #
  ###############################

  #### BAKGRUNN ####
  # Farger bakgrunnen hvit
  vindu.fill("white")

  #### GRAF ####
  # Legger bildet på riktig plass
  vindu.blit(bilde_skalert, (100, 100))


  #### KNAPP ####
  # Det som er tegnet sist vil vises, pixel for pixel

  # Hva skjer om Enter-tasten er trykket på en gang
  if enter:
    firkant_farge = "green"
  else:
    firkant_farge = "magenta"
  
  # Lager et OBJEKT som man kan "kollidere" med
  knapp = pg.Rect(10,10,100,40) 
  # Tegner et rektangel samme sted pg.draw.rect(vindu,farge,(x,y,b,h))
  if knapp.collidepoint(muspos): # HOVER (dvs ikke klikk)
    pg.draw.rect(vindu, "deeppink4", knapp)
  else:
    pg.draw.rect(vindu,firkant_farge,knapp)

  
  # Lager en tekst i form av et bilde og legger til bildet i vinduet
  # bilde = font.render(tekst, True, farge)
  # vindu.blit(bilde, (x, y)) for øvre venstre hjørne av teksten
  # teksten legger seg over firkanten pga valgte koordinater

  bilde = font.render("OK", True, "black")
  vindu.blit(bilde, (20, 15))


  #### NEDTREKKSMENY ####

  # Alternativene som skal stå i nedtrekksmenyen:
  alternativer = ["Alt 1","Alt 2","Alt 3"]
  
  # Hovedruta for nedtrekksmenyen
  nedtrekk = pg.Rect(120,10,100,40) # objekt
  pg.draw.rect(vindu,"magenta",nedtrekk) 

  

  ########################
  # KLIKK + COLLIDEPOINT #
  ########################  

  # Tegner en sirkel der man klikker, men bare på knappen, ikke utenfor
  if klikk and knapp.collidepoint((x,y)):
      # pg.draw.circle(vindu,farge,(x,y) for sirkelsentrum,radius)
      pg.draw.circle(vindu,"purple",(x,y),5)
      valg_objekter = []

  # Vis fram alternativene i nedtrekksmenyen
  elif klikk and nedtrekk.collidepoint((x,y)): # klikket på nedtrekksmenyen
    valgt = ""
    valg_objekter = []
    for i in range(len(alternativer)): # åpne nedtrekksmenyen ved å tegne firkanter
      valg_objekter.append(pg.Rect(120,50+40*i,100,40)) # settes under den forrige
      pg.draw.rect(vindu,"magenta3",valg_objekter[i])
      nedtrekk_bilde1 = font.render(alternativer[i],True,"black")
      vindu.blit(nedtrekk_bilde1,(130,55+40*i))
  else:
    # Sjekk om man klikket på et alternativ
    for i in range(len(valg_objekter)):
      if klikk and valg_objekter[i].collidepoint((x,y)):
        valgt = alternativer[i]
        klikk = False
    # Alternativene er brukt opp, eller man klikket utenfor
    valg_objekter = []


  # Oppdater nedtrekksmenyen basert på alternativ valgt
  if valgt == "":
    nedtrekk_bilde = font.render("Velg", True, "black")
    vindu.blit(nedtrekk_bilde,(130,15))
  else:
    nedtrekk_bilde = font.render(valgt, True, "black")
    vindu.blit(nedtrekk_bilde,(130,15))


  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()
