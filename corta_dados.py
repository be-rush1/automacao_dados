import rioxarray
import xarray as xr
import geopandas
import os
from shapely.geometry import mapping
arquivo = str(os.environ["ANO_ARQUIVO"])
path = str(os.environ["WORKSPACE"])
data = xr.open_dataset(path + '/chirps-v2.0.'+ arquivo + '.monthly.nc')
data.rio.set_spatial_dims(x_dim="latitude", y_dim="longitude", inplace=True)
data.rio.write_crs("epsg:4326", inplace=True)
print(str(os.system('pwd')))
print(str(os.system('cd BR_regiao_sudeste_2022')))
sudeste = geopandas.read_file('BR_regiao_sudeste_2022/BR_região_sudeste_2022.shp', crs="epsg:4326")
clipped = data.rio.clip(sudeste.geometry.apply(mapping), sudeste.crs, drop=True)
