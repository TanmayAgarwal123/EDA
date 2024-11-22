import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Identify columns with missing values
missing_values = data.isnull().sum()
print("\nColumns with Missing Values:")
print(missing_values[missing_values > 0])

# Drop columns with more than 15% missing data
threshold = 0.15 * len(data)
data_cleaned = data.loc[:, data.isnull().sum() <= threshold]

# Fill missing numerical values with mean
numeric_cols = data_cleaned.select_dtypes(include=[np.number]).columns
data_cleaned[numeric_cols] = data_cleaned[numeric_cols].fillna(data_cleaned[numeric_cols].mean())

# Fill missing categorical values with mode
categorical_cols = data_cleaned.select_dtypes(exclude=[np.number]).columns
for col in categorical_cols:
    data_cleaned[col].fillna(data_cleaned[col].mode()[0], inplace=True)

print("\nMissing Values After Cleaning:")
print(data_cleaned.isnull().sum())
