"""CE1_Codes, 11/18/16, Sajad Azami"""

import numpy as np

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


def get_sample_covariance(x_1: list, x_2: list):
    if len(x_1) != len(x_2):
        print('Lenghts are not equal')
        return
    x_1_mean = (1 / len(x_1)) * (sum(x_1))
    x_2_mean = (1 / len(x_2)) * (sum(x_2))
    sum_of_values = 0
    for i in range(0, len(x_1)):
        sum_of_values += (x_1[i] - x_1_mean) * (x_2[i] - x_2_mean)
    return (1 / (len(x_1) - 1)) * sum_of_values


def simulate():
    X1 = []
    X2 = []
    for i in range(0, 1000):
        X1.append(np.random.normal(loc=0, scale=1 / 3))
        X2.append(np.random.normal(loc=0, scale=1 / 2))
    X1_sample_mean = (1 / 1000) * (sum(X1))
    X2_sample_mean = (1 / 1000) * (sum(X2))
    print('X1 Sample Mean: ', X1_sample_mean)
    print('X2 Sample Mean: ', X2_sample_mean)
    print('Sample Cov(X1,X2): ', get_sample_covariance(X1, X2))


def main():
    simulate()


if __name__ == '__main__':
    main()
