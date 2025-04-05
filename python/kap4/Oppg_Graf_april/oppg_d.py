import csv

filnavn = "bank.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        innhold.append(rad)

overskrifter[0] = "ID"
overskrifter[1] = "Kjønn"
overskrifter[2] = overskrifter[2].capitalize() + " (kr)"
overskrifter[3] = "Rente (%)"
overskrifter.append("Etter ti år (kr)")
#print(overskrifter)
for rad in innhold:
    rad[0] = int(rad[0])
    rad[2] = int(rad[2])
    rad[3] = float(rad[3].replace(",","."))
    rad.append(rad[2]*(1+rad[3]/100)**10)

#print(innhold)


