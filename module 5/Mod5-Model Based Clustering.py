import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Use numerical columns for clustering
numerical_data = data[['Global_active_power', 'Global_reactive_power']].dropna()

# Perform model-based clustering
gmm = GaussianMixture(n_components=3, random_state=42)
data['Cluster'] = gmm.fit_predict(numerical_data)

# Plot the clusters
plt.scatter(numerical_data['Global_active_power'], numerical_data['Global_reactive_power'], c=data['Cluster'], cmap='viridis', alpha=0.7)
plt.title('Model-Based Clustering')
plt.xlabel('Global Active Power')
plt.ylabel('Global Reactive Power')
plt.show()
