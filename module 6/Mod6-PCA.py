import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna()

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(numerical_data)

# Explained variance ratio
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)

# Plot the PCA results
plt.scatter(pca_result[:, 0], pca_result[:, 1], cmap='viridis', alpha=0.7)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
