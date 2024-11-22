import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Statistical analysis of 'Global_active_power'
if 'Global_active_power' in data.columns:
    print("\n1D Statistical Analysis for 'Global_active_power':")
    print("Mean:", data['Global_active_power'].mean())
    print("Median:", data['Global_active_power'].median())
    print("Variance:", data['Global_active_power'].var())
    print("Standard Deviation:", data['Global_active_power'].std())
    print("Minimum:", data['Global_active_power'].min())
    print("Maximum:", data['Global_active_power'].max())
else:
    print("Column 'Global_active_power' not found.")
