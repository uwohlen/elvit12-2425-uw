# Oppgave

print("Oppgave: Endre diktet Regn av Sigbjørn Obstfelder til å handle om snop ved å bytte ut ord. Ordene som skal byttes ut er spesifisert i variabelen ordliste. Programmet til løsningen skal virke uten endringer selv om ordlisten i oppgaven utvides, man skal altså lett kunne bytte ut enda flere ord senere ved å bare utvide ordlisten.")

tekst = "en er en og to er to;vi hopper i vann vi triller i sand;sikk sakk vi drypper på tak;tikk takk det regner i dag;regn regn regn regn;øsende regn pøsende regn;regn regn regn regn;deilig og vått deilig og rått;en er en og to er to;vi hopper i vann vi triller i sand;sikk sakk vi drypper på tak;tikk takk det regner i dag"

dikt = tekst.split(";")
for i in range(len(dikt)):
  dikt[i] = dikt[i].split(" ")

for linje in dikt:
  print(linje)
print()

ordliste = [
  {
    "original": "regn",
    "ny": "snop"
  },
  {
    "original": "regner",
    "ny": "fråtses"
  }
]

# Løsning:

for linje in dikt:
  for ord in ordliste:
    while ord["original"] in linje:
      indeks = linje.index(ord["original"])
      linje[indeks] = ord["ny"]

for linje in dikt:
  print(linje)


"""
# eksempel på utvidelse av ordlista
ordliste = [
  {
    "original": "regn",
    "ny": "snop"
  },
  {
    "original": "regner",
    "ny": "fråtses"
  },
  {
    "original": "vi",
    "ny": "med"
  },
  {
    "original": "hopper",
    "ny": "sukker"
  },
  {
    "original": "vann",
    "ny": "alt"
  },
  {
    "original": "triller",
    "ny": "bading"
  },
  {
    "original": "sand",
    "ny": "salt"
  },
  {
    "original": "drypper",
    "ny": "alle"
  },
  {
    "original": "på",
    "ny": "slags"
  },
  {
    "original": "tak",
    "ny": "slag"
  }
]
"""