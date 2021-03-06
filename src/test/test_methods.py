import unittest
import numpy as np

from sklearn.linear_model import LinearRegression
from unittest.mock import Mock, patch
from src.main.math_methods import float_range, axes_data, linear_regression_model

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


if __name__ == "__main__":
    unittest.main()