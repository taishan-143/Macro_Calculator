import unittest

from unittest.mock import Mock, patch, mock_open
from src.main.functions.methods import *

class TestMethods(unittest.TestCase):

    def test_create_register(self):

        database = {"John": {"Johns": "Data"}, "Abbie": {"Abbie's": "Data"}}
        expected = ["John", "Abbie"]

        actual = create_register(database)

        self.assertEqual(expected, actual)

    def test_user_data(self):

        database = {"John": {"Johns": "Data"}, "Abbie": {"Abbie's": "Data"}}
        expected = {"Abbie's": "Data"}

        actual = user_data(database, "Abbie")    

        self.assertEqual(expected, actual)

    def test_table_width__empty_data(self):

        header = "Test"
        data = []
        expected = 6

        actual = table_width(header, data)

        self.assertEqual(expected, actual)

    def test_table_width__dict(self):

        header = "Test"
        data = {1: "Foo", 2: "Bar", 3: "Bazmah"}
        expected = 12

        actual = table_width(header, data)

        self.assertEqual(expected, actual)

    def test_table_width__list(self):

        header = "Test"
        data = ["Foo", "Bar", "Baz"]
        expected = 6

        actual = table_width(header, data)

        self.assertEqual(expected, actual)

    # FIX THIS TEST
    def test_table(self):
        header = "Test"
        data = ["Foo", "Bar", "Baz"]
        expected = None

        actual = table(header, data)

        self.assertEqual(expected, actual)

    # and this one
    # def test_data_table(self):
    #     pass
        
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_read_file(self, mock_file):
        assert open("path/to/file").read() == "data"
        mock_file.assert_called_with("path/to/file")
        
    @patch("builtins.input")
    def test_choose_user(self, mock_input):
        names = ["Tim", "Tom", "Dom", "Jim"]
        table("USER's", names)
        mock_input.return_value = 2
        expected_name = "Tom"

        actual_name = choose_user(names)

        self.assertEqual(expected_name, actual_name)

    @patch("builtins.input")
    def test_choose_user__invalid_input(self, mock_input):
        names = ["Tim", "Tom", "Dom", "Jim"]
        table("USER's", names)
        mock_input.return_value = 'w'
        expected_name = "Tom"

        actual_name = choose_user(names)

        self.assertNotEqual(expected_name, actual_name)

    @patch("builtins.input")
    def test_view_another_page(self, mock_input):
        message = "Would you like to test again?: "
        mock_input.return_value = "y"
        expected_result = 'y'

        actual_result = view_another_page(message)

        self.assertEqual(expected_result, actual_result)
        
    @patch("builtins.input")    
    def test_view_another_page__invalid_input_to_valid(self, mock_input):
        message = "Would you like to test again?: "
        mock_input.side_effect = ['a', 'n']
        expected_result = False

        actual_result = view_another_page(message)

        self.assertEqual(expected_result, actual_result)

    # def test_personal_information(self):
    #     pass

    # def test_app_initialisation(self):
    #     pass

    # def test_view_user_information(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
