"""Linear Regression, 1/21/17, Sajad Azami"""

import data_preparation
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")


# Fits a line that minimizes Residual Sum of Errors
# The line is Yi = B0 + B1*Xi
# feature_vector and response_vector are numpy arrays
def rss_regressor(feature_vector, respones_vector):
    Y_bar = sum(respones_vector) / len(respones_vector)
    X_bar = sum(feature_vector) / len(feature_vector)
    B1_hat = sum((feature_vector - X_bar) * (respones_vector - Y_bar)) / sum((feature_vector - X_bar) ** 2)
    B0_hat = Y_bar - B1_hat * X_bar
    return B0_hat, B1_hat


def get_points(line, B0, B1):
    points = []
    for i in line:
        points.append(B0 + B1 * i)
    return points
