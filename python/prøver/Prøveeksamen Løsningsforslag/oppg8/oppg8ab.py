"""
Kilde: Tok utgangspunkt i programmet jeg lagde for å øve på eksamen for høsten 2024
       Gjorde endringer slik at programmet passet til årets Prøveeksamen våren 2025
"""

##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
#pg.init()

# For datasett innlest fra CSV-fil
import csv

# For grafer inn i pygame
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from io import BytesIO
# Sett Matplotlib til ikke-interaktiv modus med "Agg" som backend
#matplotlib.use("Agg")

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
#vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
#font_overskrift = pg.font.SysFont("Arial",24)
#font_knapp = pg.font.SysFont("Arial",20)
#font_nedtrekk = pg.font.SysFont("Arial",20)

KNAPP_BREDDE = 160
KNAPP_HOYDE = 40
NEDTREKK_BREDDE = 160
NEDTREKK_HOYDE = 40
NEDTREKK_BREDDE_2D = 50
NEDTREKK_HOYDE_2D = 30

MENY_X = 50
MENY_Y = 50
MENY_FARGE = "magenta"
NEDTREKK_FARGE = "magenta3"
HOVER_FARGE = "green"

#######################################
# DATASETT, TABELL, STOLPEDIAGRAM     #
#######################################

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

for i in range(len(alt)):
  if alt[i][0] not in verdensdel:
    # Stolpediagram x-verdier oppg 8a
    verdensdel.append(alt[i][0])
    # Oppg 8b Tar vare på antall fra ett år, for å regne differanse året etter
    antall=int(alt[i][2]) # Verdi fra 1999 og dermed første differanse er ukjent
    alt[i].append("")
  else:
    # Oppg 8b
    alt[i].append(int(alt[i][2])-antall)
    antall = (int(alt[i][2]))
  # Stolpediagram y-verdier oppg 8a
  if alt[i][1] == "2025":
    antall2025.append(int(alt[i][2]))


print(verdensdel)

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

tabell()

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
