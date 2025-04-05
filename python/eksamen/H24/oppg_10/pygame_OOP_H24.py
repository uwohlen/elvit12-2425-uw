import pygame as pg
import sys
pg.init()


VINDU_BREDDE = 1280
VINDU_HOYDE = 720
vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  pg.display.flip()