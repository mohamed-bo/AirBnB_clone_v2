#!/usr/bin/python3
"""File storgae model"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File storrgae class

    Returns:
        any: any
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Get all

        Args:
            cls (any, optional): classes. Defaults to None.

        Returns:
            any: any
        """
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, BaseModel):
                new_dictenory = {k: v for k,
                            v in self.__objects.items() if isinstance(v, cls)}
                return new_dictenory
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            helper = {}
            helper.update(FileStorage.__objects)
            for key, val in helper.items():
                helper[key] = val.to_dict()
            json.dump(helper, f)

    def reload(self):
        """Reload on start
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            helper = {}
            with open(FileStorage.__file_path, 'r') as f:
                helper = json.load(f)
                for key, val in helper.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except Exception:
            pass

    def delete(self, obj=None):
        """Delete obj

        Args:
            obj (object, optional): will be deleted obj. Defaults to None.
        """
        if obj is None:
            return
        obj_to_del = f"{obj.__class__.__name__}.{obj.id}"

        try:
            del FileStorage.__objects[obj_to_del]
        except Exception:
            pass
