"""CE2_Codes, 12/20/16, Sajad Azami"""

import math

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


def variance_mean(samples):
    count = 0
    for i in range(0, len(samples)):
        count += samples[i]
    mean = count / len(samples)
    variance = 0
    for i in range(0, len(samples)):
        variance += (samples[i] - mean) ** 2
    variance /= len(samples)
    return variance, mean


def get_skewness(samples):
    # Computing the skewness
    mean = sum(samples) / len(samples)
    sum_of_l3 = 0
    for i in range(0, len(samples)):
        sum_of_l3 += (samples[i] - mean) ** 3
    variance, mean = variance_mean(samples)
    return (1 / len(samples)) * sum_of_l3 / (variance ** 3 / 2)


# Computing a 95% Confidence Band for the CDF F, with n observation of distributin 'dist'
def CDF_band(n_samples):
    samples = np.random.standard_cauchy(n_samples)
    # Estimated Empirical CDF
    ecdf = ECDF(samples)
    line = np.linspace(-20, 20, 100000)
    ecdf_points = []
    for i in line:
        ecdf_points.append(ecdf(i))
    plt.plot(line, ecdf_points)
    plt.show()
    variance, mean = variance_mean(samples)
    skewness = get_skewness(samples)
    # Plugin Mean
    print('Plugin Estimator for Mean is:', mean)
    # Plugin Variance
    print('Plugin Estimator for Variance is:', variance)
    # Plugin Skewness
    print('Plugin Estimator for Skewness is:', skewness)


# Simulating confidence band
def main():
    CDF_band(100)


if __name__ == '__main__':
    main()
