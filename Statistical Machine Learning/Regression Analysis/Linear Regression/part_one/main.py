"""Linear Regression, 1/21/17, Sajad Azami"""

import part_one.data_preparation as data_preparation
import part_one.linear_regression as linear_regression
import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt
import random

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

data_set_1, label_1 = data_preparation.read_data('../data_set/Dataset1.csv', 8)
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
counter = 0
for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        if counter == 9:
            break
        ax_temp = fig.add_subplot(gs[i, j])
        ax_temp.scatter(train_data_1.get(counter - 1), train_label_1)
        ax_temp.title.set_text(('Feature ' + str(counter)))
plt.show()

# Finding Simple Linear Regression models for each feature with RSS metric
linear_regressions = []
for i in range(0, 8):
    linear_regressions.append(
        linear_regression.rss_regressor(train_data_1.get(i).values, train_label_1,
                                        test_data_1.get(i), test_label_1))

# Plotting Lines fitted with each feature
fig = plt.figure()
gs = gridspec.GridSpec(3, 3)
counter = 0
for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        if counter == 9:
            break
        line = np.linspace(min(train_data_1.get(counter - 1)) - 3,
                           max(train_data_1.get(counter - 1) + 3), 10000)
        ax_temp = fig.add_subplot(gs[i, j])
        ax_temp.scatter(train_data_1.get(counter - 1), train_label_1)
        ax_temp.plot(line, linear_regression.get_points(line, linear_regressions[counter - 1][0],
                                                        linear_regressions[counter - 1][1]))
        ax_temp.title.set_text(('Line with Feature ' + str(counter)))
plt.show()

# Reporting Linear Regression Characteristics for train and test Data
for i in range(0, len(linear_regressions)):
    regression_temp = linear_regressions[i]
    b0_hat = regression_temp[0]
    b1_hat = regression_temp[1]
    estimated_epsilon = regression_temp[2]
    standard_error_b0 = regression_temp[3]
    standard_error_b1 = regression_temp[4]
    RSS_train = regression_temp[5]
    R2_train = regression_temp[6]
    RSS_test = regression_temp[7]
    R2_test = regression_temp[8]
    print('Simple Linear Regression with Feature' + str(i + 1) +
          '\nEstimated (Beta0, Beta1): (' + str(b0_hat) + ', ' + str(b1_hat) + ')\n' +
          'Standard Error of Beta0 and Beta1: (' + str(standard_error_b0) + ', ' + str(standard_error_b1) +
          ')\nEstimated Variance of Epsilon: ' + str(estimated_epsilon) + '\n' +
          'RSS_train: ' + str(RSS_train) + str('\n') +
          'R2_train: ' + str(R2_train) + str('\n') +
          'RSS_test: ' + str(RSS_test) + str('\n') +
          'R2_test: ' + str(R2_test) + str('\n'))

# Starting with Feature4(as the best feature) and adding features, then checking AIC, RSS and R2
current_AIC = linear_regression.get_log_likelihood(train_label_1, train_data_1.get(3)) - 1
print('Current AIC only using Feature4 : ' + str(current_AIC))
used_features_indexes = [3]
features_to_use = train_data_1.get(3).reshape(1, len(train_data_1.get(3)))
test_features_to_use = test_data_1.get(3).reshape(1, len(test_data_1.get(3)))
improving = True
while improving:
    improvements = {}
    features_to_use_temp = []
    test_features_to_use_temp = []
    for i in range(0, 8):
        if i in used_features_indexes:
            continue
        else:
            features_to_use_temp = np.concatenate((features_to_use, train_data_1.get(i).
                                                   reshape(1, len(train_data_1.get(i)))),
                                                  axis=0).T
            test_features_to_use_temp = np.concatenate((test_features_to_use, test_data_1.get(i).
                                                        reshape(1,
                                                                len(test_data_1.get(i)))), axis=0).T
            multiple_regression_result = \
                linear_regression.multivariate_rss_regressor(features_to_use_temp, train_label_1,
                                                             test_features_to_use_temp,
                                                             test_label_1)
            print('AIC after adding Feature' + str(i + 1) + ' :' + str(multiple_regression_result[0]))
            improvements[i] = (multiple_regression_result[0] - current_AIC)
    if len(improvements) > 0 and improvements[max(improvements)] > 0:
        best_index = max(improvements.keys(), key=(lambda k: improvements[k]))
        used_features_indexes.append(best_index)
        features_to_use = np.concatenate((features_to_use, train_data_1.get(best_index).
                                          reshape(1, len(train_data_1.get(best_index)))),
                                         axis=0)
        print_temp = 'Model Uses Feature '
        for j in range(0, len(used_features_indexes)):
            print_temp = print_temp + '(' + str(used_features_indexes[j] + 1) + ') '
        print(print_temp)
        multiple_regression_result = \
            linear_regression.multivariate_rss_regressor(features_to_use.T, train_label_1, None, None)
        print('RSS: ' + str(multiple_regression_result[1]) + ' and R2: ' + str(multiple_regression_result[2]) + '\n')
        improving = True
    else:
        improving = False

# Evaluating the LOOCV metric for different model
LOOCV = linear_regression.get_LOOCV(features_to_use, train_label_1)
print('Leave One Out Cross Validation Risk for ' + str(features_to_use.shape[0]) + ' Features is: ' +
      str(LOOCV))
temp_features = features_to_use
loocvs = [LOOCV]

# Performing the backward method
for i in range(0, 7):
    temp_features = np.delete(temp_features, 0, 0)
    LOOCV = linear_regression.get_LOOCV(temp_features, train_label_1)
    loocvs.append(LOOCV)
    print('Leave One Out Cross Validation Risk for ' + str(temp_features.shape[0]) + ' Features is: ' +
          str(LOOCV))
plt.plot(np.linspace(1, 8, 8), loocvs)
plt.title('RSS vs Number of Used Features')
plt.show()

# Testing Full-Feature model with different number of train data
features_count = [50, 100, 250, 300, 350, 400]
RSS = []
for i in features_count:
    indices = random.sample(range(0, 400), i)
    temp_data = features_to_use.T[indices].reshape(i, 8)
    temp_label = train_label_1[indices]
    RSS.append(linear_regression.multivariate_rss_regressor(
        temp_data, temp_label, None, None)[1])
plt.plot(features_count, RSS)
plt.title('Train RSS vs Number of Train')
plt.show()
print(RSS)
