import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Dot chart for 'Global_active_power'
if 'Global_active_power' in data.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(data['Global_active_power'], 'o', markersize=2, alpha=0.6)
    plt.title('Dot Chart of Global Active Power')
    plt.xlabel('Index')
    plt.ylabel('Global Active Power')
    plt.show()
else:
    print("Column 'Global_active_power' not found.")
