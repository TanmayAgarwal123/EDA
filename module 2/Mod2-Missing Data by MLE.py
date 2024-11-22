import pandas as pd
import numpy as np
from statsmodels.imputation.mice import MICEData

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Example: Use MLE for missing data imputation
numerical_cols = data.select_dtypes(include=[np.number])
data_mice = MICEData(numerical_cols)

# Impute missing values
data_mle_filled = data_mice.data
print("\nMissing Values After MLE Imputation:")
print(data_mle_filled.isnull().sum())
