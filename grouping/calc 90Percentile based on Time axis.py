# Data is 3D (valid_time,lat,lon)
# i am using xarray


data_xarray_temp['week'] = data_xarray_temp['valid_time'].dt.isocalendar().week
percentile_90_weekly = data_xarray_temp.groupby('week').quantile(0.9, dim='valid_time')
