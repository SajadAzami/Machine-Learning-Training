"""CE1_Codes, 11/4/16, Sajad Azami"""

import random

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# N coin flips with probability of p

# Flipping a coin with p probability of heads
def flip(p):
    return 'H' if random.random() < p else 'T'


# Flipping the coin N times and comparing the number of heads with np
def simulate(flip_number, h_probability):
    count = 0
    for i in range(1, flip_number):
        if flip(h_probability) == 'H':
            count += 1
    print('Coin Flips: ', flip_number)
    print('Probability of Heads: ', h_probability)
    print('np - head_count: ', int(flip_number * h_probability - count))
    print()


def main():
    simulate(10, 0.3)
    simulate(100, 0.03)
    simulate(1000, 0.03)


if __name__ == '__main__':
    main()
