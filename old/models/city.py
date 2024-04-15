#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """city class that extend BaseModel and Base

    Args:
        BaseModel (BaseModel): the base model
        Base (declarative_base): the declarative base
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
