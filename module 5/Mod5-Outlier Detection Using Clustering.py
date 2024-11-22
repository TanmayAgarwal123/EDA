import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Use numerical columns for clustering
numerical_data = data[['Global_active_power', 'Global_reactive_power']].dropna()

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=10)
data['Cluster'] = dbscan.fit_predict(numerical_data)

# Identify outliers (Cluster = -1)
outliers = data[data['Cluster'] == -1]
print("\nDetected Outliers:")
print(outliers)

# Visualize the clustering with outliers
plt.scatter(numerical_data['Global_active_power'], numerical_data['Global_reactive_power'], c=data['Cluster'], cmap='plasma', alpha=0.7)
plt.title('DBSCAN Clustering with Outlier Detection')
plt.xlabel('Global Active Power')
plt.ylabel('Global Reactive Power')
plt.show()
