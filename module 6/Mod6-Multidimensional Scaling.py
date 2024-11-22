import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna()

# Apply MDS
mds = MDS(n_components=2, random_state=42)
mds_result = mds.fit_transform(numerical_data)

# Plot the MDS results
plt.scatter(mds_result[:, 0], mds_result[:, 1], alpha=0.7, cmap='plasma')
plt.title('Multidimensional Scaling (MDS)')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
