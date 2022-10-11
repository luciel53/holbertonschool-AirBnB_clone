#!/usr/bin/python3
"""The class FileStorage"""
import json
from models.base_model import BaseModel
import os

class FileStorage():
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return objects the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key_class, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)
        

    def reload(self):
        """ Deserializes JSON to __objects (only if JSON file (__file_path) """
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                my_obj_dict = json.load(f)
                for key, val in my_obj_dict.items():
                    FileStorage.__objects[key] = eval(val['__class__'])(**val)
