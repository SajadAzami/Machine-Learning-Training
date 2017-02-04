"""PGM, 2/1/17, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt
import random
import data_preparation

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

cleveland = data_preparation.read_data('./data_set/processed.cleveland.data.txt')
hungarian = data_preparation.read_data('./data_set/processed.hungarian.data.txt')
switzerland = data_preparation.read_data('./data_set/processed.switzerland.data.txt')
va = data_preparation.read_data('./data_set/processed.va.data.txt')
print('Data set Loaded!')
