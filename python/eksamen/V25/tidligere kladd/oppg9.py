import pygame as pg
import random as rd
from pygame.locals import (K_q, K_r, K_n)

# Konstanter 
GRONN = (0,153,0)
HVIT = (255,255,255)
GUL = (255,204,0)
GRAA = (150,150,150)
SVART = (0,0,0)
FRAMES_PER_SECOND = 15
ANTALL = 40
KVADRAT = 15
VINDU_BREDDE = ANTALL*KVADRAT
VINDU_HOYDE  = VINDU_BREDDE

# Initialiserer pygame
pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Firkant:
    """
    Firkanter kan tegnes på skjermen, skifter farge, sjekker naboruter
    
    Parametre
        i (int): rad (y-retning)
        j (int): kolonne (x-retning)
        side (int): firkantens bredde og høyde
        farge (RGB-tuppel): firkantens farge
        vindusobjekt (pygame.Surface): spillebrettet
        nabotype(int): om firkanten er i et hjørne eller midt på
    
    Flere egenskaper:
        x (int): firkantens x-posisjon på spillebrettet
        y (int): firkantens y-posisjon på spillebrettet
        obj (pygame.Rect): rektangelobjekt
        brann_rundt (bool): om et nabotre brenner (True) eller ikke (False)

    Metoder:
        tegn(self): tegner firkanten i vindusobjektet
        gro_et_tre(self): bruker tilfeldighet for å avgjøre om et tre vokser opp
        lyn_blir_brann(self): bruker tilfeldighet for å avgjøre om et lyn treffer et tre
        sjekk_for_brann(self,alle): sjekker naboruter for brennende trær
        spredning_av_brann(self): oppdaterer brannstatus basert på naboruter
        
    """
    def __init__(self, i:int, j:int, nabotype:int, farge=HVIT, side:int=KVADRAT, vindusobjekt=vindu):
        self.i = i
        self.j = j
        self.x = j*side
        self.y = i*side
        self.nabotype = nabotype
        self.farge = farge
        self.side = side # bredde og høyde på firkantene
        self.vindusobjekt = vindusobjekt
        self.brann_rundt = False
        #objekt:
        self.obj = pg.Rect(self.x, self.y, self.side, self.side)

    def tegn(self):
        """Tegner firkanten"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x+1, self.y+1, self.side-2, self.side-2))

    def gro_et_tre(self):
        sjanse = rd.random()
        if sjanse < 0.003 and self.farge == HVIT and self.brann_rundt == False:
            self.farge = GRONN
        
    def lyn_blir_brann(self):
        sjanse = rd.random()
        if sjanse < 0.0003 and self.farge == GRONN:
            self.farge = GUL

    def sjekk_for_brann(self,alle):
        self.brann_rundt = False
        if self.nabotype == 0:
            for a in range(0,2):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 1:
            for a in range(0,2):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True
            
        elif self.nabotype == 2:
            for a in range(0,2):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 3:
            for a in range(-1,2):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 4:
            for a in range(-1,2):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True
        
        elif self.nabotype == 5:
            for a in range(-1,2):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 6:
            for a in range(-1,1):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 7:
            for a in range(-1,1):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        elif self.nabotype == 8:
            for a in range(-1,1):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == GUL:
                        if not(a==0 and b==0):
                            self.brann_rundt = True

        

    def spredning_av_brann(self):
        if self.farge == GRONN and self.brann_rundt:
            self.farge = GUL
        elif self.farge == GUL:
            self.farge = HVIT


# Lager objektene

ruter = [] # liste med firkanter som kan tegnes
objekter = [] # liste med Rect-objekter

for i in range(ANTALL):
    ruter.append([])
    objekter.append([])
    for j in range(ANTALL):
        if i==0 and j==0:
            ntype = 0
        elif i==0 and j<ANTALL-1:
            ntype = 1
        elif i==0 and j==ANTALL-1:
            ntype = 2
        elif i<ANTALL-1 and j==0:
            ntype = 3
        elif i<ANTALL-1 and j<ANTALL-1:
            ntype = 4
        elif i<ANTALL-1 and j==ANTALL-1:
            ntype = 5
        elif i==ANTALL-1 and j==0:
            ntype = 6
        elif i==ANTALL-1 and j<ANTALL-1:
            ntype = 7
        elif i==ANTALL-1 and j==ANTALL-1:
            ntype = 8
        else:
            print("Feil ntype")
        rute = Firkant(i, j, ntype)
        ruter[i].append(rute)
        objekter[i].append(rute.obj)

#print(len(ruter),ruter[1][1].farge, ruter[39][39].nabotype)

# Farger hele spillebrettet grått
vindu.fill(GRAA)

for i in range(len(ruter)):
    for j in range(len(ruter[i])):
        ruter[i][j].tegn()

pg.display.flip()

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        elif event.type == pg.KEYUP:

            if event.key == K_q: # quit
                fortsett = False

            elif event.key == K_r: # reset
                vindu.fill(GRAA)
                for i in range(len(ruter)):
                  for j in range(len(ruter[i])):
                      ruter[i][j].farge = HVIT             

    # Tegner ruter basert på oppdateringer i forrige runde
    vindu.fill(GRAA)
    
    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
                ruter[i][j].tegn() # ståa slik den er nå
    
    # Gjør klar for neste runde:
    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
            ruter[i][j].gro_et_tre() # der det ikke er brann i nærheten

    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
            ruter[i][j].spredning_av_brann() # basert på forrige opptelling
    
    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
            ruter[i][j].lyn_blir_brann() # nye branntilløp

    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
            ruter[i][j].sjekk_for_brann(ruter) # opptelling av ny status
    
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
    
    # Oppdaterer alt innholdet i vinduet
    #pg.display.flip()
    pg.display.update()
    

# Avslutter pygame
pg.quit()
