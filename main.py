#!/usr/bin/python3

from Model import Place, User, Review, Amenity

def add_place_to_host(place: Place, user: User):
    if user.places_hosted is None:
        user.places_hosted = []
    user.places_hosted = []
    user.places_hosted.append(place)
    place.host = user

def add_review_to_user(review: Review, user: User):
    if user.reviews_written is None:
        user.reviews_written = []
    user.reviews_written.append(review)
    review.user = user

def add_review_to_place(review: Review, place: Place):
    if place.reviews is None:
        place.reviews = []
    place.reviews.append(review)
    review.place = place

