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

if __name__ == "__main__":
    unittest.main()