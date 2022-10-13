#!/usr/bin/python3
"Unit tests for FileStorage class"
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    "Unit tests suite for FileStorage class"

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
    
    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.list_classes:("BaseModel")


if __name__ == "__main__":
    unittest.main()
