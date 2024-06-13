#!/usr/bin/python3

from dataclasses import dataclass
from amenities import Amenity
from reviews import Review
from typing import List
from user import User
from base_model import BaseModel

@dataclass
class Country(BaseModel):
    name: str = None


@dataclass
class City(BaseModel):
    name: str = None
    country: Country = None

@dataclass
class Place(BaseModel):
    id: str = None
    name: str = None
    description: str = None
    address: str = None
    city: City = None
    country: Country = None
    host_id: int = None # one-to-one relationship with User
    number_of_rooms: int = None
    number_of_bathrooms: int = None
    price_per_night: float = None
    max_guests: int = None
    amenities: List[Amenity] = None
    reviews: List[Review] = None # Placeholder for review references

"""
Pas besoin de __init__ ni de toJSON grace à la @dataclass
"""

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




def add_place_to_host(place: Place, user: User):
    """
    add place to host
    """
    if user.places_hosted is None:
        user.places_hosted = []
    user.places_hosted = []
    user.places_hosted.append(place)
    place.host = user

def add_review_to_user(review: Review, user: User):
    """
    add review to a user
    """
    if user.reviews_written is None:
        user.reviews_written = []
    user.reviews_written.append(review)
    review.user = user

def add_review_to_place(review: Review, place: Place):
    """
    add review to place
    """
    if place.reviews is None:
        place.reviews = []
    place.reviews.append(review)
    review.place = place

def add_amenity(place: Place, amenity: Amenity):
    """
    add amenity to place's listing
    """
    if place.amenities is None:
        place.amenities = []
    place.amenities.append(amenity)
    place.amenity = amenity


