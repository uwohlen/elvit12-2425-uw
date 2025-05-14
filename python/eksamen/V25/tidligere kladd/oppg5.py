import re

def manipulereBokstav(bokstav, n):
  alfabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ" 
  posisjon = alfabet.index(bokstav)
  nyPosisjon = (posisjon + n) % 29
  return alfabet[nyPosisjon]


def behandleTekst(tekst,n):
  nyTekst = ""
  for bokstav in tekst:
    if re.search("[a-zæøåA-ZÆØÅ]",bokstav):
      nyBokstav = manipulereBokstav(bokstav,n)
      nyTekst = nyTekst + nyBokstav
    else:
      nyTekst = nyTekst + bokstav
  return nyTekst


print(behandleTekst("Hei på deg!",3))
  