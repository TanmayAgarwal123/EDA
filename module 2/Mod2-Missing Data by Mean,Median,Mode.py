import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Handling missing values
numerical_cols = data.select_dtypes(include=[np.number]).columns

# Fill missing values with mean
data_mean_filled = data.copy()
for col in numerical_cols:
    data_mean_filled[col].fillna(data[col].mean(), inplace=True)

# Fill missing values with median
data_median_filled = data.copy()
for col in numerical_cols:
    data_median_filled[col].fillna(data[col].median(), inplace=True)

# Fill missing values with mode
data_mode_filled = data.copy()
for col in numerical_cols:
    data_mode_filled[col].fillna(data[col].mode()[0], inplace=True)

# Print results
print("\nMissing Values After Mean Filling:")
print(data_mean_filled.isnull().sum())

print("\nMissing Values After Median Filling:")
print(data_median_filled.isnull().sum())

print("\nMissing Values After Mode Filling:")
print(data_mode_filled.isnull().sum())
