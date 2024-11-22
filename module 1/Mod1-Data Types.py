import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Split columns into numerical and categorical
numerical_data = data.select_dtypes(include=[np.number])
categorical_data = data.select_dtypes(exclude=[np.number])

# Print numerical and categorical columns
print("Numerical Columns:", numerical_data.columns.tolist())
print("Categorical Columns:", categorical_data.columns.tolist())

# Check for datetime columns
datetime_cols = [col for col in data.columns if pd.api.types.is_datetime64_any_dtype(data[col])]
if not datetime_cols and 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    datetime_cols = ['Date']

print("\nDatetime Columns:", datetime_cols)

# Bar plot for the first categorical column (if any)
if not categorical_data.empty:
    cat_column = categorical_data.columns[0]
    print(f"\nBar plot for the first categorical column: {cat_column}")
    categorical_data[cat_column].value_counts().plot(kind='bar', color='orange')
    plt.title(f'Distribution of {cat_column}')
    plt.xlabel(cat_column)
    plt.ylabel('Frequency')
    plt.show()
else:
    print("No categorical columns available for plotting.")
