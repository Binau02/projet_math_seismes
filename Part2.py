import pandas as pd
import matplotlib.pyplot as plt

seismes = pd.read_csv("seismes_2014.csv")

F = seismes.copy()
for i in range(len(seismes)):
    if seismes.values[i]["mag"] > 3:
        F.drop(F[F["mag"] < 3].index, inplace=True)
        F.reset_index(inplace=True)
        F.drop("index", axis=1, inplace=True)