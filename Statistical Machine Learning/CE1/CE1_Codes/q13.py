"""CE1_Codes, 11/17/16, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("darkgrid")


def get_uniform():
    return np.random.uniform(0, 1)


def simulate():
    # X = Y1 - Y2
    X = []
    for i in range(0, 1000):
        Y1 = get_uniform()
        Y2 = get_uniform()
        X.append(Y1 - Y2)

    pyplot.subplot(211)
    pyplot.title('Y1 - Y2')
    n = np.linspace(1, 1000, 1000)
    pyplot.plot(n, X)

    # X = Y1Y2
    X = []
    for i in range(0, 1000):
        Y1 = get_uniform()
        Y2 = get_uniform()
        X.append(Y1 * Y2)

    pyplot.subplot(212)
    pyplot.title('Y1 * Y2')
    n = np.linspace(1, 1000, 1000)
    pyplot.plot(n, X)
    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
