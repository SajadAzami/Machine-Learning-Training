"""CE2_Codes, 12/20/16, Sajad Azami"""

import numpy as np
import math
import statsmodels.api as sm
import scipy.stats as st

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Computing a 95% Confidence Interval for the CDF F, with n Normal observation
def normal_CDF_interval(n_samples, x):
    samples = []
    for i in range(0, n_samples):
        samples.append(np.random.normal(0, 1))
    epsilon = math.sqrt((1 / (2 * n_samples) * math.log10(2 / 0.05)))

    ecdf = sm.distributions.ECDF(samples)
    L_x = max(ecdf(x) - epsilon, 0)
    U_x = min(ecdf(x) + epsilon, 1)
    real_value = st.norm.cdf(x)
    # print('A 95% Confidence Interval for F_hat of', x, 'is:', (L_x, U_x))
    # print('Real value for CDF of', x, '(which comes from N(0,1)is:', real_value)
    return L_x, U_x, real_value


# Computing a 95% Confidence Interval for the CDF F, with n Cauchy observation
def cauchy_CDF_interval(n_samples, x):
    samples = np.random.standard_cauchy(n_samples)
    epsilon = math.sqrt((1 / (2 * n_samples) * math.log10(2 / 0.05)))

    ecdf = sm.distributions.ECDF(samples)
    L_x = max(ecdf(x) - epsilon, 0)
    U_x = min(ecdf(x) + epsilon, 1)
    real_value = st.cauchy.cdf(x)
    # print('A 95% Confidence Interval for F_hat of', x, 'is:', (L_x, U_x))
    # print('Real value for CDF of', x, '(which comes from N(0,1)is:', real_value)
    return L_x, U_x, real_value


# Simulating confidence band calculation 1000 times
def main():
    contains = 0
    for i in range(0, 1000):
        result = normal_CDF_interval(100, 1)
        real_value = result[2]
        U = result[1]
        L = result[0]
        if L <= real_value <= U:
            contains += 1
    print('Normal: ', contains / 1000)

    contains = 0
    for i in range(0, 1000):
        result = cauchy_CDF_interval(100, 0)
        real_value = result[2]
        U = result[1]
        L = result[0]
        if L <= real_value <= U:
            contains += 1
    print('Cauchy: ', contains / 1000)


if __name__ == '__main__':
    main()
