import rioxarray
import rasterio
from shapely.ops import transform
import glob
from rasterio.merge import merge
from rasterio.mask import mask
from pyproj import transform as tr
from functools import partial
import pyproj


filename_in = "/dire/input.tif"
filename_out = "/dire/output.tif"
poly = #polygon

##########################
# Recut large tif files over a polygon

try:
    with rasterio.open() as src0:
        out_image, out_transform = mask(dataset=src0, shapes=[poly], crop=True)
        out_meta = src0.meta.copy()
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
        with rasterio.open(filename_out, "w", **out_meta) as dest:
            dest.write(out_image)
except:
    print("An error has occurred, maybe there is no data over the Polygon")
    print("Take care that the Polygon and raster have the same projection")
     
##########################
# Open the recut tif file

with rioxarray.open_rasterio(filename_out) as rds:
    lon = rds.x
    lat = rds.y
    data = rds.data[0,:,:]
    # data  = ma.masked_where(data<0, data)
    
##########################
# Merge of tif files

list_tif_files = glob.glob(f"my_files*.tif")

src_files_to_mosaic = []

for d in list_tif_files:
    src = rasterio.open(d)
    src_files_to_mosaic.append(src)

mosaic, out_trans = merge(src_files_to_mosaic)
out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
                        "height": mosaic.shape[1],
                        "width": mosaic.shape[2],
                        "transform": out_trans,
                        "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                        })
                        
with rasterio.open("outfile_merged.tif", "w", **out_meta) as dest:
    dest.write(mosaic)

##########################
# Convert shape (example WGS84 to EPSG:3035)
wgs84_to_3035 = partial(
    pyproj.transform,
    pyproj.Proj("+proj=longlat +datum=WGS84 +no_defs"),
    pyproj.Proj(init='EPSG:3035'),
)

poly_3035 = transform(wgs84_to_3035,  poly)

