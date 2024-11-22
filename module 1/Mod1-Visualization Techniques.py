import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Distribution of a numerical column
if 'Global_active_power' in data.columns:
    sns.histplot(data['Global_active_power'], kde=True, bins=30, color='blue')
    plt.title('Distribution of Global Active Power')
    plt.xlabel('Global Active Power')
    plt.ylabel('Frequency')
    plt.show()

# Heatmap for correlations
numerical_data = data.select_dtypes(include=[np.number])
sns.heatmap(numerical_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()
