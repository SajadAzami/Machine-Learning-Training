"""Linear Regression, 1/21/17, Sajad Azami"""

import pandas as pd

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'


# Reads train data from csv, returns pandas DF
def read_data(path):
    data = pd.read_csv(path, header=None, index_col=False)
    return data


# Reads train data from csv, returns pandas DF
def split_label(df, label_index):
    label = df.get(label_index)
    data = df.drop(label_index, axis=1)
    return data, label
