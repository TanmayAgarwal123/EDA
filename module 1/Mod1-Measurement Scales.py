import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Determine data types and categorize columns by scales
print("\nMeasurement Scales:")
for column in data.columns:
    if data[column].dtype == 'object':
        print(f"{column}: Nominal or Categorical")
    elif pd.api.types.is_integer_dtype(data[column]):
        print(f"{column}: Ordinal or Interval (check context)")
    elif pd.api.types.is_float_dtype(data[column]):
        print(f"{column}: Ratio Scale")
    elif pd.api.types.is_datetime64_any_dtype(data[column]):
        print(f"{column}: Temporal/Date-Time")
