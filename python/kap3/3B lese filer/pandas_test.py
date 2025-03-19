import pandas as pd

data = [
  [420, 234, 390],
  [50, 40, 45]
  ]

overskrifter = ["a","b","c"]
kategorier = ["Per","Pål"]

#load data into a DataFrame object:
df = pd.DataFrame(data,index=kategorier,columns=overskrifter)

print(df) 
