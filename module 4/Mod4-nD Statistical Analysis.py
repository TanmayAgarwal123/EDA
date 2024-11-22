import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: nD analysis using numerical columns
numerical_cols = data.select_dtypes(include=['number'])

if not numerical_cols.empty:
    print("\nStatistical Summary for Numerical Columns:")
    print(numerical_cols.describe())
else:
    print("No numerical columns found.")
