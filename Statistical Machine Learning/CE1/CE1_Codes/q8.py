"""CE1_Codes, 11/15/16, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import pyplot
from scipy import stats

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("darkgrid")


# Calculates the Xn = (1/n)*(sum(x_i))
def get_xn(n):
    x_i = []
    for i in range(0, n):
        x_i.append(np.random.uniform(0, 1))
    X_n = (1 / n) * (sum(x_i))
    return X_n


def simulate():
    # Plotting the PDF of Unif(0, 1)
    pyplot.subplot(211)
    x = np.linspace(stats.uniform.ppf(0), stats.uniform.ppf(1), 100)
    pyplot.title('PDF of Unif(0, 1)')
    pyplot.plot(x, stats.uniform.pdf(x))

    print("Xn is for n=1000: ", get_xn(1000))
    E_Xn = 0.5  # As we know, E(Xn) is equal to mu which is 0.5
    print("E(Xn) is : ", E_Xn)

    n = np.linspace(1, 1000, 1000)
    X_ns = []
    for i in range(1, 1001):
        X_ns.append(get_xn(i))
    pyplot.subplot(212)
    pyplot.title('f(n,Xn)')
    pyplot.plot(n, X_ns, '-g')

    print("Xn for n=1", get_xn(1))
    print("Xn for n=5", get_xn(5))
    print("Xn for n=25", get_xn(25))
    print("Xn for n=100", get_xn(100))

    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
