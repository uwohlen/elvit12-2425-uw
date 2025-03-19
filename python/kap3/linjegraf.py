import matplotlib.pyplot as plt

# Skriv
# pip install matplotlib 
# i terminalen hvis du ikke har matplotlib allerede

import random as rd

x=[]
y=[]
for i in range(10):
  x.append(i)
  y.append(rd.randint(0,40))

print(x)
print(y)

plt.plot(x,y)
plt.scatter(x,y)
plt.show()



