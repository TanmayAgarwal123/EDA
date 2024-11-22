import pandas as pd

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Contingency Table for 'Power_Bins' and 'Voltage'
if 'Power_Bins' in data.columns and 'Voltage' in data.columns:
    bins = [0, 230, 240, 250, 260]
    labels = ['Low', 'Medium', 'High', 'Very High']
    data['Voltage_Bins'] = pd.cut(data['Voltage'], bins=bins, labels=labels)

    contingency_table = pd.crosstab(data['Power_Bins'], data['Voltage_Bins'])
    print("\nContingency Table:")
    print(contingency_table)
else:
    print("Required columns for contingency table not found.")
