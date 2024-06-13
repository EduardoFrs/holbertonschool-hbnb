#!/usr/bin/python3
""" from Model.base_model import User """
from abc import ABC, abstractmethod
import sys
from Model.user import User

sys.path.insert(0, 'C:/mnt/c/Users/HSP/Documents/Holberton Python/holbertonschool-hbnb/Model/')


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
    def update(self, entity: object):
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
    Concrete implementation of persistence manager using in-memory dictionary
    """
    def __init__(self):
        self._data = {} # Dictionary where entities are stored
                        # {entity_type: {id: entity}}


    def save(self, entity: object):
        """
        Gets entity's Type/ID then stores it in dictionary
        """
        entity_type = type(entity).__name__ # Get entity type from oject
        entity_id = getattr(entity, "id") # Assuming entities have an ID attribute
        self._data.setdefault(entity_type, {}).get(entity_id)

    def get(self, entity_id: str, entity_type: str):
        """
        Retrieve entity based on ID / type
        """
        return self._data.get(entity_type, {}).get(entity_id)

    def update(self, entity: object):
        """
        Updates an existing entity (if found)
        """
        entity_type = type(entity).__name__
        entity_id = getattr(entity, "id")
        if self.get(entity_id, entity_type):
            self._data[entity_type][entity_id] = entity

    def delete(self, entity_id: str, entity_type: str):
        """
        Deletes entity based on type/ID
        Removes the key
        """
        if entity_type in self._data:
            del self._data[entity_type][entity_id]
            if not self._data[entity_type]:
                del self._data[entity_type]


user1 = User(1, "Macron")
user2 = User(2, "Chirac")

data_manager = DataManager()
data_manager.save(user1)
data_manager.save(user2)

retrieved_user = data_manager.get(1, "User")
print(retrieved_user.name)
data_manager.delete(2, "User")