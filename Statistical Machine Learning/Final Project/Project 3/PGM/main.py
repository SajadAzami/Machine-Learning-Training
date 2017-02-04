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


# Finds mean of column with respect to missing values
# Returns a list of means
def get_column_mean(data):
    means = []
    for i in range(0, data.shape[1]):
        sum_of_column = 1
        counter = 1
        tmp = data[i]
        for j in range(0, len(tmp)):
            print(tmp[j])
            # if tmp is not np.NaN and tmp is not str:
            #     sum_of_column = sum_of_column + tmp
            #     counter += 1
        means.append(sum_of_column / counter)
    return means


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
# print(get_column_mean(all_city_data))
all_city_data = all_city_data.replace('?', np.NaN)
all_city_data = all_city_data.fillna(0)
print(all_city_data)
# for i in range(0, all_city_data.shape[1]):
#     print(all_city_data[i].fillna(0))
