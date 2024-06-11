#!/usr/bin/python3

from dataclasses import dataclass
from amenities import Amenity
from reviews import Review
from typing import List
import datetime
from user import User

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

def validate_location(self):
    if self.lat