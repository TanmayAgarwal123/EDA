import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Replace specific values in 'Global_active_power'
if 'Global_active_power' in data.columns:
    # Replace negative values with NaN
    data['Global_active_power'] = data['Global_active_power'].apply(lambda x: np.nan if x < 0 else x)

    # Replace values above a threshold with a fixed value
    threshold = 10
    data['Global_active_power'] = data['Global_active_power'].apply(lambda x: threshold if x > threshold else x)

    print("\nReplaced Values in 'Global_active_power':")
    print(data['Global_active_power'].describe())
