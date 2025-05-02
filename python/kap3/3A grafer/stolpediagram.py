import matplotlib.pyplot as plt
import random as rd

liste = []
for i in range(50):
  if rd.randint(0,1) == 0:
    liste.append("M")
  else:
    liste.append("K")

print(liste)

kategorier = ["M","K"]

antall = [liste.count("M"),liste.count("K")]

print(antall)

plt.bar(kategorier, antall)
plt.show()