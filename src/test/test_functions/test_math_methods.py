import unittest
import numpy as np

from sklearn.linear_model import LinearRegression
from unittest.mock import Mock, patch
from src.main.functions.math_methods import *
class TestMathMethods(unittest.TestCase):

    def test_float_range(self):
        # Arrange
        expected = [1, 1.25, 1.5, 1.75, 2]
        # Act 
        actual = float_range(1, 2.25, 0.25)
        # Assert
        self.assertEqual(expected, actual)

    def test_axes_data(self):
        # Arrange
        expected = [1, 2, 3, 4, 5]
        # Act
        actual = axes_data([1,2,3,4,5])
        # Assert
        np.testing.assert_array_equal(expected, actual, "Arrays are NOT equal")

    def test_linear_regression_model(self):
        # Arrange
        x = axes_data([1,2,3,4,5]).reshape((-1,1))
        y = axes_data([6,7,8,9,10])
        expected = linear_regression_model(x, y)
        # Act 
        actual = LinearRegression
        #Assert
        self.assertIsInstance(expected, actual)

    def test_model_y_intercept(self):
        # Arrange
        x = axes_data([1,2,3,4,5]).reshape((-1,1))
        y = axes_data([1,2,3,4,5])
        model = linear_regression_model(x, y)
        expected = 0
        # Act 
        actual = int(model_y_intercept(model))
        ## SHOULD REALLY TEST THAT X VALUE OF INTERCEPT EQUALS 0.
        # Assert
        self.assertEqual(expected, actual)
    
    def test_model_gradient(self):
        # Arrange
        x = axes_data([1,2,3,4,5]).reshape((-1,1))
        y = axes_data([1,2,3,4,5])
        model = linear_regression_model(x, y)
        expected = 1
        # Act 
        actual = int(model_gradient(model))
        ## SHOULD REALLY TEST THAT X VALUE OF INTERCEPT EQUALS 0.
        # Assert
        self.assertEqual(expected, actual)

    def test_model_response_prediction(self):
        # Arrange
        x = axes_data([1,2,3,4,5]).reshape((-1,1))
        y = axes_data([1,2,3,4,5])
        model = linear_regression_model(x, y)
        expected = 3
        # Act
        actual = model_response_prediction(0, 1, 3)
        # Assert
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()