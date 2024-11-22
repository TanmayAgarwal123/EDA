import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Z-score for outlier detection
if 'Global_active_power' in data.columns:
    data['z_score'] = zscore(data['Global_active_power'].fillna(0))
    outliers = data[data['z_score'].abs() > 3]

    print("\nOutliers in 'Global_active_power':")
    print(outliers[['Global_active_power', 'z_score']])

    sns.boxplot(data['Global_active_power'])
    plt.title("Boxplot of Global Active Power")
    plt.show()
