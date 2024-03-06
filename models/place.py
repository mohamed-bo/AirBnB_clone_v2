#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class the will be used to interact with the places

    Args:
        BaseModel (BaseModel): The Base Model for all classes
    """
    max_guest = 0
    description = ""
    city_id = ""
    user_id = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    name = ""
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
