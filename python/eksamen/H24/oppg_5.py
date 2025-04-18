"""
Oppgave 5
b) Ta utgangspunkt i algoritmen fra punkt a). Utvid og implementer algoritmen til et program som teller opp og viser hvor mange tresifrede tall som oppfyller IF-betingelsen fra algoritmen.

READ h
SET t TO h
SET s TO 0
SET r TO 0
WHILE h NOT EQUAL TO 0
  SET r TO h % 10
  SET s TO s * 10 + r
  SET h TO h // 10
ENDWHILE
IF t EQUAL TO s
  DISPLAY True
ELSE 
  DISPLAY False
ENDIF
"""

# Tresifrede tall er fra 100 til 999
# Skal kjøre koden om igjen, lager en løkke
# Endrer DISPLAY til å være opptelling

"""
treff = 0

for h in range(100,1000):
  t=h
  s=0
  r=0
  while h != 0:
    r = h%10
    s = s*10 + r
    h = h//10
  if t == s:
    treff += 1

print("Antall tresifrede palindromtall: ",treff)
"""

# Fra aunivers.no:

def palindrom(h):
  t = h
  s = 0
  r = 0
  while h != 0:
    r = h%10
    s = s * 10 + r
    h = h//10
  if t == s:
    return(True)
  else:
    return(False)

# Hovedprogram
antall = 0
for i in range(100,1000):
  if palindrom(i):
    antall+=1

print(f"Det er {antall} palindromtall mellom 100 og 999.")