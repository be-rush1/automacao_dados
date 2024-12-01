import rioxarray
import xarray as xr
import geopandas
import os
from shapely.geometry import mapping
os.system('ls')
arquivo = str(os.environ["ANO_ARQUIVO"])
path = str(os.environ["WORKSPACE"])
data = xr.open_dataset(path + '/chirps-v2.0.'+ arquivo + '.monthly.nc')
data.rio.set_spatial_dims(x_dim="latitude", y_dim="longitude", inplace=True)
data.rio.write_crs("epsg:4326", inplace=True)
#os.system('cd BR_regiao_sudeste_2022')
sudeste = geopandas.read_file('BR_região_sudeste_2022.shp', crs="epsg:4326")
#os.system('cd ../')
clipped = data.rio.clip(sudeste.geometry.apply(mapping), sudeste.crs, drop=True)
clipped.to_netcdf("dados_cortados_" + arquivo + ".nc")

