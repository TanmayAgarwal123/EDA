import pandas as pd
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Use numerical columns for clustering
numerical_data = data[['Global_active_power', 'Global_reactive_power']].dropna()

# Perform Spectral Clustering
spectral = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', random_state=42)
data['Cluster'] = spectral.fit_predict(numerical_data)

# Visualize the clustering
plt.scatter(numerical_data['Global_active_power'], numerical_data['Global_reactive_power'], c=data['Cluster'], cmap='rainbow', alpha=0.7)
plt.title('Spectral Clustering')
plt.xlabel('Global Active Power')
plt.ylabel('Global Reactive Power')
plt.show()
