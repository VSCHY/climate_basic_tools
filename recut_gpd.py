import geopandas as gpd
import time


t0 = time.time()
dire_aqueduct = "./y2019m07d11_aqueduct30_annual_v01.gpkg"
df = gpd.read_file(dire_aqueduct)
t1 = time.time()
print(f"{t1-t0:0.02f} s.")

bounds = df.bounds

t2 = time.time()
print(f"{t2-t1:0.02f} s.")

lat0 = 48.87678393343677
lon0 = 2.2028366101239847

bb = bounds.copy()
bb = bb[lon0 < bb["maxx"]]
bb = bb[lon0 > bb["minx"]]
bb = bb[lat0 < bb["maxy"]]
bb = bb[lat0 > bb["miny"]]
print(bb)

t3 = time.time()
print(f"{t3-t2:0.02f} s.")


#########################################

# Using a polygon:

minx, miny, maxx, maxy = poly.bounds

bb = bounds.copy()
bb = bb[minx < bb["maxx"]]
bb = bb[maxx > bb["minx"]]
bb = bb[miny < bb["maxy"]]
bb = bb[maxy > bb["miny"]]

