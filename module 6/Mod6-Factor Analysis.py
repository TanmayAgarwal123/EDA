import pandas as pd
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna()

# Perform Factor Analysis
fa = FactorAnalysis(n_components=3, random_state=42)
factors = fa.fit_transform(numerical_data)

# Add factors to the dataset
for i in range(factors.shape[1]):
    data[f'Factor{i+1}'] = factors[:, i]

print("\nFactor Analysis Results (First 5 Rows):")
print(data[[f'Factor{i+1}' for i in range(factors.shape[1])]].head())

# Plot the first two factors
plt.scatter(factors[:, 0], factors[:, 1], alpha=0.7, cmap='viridis')
plt.title('Factor Analysis: Factor 1 vs Factor 2')
plt.xlabel('Factor 1')
plt.ylabel('Factor 2')
plt.show()
