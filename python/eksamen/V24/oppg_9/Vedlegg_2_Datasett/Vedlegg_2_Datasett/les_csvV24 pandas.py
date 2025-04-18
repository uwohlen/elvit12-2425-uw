import pandas as pd
filnavn = "05994_20240126-145813-csv.csv"

df = pd.read_csv(filnavn,encoding="ansi",delimiter=";",skiprows=2)

print(df.columns)