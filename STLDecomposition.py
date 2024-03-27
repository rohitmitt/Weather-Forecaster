import pandas as pd
from pandas import read_csv, to_datetime, DataFrame 
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

dataset = read_csv(r'Dataset.csv', header=0, index_col=0)
dataset.index = to_datetime(dataset.index, format='%Y%m%d')

precipitation = dataset['PRECIPITATION']
mean_temp = dataset['MEAN TEMP']

# ============== MEAN TEMP DECOMPOSITION ==================

# Perform seasonal decomposition for mean temperature
stl = STL(mean_temp, period=365, seasonal=31)
res = stl.fit()

# Plot the decomposition for mean temperature
# fig = res.plot()
# plt.savefig("mean_temperature_decomposition.pdf")
# plt.close()

# Extract components from the res object
mean_temp_trend = res.trend
mean_temp_seasonal = res.seasonal
mean_temp_residual = res.resid
# mean_temp.to_csv('mean_temp.csv', header=True)
precipitation.to_csv('precipitation.csv', header=True)
# # Compute the autocorrelation function (ACF)
# plot_acf(mean_temp_residual, lags=50)

# # Compute the partial autocorrelation function (PACF)
# plot_pacf(mean_temp_residual, lags=50)

plt.show()

# # fit model
# model = SARIMAX(mean_temp_residual, order=(1,1,0), seasonal_order=(1, ))
# model_fit = model.fit()
# # summary of fit model
# print(model_fit.summary())
# # line plot of residuals
# residuals = DataFrame(model_fit.resid)
# residuals.plot()
# pyplot.show()
# # density plot of residuals
# residuals.plot(kind='kde')
# pyplot.show()
# # summary stats of residuals
# print(residuals.describe())


# # ============== PRECIPITATION DECOMPOSITION ==================

# # ==============TUNED PRECIPITATION ==============
# stl = STL(precipitation, period=365, seasonal = 63, robust=1)
# res = stl.fit()
# # Create a figure
# fig = res.plot()
# # Set the title with the seasonal value
# plt.suptitle(f"Precipitation Decomposition")

# # # Extract components from the res object
# precipitation_observed = res.observed
# precipitation_trend = res.trend
# precipitation_seasonal = res.seasonal
# precipitation_residual = res.resid

# # Compute the autocorrelation function (ACF)
# plot_acf(precipitation_seasonal, lags=50)

# # Compute the partial autocorrelation function (PACF)
# plot_pacf(precipitation_seasonal, lags=50)

# plt.show()

# # ============== UNTUNED OLD PRECIPITATIOON ==============
# # # Plot the decomposition for precipitation
# # stl = STL(precipitation, period=365)
# # res = stl.fit()
# # fig = res.plot()
# # plt.show()
# # plt.savefig("precipitation_decomposition.pdf")
# # plt.close()

# # # Extract components from the res object
# # precipitation_observed = res.observed
# # precipitation_trend = res.trend
# # precipitation_seasonal = res.seasonal
# # precipitation_residual = res.resid

# # # Compute the autocorrelation function (ACF)
# # plot_acf(precipitation, lags=50)
# # plt.savefig("precipitation_ACF.pdf")
# # plt.close()

# # # Compute the partial autocorrelation function (PACF)
# # plot_pacf(precipitation, lags=50)
# # plt.savefig("precipitation_PACF.pdf")
# # plt.close()
