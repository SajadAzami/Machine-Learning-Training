"""CE1_Codes, 11/4/16, Sajad Azami"""

import random
from matplotlib import pyplot

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Simulating N flips of a coin with p probability of heads.

# Flipping a coin with p probability of heads
def flip(p):
    return 'H' if random.random() < p else 'T'


# Flipping the coin N times and plotting the proportion of heads as a function of N
def simulate(flip_number, h_probability):
    count = 0
    point_list = []
    for i in range(1, flip_number):
        if flip(h_probability) == 'H':
            count += 1
        point_list.append(count)

    pyplot.plot(range(1, flip_number), point_list)
    pyplot.axis([-100, 1200, -100, 500])
    pyplot.xlabel('Flips')
    pyplot.ylabel('Heads')
    pyplot.show()


def main():
    simulate(1000, 0.3)
    simulate(1000, 0.03)


if __name__ == '__main__':
    main()
