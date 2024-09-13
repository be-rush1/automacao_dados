import rioxarray
import xarray as xr
import geopandas
import os
from shapely.geometry import mapping
arquivo = str(os.environ["ano_arquivo"])
data = xr.open_dataset('chirps-v2.0.'+ arquivo + '.monthly.nc')
data.rio.set_spatial_dims(x_dim="latitude", y_dim="longitude", inplace=True)
data.rio.write_crs("epsg:4326", inplace=True)
sudeste = geopandas.read_file('teste/BR_regiao_sudeste_2022/BR_regiao_sudeste_2022.sh', crs="epsg:4326")
clipped = data.rio.clip(sudeste.geometry.apply(mapping), sudeste.crs, drop=True)
