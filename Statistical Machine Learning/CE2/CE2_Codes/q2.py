"""CE2_Codes, 12/21/16, Sajad Azami"""

import math

import numpy as np
import pandas as pd
import seaborn as sns

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("whitegrid")


# Simulation of bootsrap sampling
def bootstrap(samples):
    return np.random.choice(samples, len(samples))


# Prepares data for processing
def prepare_data(PATH):
    data = []
    with open(PATH, 'r') as f:
        index = 0
        for line in f:
            if index >= 25:
                line = line.replace('\n', '') \
                           .replace('\r', '') \
                           .replace('       ', ',') \
                           .replace('      ', ',').replace('     ', ',') + '\n'
                data.append(line)
            index += 1
    new_f = open('./data/Old Faithful Geyser Data Cleaned.csv', 'w')
    data[0] = 'id,eruptions,waiting\n'
    for i in range(0, len(data)):
        new_f.write(data[i])
    new_f.close()


# Reads data
def read_data():
    return pd.read_csv('./data/Old Faithful Geyser Data Cleaned.csv')


# Estimates the mean waiting time and se of the estimation, and a 90% Confidence Interval
def mean_estimator(data):
    bootstrapped_samples = []
    for i in range(0, 1000):
        bootstrapped_samples.extend(bootstrap(data['waiting'].values))
    # Calculating estimated mean with plug-in estimator 1/n sum(Xi)
    count = 0
    for i in range(0, len(bootstrapped_samples)):
        count += bootstrapped_samples[i]
    mean = count / len(bootstrapped_samples)

    # Calculating standard error sqrt(1/n sum((Xi - mean)^2)) / sqrt(n)
    variance = 0
    for i in range(0, len(bootstrapped_samples)):
        variance += (bootstrapped_samples[i] - mean) ** 2
    variance /= len(bootstrapped_samples)
    se = math.sqrt(variance)
    print('Estimated Mean: ', mean)
    print('Standard Error: ', se)

    # Now calculating a 90% confidence interval
    critical_value = 1.645
    confidence_interval = (mean - (se * critical_value), mean + (se * critical_value))
    print('90% Confidence Interval for estimated mean:', confidence_interval)


def main():
    data = read_data()
    data = data.drop('id', axis=1)
    mean_estimator(data)


if __name__ == '__main__':
    main()
