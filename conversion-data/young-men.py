## All dictionaries are in the form {Measurement in inches : Constant value}
import decimal
from src.math_methods import float_range

### CONSTANTS ###
UPPER_ARM_CONSTANTS = [25.91, 26.83, 27.76, 28.68, 29.61, 30.53, 31.46, 32.38, 33.31, 34.24, 35.16, 36.09, 37.01, 37.94, 38.86, 39.79, 40.71, 41.64, 42.56, 43.49, 44.41, 45.34, 46.26, 47.19, 48.11, 49.04, 49.96, 50.89, 51.82, 52.74, 53.67, 54.59, 55.52, 56.44, 57.37, 58.29, 59.22, 60.14, 61.07, 61.99, 62.92, 63.84, 64.77, 65.69, 66.62, 67.54, 68.47, 69.40, 70.32, 71.25, 72.17, 73.10, 74.02, 74.95, 75.87, 76.80, 77.72, 78.65, 79.57, 80.50, 81.42]
ABDOMEN_CONSTANTS = [27.56, 27.88, 28.21, 28.54, 28.87, 29.20, 29.52, 29.85, 30.18, 30.51, 30.84, 31.16, 31.49, 31.82, 32.15, 32.48, 32.80, 33.13, 33.46, 33.79, 34.12, 34.44, 34.77, 35.10, 35.43, 35.76, 36.09, 36.41, 36.74, 37.07, 37.40, 37.73, 38.05, 38.38, 38.71, 39.04, 39.37, 39.69, 40.02, 40.35, 40.68, 41.01, 41.33, 41.66, 41.99, 42.32, 42.65, 42.97, 43.30, 43.63, 43.96, 44.29, 44.61, 44.94, 45.27, 45.60, 45.93, 46.25, 46.85, 46.91, 47.24, 47.57, 47.89, 48.22, 48.55, 48.88, 49.21, 49.54, 49.86, 50.19, 50.52, 50.85, 51.18, 51.50, 51.83, 52.16, 52.49, 52.82, 53.14, 53.47, 53.80, 54.13, 54.46, 54.78, 55.11]
FOREARM_CONSTANTS = [38.01, 39.37, 40.72, 42.08, 43.33, 44.80, 46.15, 47.51, 48.87, 50.23, 51.58, 52.94, 54.30, 55.65, 57.01, 58.37, 59.73, 61.08, 62.44, 63.80, 65.16, 66.51, 67.87, 69.23, 70.59, 71.94, 73.30, 74.66, 76.02, 77.37, 78.73, 80.09, 81.45, 82.20, 84.16, 85.52, 86.88, 88.23, 89.59, 90.95, 92.31, 93.66, 95.02, 96.38, 97.74, 99.09, 100.45, 101.81, 103.17, 104.52, 105.88, 107.24, 108.60, 109.95, 111.31, 112.67, 114.02, 115.38, 116.74, 118.10, 119.45]

### MEASURES IN INCHES ### 
UPPER_ARM_MEASURE = list(float_range(7, 22.25, 0.25))
ABDOMEN_MEASURE = list(float_range(21, 42.25, 0.25))
FOREARM_MEASURE = list(float_range(7, 22.25, 0.25))

### DICTIONARY {MEASURE:CONSTANT}
UPPER_ARM = zip(UPPER_ARM_MEASURE, UPPER_ARM_CONSTANTS)
ABDOMEN = zip(ABDOMEN_MEASURE, ABDOMEN_CONSTANTS)
FOREARM = zip(FOREARM_MEASURE, FOREARM_CONSTANTS)
