import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Dataset Summary
print("\nDataset Summary:")
print(data.describe(include='all'))

# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Pairplot for numerical data
numerical_data = data.select_dtypes(include=[np.number])
sns.pairplot(numerical_data, diag_kind='kde')
plt.suptitle("Pairplot of Numerical Features", y=1.02)
plt.show()

# Correlation heatmap
correlation_matrix = numerical_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
