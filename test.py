import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr
from mpl_toolkits.basemap import Basemap

bm = Basemap(projection="merc",
                 resolution='i',
                 llcrnrlon=-180.0,
                 llcrnrlat=-85.0,
                 urcrnrlon=180.0,
                 urcrnrlat=85.0)

lon, lat = 48.866667, 2.333333 # test coords
x, y = bm(lon, lat)
value = bm.is_land(x, y)


print(value) 