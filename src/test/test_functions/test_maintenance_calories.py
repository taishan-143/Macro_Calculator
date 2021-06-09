import unittest

from unittest.mock import Mock, patch
from src.main.functions.maintenance_calories import *

class TestMaintenanceCalories(unittest.TestCase):

    def test_male_REE(self):
        weight = 100
        height = 180
        age = 25
        expected_result = 2005

        actual_result = male_REE(weight, height, age)

        self.assertEqual(expected_result, actual_result)

    def test_female_REE(self):
        weight = 70
        height = 150
        age = 25
        expected_result = 1351.5

        actual_result = female_REE(weight, height, age)

        self.assertEqual(expected_result, actual_result)

    def test_calculate_REE__male(self):
        sex = "male"
        weight = 100
        height = 180
        age = 25

        expected_result = male_REE(weight, height, age)

        actual_result = calculate_REE(sex, weight, height, age)

        self.assertEqual(expected_result, actual_result)

    def test_calculate_REE__female(self):
        sex = "female"
        weight = 100
        height = 180
        age = 25

        expected_result = female_REE(weight, height, age)

        actual_result = calculate_REE(sex, weight, height, age)

        self.assertEqual(expected_result, actual_result)


    @patch("builtins.input")
    def test_determine_TDEE_constant(self, mock_input):
        activity = "test"
        # this side effect will first test that the function doesn't accept values out of the bounded area
        mock_input.side_effect = [0, 5, 1]
        expected_result = 1.2

        actual_result = determine_TDEE_constant(activity)

        self.assertEqual(expected_result, actual_result)

    def test_calculate_TDEE(self):
        TDEE_constant = 1.2
        REE = 1500

        expected_value = 1800

        actual_value = calculate_TDEE(TDEE_constant, REE)

        self.assertEqual(expected_value, actual_value)


        
if __name__ == "__main__":
    unittest.main()