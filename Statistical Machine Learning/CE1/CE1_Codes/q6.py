"""CE1_Codes, 11/15/16, Sajad Azami"""

import math

import numpy as np
import seaborn as sns
from matplotlib import pyplot
from scipy.stats import norm

sns.set_style("whitegrid")

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


def normal_dist(x): (1 / math.sqrt(math.pi * 2 * 1)) * math.exp(-((x - 0) ** 2) / 2 * 1)


# X = N(5,18), Finding the PDF and CDF and some probability
def simulate():
    line = np.linspace(-100, 100, 201)
    X = norm.pdf(line, loc=5, scale=18)

    # Plotting the PDF and CDF of N(5,18) over the range of (-100, 100)
    pyplot.subplot(211)
    pyplot.plot(line, X)
    pyplot.title('PDF')
    CDF = np.cumsum(X)
    pyplot.subplot(212)
    pyplot.title('CDF')
    pyplot.plot(line, CDF)
    pyplot.show()

    # 1. P(X<8)
    print('P(X<8): ', norm.cdf(8, loc=5, scale=18))

    # 2. P(X>-2)
    print('P(X>-2): ', 1 - norm.cdf(-2, loc=5, scale=18))

    # 3. x such that P(X>x) = 0.05
    print('x such that P(X>x) = 0.05: ', norm.ppf(0.95, loc=5, scale=18))

    # 4. P(0<=X<4)
    print('P(0<=X<4: ', norm.cdf(4, loc=5, scale=18) - norm.cdf(0, loc=5, scale=18))

    # 5. x such that P(abs(X) > abs(x)) = 0.05
    print('x such that P(abs(X) > abs(x)) = 0.05: ', norm.ppf(0.975, loc=5, scale=18))


def main():
    simulate()


if __name__ == '__main__':
    main()
