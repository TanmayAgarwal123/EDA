import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Summary statistics for all numerical columns
numerical_cols = data.select_dtypes(include=['number'])

if not numerical_cols.empty:
    print("\nStatistical Summary Measures:")
    print(numerical_cols.describe())
else:
    print("No numerical columns found.")
