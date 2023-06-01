import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


seismes = pd.read_csv("seismes_2014.csv")
seismes.drop(seismes[pd.isna(seismes["mag"])].index, inplace=True)
seismes.reset_index(inplace=True)
seismes.drop("index", axis=1, inplace=True)

F = seismes.copy()
F.drop(F[F["mag"] < 3].index, inplace=True)
F.reset_index(inplace=True)
F.drop("index", axis=1, inplace=True)
F['m'] = np.floor(F['mag'])


fig = px.scatter_mapbox(F[F["mag"] < 5], lat="lat", lon="lon", hover_name="pays", hover_data=["mag", "profondeur"], color_continuous_scale=["red"], zoom=3, height=700, title="Carte des séismes de magnitude 3 et 4 en 2014")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()

fig = px.density_mapbox(F[F["mag"] < 5], lat="lat", lon="lon", hover_name="pays", hover_data=["mag", "profondeur"], zoom=3, height=700, radius=15, title="Carte de chaleur des séismes de magnitude 3 et 4 en 2014")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()

F['size'] = 10+10*(F["m"]-3)
palette = ["hotpink", "green", "chocolate", "blue", "red", "black"]
fig = px.scatter_mapbox(F, lat="lat", lon="lon", hover_name="pays", hover_data=["mag", "profondeur"], color="m", color_continuous_scale=palette, size="size", size_max=30, opacity=0.5, zoom=3, height=700, title="Carte des séismes de magnitudes 3 à 8 en 2014")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()

F['size'] = 10+10*(F["m"]-5)
palette = ["chocolate", "blue", "red", "black"]
fig = px.scatter_mapbox(F[F["mag"] >= 5], lat="lat", lon="lon", hover_name="pays", hover_data=["mag", "profondeur"], color="m", color_continuous_scale=palette, size="size", size_max=30, opacity=0.5, zoom=3, height=700, title="Carte des séismes de magnitudes 5 à 8 en 2014")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()

