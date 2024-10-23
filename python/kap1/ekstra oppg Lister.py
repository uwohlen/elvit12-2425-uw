femten_tall = [
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15]
]

print("Partall:",end=" ")

for i in range(len(femten_tall)):
  for j in range(len(femten_tall[i])):
    if femten_tall[i][j] % 2 == 0:
      print(femten_tall[i][j], end = " ")

print()
print("Oddetall:",end=" ")

for i in range(len(femten_tall)):
  for j in range(len(femten_tall[i])):
    if femten_tall[i][j] % 2 != 0:
      print(femten_tall[i][j], end = " ")

print()
print("Tregangen:",end=" ")

for i in range(len(femten_tall)):
  for j in range(len(femten_tall[i])):
    if femten_tall[i][j] % 3 == 0:
      print(femten_tall[i][j], end = " ")

print()
print("Partall:",end=" ")

for i in range(len(femten_tall)):
  for j in range(len(femten_tall[i])):
    if (i+j) % 2 != 0:
      print(femten_tall[i][j], end = " ")

print()
print("Oddetall:",end=" ")

for i in range(len(femten_tall)):
  for j in range(len(femten_tall[i])):
    if (i+j) % 2 == 0:
      print(femten_tall[i][j], end = " ")

print()
