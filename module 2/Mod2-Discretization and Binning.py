import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Discretizing 'Global_active_power'
if 'Global_active_power' in data.columns:
    bins = [0, 2, 4, 6, 8, np.inf]
    labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
    data['Power_Bin'] = pd.cut(data['Global_active_power'], bins=bins, labels=labels)

    print("\nBinned Data (First 5 Rows):")
    print(data[['Global_active_power', 'Power_Bin']].head())

    # Visualize Binning
    data['Power_Bin'].value_counts().sort_index().plot(kind='bar', color='orange')
    plt.title("Distribution of Power Bins")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.show()
