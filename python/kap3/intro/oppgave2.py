import matplotlib.pyplot as plt
import random as rd
import math
import statistics as stat

tall = []
kategorier = ["<<-,g-2s>","[g-2s,g-s>","[g-s,g>","[g,g+s>","[g+s,g+2s>","[g+2s,->>"]
antall = [0,0,0,0,0,0]

listelengde = 10000
for i in range(listelengde):
  #tall.append(rd.randint(1,100))
  tall.append(rd.normalvariate())

#print(tall)
snitt = sum(tall)/listelengde
print(snitt)
print(stat.mean(tall))

sum_kvadrat_avvik = 0
for i in range(listelengde):
  kvadrat_avvik = (snitt - tall[i])**2
  sum_kvadrat_avvik += kvadrat_avvik

std = math.sqrt(sum_kvadrat_avvik / listelengde)
print(std)
print(stat.pstdev(tall))

for i in range(listelengde):
  if tall[i] < snitt - 2*std:
    antall[0] += 1
  elif tall[i] < snitt - std:
    antall[1] += 1
  elif tall[i] < snitt:
    antall[2] += 1
  elif tall[i] < snitt + std:
    antall[3] += 1
  elif tall[i] < snitt + 2*std:
    antall[4] += 1
  else:
    antall[5] += 1

print(antall)

plt.bar(kategorier,antall)
plt.show()