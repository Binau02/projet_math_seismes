import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr
from mpl_toolkits.basemap import Basemap



# getting the month number from the date format YYYY-MM-DDTHH:MM:SS.XXXZ
def get_month(time):
  return(time[5:7])

# getting the number of days since the beginning of the year (± 1 day) from the date format YYYY-MM-DDTHH:MM:SS.XXXZ
def get_days(time):
  return int(time[8:10]) + 30*(int(time[5:7])-1)

# getting the percentage of seismes in Chile ≥ mag
def get_percentage(seismes, seismes_out_chile, magnitude=False):
  if magnitude == False:
    return len(seismes)*100/len(seismes_out_chile)
  return len(seismes[seismes["mag"] >= magnitude])*100/len(seismes_out_chile[seismes_out_chile["mag"] >= magnitude])

# getting a lot of data about earthquakes in Chile, from inicio to fin
def chile_vacaciones(inicio, fin):
  # reading the csv(s) + dropping NaN mag and place values
  seismes = []
  seismes_out_chile = []
  for i in range(inicio, fin+1):
    temp = pd.read_csv(str(i) + "-mag_sup_4.csv")
    temp.drop(temp[pd.isna(temp["mag"])].index, inplace=True)
    temp.reset_index(inplace=True)
    temp.drop("index", axis=1, inplace=True)
    temp.drop(temp[pd.isna(temp["place"])].index, inplace=True)
    temp.reset_index(inplace=True)
    temp.drop("index", axis=1, inplace=True)
    seismes.append(temp)
    seismes_out_chile.append(temp.copy())
    # keeping only Chile earthquakes and adding columns
    seismes[i-inicio].drop(seismes[i-inicio][seismes[i-inicio]["place"].str.find("Chile") < 0].index, inplace=True)
    seismes[i-inicio].reset_index(inplace=True)
    seismes[i-inicio].drop("index", axis=1, inplace=True)
    seismes[i-inicio]["power"] = 10**(seismes[i-inicio]["mag"])
    seismes[i-inicio]["month"] = seismes[i-inicio]["time"].apply(get_month)
    seismes[i-inicio]["days"] = seismes[i-inicio]["time"].apply(get_days)
  seismes_total = pd.concat(seismes)
  seismes_out_chile_total = pd.concat(seismes_out_chile)

  # calculating pearson coeficient between the magnitude and the day of the year (0-365)
  corr, _ = pearsonr(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())
  print("Pearson coeficient : " + str(corr))

  # plotting map of mag [4, 8.9], by power
  fig = px.scatter_mapbox(seismes_total, lat="latitude", lon="longitude", hover_name="place", hover_data=["mag", "depth"], size="power", size_max=30, color="month", opacity=1, zoom=3, height=700, title="là où il faut pas aller en vacances")
  fig.update_layout(mapbox_style="open-street-map")
  fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
  fig.show()
  # plotting, for each year and for all years together, the magnitude according to the day of the year (0-365)
  fig_plt, axs = plt.subplots(2, fin-inicio+2)
  for i in range(fin-inicio+1):
    axs[0, i].plot(seismes[i]["days"].to_numpy(), seismes[i]["mag"].to_numpy())
    axs[0, i].set_title("Magnitude of earthquakes in 2014 in Chile")
    axs[1, i].plot(seismes[i]["days"].to_numpy(), seismes[i]["power"].to_numpy())
    axs[1, i].set_title("Power of earthquakes in 2014 in Chile")
  axs[0, fin-inicio+1].plot(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())
  axs[0, fin-inicio+1].set_title("Magnitude of earthquakes from " + str(inicio) + " to " + str(fin) + " in Chile")
  axs[1, fin-inicio+1].plot(seismes_total["days"].to_numpy(), seismes_total["power"].to_numpy())
  axs[1, fin-inicio+1].set_title("Power of earthquakes from " + str(inicio) + " to " + str(fin) + " in Chile")
  # scatter plotting for all years together the magnitude according to the day of the year (0-365)
  plt.figure("magnitude by date")
  plt.scatter(seismes_total["days"].to_numpy(), seismes_total["mag"].to_numpy())

  # getting the percentage of earthquakes in Chile (from inicio to fin) for each magnitude
  for i in range(4, 9):
    print(str(get_percentage(seismes_total, seismes_out_chile_total, i)) + " % of the earthquakes of magnitude >= " + str(i) + " are situated in Chile. (sample of " + str(len(seismes_out_chile_total)) + " values and " + str(len(seismes_out_chile_total[seismes_out_chile_total["mag"] >= i])) + " elements on the category).")

  # plotting the number of seismes by month
  counts = seismes_total["month"].value_counts().sort_index()
  plt.figure("number of earthquakes by month")
  plt.bar(counts.index.to_numpy(), counts.values)

  # calculating pearson coeficient between the number of seismes and the month of the year (0-365)
  corr, _ = pearsonr(counts.index.to_numpy().astype(int), counts.values)
  print("Pearson coeficient : " + str(corr))

  plt.show()


chile_vacaciones(2014, 2022)
