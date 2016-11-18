"""CE1_Codes, 11/18/16, Sajad Azami"""

import numpy as np
from scipy import stats
import seaborn as sns
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("darkgrid")


# Comparing Binomial(100,0.6) with Poisson(6)
def simulate():
    x = np.arange(stats.poisson.ppf(0.01, 6),
                  stats.poisson.ppf(0.99, 6))
    binomial = np.random.binomial(1, 0.06, 100)
    n = np.linspace(0, 100, 100)
    poisson = stats.poisson.pmf(x, 6)
    pyplot.subplot(211)
    pyplot.plot(n, binomial)
    pyplot.subplot(212)
    pyplot.plot(x, poisson)
    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
