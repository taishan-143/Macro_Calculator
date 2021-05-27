import unittest
import numpy as np

from unittest.mock import Mock, patch
from src.main.functions.body_fat_percentage_calc import * 

class TestBodyFatPercentageCalc(unittest.TestCase):

    def test_male_body_fat_percentage(self):
        # Arrange 
        ## all in inches
        test_neck = 12
        test_abdomen = 35
        test_height = 71
        expected_value = 86.010 * np.log10(test_abdomen - test_neck) - 70.041 * np.log10(test_height) + 36.76 
        # Act
        actual_value = male_body_fat_percentage(test_neck, test_abdomen, test_height)
        # Assert
        self.assertEqual(expected_value, actual_value)

    def test_female_body_fat_percentage(self):
        ## all in inches
        test_neck = 8
        test_waist = 25
        test_hips = 32
        test_height = 66
        expected_value = 163.205 * np.log10(test_waist + test_hips - test_neck) - (97.684 * np.log10(test_height)) - 78.387

        actual_value = female_body_fat_percentage(test_neck, test_waist, test_hips, test_height)

        self.assertEqual(expected_value, actual_value)

    @patch("builtins.input")
    def test_body_fat_percentage_calc__male(self, mock_input):
        
        mock_body_fat = Mock(body_fat_percentage_calc)
        user_data = {"Age": 25, "Sex": "Male", "Weight": 104, "Height": 180}
        mock_input.side_effect = [10, 35]
        expected = 27.39

        actual = body_fat_percentage_calc(user_data)

        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_body_fat_percentage_calc__female(self, mock_input):
        
        mock_body_fat = Mock(body_fat_percentage_calc)
        user_data = {"Age": 25, "Sex": "Female", "Weight": 74, "Height": 165}
        mock_input.side_effect = [8, 25, 30]
        expected = 17.44

        actual = body_fat_percentage_calc(user_data)

        self.assertEqual(expected, actual)
    
    @patch("builtins.input")
    def test_body_fat_percentage_calc__key_error(self, mock_input):
    
        mock_body_fat = Mock(body_fat_percentage_calc)
        user_data = {"Age": 200, "Sex": "Unknown", "Weight": 2500, "Height": 1000}
        mock_input.side_effect = [1, 1, 1]
        expected = None

        actual = body_fat_percentage_calc(user_data)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()