import pandas as pd
import matplotlib.pyplot as plt

filnavn = "Datasett_fodselstall.csv"

df = pd.read_csv(filnavn,encoding="ansi",delimiter="\t")

print(df)