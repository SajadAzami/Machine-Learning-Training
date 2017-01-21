"""Linear Regression, 1/21/17, Sajad Azami"""

import pandas as pd

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Reads train data from csv, returns pandas DF
def read_data(path):
    data = pd.read_csv(path, header=None)
    label = data.get(8)
    data = data.drop(8, axis=1)
    return data, label
