"""CE1_Codes, 11/18/16, Sajad Azami"""

import numpy as np

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# The result should be approximately 1/16, but it is almost zero
def simulate(n, p, eps):
    count = 0
    for i in range(0, n):
        X = np.random.binomial(1, p, 100)
        X_n = (1 / 100) * (sum(X))
        if abs(X_n - p) > eps:
            count += 1
    print(count / n)


def main():
    simulate(100, 0.3, 0.2)
    simulate(100, 0.5, 0.2)


if __name__ == '__main__':
    main()
