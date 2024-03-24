#!/usr/bin/python3
"""FileStorage"""
import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.user import User


class FileStorage:
    """class File"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            dictona = {}
            for key, value in self.__objects.items():
                if type(v) == cls:
                    dictona[key] = value
            return dictona
        return self.__objects

    def new(self, obj):
        """new"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """save"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """reload"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for object in json.load(f).values():
                    name = object["__class__"]
                    del object["__class__"]
                    self.new(eval(name)(**object))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """close"""
        self.reload()
