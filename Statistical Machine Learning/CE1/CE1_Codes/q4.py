"""CE1_Codes, 11/4/16, Sajad Azami"""

import random

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Rolling a die
def roll():
    return random.randint(1, 6)


# Rolling a die N times
def simulate(roll_number):
    A = [2, 3, 6]
    B = [1, 2, 3, 4]
    A_count = 0
    B_count = 0
    AB_count = 0
    for i in range(0, roll_number):
        rolled = roll()
        if rolled in A:
            A_count += 1
        if rolled in B:
            B_count += 1
        if rolled in A and rolled in B:
            AB_count += 1
    pAB = AB_count / roll_number
    pA = A_count / roll_number
    pB = B_count / roll_number
    print("P(A): ", pA)
    print("P(B): ", pB)
    print("P(AB): ", pAB)
    print(pA * pB)
    print(pA * pB == pAB)


# Defining two sets and verify independence
def main():
    simulate(10000)


if __name__ == '__main__':
    main()
