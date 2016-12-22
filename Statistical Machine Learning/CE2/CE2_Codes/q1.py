"""CE2_Codes, 12/20/16, Sajad Azami"""

import numpy as np
import math
from statsmodels.distributions.empirical_distribution import ECDF
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


# Simulation of bootsrap sampling
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
        return

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
    real_values = []
    if dist == 'Normal':
        real_values = st.norm.cdf(line)
    elif dist == 'Cauchy':
        real_values = st.cauchy.cdf(line)
    plt.subplot(211)
    plt.title('Blue: ECDF | Black: CDF ' + dist)
    plt.plot(line, ecdf_points)
    plt.plot(line, real_values, color='black')

    # Creating the confidence band
    epsilon = math.sqrt((1 / (2 * 100) * math.log10(2 / 0.05)))
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
    plt.plot(line, real_values, color='black')
    plt.show()

    # Computing how many times the CB contains the true value
    count = 0
    for i in range(0, len(line)):
        if lower_band_points[i] <= real_values[i] <= upper_band_points[i]:
            pass
        else:
            count += 1
    print(count, 'times Confidence Band does not contain the true value from ', len(line), 'points')


# Simulating confidence band
def main():
    CDF_band(100, 'Normal')
    CDF_band(100, 'Cauchy')


if __name__ == '__main__':
    main()
