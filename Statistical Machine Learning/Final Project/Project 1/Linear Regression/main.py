"""Linear Regression, 1/21/17, Sajad Azami"""

import data_preparation
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
import linear_regression
import numpy as np

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

data_set_1, label_1 = data_preparation.read_data('./data_set/Dataset1.csv')
print('Data set Loaded!')

# Split train and test data
train_data_1 = data_set_1[:400]
train_label_1 = label_1[:400]
test_data_1 = data_set_1[400:]
test_label_1 = label_1[400:]

print('Train data size:', len(train_data_1))
print('Test data size:', len(test_data_1))

# Scatter plot each feature vs label
fig = plt.figure()
gs = gridspec.GridSpec(3, 3)
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(train_data_1.get(0), train_label_1)
ax1.title.set_text('Feature 1')
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(train_data_1.get(1), train_label_1)
ax2.title.set_text('Feature 2')
ax3 = fig.add_subplot(gs[0, 2])
ax3.scatter(train_data_1.get(2), train_label_1)
ax3.title.set_text('Feature 3')
ax4 = fig.add_subplot(gs[1, 0])
ax4.scatter(train_data_1.get(3), train_label_1)
ax4.title.set_text('Feature 4')
ax5 = fig.add_subplot(gs[1, 1])
ax5.scatter(train_data_1.get(4), train_label_1)
ax5.title.set_text('Feature 5')
ax6 = fig.add_subplot(gs[1, 2])
ax6.scatter(train_data_1.get(5), train_label_1)
ax6.title.set_text('Feature 6')
ax7 = fig.add_subplot(gs[2, 0])
ax7.scatter(train_data_1.get(6), train_label_1)
ax7.title.set_text('Feature 7')
ax8 = fig.add_subplot(gs[2, 1])
ax8.scatter(train_data_1.get(7), train_label_1)
ax8.title.set_text('Feature 8')
plt.show()

# Finding Simple Linear Regression models for each feature with RSS metric
linear_regression_1 = linear_regression.rss_regressor(train_data_1.get(0).values, train_label_1)
print(linear_regression_1)
line = np.linspace(-5, 5, 10000)
plt.scatter(train_data_1.get(0), train_label_1)
plt.plot(line, linear_regression.get_points(line, linear_regression_1[0], linear_regression_1[1]))
plt.show()
