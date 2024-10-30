import dyreklasser as dk

help(dk.Katt)

# legg merke til at jeg skriver liv=2, ikke bare 2, siden jeg hopper over hale
mine_dyr = [
  dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2), 
  dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1),
  dk.Hund("Kaisa","Labrador retriever","Svart")
]

print(mine_dyr[0].hale)
mine_dyr[0].antall_liv()


# dk.  gir meg valg mellom Dyr, Hund og Katt


for dyr in mine_dyr:
  dyr.dyr_info()
  dyr.aldring(3)
  dyr.snakk()
  print(type(dyr))

mine_dyr[2].aldring(5)

for i in range(6):
  mine_dyr[0].antall_liv()