tall = [5,8,2,2,6]

for i in range(len(tall)-1,-1,-1):
  if tall[i] == 2:
    tall.pop(i)
  else:
    print(tall[i])
print(tall)