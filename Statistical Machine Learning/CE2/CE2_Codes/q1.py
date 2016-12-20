"""CE2_Codes, 12/20/16, Sajad Azami"""

import numpy as np
import math
import statsmodels.api as sm
import scipy.stats

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
    print('A 95% Confidence Interval for F_hat of', x, 'is:', (L_x, U_x))
    print('True value for CDF of', x, '(which comes from N(0,1)is:', )


def main():
    normal_CDF_interval(100, 0)


if __name__ == '__main__':
    main()
