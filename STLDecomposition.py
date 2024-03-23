from random import randrange
from pandas import read_csv
from pandas import read_csv, to_datetime
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import STL
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

dataset = read_csv(r'./Weather-Forecaster/Dataset.csv', header=0, index_col=0)
dataset.index = to_datetime(dataset.index, format='%Y%m%d')

precipitation = dataset['PRECIPITATION']
mean_temp = dataset['MEAN TEMP']

# ============== MEAN TEMP DECOMPOSITION ==================

# Perform seasonal decomposition for mean temperature
stl = STL(mean_temp, period=365)
res = stl.fit()

# Plot the decomposition for mean temperature
fig = res.plot()
plt.savefig("mean_temperature_decomposition.pdf")
plt.close()

# Extract components from the res object
mean_temp_observed = res.observed
mean_temp_trend = res.trend
mean_temp_seasonal = res.seasonal
mean_temp_residual = res.resid

# Compute the autocorrelation function (ACF)
plot_acf(mean_temp, lags=50)
plt.savefig("mean_temp_ACF.pdf")
plt.close()

# Compute the partial autocorrelation function (PACF)
plot_pacf(mean_temp, lags=50)
plt.savefig("mean_temp_PACF.pdf")
plt.close()

# ============== PRECIPITATION DECOMPOSITION ==================

# Perform seasonal decomposition for precipitation
stl = STL(precipitation, period=365, seasonal=13)
res = stl.fit()

# Plot the decomposition for precipitation
fig = res.plot()
plt.savefig("precipitation_decomposition.pdf")
plt.close()

# Extract components from the res object
precipitation_observed = res.observed
precipitation_trend = res.trend
precipitation_seasonal = res.seasonal
precipitation_residual = res.resid

# Compute the autocorrelation function (ACF)
plot_acf(precipitation, lags=50)
plt.savefig("precipitation_ACF.pdf")
plt.close()

# Compute the partial autocorrelation function (PACF)
plot_pacf(precipitation, lags=50)
plt.savefig("precipitation_PACF.pdf")
plt.close()
