import pandas as pd
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('powerconsumption.csv')

# Select numerical data
numerical_data = data.select_dtypes(include=['number']).dropna().values

# Initialize SOM
som = MiniSom(x=10, y=10, input_len=numerical_data.shape[1], sigma=1.0, learning_rate=0.5, random_seed=42)
som.random_weights_init(numerical_data)
som.train_random(numerical_data, 100)

# Plot the SOM
plt.figure(figsize=(10, 7))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar(label='Distance')
plt.title('Self Organising Map (SOM)')
plt.show()
