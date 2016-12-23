"""CE2_Codes, 12/23/16, Sajad Azami"""

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


# Simulation of bootsrap sampling
def bootstrap(samples):
    return np.random.choice(samples, len(samples))


def standard_error(bootstrapped_samples):
    count = 0
    for i in range(0, len(bootstrapped_samples)):
        count += bootstrapped_samples[i]
    mean = count / len(bootstrapped_samples)
    variance = 0
    for i in range(0, len(bootstrapped_samples)):
        variance += (bootstrapped_samples[i] - mean) ** 2
    variance /= len(bootstrapped_samples)
    se = math.sqrt(variance)
    return se


# Reads data
def read_data():
    return pd.read_csv('./data/Earthquakes.txt')


def CDF_estimator(data):
    # Bootsrapping 1000 times
    # Also creating the theta_star each time, for third part of question
    bootstrapped_samples = []
    theta_star = []
    for i in range(0, 1000):
        temp = bootstrap(data['mag'].values)
        temp_ecdf = ECDF(temp)
        theta_star.append(temp_ecdf(4.9) - temp_ecdf(4.3))
        bootstrapped_samples.extend(temp)
    # Estimated Empirical CDF
    ecdf = ECDF(bootstrapped_samples)

    line = np.linspace(3.5, 6.5, 1000)
    ecdf_points = []
    for i in line:
        ecdf_points.append(ecdf(i))
    plt.plot(line, ecdf_points)

    # Creating the confidence band
    epsilon = math.sqrt((1 / (2 * len(data)) * math.log10(2 / 0.05)))
    lower_band_points = []
    upper_band_points = []
    for x in line:
        lower_band_points.append(max(ecdf(x) - epsilon, 0))
    for x in line:
        upper_band_points.append(min(ecdf(x) + epsilon, 1))
    plt.title('Red: Lower CB | Green: Upper CB')
    plt.plot(line, lower_band_points, color='red')
    plt.plot(line, upper_band_points, color='green')
    plt.show()

    # Computing 3 types of CI for F(4.9) - F(4.3)
    # Normal:
    se = standard_error(theta_star)
    theta_hat = ecdf(4.9) - ecdf(4.3)
    normal_CI = (theta_hat - 1.96 * se, theta_hat + 1.96 * se)
    print('Normal Interval:', normal_CI)
    # Percentile
    percentile_CI = (np.percentile(theta_star, 0.025), np.percentile(theta_star, 97.5))
    print('Percentile Interval:', percentile_CI)
    # Pivotal
    pivotal_CI = (2 * theta_hat - np.percentile(theta_star, 97.5)
                  , 2 * theta_hat + np.percentile(theta_star, 0.025))
    print('Pivotal Interval:', pivotal_CI)


def main():
    data = read_data()
    CDF_estimator(data)


if __name__ == '__main__':
    main()
