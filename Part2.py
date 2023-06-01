import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

seismes = pd.read_csv("seismes_2014.csv")

F = seismes.copy()
F.drop(F[F["mag"] < 3].index, inplace=True)
F.reset_index(inplace=True)
F.drop("index", axis=1, inplace=True)
F['m'] = np.floor(F['mag'])
print(F)