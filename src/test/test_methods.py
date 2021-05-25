import unittest

from unittest.mock import Mock, patch
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
    def test_data_table(self):
        pass
        

    def test_read_file(self):
        pass

    def test_choose_user(self):
        pass

    def test_view_another_page(self):
        pass

    def test_personal_information(self):
        pass

    def test_app_initialisation(self):
        pass

    def test_view_user_information(self):
        pass

if __name__ == "__main__":
    unittest.main()