import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Scatter plot for 'Global_active_power' vs 'Voltage'
if 'Global_active_power' in data.columns and 'Voltage' in data.columns:
    plt.scatter(data['Global_active_power'], data['Voltage'], alpha=0.5, color='red')
    plt.title('Scatter Plot: Global Active Power vs Voltage')
    plt.xlabel('Global Active Power')
    plt.ylabel('Voltage')
    plt.show()
else:
    print("Required columns for scatter plot not found.")
