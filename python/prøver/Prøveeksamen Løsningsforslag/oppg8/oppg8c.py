"""
Kilde: Tok utgangspunkt i programmet jeg lagde for å øve på eksamen for høsten 2024
       Gjorde endringer slik at programmet passet til årets Prøveeksamen våren 2025

"""

##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# For datasett innlest fra CSV-fil
import csv

# For grafer inn i pygame
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from io import BytesIO
# Sett Matplotlib til ikke-interaktiv modus med "Agg" som backend
matplotlib.use("Agg")

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q, K_x)

# Egne KLASSER for knapper og nedtrekksmenyer 
import pygame_graf_H24_klasser_final as pk

######################################
# KONSTANTER, VINDU og FONT          #
######################################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 1000
VINDU_HOYDE  = 700

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font_overskrift = pg.font.SysFont("Arial",24)
font_knapp = pg.font.SysFont("Arial",20)
font_nedtrekk = pg.font.SysFont("Arial",20)

KNAPP_BREDDE = 300
KNAPP_HOYDE = 40
NEDTREKK_BREDDE = 300
NEDTREKK_HOYDE = 40

MENY_X = 50
MENY_Y = 50
MENY_FARGE = "magenta"
NEDTREKK_FARGE = "magenta3"
HOVER_FARGE = "green"

##########################################
# DATASETT, TABELL, STOLPEDIAGRAM        #
##########################################

filnavn = "Innvandring fra 2000.csv"
alt = []

# Leser med csv.reader for å kunne endre overskriftene som inneholder å og ø
with open(filnavn,encoding="ansi") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  tittel = next(hele_filen)
  tom = next(hele_filen)
  overskrifter = next(hele_filen)
  for linje in hele_filen:
    alt.append(linje)

#print(alt)
verdensdel = []
antall = 0
antall2025 = []
aar = []

for i in range(len(alt)):
  if alt[i][0] not in verdensdel:
    # Stolpediagram x-verdier oppg 8a, valgmuligheter oppg 8c
    verdensdel.append(alt[i][0])
    # Tar vare på antall fra ett år, for å regne differanse året etter
    antall=int(alt[i][2])
    alt[i].append("") # Verdi fra 1999 og dermed første differanse er ukjent
  else:
    # Oppg 8b
    alt[i].append(int(alt[i][2])-antall)
    antall = (int(alt[i][2]))
  # Stolpediagram oppg 8a
  if alt[i][1] == "2025":
    antall2025.append(int(alt[i][2]))
  # Linjediagram x-verdier oppg 8c
  if int(alt[i][1]) not in aar:
    aar.append(int(alt[i][1]))


#print(verdensdel)
#print(aar)

# Oppg 8ab
def tabell():
  print("Verdensdel                          | Årstall    | Innvandrere  | Endring" )
  for i in range(79):
    print("-", end="")
  print()

  for i in range(len(alt)):
    if int(alt[i][1]) >= 2020:
      print(f"{alt[i][0]:35}" + " | ",end="")
      print(f"{str(alt[i][1]):>10}" + " | ",end="")
      print(f"{str(alt[i][2]):>12}" + " | ",end="")
      print(f"{str(alt[i][3]):>10}" + " | ")

  for i in range(79):
    print("-", end="")
  print()

#tabell()

# Oppg 8a
def bargraf():
  nr = []
  referanse = []
  for i in range(len(verdensdel)):
    nr.append(str(i+1))
    referanse.append(str(i+1) + ": " + verdensdel[i])


  fig, ax = plt.subplots()
  bar_colors = ["red", "green", "orange", "gray", "pink", "purple", "cyan", "olive", "brown", "yellow"]
  ax.bar(nr, antall2025,label=referanse, color=bar_colors)
  ax.set_xlabel("Årstall")
  ax.set_ylabel("Antall personer")
  ax.set_title("Innvandring pr 2025")
  ax.grid(axis="y") # linjer i y-retning
  ax.legend(title='Verdensdel',loc=1, prop={'size': 7}) # Font 7

  plt.show()

#bargraf()



##########################
# GRAF                   #
##########################

def graf(xliste,yliste,start,slutt,kolonne):

  tittel = kolonne + "   " + str(start) + " - " + str(slutt)
  # Lag en figur-variabel, og putt grafen inn i den
  fig, ax = plt.subplots()
  ax.plot(xliste, yliste)
  ax.scatter(xliste, yliste)
  ax.set_xlabel("Årstall")
  ax.set_ylabel("Antall personer")
  ax.set_title(tittel)
  ax.set_ylim(0,650000)

  # For verdiene på x-aksen:
  ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  
  # Lagre diagrammet som en bildebuffer
  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig) # Putter figurvariabelen inn i png-filen
  bilde_av_graf = pg.image.load(buf)

  # Skalerer bildet til å passe til vinduet.
  #bilde_skalert = pg.transform.scale(bilde_av_graf,(800,600))
  return bilde_av_graf


###########################
# OBJEKTER                #
###########################


#### LAG KNAPPER FOR VALG ####
titler = ["Velg verdensdel"]
kolonne = pk.Nedtrekk(vindu,MENY_X,MENY_Y,KNAPP_BREDDE,KNAPP_HOYDE,MENY_FARGE,titler[0],font_knapp,verdensdel,NEDTREKK_FARGE,True)

kolonne.lag_alt_obj(NEDTREKK_BREDDE,NEDTREKK_HOYDE,font_nedtrekk)


nedtrekk = [kolonne]

###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet

# Globale variabler - status-sjekk
klikk = False   # Har brukeren klikket med musepekeren?
hover = False

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
  if trykkede_taster[K_q] or trykkede_taster[K_x]: # q for quit, x for eXit
    pg.quit()
    sys.exit()
  
  # Museposisjon for hover-farge
  muspos = pg.mouse.get_pos()
  hover = False

   

  ###############################
  # OBJEKTER, FIGURER og TEKST  #
  ###############################

  #### BAKGRUNN ####
  vindu.fill("bisque")

  #### OVERSKRIFT ####
  pg.display.set_caption("Oppgave 8c")
  overskrift = font_overskrift.render("Innvandring 2000 - 2025", True, "black")
  vindu.blit(overskrift,(10,10))

  #######################
  # VELG FRA MENYENE    #
  #######################

  #### VELG KOLONNE PÅ NYTT, FJERN ÅRSTALL ####
  if klikk and kolonne.obj.collidepoint(x,y):
    if not(kolonne.vis):
      kolonne.tekst = titler[0]
    kolonne.vis = not(kolonne.vis)
    klikk = False

  #### VELG ÅRSTALL PÅ NYTT ####

  #### VELG ALTERNATIVER ####
  else:
    #### VELG KOLONNE, OG VIS FRAM STARTÅR ####
    for n in kolonne.alt_obj:
      if klikk and n.obj.collidepoint(x,y) and kolonne.vis:
        kolonne.tekst = n.tekst
        # Bytt visning
        kolonne.vis = False
        klikk = False
        break
        

  #### TEGN NEDTREKKSMENYER ####
  # Tegn hovedfirkanten med svart kant, vis tekst
  for objekt in nedtrekk:
    if objekt.obj.collidepoint(muspos): # hover
      objekt.tegn(farge=HOVER_FARGE)
      hover = True
    else:
      objekt.tegn()
    objekt.tegn(bredde=2)
    objekt.vis_tekst()

    # Tegn alle alternativene hvis aktuelt
    if objekt.vis:
      for n in objekt.alt_obj:
        if n.obj.collidepoint(muspos): # hover
          n.tegn(farge=HOVER_FARGE)
          hover = True
        else:
          n.tegn()
        n.tegn(bredde=1)
        n.vis_tekst()
  
  #### TEGN GRAF ####
  # Alle tre menyer har verdier
  if kolonne.tekst != titler[0]:
    y_verdier = []

    # Hent x-verdier (årstall) og y-verdier (kolonne) fra datasettet, der det er verdier
    for rad in alt:
        if rad[0] == kolonne.tekst:
          y_verdier.append(int(rad[2]))

    # Tegn grafen
    bilde_skalert = graf(aar, y_verdier, 2000,2025,kolonne.tekst)
    vindu.blit(bilde_skalert, (MENY_X + KNAPP_BREDDE, 3*KNAPP_HOYDE))

  # Musepeker
  if hover:
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
  else:
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    

  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()


