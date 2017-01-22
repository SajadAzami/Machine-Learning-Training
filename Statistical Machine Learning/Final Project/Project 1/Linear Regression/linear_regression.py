"""Linear Regression, 1/21/17, Sajad Azami"""

import data_preparation
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib import gridspec

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")


# Fits a line that minimizes Residual Sum of Errors
# The line is Yi = B0 + B1*Xi
# feature_vector(Xi) and response_vector(Yi) are numpy arrays
# returns B0, B1, sigma2_hat(estimated variance of epsilon)
# standard errors of B0 and B1, RSS and R2 Metrics
def rss_regressor(feature_vector, response_vector, feature_vector_test, response_vector_test):
    Y_bar = sum(response_vector) / len(response_vector)
    Y_bar_test = sum(response_vector_test) / len(response_vector_test)
    X_bar = sum(feature_vector) / len(feature_vector)
    B1_hat = sum((feature_vector - X_bar) * (response_vector - Y_bar)) / sum((feature_vector - X_bar) ** 2)
    B0_hat = Y_bar - B1_hat * X_bar

    RSS_train = sum((response_vector - (B0_hat + B1_hat * feature_vector)) ** 2)
    RSS_test = sum((response_vector_test - (B0_hat + B1_hat * feature_vector_test)) ** 2)

    sigma2_hat = 1 / (len(feature_vector) - 2) * RSS_train

    S_x = (1 / len(feature_vector)) * sum((feature_vector - X_bar) ** 2)
    standard_error_B1 = math.sqrt(sigma2_hat) / S_x * math.sqrt(len(feature_vector))
    standard_error_B0 = standard_error_B1 * math.sqrt(sum(feature_vector ** 2) / len(feature_vector))

    TSS_train = sum((response_vector - Y_bar) ** 2)
    R2_train = 1 - (RSS_train / TSS_train)
    TSS_test = sum((response_vector_test - Y_bar_test) ** 2)
    R2_test = 1 - (RSS_test / TSS_test)
    return B0_hat, B1_hat, sigma2_hat, standard_error_B0, standard_error_B1, RSS_train, R2_train, RSS_test, R2_test


# Gets points of fitted line for plotting purpose
def get_points(line, B0, B1):
    points = []
    for i in line:
        points.append(B0 + B1 * i)
    return points
