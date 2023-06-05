import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr
# import numpy as np
# from scipy import stats
# from mpl_toolkits.basemap import Basemap
# from mpl_toolkits.basemap import cm


def get_month(time):
  return(time[5:7])


def get_days(time):
  return int(time[8:10]) + 30*(int(time[5:7])-1)


def chile_vacaciones(inicio, fin):
  seismes = []
  for i in range(inicio, fin+1):
    seismes.append(pd.read_csv(str(i) + "-mag_sup_4.csv"))
    seismes[i-inicio].drop(seismes[i-inicio][seismes[i-inicio]["place"].str.find("Chile") < 0].index, inplace=True)
    seismes[i-inicio]["power"] = 10**(seismes[i-inicio]["mag"])
    seismes[i-inicio]["month"] = seismes[i-inicio]["time"].apply(get_month)
    seismes[i-inicio]["days"] = seismes[i-inicio]["time"].apply(get_days)
  seismes_total = pd.concat(seismes)

  corr, _ = pearsonr(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())

  print(corr)

  fig = px.scatter_mapbox(seismes_total, lat="latitude", lon="longitude", hover_name="place", hover_data=["mag", "depth"], size="power", size_max=30, color="month", opacity=1, zoom=3, height=700, title="là où il faut pas aller en vacances")
  fig.update_layout(mapbox_style="open-street-map")
  fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
  fig.show()
  fig, axs = plt.subplots(2, fin-inicio+2)
  for i in range(fin-inicio+1):
    axs[0, i].plot(seismes[i]["days"].to_numpy(), seismes[i]["mag"].to_numpy())
    axs[0, i].set_title("Magnitude of earthquakes in 2014 in Chile")
    axs[1, i].plot(seismes[i]["days"].to_numpy(), seismes[i]["power"].to_numpy())
    axs[1, i].set_title("Power of earthquakes in 2014 in Chile")
  axs[0, fin-inicio+1].plot(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())
  axs[0, fin-inicio+1].set_title("Magnitude of earthquakes from " + str(i+inicio) + " to " + str(i+fin) + " in Chile")
  axs[1, fin-inicio+1].plot(seismes_total["days"].to_numpy(), seismes_total["power"].to_numpy())
  axs[1, fin-inicio+1].set_title("Power of earthquakes from " + str(i+inicio) + " to " + str(i+fin) + " in Chile")
  plt.figure("magnitude by date")
  plt.scatter(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())
  plt.show()


chile_vacaciones(2014, 2022)

# seismes = pd.read_csv("2014-mag_sup_4.csv")
# seismes.drop(seismes[seismes["place"].str.find("Chile") < 0].index, inplace=True)
# seismes["power"] = 10**(seismes["mag"])
# seismes["month"] = seismes["time"].apply(get_month)
# seismes["days"] = seismes["time"].apply(get_days)

