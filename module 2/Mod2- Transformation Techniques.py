import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PowerTransformer, MinMaxScaler, StandardScaler

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical columns for transformations
numerical_cols = data.select_dtypes(include=[np.number]).columns

# Log Transformation
if 'Global_active_power' in numerical_cols:
    data['Log_Global_active_power'] = np.log1p(data['Global_active_power'].fillna(0))
    plt.hist(data['Log_Global_active_power'], bins=30, color='green', alpha=0.7)
    plt.title("Log Transformed Global Active Power")
    plt.show()

# Min-Max Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data[numerical_cols].fillna(0))
scaled_df = pd.DataFrame(scaled_data, columns=numerical_cols)
print("\nMin-Max Scaled Data (First 5 Rows):")
print(scaled_df.head())

# Standard Scaling
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(data[numerical_cols].fillna(0))
standardized_df = pd.DataFrame(standardized_data, columns=numerical_cols)
print("\nStandardized Data (First 5 Rows):")
print(standardized_df.head())
