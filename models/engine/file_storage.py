#!/usr/bin/python3
"""Module for FileStorage class."""

import json


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
                self.__objects = {}
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        obj_dict = value
                        from models.base_model import BaseModel
                        obj = BaseModel(**obj_dict)
                    elif class_name == "User":
                        obj_dict = value
                        from models.user import User
                        obj = User(**obj_dict)
                    elif class_name == "Place":
                        obj_dict = value
                        from models.place import Place
                        obj = Place(**obj_dict)
                    elif class_name == "State":
                        from models.state import State
                        obj_dict = value
                        obj = State(**obj_dict)
                    elif class_name == "City":
                        obj_dict = value
                        from models.city import City
                        obj = City(**obj_dict)
                    elif class_name == "Amenity":
                        obj_dict = value
                        from models.amenity import Amenity
                        obj = Amenity(**obj_dict)
                    elif class_name == "Review":
                        obj_dict = value
                        from models.review import Review
                        obj = Review(**obj_dict)
                    FileStorage.__objects[key] = obj
        except Exception:
            pass
