import unittest

from unittest.mock import Mock, patch
from src.main.classes.person import * 

class TestPerson(unittest.TestCase):
    
    
    @patch("builtins.input")
    def test_input_name(self, mock_input):
        mock_input.return_value = "john doe"
        expected = "John Doe"

        actual = Person().input_name()

        self.assertEqual(expected, actual)

    @patch("builtins.input") # mock the print function here
    def test_input_age(self, mock_input):
        mock_input.side_effect = [-4, 0, 25]
        expected = 25

        actual = Person().input_age()

        self.assertEqual(expected, actual)

    @patch("builtins.input") # and here
    def test_input_sex(self, mock_input):
        mock_input.side_effect = ['e', 'f']
        expected = 'f'

        actual = Person().input_sex()

        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_input_weight(self, mock_input):
        mock_input.side_effect = [-5, 100]
        expected = 100

        actual = Person().input_weight()

        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_input_height(self, mock_input):
        mock_input.side_effect = [-44, 180]
        expected = 180

        actual = Person().input_height()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

