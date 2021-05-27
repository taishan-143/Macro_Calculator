import unittest

from unittest.mock import Mock, patch, mock_open
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



        
if __name__ == "__main__":
    unittest.main()