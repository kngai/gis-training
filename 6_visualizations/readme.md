# Exercise 6

**Credit**  
Big thanks to Patrick Curran for the idea, and the data.

You will find the data in `MSC_ModelData_vectorized` folder. It consists of:
* `humidex_05.geojson` - Gridded Humidex Values
* `wind_speed_05.geojson` - Gridded Wind Speed (ht = 10 m) Values
* `WxO_Demo_Smaller_Extent.geojson` - Clip Box
* `land_PubStdZone_coarse_unproj.shp` - MSC Standard Forecast Zones


**Preparing data**:
* Load the following files into memory, and store them in GeoDataFrames. Use the provided names for your data structure:
    * `humidex_05.geojson` -> `humidex`
    * `wind_speed_05.geojson` -> `wind`
    * `WxO_Demo_Smaller_Extent.geojson` -> `clip_box`
    * `land_PubStdZone_coarse_unproj.shp` -> `forecast_zones`
* Clip the `humidex`, `wind` and `forecast_zones` to the boundaries of `clip_box`

## Problem 1: Create heatmap for humidex and wind speed

The goal of this problem is to create heatmap for humidex and wind speed with bokeh.

**Steps**
* Classify `humidex` values using a map classifier. Add a `class` column to both dataframes.
    Experiment with different classifiers. Try finding one that best highlights the differences in data.
* For each `class` in `humidex` create a geometry that covers all gridpoints with the same `class` values.
* Create a `humidex_classified` dataframe with the following values:
    * class
    * geometry
    * min_humidex_value
    * max_humidex_value
    The `humidex_classified` should have as many rows, as classes you defined.
* Plot `humidex_classified` using bokeh
* Repeat all steps for `wind` data.


## Problem 2: Report precise values for meteorological stations

Thus far, we aggregated data into buckets. That's handy when trying to distinguish zones with higher, and lower values.
However, sometimes you will be interested in knowing a precise value at certain location. Let's now add the humidex and windspeed values for meteorological stations.

**Steps**
* Find list of meteorological stations in the area
    *Hint*
    If you cannot easily find addresses of meteorological stations, use list of cities instead.
* Geocode them. Store the results in `stations` dataframe.
* Remove any `stations` outside of the `clip_box`
* For each station, find humidex and wind speed values. Store the values in `stations` dataframe.
* Add stations to the map from Problem 1.
* Use `HoverTool` to the precise humidex and windspeed at the location.


## Problem 3: Analyze weather zones

Now, let's try to find weather forecast zones that had expected the most extreme humidex and windspeed values.

**Steps**
* Find the class number for the highest `humidex`. Store its geometry as `highest_humidex_zone`
* For each `forecast_zone` find the area that overlaps with `highest_humidex_zone`.
Store this new geometry in `geom_humidex_high` column.
* Calculate the area of forecast zone, and `geom_humidex_high`. Divide `geom_humidex_high` area by forecast zone area.
  Store the results in `ratio` column.
* Visualize your results (`ratio` per `forecast_zone`) using bokeh.
* Calculate `min`, `max` and `median` humidex value in each forecast zone.
* Add this information to the map. Use `HoverTool`.
