"""Time Series Analysis, 2/8/17, Sajad Azami"""

import numpy as np
import seaborn as sns
from matplotlib import gridspec
import matplotlib.pyplot as plt
import random
import pandas as pd
import data_preparation
from arch import arch_model
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("darkgrid")

# Load dataset
data_set = data_preparation.read_data('./data_set/HourlyDemands_2002-2016.csv')
data, label = data_preparation.split_label(data_set, 'Ontario Demand')
print('Data set Loaded!')
print(data.shape)
print(label.shape)
# Plot 200 data point
line = np.linspace(0, 200, 200)
plt.plot(line, label[0:200])
plt.show()
