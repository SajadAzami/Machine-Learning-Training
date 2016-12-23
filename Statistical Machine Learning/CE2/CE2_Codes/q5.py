"""CE2_Codes, 12/23/16, Sajad Azami"""
import math

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")


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
    return se, mean


def simulate():
    # Generating 100 N(10,1)
    Xi = []
    for i in range(0, 100):
        temp = np.random.normal(loc=10, scale=1)
        Xi.append(temp)
    # Computing a 95% normal CI for miu
    bootstrapped_samples = []
    theta_star = []
    for i in range(0, 1000):
        temp = bootstrap(Xi)
        theta_star.append(math.exp(1 / len(temp) * sum(temp)))
        bootstrapped_samples.extend(temp)
    se, mean = standard_error(theta_star)
    normal_CI = (mean - 1.96 * se, mean + 1.96 * se)
    print('Normal Confidence Interval:', normal_CI)
    plt.hist(theta_star)
    plt.axvline(x=math.exp(1 / len(Xi) * sum(Xi)), ymin=0, ymax=300, linewidth=2, color='red')
    plt.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
