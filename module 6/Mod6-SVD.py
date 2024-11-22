import pandas as pd
from scipy.linalg import svd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna().values

# Perform SVD
U, S, Vt = svd(numerical_data)

# Plot singular values
plt.plot(np.arange(1, len(S)+1), S, 'o-')
plt.title('Singular Values from SVD')
plt.xlabel('Index')
plt.ylabel('Singular Value')
plt.grid()
plt.show()
