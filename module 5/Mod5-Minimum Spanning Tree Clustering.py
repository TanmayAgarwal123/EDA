import pandas as pd
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from sklearn.metrics.pairwise import euclidean_distances

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Use a subset of numerical columns
numerical_data = data[['Global_active_power', 'Global_reactive_power']].dropna()

# Compute the distance matrix
distance_matrix = euclidean_distances(numerical_data)

# Compute the minimum spanning tree
mst = minimum_spanning_tree(distance_matrix)

print("\nMinimum Spanning Tree:")
print(mst.toarray())
