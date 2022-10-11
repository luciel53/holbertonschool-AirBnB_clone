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
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file_obj_ser:
            json.dump(new_dict, file_obj_ser)

    def reload(self):
        """ Deserializes JSON to __objects (only if JSON file (__file_path) """
        try:
            with open(self.__file_path, "r") as file_obj_des:
                obj_dict = json.load(file_obj_des)

                for key, value in obj_dict.items():
                    name_class = eval(value["__class__"])(**value)
                    self.__objects[key] = name_class

        except FileNotFoundError:
            return
