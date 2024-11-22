import pandas as pd
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna()

# Apply Isomap for manifold learning
isomap = Isomap(n_neighbors=5, n_components=2)
manifold = isomap.fit_transform(numerical_data)

# Plot the manifold
plt.scatter(manifold[:, 0], manifold[:, 1], cmap='coolwarm', alpha=0.7)
plt.title('Isomap - Manifold Learning')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
