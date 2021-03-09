import decimal
import numpy as np
from src.main.math_methods import *
from sklearn.metrics import mean_squared_error, r2_score

### CONSTANTS ###

# CONSTANT A
BUTTOCKS_CONSTANTS = [29.34, 29.60, 29.87, 30.13, 30.39, 30.65, 30.92, 31.18, 31.44, 31.70, 31.96, 32.22, 32.49, 32.75, 33.01, 33.27, 33.54, 33.80, 34.06, 34.32, 34.58, 34.84, 35.11, 35.37, 35.63, 35.89, 36.16, 36.42, 36.68, 36.94, 37.20, 37.46, 37.73, 37.99, 38.25, 38.51, 38.78, 39.04, 39.30, 39.56, 39.82, 40.08, 40.35, 40.61, 40.87, 41.13, 41.39, 41.66, 41.92, 42.18, 42.44, 42.70, 42.97, 43.23, 43.49, 43.75, 44.02, 44.28, 44.54, 44.80, 45.06, 45.32, 45.59, 45.85, 46.12, 46.37, 46.64, 46.89, 47.16, 47.42, 47.68, 47.94, 48.21, 48.47, 48.73, 48.99, 49.26, 49.52, 49.78, 50.04, 50.30, 50.56, 50.83, 51.09, 51.35]
# CONSTANT B
ABDOMEN_CONSTANTS = [22.84, 23.06, 23.29, 23.51, 23.73, 23.96, 24.18, 24.40, 24.63, 24.85, 25.08, 25.29, 25.52, 25.75, 25.97, 26.19, 26.42, 26.64, 26.87, 27.09, 27.32, 27.54, 27.76, 27.98, 28.21, 28.43, 28.66, 28.88, 29.11, 29.33, 29.55, 29.78, 30.00, 30.22, 30.45, 30.67, 30.89, 31.12, 31.35, 31.57, 31.79, 32.02, 32.24, 32.46, 32.69, 32.91, 33.14, 33.36, 33.58, 33.81, 34.03, 34.26, 34.48, 34.70, 34.93, 35.15, 35.38, 35.59, 35.82, 36.05, 36.27, 36.49, 36.72, 36.94, 37.17, 37.39, 37.62, 37.87, 38.06, 38.28, 38.51, 38.73, 38.96, 39.18, 39.14, 39.63, 39.85, 40.08, 40.30]
# CONSTANT C
FOREARM_CONSTANTS = [21.01, 21.76, 22.52, 23.26, 24.02, 24.76, 25.52, 26.26, 27.02, 27.76, 28.52, 29.26, 30.02, 30.76, 31.52, 32.27, 33.02, 33.77, 34.52, 35.27, 36.02, 36.77, 37.53, 38.27, 39.02, 39.77, 40.53, 41.27, 42.03, 42.77, 43.53, 44.27, 45.03, 45.77, 46.53, 47.28, 48.03, 48.78, 49.53, 50.28, 51.03, 51.78, 52.54, 53.28, 54.04, 54.78]

### MEASURES IN INCHES
BUTTOCKS_MEASURE = list(float_range(28, 49.25, 0.25))
ABDOMEN_MEASURE = list(float_range(25.5, 45.25, 0.25))
FOREARM_MEASURE = list(float_range(7, 18.5, 0.25))

### DICTIONARY {MEASURE:CONSTANT}
BUTTOCKS = zip(BUTTOCKS_MEASURE, BUTTOCKS_CONSTANTS)
ABDOMEN = zip(ABDOMEN_MEASURE, ABDOMEN_CONSTANTS)
FOREARM = zip(FOREARM_MEASURE, FOREARM_CONSTANTS)

# print(BUTTOCKS_CONSTANTS)
# print(BUTTOCKS_MEASURE)


x = axes_data(BUTTOCKS_MEASURE).reshape((-1,1))
y = axes_data(BUTTOCKS_CONSTANTS)
model = linear_regression_model(x, y)

y_intercept = model_y_intercept(model)
gradient = model_gradient(model)

model_value = model_response_prediction(y_intercept, gradient, x)
print(model_value)
model_score = model_R_squared(model, x, y)
print(model_score)

print('\n')

import_model_score = r2_score(y, model_value)
print(import_model_score)
rmse = mean_squared_error(y, model_value)
print(rmse)
