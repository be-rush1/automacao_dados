import numpy as np
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Abrir o arquivo NetCDF
netcdf_path = "/Users/elizabetenunes/Desktop/dados_cortados_media_pr_19610101_19801231_BR-DWGD_UFES_UTEXAS_v_3.2.3.nc"
xrds = xr.open_dataset(netcdf_path)

# Carregar o shapefile da região Sudeste
shapefile_path = "/Users/elizabetenunes/Desktop/BR_regiao_sudeste_2022/BR_região_sudeste_2022.shp"
sudeste_shape = gpd.read_file(shapefile_path)

# Selecionar a variável de precipitação
pr = xrds['pr']

# Selecionar o período de referência
precip_ref = pr.sel(time=slice("1961-01-01", "1980-12-31"))

# Calcular a média climatológica
media_climatologica = precip_ref.groupby('time.month').mean(dim='time', skipna=True)

# Calcular a anomalia de precipitação
anomalia_precip = precip_ref.groupby('time.month') - media_climatologica

# Selecionar a região Sudeste (usando limites do shapefile para restringir a área)
# Obtenha o bounding box do shapefile
minx, miny, maxx, maxy = sudeste_shape.total_bounds
sudeste_precip = anomalia_precip.sel(latitude=slice(miny, maxy), longitude=slice(minx, maxx))

# Selecionar uma data específica para plotar, por exemplo, 15 de janeiro de 1975
data_especifica = "1975-01"
anomalia_data_especifica = sudeste_precip.sel(time=data_especifica)

# Normalizar a anomalia para o intervalo [-1, 1]
anomalia_values = anomalia_data_especifica.values
min_val = np.nanmin(anomalia_values)
max_val = np.nanmax(anomalia_values)
anomalia_normalizada = 2 * (anomalia_values - min_val) / (max_val - min_val) - 1

# Criar um DataArray para a anomalia normalizada com as mesmas coordenadas
anomalia_data_especifica_normalizada = xr.DataArray(
    anomalia_normalizada,
    coords=anomalia_data_especifica.coords,
    dims=anomalia_data_especifica.dims
)

# Plotar o mapa com a anomalia normalizada
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Limites do mapa baseados na região Sudeste
ax.set_extent([minx, maxx, miny, maxy], crs=ccrs.PlateCarree())

# Adicionar o shapefile da região Sudeste ao mapa
sudeste_shape.plot(ax=ax, edgecolor='black', facecolor='none', linewidth=1)

# Plotar a anomalia normalizada
anomalia_data_especifica_normalizada.plot(
    ax=ax,
    transform=ccrs.PlateCarree(),
    cmap='RdBu',
    vmin=-1, vmax=1,  # Intervalo de normalização entre -1 e 1
    cbar_kwargs={'label': 'Anomalia Normalizada de Precipitação'}
)

# Título e exibição
plt.title(f"Anomalia Normalizada de Precipitação - Região Sudeste ({data_especifica})")

# Salvar a figura no disco local
output_path = f"/Users/elizabetenunes/Desktop/anomalia_sudeste_{data_especifica}_normalizada.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Mostrar o plot
plt.show()
