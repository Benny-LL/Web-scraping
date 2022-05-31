import pandas as pd
import numpy as np

df = pd.read_csv('./cnp 3-yrs_web-scrap.csv')
df = df.drop("Unnamed: 0", axis=1)
df = df.dropna(axis=0)

df["P-ASP Date"] = pd.to_datetime(df["P-ASP Date"],format='%d/%m/%y')
print(df)