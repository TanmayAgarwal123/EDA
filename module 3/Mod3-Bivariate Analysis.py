import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Bivariate Analysis of 'Global_active_power' and 'Global_reactive_power'
if 'Global_active_power' in data.columns and 'Global_reactive_power' in data.columns:
    # Scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Global_active_power', y='Global_reactive_power', data=data, color='purple')
    plt.title('Global Active Power vs Global Reactive Power')
    plt.xlabel('Global Active Power')
    plt.ylabel('Global Reactive Power')
    plt.show()

    # Correlation
    correlation = data[['Global_active_power', 'Global_reactive_power']].corr()
    print("\nCorrelation Matrix:")
    print(correlation)
else:
    print("Required columns not found.")
