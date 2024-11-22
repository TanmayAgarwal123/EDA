import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Use numerical columns for clustering
numerical_data = data.select_dtypes(include=['number']).dropna()

# Perform hierarchical clustering
linked = linkage(numerical_data, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 6))
dendrogram(linked, truncate_mode='lastp', p=10, leaf_rotation=45, leaf_font_size=12)
plt.title('Hierarchical Agglomerative Clustering Dendrogram')
plt.xlabel('Cluster Index')
plt.ylabel('Distance')
plt.show()
