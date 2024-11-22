import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Bar plot for frequency of 'Global_active_power' bins
if 'Global_active_power' in data.columns:
    bins = [0, 2, 4, 6, 8, 10]
    labels = ['0-2', '2-4', '4-6', '6-8', '8-10']
    data['Power_Bins'] = pd.cut(data['Global_active_power'], bins=bins, labels=labels)

    data['Power_Bins'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Bar Plot of Global Active Power Bins')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Column 'Global_active_power' not found.")
