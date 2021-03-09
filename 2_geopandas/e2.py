# Import CRS class from pyproj
from pyproj import CRS
import geopandas as gpd
import os

# Import necessary geometric objects from shapely module
from shapely.geometry import Point, LineString, Polygon

# import matplotlib
import matplotlib.pyplot as plt

# Read in data
path_stations = ["C:\\", "Users", "ngaik", "Documents" , "gis-training", "data", "London", "metro_stations.csv"]
fp_stations = os.path.join(*path_stations)
print('File path stations: ', fp_stations)

# path_routes = ['.', 'data', 'London', 'metro_routes.csv']
# fp_routes = os.path.join(*path_routes)
# print('File path routes: ', fp_routes)

segments = gpd.read_file(fp_stations)
segments.set_crs(epsg=4326)

stations1 = segments[['station1', 'station1_lon', 'station1_lat', 'geometry']]
stations2 = segments[['station2', 'station2_lon', 'station2_lat', 'geometry']]

colname1 = {
    'station1': 'station',
    'station1_lon': 'lon',
    'station1_lat': 'lat'
}
colname2 = {
    'station2': 'station',
    'station2_lon': 'lon',
    'station2_lat': 'lat'
}

stations1 = stations1.rename(columns=colname1)
stations2 = stations2.rename(columns=colname2)

stations = stations1.append(stations2)
stations = stations.drop_duplicates()

geom = []
for index, row in stations.iterrows():
    geom.append(Point(float(row.lon), float(row.lat)))
stations['geometry'] = geom

# stations["geometry"] = stations[["lon", "lat"]].apply(lambda x: Point(float(x)), axis=1)


print(stations.head())

stations.plot(figsize=(10,10))
plt.show()