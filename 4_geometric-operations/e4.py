import os

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, box
from pyproj import CRS

import matplotlib.pyplot as plt
from shapely import speedups
from geopandas.tools import geocode

# File inputs
fp_pop = ['data', 'Zurich', 'population.shp']
input_file_pop = os.path.join(*fp_pop)

fp_borders = ['data', 'Zurich', 'border.geojson']
input_file_borders = os.path.join(*fp_borders)

pop = gpd.read_file(input_file_pop)
borders = gpd.read_file(input_file_borders, driver='geojson')

# CRS check
epsg2056wkt = CRS.from_epsg(2056).to_wkt()
pop.crs = epsg2056wkt
borders2056 = borders.to_crs(pop.crs)
print('Pop CRS: {}\n'.format(pop.crs))
print('Borders2056 CRS: {}\n'.format(borders2056.crs))

# crop pop grid to within borders
pop_cropped = gpd.overlay(pop, borders, how="intersection")

# geocode stations
# Geocode addresses using Nominatim. Remember to provide a custom "application name" in the user_agent parameter!
train_stations = [
   "Bahnhof Wiedikon",
   "Bahnhof Wipkingen",
   "Bahnhof Wollishofen",
   "Bahnhof Altstetten",
   "Bahnhof Enge",
   "Bahnhof Zürich Flughafen",
   "Bahnhof Oerlikon",
   "Bahnhof Stadelhofen",
   "Bahnhof Affoltern",
   "Bahnhof Tiefenbrunnen",
   "Bahnhof Zürich HB"
]
geo_trains = geocode(train_stations, provider='nominatim', user_agent='gis-training-kevin', timeout=30)
geo_trains = geo_trains.to_crs(pop.crs)

# stations within borders
geo_trains_mask = geo_trains.within(borders)
geo_trains_within = geo_trains[geo_trains_mask]

# plot
# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(10,10))
borders2056.plot()
# pop_cropped.plot(column='pop_total', scheme='Natural_Breaks')
# geo_trains_within.plot(color="green", markersize=10)

plt.show()