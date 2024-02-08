#!/usr/bin/python3
import json
from models.base_model import BaseModel

"""Module to control serialization and deserialization of Json files"""


class FileStorage:
    """A class to serialize and deserializes instances to and
    from files to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Method to return the dictionary objects"""

        return self.__objects

    def new(self, obj):
        """Sets a new object with key <obj class name>.id"""

        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj
        print(self.__objects)

    def save(self):
        """Serializes objects into a json file"""

        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Deserialize the json file into objects, but only
        if it exists. If it doesn't, do nothing"""

        try:
            with open(self.__file_path, 'r') as file:
                new_object = json.load(file)
        except FileNotFoundError:
            return

        for key, value in new_object.items():
            class_name, obj_id = key.split('.')
            obj_dict = value
            obj = eval(class_name)(**obj_dict)
            self.__objects[key] = obj
