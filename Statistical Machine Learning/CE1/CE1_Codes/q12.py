"""CE1_Codes, 11/16/16, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("darkgrid")


# Calculates the Xn = (1/n)*(sum(x_i))
def get_xn(n):
    x_i = []
    for i in range(0, n):
        x_i.append(np.random.normal(loc=0, scale=1))
    X_n = (1 / n) * (sum(x_i))
    return X_n


def simulate():
    n = np.linspace(1, 1000, 1000)
    X_ns = []

    for i in range(1, 1001):
        X_ns.append(get_xn(i))
    pyplot.title('f(n,Xn)')
    pyplot.plot(n, X_ns, '-g')
    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
