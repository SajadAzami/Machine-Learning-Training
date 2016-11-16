"""CE1_Codes, 11/16/16, Sajad Azami"""

import random

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Finding probability of two or more students having birthday of jan 1st in a group of 28 students
def simulate():
    count = 0
    for j in range(0, 10000):
        birthdays = []
        for i in range(0, 28):
            birthdays.append(random.randint(1, 365))
        if 1 in birthdays:
            count += 1
    print(count / 10000)


def main():
    simulate()


if __name__ == '__main__':
    main()
