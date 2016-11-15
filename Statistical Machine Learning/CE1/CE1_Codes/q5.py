"""CE1_Codes, 11/4/16, Sajad Azami"""
# TODO Correct the answer
import pylab
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# X has distribution N(0,1), let Y = exp(X)
# In part a, we will plot the PDF of Y
# Then, we will create vector Xi which is 10000 random x of N(0,1)
# and Yi which is exp(Xi). Then we will plot the histogram of y
# Compare this to PDF we plotted in part a
def simulate():
    # Part a
    x = np.linspace(-10, 10, 100000)
    y = np.random.normal(0, 1, 100000)
    z = np.exp(y)
    pylab.plot(x, np.exp(y))
    pylab.show()

    # Part b
    x = []  # Xi Vector
    y = []  # Yi Vector
    for i in range(0, 1000):
        x.append(np.random.normal(0, 1))
        y.append(np.exp(x))
        print(i)

    plt.hist(y)
    plt.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
