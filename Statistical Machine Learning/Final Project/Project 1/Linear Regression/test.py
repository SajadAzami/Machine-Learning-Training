"""Linear Regression, 1/25/17, Sajad Azami"""

import numpy as np

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

a = [1, 2, 3]
b = [4, 5, 6]
a = np.array(a)
b = np.array(b)
print(a)
a = a.reshape(1, len(a))
b = b.reshape(1, 3)

print(a)
print(a.shape)
print(b.shape)
con = np.concatenate((a, b), axis=0)
print(con.shape)
