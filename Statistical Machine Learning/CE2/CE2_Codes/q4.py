"""CE2_Codes, 12/23/16, Sajad Azami"""
import math

import numpy as np
import seaborn as sns

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


# Simulation of bootsrap sampling
def bootstrap(samples):
    return np.random.choice(samples, len(samples))


def get_skewness(bootstrapped_samples):
    # Computing the skewness
    mean = sum(bootstrapped_samples) / len(bootstrapped_samples)
    sum_of_l3 = 0
    for i in range(0, len(bootstrapped_samples)):
        sum_of_l3 += (bootstrapped_samples[i] - mean) ** 3
    se = standard_error(bootstrapped_samples)
    return (1 / len(bootstrapped_samples)) * sum_of_l3 / (se ** 3)


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


# Compares 3 methods of bootsrap confidence intervals
def CI_compare():
    Yi = []
    Xi = []
    for i in range(0, 50):
        temp = np.random.normal()
        Yi.append(temp)
        Xi.append(math.exp(temp))

    # Simulating the bootsrap
    bootstrapped_samples = []
    theta_star = []
    for i in range(0, 1000):
        temp = bootstrap(Xi)
        bootstrapped_samples.extend(temp)
        theta_star.append(get_skewness(temp))
    # Constructing the Confidene Intervals
    theta_hat = get_skewness(bootstrapped_samples)
    # print(theta_hat)
    se = standard_error(bootstrapped_samples)
    normal_CI = (theta_hat - 1.96 * se, theta_hat + 1.96 * se)
    # print('Normal Interval:', normal_CI)
    # Percentile
    percentile_CI = (np.percentile(theta_star, 0.025), np.percentile(theta_star, 97.5))
    # print('Percentile Interval:', percentile_CI)
    # Pivotal
    pivotal_CI = (2 * theta_hat - np.percentile(theta_star, 97.5)
                  , 2 * theta_hat + np.percentile(theta_star, 0.025))
    # print('Pivotal Interval:', pivotal_CI)
    return normal_CI, percentile_CI, pivotal_CI


def main():
    normal_l = 0
    normal_u = 0
    percentile_l = 0
    percentile_u = 0
    pivotal_l = 0
    pivotal_u = 0
    for i in range(0, 500):
        normal_CI, percentile_CI, pivotal_CI = CI_compare()
        normal_l += normal_CI[0]
        normal_u += normal_CI[1]
        percentile_l += percentile_CI[0]
        percentile_u += percentile_CI[1]
        pivotal_l += pivotal_CI[0]
        pivotal_u += pivotal_CI[1]
    print('Normal CI converges to:', (normal_l / 500, normal_u / 500))
    print('Percentile CI converges to:', (percentile_l / 500, percentile_u / 500))
    print('Pivotal CI converges to:', (pivotal_l / 500, pivotal_u / 500))


if __name__ == '__main__':
    main()
