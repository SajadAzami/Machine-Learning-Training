"""Linear Regression, 1/21/17, Sajad Azami"""

import pandas as pd

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Reads train data from csv, returns pandas DF
def read_data(path, label_index):
    data = pd.read_csv(path, header=None)
    label = data.get(label_index)
    data = data.drop(label_index, axis=1)
    return data, label
