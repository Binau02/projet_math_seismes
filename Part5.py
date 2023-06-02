import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# seismes = pd.read_csv("seismes_2014.csv")

# seismes.drop(seismes[pd.isna(seismes["pays"])].index, inplace=True)
# seismes.drop(seismes[pd.isna(seismes["mag"])].index, inplace=True)

# seismes.reset_index(inplace=True)
# seismes.drop("index", axis=1, inplace=True)


# worst_countries = []
# search_max = seismes.copy()
# while(len(search_max) > 0):
#   max = search_max.values[search_max["mag"].idxmax()]
#   print(max[3] + " with a magnitude of : " + str(max[4]))
#   worst_countries.append(max[3])
#   search_max.drop(search_max[search_max["pays"] == max[3]].index, inplace=True)
#   search_max.reset_index(inplace=True)
#   search_max.drop("index", axis=1, inplace=True)

# print(worst_countries)

seismes = pd.read_csv("2014-mag_sup_4.csv")

seismes.drop(seismes[seismes["place"].str.find("Chile") < 0].index, inplace=True)
# search_max = seismes.copy()
# print(seismes)

# max = search_max.values[search_max["impact.significance"].idxmax()]
# print(max)

# seismes.drop(seismes[pd.isna(seismes["pays"])].index, inplace=True)
# seismes.drop(seismes[pd.isna(seismes["mag"])].index, inplace=True)

# seismes.reset_index(inplace=True)
# seismes.drop("index", axis=1, inplace=True)

# worst_countries = []
# search_max = seismes.copy()
# # while(len(search_max) > 0):
# for i in range(20):
#   max = search_max.values[search_max["impact.significance"].idxmax()]
#   print(max[9] + " (" + str(max[7]) + " " + str(max[8]) + ") with an impact significance of : " + str(max[3]))
#   # worst_countries.append(max[3])
#   search_max.drop(search_max[search_max["impact.significance"] == max[3]].index, inplace=True)
#   search_max.reset_index(inplace=True)
#   search_max.drop("index", axis=1, inplace=True)

# , color="m", color_continuous_scale=palette

# seismes["power"] = 10**(1.5*seismes["mag"]+9.105)
seismes["power"] = 10**(seismes["mag"])

def get_month(time):
  return(time[5:7])

seismes["month"] = seismes["time"].apply(get_month)
# print(seismes)

# print(seismes["month"].value_counts())



fig = px.scatter_mapbox(seismes, lat="latitude", lon="longitude", hover_name="place", hover_data=["mag", "depth"], size="power", size_max=30, color="month", opacity=1, zoom=3, height=700, title="là où il faut pas aller en vacances")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()

def get_days(time):
  return int(time[8:10]) + 30*(int(time[5:7])-1)

seismes["days"] = seismes["time"].apply(get_days)
# print(seismes["days"].to_numpy())

plt.plot(seismes["days"].to_numpy(), seismes["mag"].to_numpy())
# plt.plot(seismes["days"].to_numpy(), seismes["power"].to_numpy())
plt.show()