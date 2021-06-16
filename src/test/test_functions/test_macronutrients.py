import unittest

from unittest.mock import Mock, patch
from src.main.functions.macronutrients import *

class TestMacronutrients(unittest.TestCase):

    @patch("builtins.input")
    def test_new_caloric_intake(self, mock_input):
        maintenance_calories = 2000
        preference = "bulking"
        mock_input.side_effect = [-10, 150, 60]

        expected_value = 3200

        actual_value = new_caloric_intake(preference, maintenance_calories)

        self.assertEqual(expected_value, actual_value)

    @patch("builtins.input")
    def test_protein_choice(self, mock_input):
        mock_input.side_effect = [-4, 132, 35]
        expected = 35

        actual = protein_choice()

        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_fat_choice(self, mock_input):
        protein = 35
        mock_input.side_effect = [-55, 70, 30]
        expected = 30

        actual = fat_choice(protein)

        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_macronutrient_ratios(self, mock_input):
        new_caloric_intake = 1500
        mock_input.side_effect = [30, 30]
        expected = {112.5: 30, 50: 30, 150: 40}

        actual = macronutrient_ratios(new_caloric_intake)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()        