import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna()

# Compute intrinsic dimensionality using MLE
nbrs = NearestNeighbors(n_neighbors=10).fit(numerical_data)
distances, _ = nbrs.kneighbors(numerical_data)

# Estimate intrinsic dimensionality
mean_distance = np.mean(np.log(np.mean(distances, axis=1)))
intrinsic_dim = mean_distance / np.log(np.mean(distances[:, -1]))
print(f"Estimated Intrinsic Dimensionality: {intrinsic_dim:.2f}")
