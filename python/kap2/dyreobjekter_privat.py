import dyreklasser_privat as dk

dk.Dyr._dyr_nr = 25      # Bør beskyttes mot endringer!

# Hunder og valper
mine_dyr = {
  "Heidi": dk.Hund("Heidi","Norsk buhund","Svart og hvit"),
}

nabo_dyr = {
  "Festus": dk.Hund("Festus","Norsk elghund","Grå-brun")
}

# Heidis valper
valper = ["Sniff","Prikken","Junior","Brumlemann","Trulte","Knoll","Tott"]

for valp in valper:
  mine_dyr["Heidi"].avkom(valp)
  nabo_dyr["Festus"].avkom(valp)
  mine_dyr[valp] = mine_dyr["Heidi"] + nabo_dyr["Festus"]
  mine_dyr[valp].navn = valp
  mine_dyr[valp].sett_mor(mine_dyr["Heidi"])
  mine_dyr[valp].sett_far(nabo_dyr["Festus"])

# Ny hund
mine_dyr["Rita"] = dk.Hund("Rita","Schäferhund","Svart og brun")

# Kattene
mine_dyr["Silkesvarten"] = dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2)
mine_dyr["Tigergutt"] = dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1)
mine_dyr["Lillesvarten"] = dk.Katt("Lillesvarten","Katt med ukjent far","Svart")

mine_dyr["Silkesvarten"].avkom("Lillesvarten")
mine_dyr["Lillesvarten"].sett_mor(mine_dyr["Silkesvarten"])

# Ny hund
mine_dyr["Kaisa"] = dk.Hund("Kaisa","Labrador retriever","Svart")


# Problematisk:

mine_dyr["Kaisa"]._dyr_nr = 7  # Skulle vært unik, bør beskyttes fra endringer!


for dyr in mine_dyr.values():
  print(dyr)

for dyr in nabo_dyr.values():
  print(dyr)
