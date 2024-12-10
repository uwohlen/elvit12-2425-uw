import personklasser as pk
import vareklasser as vk

ansatte = []

ansatte.append(pk.Ansatt("Unni","Wohlen",90837117,"Baker"))
ansatte.append(pk.Ansatt("Bakermester","Harepus",11111111,"Bakermester"))
varer = []
varer.append(vk.Vare("Pepperkake",3))
varer.append(vk.Vare("Berlinerkranser",28))

kunder = [] 
kunder.append(pk.Kunde("Mikkel","Rev",12345678,"Hakkebakkeskogen","0011"))
kunder.append(pk.Kunde("Morten","Skogmus",12345678,"Hakkebakkeskogen","0011"))

print(ansatte[0])
print(ansatte[1])
print(varer[0])
print(varer[1])
print(kunder[0])
print(kunder[1])

bestillinger = []
bestillinger.append(vk.Bestilling())
bestillinger[0].legg_til_kunde(kunder[0])
bestillinger[0].legg_til_vare(varer[0])
bestillinger[0].legg_til_vare(varer[0])
bestillinger[0].legg_til_vare(varer[0])
bestillinger[0].legg_til_vare(varer[0])

bestillinger.append(vk.Bestilling())
bestillinger[1].legg_til_kunde(kunder[1])
bestillinger[1].legg_til_vare(varer[1])
bestillinger[1].legg_til_vare(varer[1])

print(bestillinger[0])
print(bestillinger[1])