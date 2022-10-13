#!/usr/bin/python3
"Unit tests for FileStorage class"
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    "Unit tests suite for FileStorage class"

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file type is correct after deserialization string-str"""
        file_path_str = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(file_path_str))

    def test_object(self):
        """Test __object is type dict after deserialization object - dict"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))


if __name__ == "__main__":
    unittest.main()
