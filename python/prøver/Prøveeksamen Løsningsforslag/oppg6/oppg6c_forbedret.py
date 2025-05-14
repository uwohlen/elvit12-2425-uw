#import oppg6b as pk
import oppg6d_forbedret as pk

# Lager objekt for registrering av nedbør
nedbor = pk.Registrering()

print("Test punkt 1: vanlige verdier virker")

test_data1 = [2.4,0,250]

for i in range(len(test_data1)):
  sjekk = nedbor.legg_til_en(test_data1[i])
  print(test_data1[i],sjekk)


for verdi in nedbor.get_liste():
  print("Dag:",verdi.get_ukedag(),"\tNedbør",verdi.get_mm(),"mm")

try:
  q = nedbor.total()
  print("Bestått: Total nedbør er",q,"mm")
except:
  print("Feilet")

print()
print("Test punkt 2: Negative verdier skal ikke lagres")
test_data2 = -0.1
sjekk = nedbor.legg_til_en(test_data2)
print(test_data2,sjekk)
print("Dag:",nedbor.get_liste()[-1].get_ukedag(),"\tNedbør:",nedbor.get_liste()[-1].get_mm(),"mm")

print()
print("Test punkt 3: For store verdier skal ikke lagres")
test_data3 = 250.1
sjekk = nedbor.legg_til_en(test_data3)
print(test_data3,sjekk)
print("Dag:",nedbor.get_liste()[-1].get_ukedag(),"\tNedbør:",nedbor.get_liste()[-1].get_mm(),"mm")

print()
print("Test punkt 4: Kun data på format av typen int eller float lagres")
print('4.1 String som er tall: "2.4"')
test_data4_1 = "2.4"
sjekk = nedbor.legg_til_en(test_data4_1)
print(test_data4_1,sjekk)
try:
  pluss1 = nedbor.get_liste()[-1].get_mm() + 1
  print("Kunne regne",test_data4_1," +1 = ",pluss1)
except:
  print("Kunne ikke regne",test_data4_1," +1")
print("Dag:",nedbor.get_liste()[-1].get_ukedag(),"\tNedbør:",nedbor.get_liste()[-1].get_mm(),"mm")

print('4.2 String som ikke er tall: "2.4.0"')
test_data4_2 = "2.4.0"
sjekk = nedbor.legg_til_en(test_data4_2)
print(test_data4_2,sjekk)
print("Dag:",nedbor.get_liste()[-1].get_ukedag(),"\tNedbør:",nedbor.get_liste()[-1].get_mm(),"mm")

print('4.3 Boolean: False')
test_data4_3 = False
sjekk = nedbor.legg_til_en(test_data4_3)
print(test_data4_3,sjekk)
print("Dag:",nedbor.get_liste()[-1].get_ukedag(),"\tNedbør:",nedbor.get_liste()[-1].get_mm(),"mm")
