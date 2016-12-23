"""CE2_Codes, 12/23/16, Sajad Azami"""
import math

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

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
    return se, mean


def simulate():
    # Generating 100 N(10,1)
    Xi = []
    theta = []
    for i in range(0, 100):
        temp = np.random.normal(loc=10, scale=1)
        Xi.append(temp)
    se, mean = standard_error(Xi)
    line = np.linspace(-0, 20, 10000)
    scale_pdf = (se ** 2)
    pdf_values = st.norm.pdf(line, mean, scale_pdf)
    plt.subplot(211)
    plt.title('Posterior Density')
    plt.plot(line, pdf_values)

    simulated_from_posterior = []
    for i in range(0, 1000):
        simulated_from_posterior.append(np.random.normal(mean, scale_pdf))
    plt.subplot(212)
    plt.hist(simulated_from_posterior)
    plt.title('1000 Simulate Draws from Posterior')
    plt.show()
    # Part d, e, f
    for i in range(0, 100):
        temp = bootstrap(Xi)
        miu = sum(temp) * 1 / len(temp)
        theta.append(math.exp(miu))
    plt.hist(theta)
    plt.show()
    theta_hat = math.exp(sum(Xi) * 1 / len(Xi))
    # Percentile
    percentile_CI = (np.percentile(theta, 0.025), np.percentile(theta, 97.5))
    print('Percentile Interval:', percentile_CI)
    # Pivotal
    pivotal_CI = (2 * theta_hat - np.percentile(theta, 97.5)
                  , 2 * theta_hat - np.percentile(theta, 0.025))
    print('Pivotal Interval:', pivotal_CI)


def main():
    simulate()


if __name__ == '__main__':
    main()
