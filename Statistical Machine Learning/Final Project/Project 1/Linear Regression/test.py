"""Linear Regression, 1/25/17, Sajad Azami"""

import operator

stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
print(max(stats.keys(), key=(lambda k: stats[k])))