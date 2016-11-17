"""CE1_Codes, 11/18/16, Sajad Azami"""

import numpy as np
import math

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


def simulate():
    error_sum = 0
    for i in range(0, 10000):
        X = np.random.normal(loc=0, scale=1)
        Y = np.random.normal(loc=0, scale=1)
        error_sum += math.sqrt(math.pow(X, 2) + math.pow(Y, 2))
    print('Average Distance is:', error_sum / 10000)


def main():
    simulate()


if __name__ == '__main__':
    main()
