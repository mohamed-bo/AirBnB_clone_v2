#!/usr/bin/python3
"""DBStorage engine"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """databse class"""

    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        sessFACT = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(sessFACT)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.close()
