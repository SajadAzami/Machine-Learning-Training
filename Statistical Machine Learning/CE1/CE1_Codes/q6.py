"""CE1_Codes, 11/15/16, Sajad Azami"""

from scipy.stats import norm
import numpy as np
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# X = N(5,18), Finding the PDF and CDF and some probability
def simulate():
    line = np.linspace(-100, 100, 200)
    X = norm.pdf(line, loc=5, scale=18)
    pyplot.plot(line, X)
    # pyplot.show()

    CDF = np.cumsum(X)
    pyplot.plot(line, CDF)
    # pyplot.show()

    # 1. P(X<8)
    print(CDF[108])


def main():
    simulate()


if __name__ == '__main__':
    main()
