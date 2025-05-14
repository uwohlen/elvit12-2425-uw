#1 Opprett bøker, lån dem ut til en låner
#2 Test at boken kan lånes ut og leveres tilbake korrekt
#3 Test at det ikke er mulig å låne ut en bok som allerede er utlånt
#4 Identifiser en mulig feil og ett unntak som kan oppstå i programmet

import oppg6BD as kl


# Oppgave 6-C-1, 6-C-2

print("6-C-1 & 2")

bok1 = kl.Bok("Beatles","Lars Saabye Christensen")
bok2 = kl.Bok("The Hobbit","JRR Tolkien")
bok3 = kl.Bok("Murder is easy","Agatha Christie")

print("Lager bøker og lånere")
print(bok1.visInfo())
print(bok2.visInfo())
print(bok3.visInfo())

låner1 = kl.Låner()
låner2 = kl.Låner()

print(låner1)
print(låner2)
print()

print("Låner ut bøker")
bok1.lånUt(låner1)
bok2.lånUt(låner1)
bok3.lånUt(låner1)

print(bok1.visInfo())
print(bok2.visInfo())
print(bok3.visInfo())
print(låner1)

print()
print("Leverer tilbake bøker")
bok2.leverTilbake()
print(låner1)

bok1.leverTilbake()
print(bok1.visInfo())
print(bok2.visInfo())
print(bok3.visInfo())
print(låner1)

print("Låner bøker")
låner2.lånBok(bok2)
låner2.lånBok(bok1)
print(bok1.visInfo())
print(bok2.visInfo())
print(bok3.visInfo())
print(låner2)

print("Leverer bøker")
låner2.leverTilbakeBok(bok1)

print(bok1.visInfo())
print(bok2.visInfo())
print(bok3.visInfo())
print(låner2)

# oppgave 6-C-3

print("6-C-3")
bok2.lånUt(låner1)
låner2.lånBok(bok3)

# oppgave 6-C-4
"""
En mulig feil er at man prøver å levere tilbake feil bok, 
en som ikke har lånt ut, eller ikke til den personen.
"""
print()
print("6-C-4: Leverer tilbake en bok som ikke er lånt ut / som man ikke har lånt")
#bok1.leverTilbake()
#låner1.leverTilbakeBok(bok2)
# ga feilmelding: ValueError: list.remove(x): x not in list
print("Etter implementering:")
bok1.leverTilbake()
låner1.leverTilbakeBok(bok2)
låner2.leverTilbakeBok(bok1)
