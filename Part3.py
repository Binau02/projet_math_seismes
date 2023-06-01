import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

seismes = pd.read_csv("seismes_2014.csv")
seismes.drop(seismes[pd.isna(seismes["mag"])].index, inplace=True)
seismes.reset_index(inplace=True)
seismes.drop("index", axis=1, inplace=True)

F = seismes.copy()
F.drop(F[F["mag"] < 3].index, inplace=True)
F.reset_index(inplace=True)
F.drop("index", axis=1, inplace=True)
F['m'] = np.floor(F['mag'])

E = F["m"].value_counts()
# print(E[4])

F['size'] = 10+10*(F["m"]-3)
palette = ["hotpink", "green", "chocolate", "blue", "red", "black"]
fig1 = px.scatter_geo(F, lat="lat", lon="lon", hover_name="pays", hover_data=["mag", "profondeur"], color="m", color_continuous_scale=palette, size="size", size_max=30, opacity=0.5, title="Carte des séismes de magnitudes 3 à 8 en 2014")
fig1.update_layout(mapbox_style="kavrayskiy7")
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig1.append_trace

fig2 = px.pie(F, names='m')
fig2.update_layout(margin={"r":0,"t":500,"l":0,"b":0})
fig2.update_layout(width=10)
fig2.update_layout(height=10)

fig = go.Figure(data=fig1.data + fig2.data)
fig.show()

# print(px.data.tips())