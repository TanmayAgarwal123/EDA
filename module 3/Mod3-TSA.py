import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Ensure 'Date' is in datetime format and sort by date
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.sort_values('Date')

    # Example: Time Series Analysis of 'Global_active_power'
    if 'Global_active_power' in data.columns:
        # Set 'Date' as the index
        ts_data = data.set_index('Date')['Global_active_power'].dropna()

        # Plot the time series
        plt.figure(figsize=(12, 6))
        ts_data.plot(color='blue')
        plt.title('Time Series of Global Active Power')
        plt.xlabel('Date')
        plt.ylabel('Global Active Power')
        plt.show()

        # Decompose the time series
        decomposition = seasonal_decompose(ts_data, model='additive', period=24)
        decomposition.plot()
        plt.suptitle("Time Series Decomposition", y=1.02)
        plt.show()
    else:
        print("Column 'Global_active_power' not found.")
else:
    print("Column 'Date' not found or not in proper format.")
