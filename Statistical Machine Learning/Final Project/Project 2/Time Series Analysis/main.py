"""Time Series Analysis, 2/8/17, Sajad Azami"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.tools.plotting import autocorrelation_plot
from pandas.tools.plotting import lag_plot
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.ar_model import AR

import data_preparation

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'
sns.set_style("dark")

# Load dataset
data_set = data_preparation.read_data('./data_set/HourlyDemands_2002-2016.csv')
data, label = data_preparation.split_label(data_set, 'Ontario Demand')
print('Data set Loaded!')
print(data.shape)
print(label.shape)

# Plot 2 weeks of data points
line = np.linspace(0, 336, 336)
plt.plot(line, label[0:336])
plt.xlabel('Hour')
plt.ylabel('Power Demand')
plt.title('Power Demand of first 14 days')
plt.show()
lag_plot(label)

# Plotting the lag plot of target feature
plt.title('Lag plot of Power Demand')
plt.xlabel('P(t)')
plt.ylabel('P(t+1)')
plt.show()

# Plotting auto-correlation
autocorrelation_plot(label[0:1000])
plt.show()

# Splitting train and test data
train_data, test_data = data[0:119832], data[119832:]
train_label, test_label = label[0:119832], label[119832:]

# Implementing Persistence Model
df = pd.concat([label.shift(48), label], axis=1)
df.columns = ['t-1', 't+1']
X = df.values
train, test = X[0:119832], X[119832:]
train_X, train_y = train[:, 0], train[:, 1]
test_X, test_y = test[:, 0], test[:, 1]


# Persistence model
def model_persistence(x):
    return x


# Walk-forward validation
predictions = list()
for x in test_X:
    y_hat = model_persistence(x)
    predictions.append(y_hat)
test_score = mean_absolute_error(test_y, predictions)
print('Test MAE: %.3f' % test_score)
# plot predictions vs expected
plt.plot(test_y, label="real values")
plt.plot(predictions, color='red', label="predictions")
plt.legend(loc='upper left')
plt.show()


# Implementing Auto Regression Model
# Training Autoregression
print(train[:, 1])
model = AR(train_y)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)

# Making predictions
predictions = model_fit.predict(start=len(train_y), end=len(train_y) + len(test_y) - 1, dynamic=False)
# for i in range(len(predictions)):
#     print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_absolute_error(test_y, predictions)
print('Test MAE: %.3f' % error)

# Plotting results
plt.plot(test_y, label="real values")
plt.plot(predictions, color='red', label="predictions")
plt.legend(loc='upper left')

plt.show()
