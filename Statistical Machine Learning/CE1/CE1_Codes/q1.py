"""CE1_Codes, 11/4/16, Sajad Azami"""

import random

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

# Q1: Monty Hall Problem

# Experiment without changing the selected door
not_changing_win_count = 0
for i in range(1, 1000):
    selected_door = random.randint(1, 3)
    prize_door = random.randint(1, 3)
    if selected_door == prize_door:
        not_changing_win_count += 1

print('Probability Without Changing the Selected Door: ', not_changing_win_count / 1000)

# Experiment with changing the selected door
changing_win_count = 0
for j in range(1, 1000):
    door_set = [1, 2, 3]
    selected_door = random.randint(1, 3)
    prize_door = random.randint(1, 3)

    # Opening one of empty doors, which is not selected
    door_set.remove(selected_door)
    if selected_door != prize_door:
        door_set.remove(prize_door)

    opened_door = random.sample(door_set, 1)
    choice_set = [1, 2, 3]
    choice_set.remove(selected_door)
    choice_set.remove(opened_door.pop())
    if choice_set.pop() == prize_door:
        changing_win_count += 1

print('Probability With Changing the Selected Door: ', changing_win_count / 1000)
