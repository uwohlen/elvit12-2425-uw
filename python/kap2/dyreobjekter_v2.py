import dyreklasser as dk

mine_dyr = {
  "Silkesvarten": dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2),
  "Mini": dk.Katt("Mini","Katt med ukjent far","Svart"), 
  "Tigergutt": dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1),
  "Kaisa": dk.Hund("Kaisa","Labrador retriever","Svart"),
  "Rita": dk.Hund("Rita","Schäferhund","Svart og brun"),
  "Heidi": dk.Hund("Heidi","Norsk buhund","Svart og hvit")
}

print(mine_dyr["Silkesvarten"].hale)   # Halen får standardverdien
mine_dyr["Silkesvarten"].antall_liv()  # Antall liv har verdi liv=2, og får +1 fra metoden

for dyr in mine_dyr.values():
  dyr.dyr_info()
  dyr.aldring(3)
  dyr.snakk()
  print(type(dyr))        # dyreklasser.Katt viser at klassen er definert i filen dyreklasser.py

mine_dyr["Kaisa"].aldring(5)


for i in range(6):
  mine_dyr["Silkesvarten"].antall_liv()

print("*******************************")
print()
mine_dyr["Silkesvarten"].avkom("Mini")
print()
mine_dyr["Silkesvarten"].avkom("Midi")
print()
mine_dyr["Silkesvarten"].avkom("Maxi")
print()
print(mine_dyr["Silkesvarten"].barn)

mine_dyr["Mini"].sett_mor(mine_dyr["Silkesvarten"])

print(mine_dyr["Mini"].mor.navn)
print(mine_dyr["Mini"].mor.liv)