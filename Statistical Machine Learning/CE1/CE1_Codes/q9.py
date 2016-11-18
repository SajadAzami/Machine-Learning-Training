"""CE1_Codes, 11/16/16, Sajad Azami"""

import random

import seaborn as sns
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

sns.set_style("white")


# Rolling a biased die, P(6) = 1/4, P(others) = 3/20
def roll():
    rand = random.randint(1, 20)
    if rand <= 5:
        return 6
    if 8 >= rand >= 6:
        return 5
    if 11 >= rand >= 9:
        return 4
    if 14 >= rand >= 12:
        return 3
    if 17 >= rand >= 15:
        return 2
    if 20 >= rand >= 18:
        return 1


# Simulating rolling a biased die
def simulate():
    rolled = []
    for i in range(0, 10):
        rolled.append(roll())
    pyplot.subplot(221)
    pyplot.title('Biased Die Histogram')
    pyplot.hist(rolled, range=[0, 7], align='mid')

    pyplot.subplot(222)
    pyplot.title('Normalized Histogram')
    pyplot.hist(rolled, range=[0, 7], color='red', align='mid', normed=True)

    pyplot.subplot(223)
    pyplot.title('Normed and PDF Histogram Together')
    pyplot.hist(rolled, range=[0, 7], align='mid', normed=True)
    pyplot.hist(rolled, range=[0, 7], color='green', align='mid', alpha=0.5)

    pyplot.show()


def main():
    simulate()


if __name__ == '__main__':
    main()
