import xarray as xr
import rioxarray as rio
import geopandas as gpd

# Load your 3D data
# data_path = "path_to_your_3D_data.nc"
data = hi_daily

# Load the India shapefile or GeoJSON
india_shapefile = "path_to_india_boundary.json"
india_boundary = gpd.read_file("D:\HBAASIT\Monsoon_data_mn_5678\T\SHI\india_boundary.geojson")

# Ensure the data has a CRS and is properly georeferenced
data = data.rio.write_crs("EPSG:4326")  # Assuming your data is in WGS84; modify if needed

# Clip the data using the India boundary
clipped_data = data.rio.clip(india_boundary.geometry, india_boundary.crs, drop=True)

# Save the clipped data if needed
# clipped_data.to_netcdf("clipped_data_india.nc")

# Display summary of the clipped data
print(clipped_data)



# to then plot this data

plot data = np.nan_to_num(clipped_data, nan=0) 
