import xarray as xr
import numpy as np

#################

lons = np.arange(-179.5,180,0.5)
lats = np.arange(-89.5,90,0.5)
data = np.zeros((lats.shape[0], lons.shape[0]))

xarlon = xr.IndexVariable("longitude", lons, 
        attrs={"unit":"degrees_east",
               "standard_name": "longitude", 
               "long_name" : "longitude", 
               "axis":"X"})
xarlat = xr.IndexVariable("latitude", lats, 
        attrs={"unit":"degrees_north",
               "standard_name": "latitude", 
               "long_name" : "latitude", 
               "axis":"Y"})
    
#################
           
dims = ['latitude',"longitude"]
coords = {'latitude':xarlat,"longitude":xarlon}

D_export = {}
D_export[event] = xr.DataArray(data = data, dims = dims, coords = coords, attrs  = {"long_name":f"my data",'units': '-'}) 

ds = xr.Dataset(D_export,attrs = {})
ds.to_netcdf("my_file.nc")

#################
