#!/usr/bin/python3
"Unit tests for FileStorage class"
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import time
import json
import os


class TestFileStorage(unittest.TestCase):
    "Unit tests suite for FileStorage class"

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def Help_test_all(self, classname):
        """ tests for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        new = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(new).__name__, new.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], new)


if __name__ == "__main__":
    unittest.main()
