import decimal
import numpy as np
from sklearn.linear_model import LinearRegression

def float_range(start, stop, step): # Use np.linspace()
  range_list = []
  while start < stop:
    range_list.append(start)
    start += float(decimal.Decimal(step))
  return range_list

"""RESEARCH LINEAR REGRESSION"""

def axes_data(list_of_data):
  return np.array(list_of_data)
  
def linear_regression_model(x_data, y_data):
  return LinearRegression().fit(x_data, y_data)

def model_y_intercept(linear_regression_model):
  return linear_regression_model.intercept_ 


