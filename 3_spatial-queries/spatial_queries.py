# Import necessary modules
import os

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, box
from pyproj import CRS

import matplotlib.pyplot as plt
from shapely import speedups

# File inputs
fp = ['data', 'ufo', 'ufo-scrubbed-geocoded-time-standardized.csv']
input_file = os.path.join(*fp)

fp2 = ['data', 'ufo', 'cb_2016_us_county_5m.shp']
input_file2 = os.path.join(*fp2)

events = gpd.read_file(input_file)
# print(events.head())

# add geometry to events
points = []
for index, row in events.iterrows():
    points.append(Point(float(row['lat']), float(row['lng'])))
events['geometry'] = points

# CRS
events.crs = CRS.from_epsg(4269).to_wkt()
print(events.head())
# print('Events: {}'.format(events.crs))

counties = gpd.read_file(input_file2)
print(counties.head())
# print('Counties: {}'.format(counties.crs))
events.to_crs(counties.crs)
print('Match CRS? {}\n\n'.format(counties.crs == events.crs))

# Join events with counties
# sightings_per_county = counties.join(events, lsuffix='NAME', rsuffix='geometrycity')

# print(p.head())

# Mask method attempt
# events_mask = events.within(counties)
# print('Any events within counties?\n')
# for index, value in events_mask.iteritems():
#     if (!value):
#         print(index, value)
# print(events_mask)
# counties_mask = counties[events_mask]

# Spatial join
# sightings_per_county = gpd.sjoin(counties, events, how='inner', op='contains')
# county_counts = sightings_per_county.groupby([
#     "GEOID",
# ]).agg(dict(observed="count")).reset_index()

# Spatial join 2
sightings_per_county = gpd.sjoin(events, counties, how='inner', op='within')

print('type: {}\n'.format(type(sightings_per_county)))
print(sightings_per_county.head())

# Plot
# continental_us = box(-124.848974, 24.396308, 66.885444, 49.384358)
# clipped_gdf = sightings_per_county[
#     sightings_per_county.geometry.intersects(continental_us)
# ]

sightings_per_county.plot(figsize=(10, 10))
plt.show()