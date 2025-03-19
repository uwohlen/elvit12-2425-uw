sparebeløp = 10000
rente = 0.03
vekstfaktor = rente + 1

def f(x):
    return sparebeløp*vekstfaktor**x

print(f(5))
print()

år = 0
slutt = sparebeløp
sumrente = 0
print("År    På starten     Rente   Slutten av året")
#print(f"{år}    {sparebeløp}      {sparebeløp*rente:8.2f}   {sparebeløp + sparebeløp*rente:10.2f}")

#while år < 20:
while slutt < 2*sparebeløp:
    år = år + 1
    start = slutt
    rentekr = start*rente
    sumrente = sumrente + rentekr
    slutt = start + rentekr
    print(f"{år:3.0f}  {start:10.2f}  {rentekr:10.2f}  {slutt:10.2f}")

#print(f"{år:3.0f}  {start:10.2f}  {rentekr:10.2f}  {slutt:10.2f}")
print()
print(f"Summen av renta er {sumrente:10.2f}")
