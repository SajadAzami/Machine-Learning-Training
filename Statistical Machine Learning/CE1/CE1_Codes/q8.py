"""CE1_Codes, 11/15/16, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import pyplot
from scipy import stats

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("whitegrid")


def simulate():
    x = np.linspace(stats.uniform.ppf(0), stats.uniform.ppf(1), 100)
    pyplot.plot(x, stats.uniform.pdf(x))
    # pyplot.show()
    x_i = []
    for i in range(1, 1000):
        x_i.append(np.random.uniform(0, 1))
    X_n = (1 / 1000) * (sum(x_i))
    print("Xn is : ", X_n)
    E_Xn = 0  # TODO Find Expectation of XN
    print("E(Xn) is : ", E_Xn)


def main():
    simulate()


if __name__ == '__main__':
    main()
