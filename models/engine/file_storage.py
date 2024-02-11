#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        obj_dict = value
                        obj = BaseModel(**obj_dict)
                    elif class_name == "User":
                        obj_dict = value
                        obj = User(**obj_dict)
                    elif class_name == "Place":
                        obj_dict = value
                        obj = Place(**obj_dict)
                    elif class_name == "State":
                        obj_dict = value
                        obj = State(**obj_dict)
                    elif class_name == "City":
                        obj_dict = value
                        obj = City(**obj_dict)
                    elif class_name == "Amenity":
                        obj_dict = value
                        obj = Amenity(**obj_dict)
                    elif class_name == "Review":
                        obj_dict = value
                        obj = Review(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
