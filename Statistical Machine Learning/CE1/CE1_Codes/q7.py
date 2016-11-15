"""CE1_Codes, 11/15/16, Sajad Azami"""

import numpy as np
from matplotlib import pyplot
import seaborn as sns

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("whitegrid")


# Let Xi be random variables of N(0,1) and let Xn = 1/n(sum(Xi))
# We will plot Xn versus n for n = 1,...,10000
# We will do this for Xi being random variables of Cauchy
def simulate():
    # Xi be random variables of N(0,1)
    n = []
    Xn = []
    for i in range(1, 10001):
        X_i = np.random.normal(0, 1, i)
        Xn.append(1 / i * (np.sum(X_i)))
        n.append(i)
    pyplot.plot(n, Xn)
    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
