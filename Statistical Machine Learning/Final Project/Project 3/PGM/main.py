"""PGM, 2/1/17, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt
import random
import pandas as pd
import data_preparation
from sklearn.naive_bayes import MultinomialNB
from mpl_toolkits.mplot3d import Axes3D
import warnings
from pgmpy.models import BayesianModel

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("whitegrid")


def warn(*args, **kwargs):
    pass


warnings.warn = warn


# Calculates Leave One Out Cross Validation Error
def get_LOOCV(features_to_use, train_label):
    RSS_list = []
    for i in range(0, features_to_use.shape[1]):
        temp_data = features_to_use.drop(i, axis=0)
        temp_label = np.delete(train_label.reshape(len(train_label), 1), i, 0)
        mnnb = MultinomialNB()
        mnnb.fit(temp_data, temp_label)
        pred = mnnb.predict(features_to_use.iloc[[i]])
        RSS_list.append(sum((train_label[i] - pred) ** 2))
    LOOCV = sum(RSS_list) / len(RSS_list)
    return LOOCV


# Learning naive bayes model from feature set of feature_list
def naive_bayes_with_some_features(all_city_data, all_city_label, feature_list):
    all_city_label = all_city_label.reshape(len(all_city_label), )
    features_to_use = all_city_data.loc[:, feature_list]
    mnnb = MultinomialNB()
    mnnb.fit(features_to_use, all_city_label)
    pred = mnnb.predict(features_to_use)
    print("Number of mislabeled points out of a total " + str(features_to_use.shape[0]) + ' points: ' + (
        str((all_city_label != pred).sum())))
    # LOOCV risk
    print('Feature set: ' + str(feature_list) + '\nLOOCV: ' + str(get_LOOCV(features_to_use, all_city_label)))
    print('')
    return mnnb


# Load dataset
cleveland = data_preparation.read_data('./data_set/processed.cleveland.data.txt')
hungarian = data_preparation.read_data('./data_set/processed.hungarian.data.txt')
switzerland = data_preparation.read_data('./data_set/processed.switzerland.data.txt')
va = data_preparation.read_data('./data_set/processed.va.data.txt')
print('Data set Loaded!')

# Merge datasets
frames = [cleveland, hungarian, switzerland, va]
all_city_data = pd.concat(frames)

# Split label and features
all_city_data, all_city_label = data_preparation.split_label(all_city_data, 13)
all_city_label = all_city_label.reshape(len(all_city_label), 1)
all_city_data = all_city_data.reset_index(drop=True)

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

# Decreasing label classes from 5 to 2(0 or 1)
for i in range(0, len(all_city_label)):
    if all_city_label[i] != 0:
        all_city_label[i] = 1

# Discretizing values of continuous columns [0, 3, 4, 7, 9]
all_city_data[0] = pd.cut(all_city_data[0].values, 5,
                          labels=[0, 1, 2, 3, 4]).astype(list)
all_city_data[3] = pd.cut(all_city_data[3].values, 3,
                          labels=[0, 1, 2]).astype(list)
all_city_data[4] = pd.cut(all_city_data[4].values, 5,
                          labels=[0, 1, 2, 3, 4]).astype(list)
all_city_data[7] = pd.cut(all_city_data[7].values, 5,
                          labels=[0, 1, 2, 3, 4]).astype(list)
all_city_data[9] = pd.cut(all_city_data[9].values, 3,
                          labels=[0, 1, 2]).astype(list)

# # Scatter plot each feature vs label after filling missing values
# fig = plt.figure()
#
# gs = gridspec.GridSpec(3, 3)
# counter = 0
# # Discrete values
# for k in range(0, 3):
#     for j in range(0, 3):
#         if counter == 8:
#             break
#         ax_temp = fig.add_subplot(gs[k, j], projection='3d')
#
#         x = all_city_data[mode_indices[counter]].values.reshape(len(all_city_data[mode_indices[counter]]), 1)
#         y = all_city_label
#         d = {}
#         for i in range(0, len(x)):
#             if (x[i][0], y[i][0]) in d.keys():
#                 d[(x[i][0], y[i][0])] += 1
#             else:
#                 d[(x[i][0], y[i][0])] = 0
#         x = []
#         y = []
#         z = []
#         for i in d.items():
#             x.append(i[0][0])
#             y.append(i[0][1])
#             z.append(i[1])
#         ax_temp.bar(x, z, zs=y, zdir='y', alpha=0.6, color='r' * 4)
#         ax_temp.set_xlabel('X')
#         ax_temp.set_ylabel('Y')
#         ax_temp.set_zlabel('Z')
#         ax_temp.title.set_text(('Feature ' + str(mode_indices[counter])))
#         counter += 1
# plt.show()
#
# # Continuous values
# fig = plt.figure()
# gs = gridspec.GridSpec(2, 3)
# counter = 0
# for k in range(0, 2):
#     for j in range(0, 3):
#         if counter == 5:
#             break
#         # print(counter)
#         ax_temp = fig.add_subplot(gs[k, j], projection='3d')
#
#         x = all_city_data[mean_indices[counter]].values.reshape(len(all_city_data[mean_indices[counter]]), 1)
#         y = all_city_label
#         d = {}
#         for i in range(0, len(x)):
#             if (x[i][0], y[i][0]) in d.keys():
#                 d[(x[i][0], y[i][0])] += 1
#             else:
#                 d[(x[i][0], y[i][0])] = 0
#         x = []
#         y = []
#         z = []
#         for i in d.items():
#             x.append(i[0][0])
#             y.append(i[0][1])
#             z.append(i[1])
#         ax_temp.bar(x, z, zs=y, zdir='y', alpha=0.6, color='r' * 4)
#         ax_temp.set_xlabel('X')
#         ax_temp.set_ylabel('Y')
#         ax_temp.set_zlabel('Z')
#         ax_temp.title.set_text(('Feature ' + str(mean_indices[counter])))
#         counter += 1
# plt.show()

# Learning naive bayes model from various subsets of data
naive_bayes_with_some_features(all_city_data, all_city_label, feature_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
naive_bayes_with_some_features(all_city_data, all_city_label, feature_list=[0, 1, 2])
naive_bayes_with_some_features(all_city_data, all_city_label, feature_list=[0, 1, 2, 4])
naive_bayes_with_some_features(all_city_data, all_city_label, feature_list=[0, 1, 2, 3, 4, 5])

# Implementing PGM model on data