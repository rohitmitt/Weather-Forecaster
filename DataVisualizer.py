import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv(r"./Weather-Forecaster/Dataset.csv")

# Convert 'YYYYMMDD' column to datetime format
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Plotting Precipitation
plt.figure(figsize=(10, 6))
plt.plot(df['YYYYMMDD'], df['PRECIPITATION'])
plt.title('Precipitation by Date', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Precipitation (inches)', fontsize=14)
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("precipitation_plot.pdf")

# Plotting Mean Temperature
plt.figure(figsize=(10, 6))
plt.plot(df['YYYYMMDD'], df['MEAN TEMP'])
plt.title('Mean Temperature by Date', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Mean Temperature (Fahrenheit)', fontsize=14)
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("mean_temperature_plot.pdf")

plt.show()
