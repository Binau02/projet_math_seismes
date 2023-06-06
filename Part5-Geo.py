import pandas as pd
import matplotlib.pyplot as plt

seismes = pd.read_csv("chili.csv")

print("There was " + str(len(seismes)) + " earthquakes in Chile with a magnitude arround to 6.")

#On enlève les séismes qui n'ont pas de localisation précises
seismes.drop(seismes[seismes['Location Name'] == "CHILE"].index, inplace=True)
seismes.reset_index(inplace=True)
seismes.drop("index", axis=1, inplace=True)

#On regarde les régions les plus touchées
print(seismes['Location Name'].value_counts())

#
counts = seismes["Location Name"].value_counts().sort_index()
plt.figure("number of earthquakes by region")
plt.bar(counts.index.to_numpy(), counts.values)

plt.show()