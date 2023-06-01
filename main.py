import pandas as pd
import matplotlib.pyplot as plt

seismes = pd.read_csv("seismes_2014.csv")


#Number of earthquake in 2014
print("There was " + str(len(seismes)) + " earthquakes in the World in 2014.")


#20 most eartquake-friendly countries
noms = seismes["pays"].value_counts().keys()[0:20]


# remove the countries which are not in the top 20 + countries with NaN values
to_remove = seismes["pays"].value_counts().keys()[20:]
for country in to_remove:
  seismes.drop(seismes[seismes["pays"] == country].index, inplace=True)
seismes.drop(seismes[pd.isna(seismes["pays"])].index, inplace=True)

seismes.reset_index(inplace=True)
seismes.drop("index", axis=1, inplace=True)


# plotting the boxplot
# seismes.boxplot(by = 'pays', column = ['mag'], grid = False, whis=10)
# plt.show()


# Searching the 6 countries with the highest magnitudes
print()
print("The countries with the highest magnitude are :")
search_max = seismes.copy()
for i in range(6):
  max = search_max.values[search_max["mag"].idxmax()]
  print(max[3] + " with a magnitude of : " + str(max[4]))
  search_max.drop(search_max[search_max["pays"] == max[3]].index, inplace=True)
  search_max.reset_index(inplace=True)
  search_max.drop("index", axis=1, inplace=True)


# found the number of earthquakes of magnitudes <= 2 in California and Alaska
test_countries = ['California', 'Alaska']

print()
for country in test_countries:
  print("There was " + str(len(seismes[seismes["pays"] == country][seismes[seismes["pays"] == country]["mag"] <= 2])) + " earthquakes of magnitudes <= 2 in " + country + " in 2014.")

