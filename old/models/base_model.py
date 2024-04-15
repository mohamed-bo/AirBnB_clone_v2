#!/usr/bin/python3
"""The base model
Returns:
    any: anything
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()

class BaseModel:
    """_summary_

    Returns:
        _type_: _description_
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new base model that will be inherted"""
        self.id = str(uuid.uuid4())
        if not kwargs:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if kwargs:
            date_formate = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, date_formate)
                if hasattr(self, k):
                    setattr(self, k, v)

    def __str__(self):
        """Function to make the obj string

        Returns:
            String: Object as a string
        """
        str_cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f'[{str_cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """To save the new objs
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        trans_dict = {}
        trans_dict.update(self.__dict__)
        trans_dict.update({'__class__':
                         (str(type(self)).split('.')[-1]).split('\'')[0]})
        trans_dict['created_at'] = self.created_at.isoformat()
        trans_dict['updated_at'] = self.updated_at.isoformat()
        try:
            if trans_dict["_sa_instance_state"]:
                del trans_dict["_sa_instance_state"]
        except Exception:
            pass
        return trans_dict

    def delete(self):
        """Function that delete an obj
        """
        from models import storage
        storage.delete(self)
