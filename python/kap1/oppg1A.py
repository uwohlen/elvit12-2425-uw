# Blandede oppgaver
# Oppgave 1

# 50 km/h, lengde 100 m, radius 31,83 m
# a) banens lengde
# b) gjennomsnittsfart i m/s
# c) tid på 10 runder

import math

fart_km_h = 50
lengde = 100
radius = 31.83

omkrets = 2*math.pi*radius
bane_lengde = omkrets + 2*lengde
print(f"a) Banelengden er {bane_lengde:.0f} meter.")

fart_m_s = fart_km_h / 3.6

print(f"b) Farten er {fart_m_s:.1f} m/s")

tid_s = bane_lengde * 10 / fart_m_s

tid_m = tid_s // 60
tid_m_s = tid_s % 60

print(f"c) Tiden på 10 runder er {tid_m:.0f}:{tid_m_s:.0f} (minutter og sekunder)")

# a) Banelengden er 400 meter.
# b) Farten er 13.9 m/s
# c) Tiden på 10 runder er 4:48 (minutter og sekunder)