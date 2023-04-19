lons = df["lon"]
lats = df["lat"]

L = [{"id":idd, 
      "longitude":lon, 
      "latitude":lat} for idd,lon,lat in zip(np.arange(len(lons)), lons, lats)]

# Considering lon / lat coordinates in epsg 4326
locations = pd.DataFrame(L)        
locations_gpd = gpd.GeoDataFrame(locations, 
                    geometry=gpd.points_from_xy(locations.longitude,locations.latitude),
                    crs = "epsg:4326")
                    
locations_gpd_1 = locations_gpd.to_crs("EPSG:3035")
# Add buffer in meter
locations_gpd_1.geometry = locations_gpd_1.geometry.buffer(300,6)
locations_gpd_2 = locations_gpd_1.to_crs("EPSG:4326")
