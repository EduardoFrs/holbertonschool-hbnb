#!/usr/bin/python3

from dataclasses import dataclass
from amenities import Amenity
from reviews import Review
from typing import List
from user import User
from base_model import BaseModel as MyBaseModel

@dataclass
class Country:
    name: str


@dataclass
class City:
    name: str
    country: Country

@dataclass
class Place:
    name: str
    description: str
    address: str
    city: City
    country: Country
    latitude: float
    longitude: float
    host: User # one-to-one relationship with User
    number_of_rooms: int
    number_of_bathrooms: int
    price_per_night: float
    max_guests: int
    amenities: List[Amenity] = None
    reviews: List[Review] = None # Placeholder for review references

# Error handling for places

def validate_location(self):
    """
    Latitude/longitude validation
    """
    if self.latitude < -90 or self.latitude > 90:
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if self.longitude < -180 or self.longitude > 180:
        raise ValueError("Longitude must be between -180 and 180 degrees.")

def validate_price(self):
    """
    Price validation
    """
    if self.price_per_night < 0:
        raise ValueError("Price can not be negative.")

def validate_max_guests(self):
    """
    Max guests validation
    """
    if self.max_guests < 0:
        raise ValueError("Max guests can not be negative.")

