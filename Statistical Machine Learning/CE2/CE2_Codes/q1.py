"""CE2_Codes, 12/20/16, Sajad Azami"""

import numpy as np
import math
from statsmodels.distributions.empirical_distribution import ECDF
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


def bootstrap(samples):
    return np.random.choice(samples, 100)


# Computing a 95% Confidence Band for the CDF F, with n observation of distributin 'dist'
def CDF_band(n_samples, dist):
    samples = []
    if dist == 'Normal':
        for i in range(0, n_samples):
            samples.append(np.random.normal(0, 1))
    elif dist == 'Cauchy':
        samples = np.random.standard_cauchy(n_samples)
    else:
        print('Wrong distribution!')

    # Now we bootstrap 100 samples 1000 times
    bootstraped_samples = []
    for i in range(0, 1000):
        bootstraped_samples.extend(bootstrap(samples))
    # Adding the original samples
    bootstraped_samples.extend(samples)

    # Estimated Empirical CDF
    ecdf = ECDF(bootstraped_samples)

    line = np.linspace(-5, 5, 1000)
    ecdf_points = []
    for i in line:
        ecdf_points.append(ecdf(i))
    plt.subplot(211)
    plt.title('Blue: ECDF | Red: CDF ' + dist)
    plt.plot(line, ecdf_points)
    plt.plot(line, st.norm.cdf(line), color='red')

    # Creating the confidence band
    epsilon = math.sqrt((1 / (2 * len(bootstraped_samples)) * math.log10(2 / 0.05)))
    lower_band_points = []
    upper_band_points = []
    for x in line:
        lower_band_points.append(max(ecdf(x) - epsilon, 0))
    for x in line:
        upper_band_points.append(min(ecdf(x) + epsilon, 1))
    plt.subplot(212)
    plt.title('Red: Lower CB | Green: Upper CB')
    plt.plot(line, lower_band_points, color='red')
    plt.plot(line, upper_band_points, color='green')
    plt.show()


# Computing a 95% Confidence Band for the CDF F, with n Cauchy observation
def cauchy_CDF_band(n_samples, x):
    samples = np.random.standard_cauchy(n_samples)
    epsilon = math.sqrt((1 / (2 * n_samples) * math.log10(2 / 0.05)))

    ecdf = ECDF(samples)
    print(type(ecdf))
    L_x = max(ecdf(x) - epsilon, 0)
    U_x = min(ecdf(x) + epsilon, 1)
    real_value = st.cauchy.cdf(x)
    # print('A 95% Confidence Interval for F_hat of', x, 'is:', (L_x, U_x))
    # print('Real value for CDF of', x, '(which comes from N(0,1)is:', real_value)
    return L_x, U_x, real_value


# Simulating confidence band
def main():
    CDF_band(100, 'Normal')
    CDF_band(100, 'Cauchy')


if __name__ == '__main__':
    main()
