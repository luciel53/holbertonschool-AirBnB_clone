#!/usr/bin/python3
"""The class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage():
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return objects the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {key_obj: obj.to_dict()
                        for key_obj, obj in self.__objects.items()}
            json.dump(obj_dict, f)
        

    def reload(self):
        """ Deserializes JSON to __objects (only if JSON file (__file_path) """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
