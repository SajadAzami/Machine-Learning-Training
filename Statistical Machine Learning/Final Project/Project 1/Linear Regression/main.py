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

# # Scatter plot each feature vs label
# fig = plt.figure()
# gs = gridspec.GridSpec(3, 3)
# counter = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         counter += 1
#         if counter == 9:
#             break
#         ax_temp = fig.add_subplot(gs[i, j])
#         ax_temp.scatter(train_data_1.get(counter - 1), train_label_1)
#         ax_temp.title.set_text(('Feature ' + str(counter)))
# plt.show()
#
# # Finding Simple Linear Regression models for each feature with RSS metric
# linear_regressions = []
# for i in range(0, 8):
#     linear_regressions.append(
#         linear_regression.rss_regressor(train_data_1.get(i).values, train_label_1,
#                                         test_data_1.get(i), test_label_1))
#
# # Plotting Lines fitted with each feature
# fig = plt.figure()
# gs = gridspec.GridSpec(3, 3)
# counter = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         counter += 1
#         if counter == 9:
#             break
#         line = np.linspace(min(train_data_1.get(counter - 1)) - 3,
#                            max(train_data_1.get(counter - 1) + 3), 10000)
#         ax_temp = fig.add_subplot(gs[i, j])
#         ax_temp.scatter(train_data_1.get(counter - 1), train_label_1)
#         ax_temp.plot(line, linear_regression.get_points(line, linear_regressions[counter - 1][0],
#                                                         linear_regressions[counter - 1][1]))
#         ax_temp.title.set_text(('Line with Feature ' + str(counter)))
# plt.show()
#
# # Reporting Linear Regression Characteristics for train and test Data
# for i in range(0, len(linear_regressions)):
#     regression_temp = linear_regressions[i]
#     b0_hat = regression_temp[0]
#     b1_hat = regression_temp[1]
#     estimated_epsilon = regression_temp[2]
#     standard_error_b0 = regression_temp[3]
#     standard_error_b1 = regression_temp[4]
#     RSS_train = regression_temp[5]
#     R2_train = regression_temp[6]
#     RSS_test = regression_temp[7]
#     R2_test = regression_temp[8]
#     print('Simple Linear Regression with Feature' + str(i + 1) +
#           '\nEstimated (Beta0, Beta1): (' + str(b0_hat) + ', ' + str(b1_hat) + ')\n' +
#           'Standard Error of Beta0 and Beta1: (' + str(standard_error_b0) + ', ' + str(standard_error_b1) +
#           ')\nEstimated Variance of Epsilon: ' + str(estimated_epsilon) + '\n' +
#           'RSS_train: ' + str(RSS_train) + str('\n') +
#           'R2_train: ' + str(R2_train) + str('\n') +
#           'RSS_test: ' + str(RSS_test) + str('\n') +
#           'R2_test: ' + str(R2_test) + str('\n'))

# Starting with Feature4(as the best feature) and adding features, then checking AIC
current_AIC = linear_regression.get_log_likelihood(train_label_1, train_data_1.get(3)) - 1
print('Current AIC only using Feature4 : ' + str(current_AIC))
used_features = [3]
features_to_use = []
for i in range(0, 8):
    if i in used_features:
        continue
    else:
        features_to_use = np.concatenate((train_data_1.get(3).reshape(1, len(train_data_1.get(3))),
                                          train_data_1.get(i).reshape(1, len(train_data_1.get(i)))), axis=0).T
        test_features_to_use = np.concatenate((test_data_1.get(3).reshape(1, len(test_data_1.get(3))),
                                               test_data_1.get(i).reshape(1, len(test_data_1.get(i)))), axis=0).T
        multiple_regression_result = linear_regression.multivariate_rss_regressor(features_to_use, train_label_1,
                                                                                  test_features_to_use, test_label_1)
        print('AIC after adding Feature' + str(i + 1) + ' :' + str(multiple_regression_result))

used_features.append(7)

