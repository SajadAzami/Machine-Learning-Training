"""PGM, 2/1/17, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt
import random
import pandas as pd
import data_preparation

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

# Load dataset
cleveland = data_preparation.read_data('./data_set/processed.cleveland.data.txt')
hungarian = data_preparation.read_data('./data_set/processed.hungarian.data.txt')
switzerland = data_preparation.read_data('./data_set/processed.switzerland.data.txt')
va = data_preparation.read_data('./data_set/processed.va.data.txt')
print('Data set Loaded!')
print(cleveland.shape)
print(hungarian.shape)
print(switzerland.shape)
print(va.shape)

# Merge datasets
frames = [cleveland, hungarian, switzerland, va]
all_city_data = pd.concat(frames)

# Split label and features
all_city_data, all_city_label = data_preparation.split_label(all_city_data, 13)
all_city_label = all_city_label.reshape(len(all_city_label), 1)
print(all_city_label.shape)
print(all_city_data.shape)

# Filling missing values with each columns mean for column [0, 3, 4, 7, 9] and mode for the rest
all_city_data = all_city_data.replace('?', -10)
all_city_data = all_city_data.astype(np.float)
all_city_data = all_city_data.replace(-10, np.NaN)

means = all_city_data.mean()
mean_indices = [0, 3, 4, 7, 9]
mode_indices = [1, 2, 5, 6, 8, 10, 11, 12]
for i in mean_indices:
    all_city_data[i] = all_city_data[i].fillna(means[i])
for i in mode_indices:
    all_city_data[i] = all_city_data[i].fillna(all_city_data[i].mode()[0])

print(all_city_data)

# Decreasing label classes from 5 to 2(0 or 1)
for i in range(0, len(all_city_label)):
    if all_city_label[i] != 0:
        all_city_label[i] = 1
