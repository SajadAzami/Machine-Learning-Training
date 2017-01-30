"""Linear Regression, 1/30/17, Sajad Azami"""

import part_one.data_preparation as data_preparation
import part_one.linear_regression as linear_regression
import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

data_set_1, label_1 = data_preparation.read_data('../data_set/Dataset2.csv', 6)
print('Data set Loaded!')

# Split train and test data
train_data_1 = data_set_1[:200]
train_label_1 = label_1[:200]
test_data_1 = data_set_1[200:]
test_label_1 = label_1[200:]

print('Train data size:', len(train_data_1))
print('Test data size:', len(test_data_1))

# Scatter plot each feature vs label
fig = plt.figure()
gs = gridspec.GridSpec(2, 3)
counter = 0
for i in range(0, 2):
    for j in range(0, 3):
        counter += 1
        ax_temp = fig.add_subplot(gs[i, j])
        ax_temp.scatter(train_data_1.get(counter - 1), train_label_1)
        ax_temp.title.set_text(('Feature ' + str(counter)))
plt.show()
