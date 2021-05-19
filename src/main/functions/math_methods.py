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
# defines an array of data to be places on an axis of a graph
def axes_data(list_of_data):
  return np.array(list_of_data)

# fits a graph with 2 sets of data, on an x and y axis
def linear_regression_model(x_data, y_data):
  return LinearRegression().fit(x_data, y_data)

# calculates the y-intercept of the graph
def model_y_intercept(linear_regression_model):
  return linear_regression_model.intercept_ 

# calculates the gradient of the graph 
def model_gradient(linear_regression_model):
  return linear_regression_model.coef_[0] 

# returns the response for a given regressor i.e. y = mx + c
def model_response_prediction(model_y_intercept, model_gradient, input_measure):
  return model_y_intercept + (model_gradient * input_measure)

def model_R_squared(linear_regression_model, x_data, y_data):
  return linear_regression_model.score(x_data, y_data)

### summation of the above methods
def constant_evaluation(measures, constants, input_measure):
  x_data = axes_data(measures).reshape((-1,1))
  y_data = axes_data(constants)
  Model = linear_regression_model(x_data, y_data)
  y_intercept = model_y_intercept(Model)
  gradient = model_gradient(Model)
  return model_response_prediction(y_intercept, gradient, input_measure)

def body_fat_percentage(age, sex, constant_A, constant_B, constant_C):
  if sex[0] == 'm':
    if age < 30:
      return constant_A + constant_B - constant_C - 10.2
    else:
      return constant_A + constant_B - constant_C - 15
  elif sex[0] == 'f':
      return constant_A + constant_B - constant_C - 19.6
  else:
    raise KeyError

'''IMPLEMENT IN THE FUTURE'''