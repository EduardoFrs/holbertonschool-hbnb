#!/usr/bin/python3

from Model import Place, User, Review, Amenity
from Persistence import repository
from abc import ABC, abstractmethod

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

class IPersistenceManager(ABC):
    """
    Interface outlining methods for data persistence operations
    """
    @abstractmethod
    def save(self, entity: object):
        """
        Saves an entity to persistent storage
        Args: entity(object)
        """
        pass

    @abstractmethod
    def get(self, entity_id: str, entity_type: str):
        """
        Retrieves entity from persistent storage by ID and type
        Args: ID & type
        Returns: the entity (object), or None
        """
        pass

    @abstractmethod
    def update(self, entity: object)
        """
        Updates an existing entity in persistent storage
        Args: entity (object)
        """
        pass

    @abstractmethod
    def delete(self, entity_id: str, entity_type: str):
        """
        Deletes an entity from persistent storage by its ID / Type
        Args: ID & type
        """
        pass



class DataManager(IPersistenceManager):
    """
    subclass of IPersistenceManager
    inherits of methods from parent class.
    """
    def save(self, entity):
        """
        save entity into storage
        """
        pass

    def get(self, entity_id, entity_type):
        """
        retrieve entity based on ID / type
        """
        pass

    def delete(self, entity_id, entity_type):
        """
        delete entity from storage
        """
        pass

