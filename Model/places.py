#!/usr/bin/python3

from dataclasses import dataclass
from amenities import Amenity
from reviews import Review

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
    host: str
    number_of_rooms: int
    number_of_bathrooms: int
    price_per_night: float
    max_guests: int
    amenities: list[Amenity] = None
    reviews: list[Review] = None
