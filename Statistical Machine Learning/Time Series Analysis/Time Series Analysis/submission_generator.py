"""Time Series Analysis, 2/11/17, Sajad Azami"""

import pandas as pd
import numpy as np

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

df = pd.DataFrame({'Date': [1, 2, 3], 'Hour': [4, 5, 6], 'Demand': [7, 8, 9]})
print(df)


def generate(arr):
    hours = []
    date = []
    day_counter = 1
    hour_counter = 1
    month = 'Jan'
    for i in range(0, len(arr)):
        if day_counter == 31:
            day_counter = 1
            month = 'Feb'
        if hour_counter == 25:
            day_counter += 1
        if hour_counter == 25:
            hour_counter = 1
        date.append(str(day_counter) + '-' + month + '-17')
        hours.append(hour_counter)
        hour_counter += 1
    print(type(date))
    print(type(hours))
    print(type(arr))
    # arr_int = arr.astype(int)
    # print(arr.tolist())
    df = pd.DataFrame({'Date': date, 'Hour': hours, 'Demand': arr})
    print(df)
    df.to_csv('2017_predictions.csv', index=False)
