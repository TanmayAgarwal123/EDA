import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Data elaboration: Creating new features
if 'Global_active_power' in data.columns and 'Global_intensity' in data.columns:
    data['Power_to_Intensity'] = data['Global_active_power'] / data['Global_intensity']
    print("\nNew Feature 'Power_to_Intensity' Created:")
    print(data[['Global_active_power', 'Global_intensity', 'Power_to_Intensity']].head())
else:
    print("Required columns for data elaboration not found.")
