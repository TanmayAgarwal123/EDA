import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Univariate Analysis of 'Global_active_power'
if 'Global_active_power' in data.columns:
    # Histogram
    sns.histplot(data['Global_active_power'], kde=True, bins=30, color='blue')
    plt.title('Histogram of Global Active Power')
    plt.xlabel('Global Active Power')
    plt.ylabel('Frequency')
    plt.show()

    # Boxplot
    sns.boxplot(data['Global_active_power'], color='green')
    plt.title('Boxplot of Global Active Power')
    plt.show()

    # Summary statistics
    print("\nSummary Statistics for 'Global_active_power':")
    print(data['Global_active_power'].describe())
else:
    print("Column 'Global_active_power' not found.")
