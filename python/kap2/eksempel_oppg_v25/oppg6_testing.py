import oppg6_klasser as bk

print("Oppgave 6c - klassen og metodene virker")
b0 = bk.Batteri(1,10,100)
print("Skal vise energinivå 10")
print(b0.vis_niva())

b0.lad_batteri(30)
print("Skal vise energinivå 10+30=40")
print(b0.vis_niva())

b0.bruk_energi(5)
print("Skal vise energinivå 40-5=35")
print(b0.vis_niva())

print()

print("Oppgave 6d og 6e - feil og unntak")

b1 = bk.Batteri(1,10,100)
print("1.1 Skal vise energinivå 10 og en melding om å ikke bruke mer enn nåværende energinivå")
b1.bruk_energi(20)
print(b1.vis_niva())

b2 = bk.Batteri(2,60,100)
print("2.1 Skal vise energinivå 10 og en melding om å ikke lade mer enn kapasiteten")
b2.lad_batteri(50)
print(b2.vis_niva())

b3_1 = bk.Batteri(31,10,100)
print("3.1 Skal vise energinivå 10 og en melding om å angi energi som heltall")
b3_1.lad_batteri(5.4)
print(b3_1.vis_niva())

b3_2 = bk.Batteri(32,10,100)
print("3.2 Skal vise energinivå 10 og en melding om å angi energi som heltall")
b3_2.lad_batteri("A")
print(b3_2.vis_niva())

b3_3 = bk.Batteri(33,10,100)
print("3.3 Skal vise energinivå 10 og en melding om å angi energi som et positivt tall")
b3_3.lad_batteri(-10)
print(b3_3.vis_niva())

b3_4 = bk.Batteri(31,10,100)
print("3.4 Skal vise energinivå 10 og en melding om å angi energi som heltall")
b3_4.bruk_energi(5.4)
print(b3_4.vis_niva())

b3_5 = bk.Batteri(32,10,100)
print("3.5 Skal vise energinivå 10 og en melding om å angi energi som heltall")
b3_5.bruk_energi("A")
print(b3_5.vis_niva())

b3_6 = bk.Batteri(33,10,100)
print("3.6 Skal vise energinivå 10 og en melding om å angi energi som et positivt tall")
b3_6.bruk_energi(-10)
print(b3_6.vis_niva())

