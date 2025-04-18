import csv
filnavn = "05994_20240126-145813-csv.csv"
alt = []

with open(filnavn,encoding="ansi") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  kast = next(hele_filen)
  kast = next(hele_filen)
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

print(overskrifter)
print(alt)
