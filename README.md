# Weather-Forecaster
Repository for 'Weather Forecaster'. Analyzing 30+ years of Gainesville regional weather data to identify seasonal trends using STL and projecting forecasts with SARIMA.

## Project Title: A Statistical Approach to Weather Forecasting
Team Information:
Team Lead – Rohit Mittal – ID: 3945-8163
Developer – Nolan Willett – ID: 3946-9097

## Problem Statement:
Can a statistical model effectively use historical weather data to accurately forecast weather conditions? This project aims to develop a predictive model using historical weather data to forecast temperature and precipitation. An accurate forecast allows a variety of industries to make informed decisions, mitigate risks, and optimize operations.

## Dataset Description: 
Our dataset is sourced from the Florida Climate Center at Florida State University and provides approximately 65 years of mean temperature (Fahrenheit) and precipitation (inches) data from Gainesville Regional Airport.

## Evaluation Metric:
We will partition the data into training (70%), validation (15%), and testing (15%) sets. We will use metrics like Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and correlation coefficient to compare model predictions with historical observations across all metrics. This approach ensures a thorough evaluation of our model's accuracy and reliability in forecasting weather patterns.
Baseline Techniques: Weather forecasting commonly uses statistical models to analyze time-series nature of weather data. Weather data exhibits seasonal trends. Seasonality is where trends repeat over a period of time within a given year; hence the four seasons summer, fall, winter, spring. Recent papers involving predicting rainfall, temperature or other weather patterns have used time series decomposition techniques to isolate trend-cycle, seasonal, and remainder components [1]. A common method uses “Seasonal and Trend decomposition using LOESS” (STL) [2, 3]. Traditional forecasting models like autoregressive integrated moving average (ARIMA) have proven successful for modeling weather patterns 
[3,4]. More recently, machine learning approaches using neural networks are increasingly explored. RNNs [4], and even GNNs [6], offer the potential to model complex dependencies and noise in weather data.

## Proposed Approach and Tools:
### Tools:
Python, pandas, matplotlib, and statsmodel for decomposing and visualizing the data and R or pmdarima (python lib) for ARIMA forecasting.
### Approach: 
Exploratory Data Analysis: Using plots, we will explore trends in each of the weather variables from the dataset. This will help visualize seasonal cycles and the strength of the trend when tuning STL parameters.
Decomposition: We will decompose the training data using the STL model with the statsmodel python library. Extract trend, seasonal, and remainder components from the STL decomposition. Forecasting: Before model fitting, we will re-check the stationarity of the remainder component. We will determine the best ARIMA fitting model for forecasting by plotting the autocorrelation function (ACF) and partial autocorrelation function (PACF) of this remainder component. If the weather variable is stationary, we can use a standard ARIMA(p,d,q), otherwise we will fit a seasonal ARIMA(p, d, q) x (P, D, Q) model. We will use an auto ARIMA function to find a starting point for parameters, and then tune using insights from STL, ACF and PACF. Once the model is fit using ARIMA, we can identify goodness of fit by analyzing the remainder of the fitted model with a Q-Q plot. We can then evaluate this tuned ARIMA model for predicting temperature and precipitation. 

- [1] https://climatecenter.fsu.edu/climate-data-access-tools/downloadable-data 
- [2] https://otexts.com/fpp2/decomposition.html 
- [3] https://www.sciencedirect.com/science/article/abs/pii/S095070512200555X 
- [4] https://iopscience.iop.org/article/10.1088/1742-6596/1921/1/012041/pdf 
- [5] https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=6510&context=etd 
- [6] https://www.sciencedirect.com/science/article/pii/S0360132321000160?via%3Dihub 
- [7] https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/
