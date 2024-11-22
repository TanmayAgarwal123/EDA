import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Covariance and Correlation of 'Global_active_power' and 'Global_reactive_power'
if 'Global_active_power' in data.columns and 'Global_reactive_power' in data.columns:
    cov = np.cov(data['Global_active_power'], data['Global_reactive_power'])
    corr = np.corrcoef(data['Global_active_power'], data['Global_reactive_power'])
    print("\nCovariance Matrix:")
    print(cov)
    print("\nCorrelation Coefficient Matrix:")
    print(corr)
else:
    print("Required columns not found.")
