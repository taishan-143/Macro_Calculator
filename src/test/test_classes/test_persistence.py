import unittest

from unittest.mock import Mock, patch
from src.main.classes.persistence import * 

class TestPersistence(unittest.TestCase):

    def test_save_data(self):
        database = {"John Doe": {"Age": 25, "Sex": "Male", "Weight": 100, "Height": 189.0, "Body Fat Percentage": 25, "Maintenance Calories": 2750}}
        filepath = "src/test/test_classes/resources/test_data.json"
        expected_json = {"John Doe": {
                        "Age": 25, 
                        "Sex": "Male", 
                        "Weight": 100, 
                        "Height": 189.0, 
                        "Body Fat Percentage": 20, 
                        "Maintenance Calories": 2750
                        }
                    }
        saved_data = Persistence().save_data(database, filepath, "John Doe", "Body Fat Percentage", 20)

        actual_json = Persistence().load_data("src/test/test_classes/resources/test_data.json")
    

        self.assertEqual(expected_json, actual_json)

if __name__ == "__main__":
    unittest.main()

