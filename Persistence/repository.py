import sys
import os
import json
from configparser import ConfigParser
from IPersistenceManager import IPersistenceManager


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DataManager(IPersistenceManager):
    # Concrete implementation of persistence manager using in-memory dictionary
    def __init__(self):
        # stores the data path retrieved in config.json
        config = ConfigParser()
        config.read("data/config.json")
        self._data_path = config["DEFAULT"]["data_path"]
        self._load_data()
        self.supported_entity_types = []
        # dynamic registration of entity types
    def register_entity_type(self, entity_type: str):
        self._supported_entity_types.append(entity_type)

    def get_supported_entity_types(self):
        # return list of supported entities
        return list(self.supported_entity_types)

    def _load_data(self):
        for entity_type in self.get_support_entity_types():
            file_path = os.path.join(self._data_path, f"{entity_type}.json")
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.data[entity_type] = data
            except (FileNotFoundError, json.JSONDecodeError):
                raise TypeError("File Error.")

    def save_data(self):
        for entity_type, data in self._data.items():
            file_path = os.path.join(self._data_path, f"{entity_type}.json")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

    def save(self, entity: object):
        # Saves an entity object to corresponding JSON file
        # Args: entity(object) to be saved
        # Raises: typeerror if entity object doesn't have ID attribute
        entity_type = type(entity).__name__ # Get entity type from oject
        entity_id = getattr(entity, "id") # Assuming entities have an ID attribute
        self._data.setdefault(entity_type, {}).get(entity_id)
        self._save_data()

    def get(self, entity_type: str, entity_id: str) -> object:
        # Retrieve entity based on type / ID
        # Args: entity_type (str)
        #       entity_id (str)
        # Returns: object found or None
        entity_data = self.data.get(entity_type, {})
        return self._data.get(entity_type, {}).get(entity_id)

    def update(self, entity: object):
        # Updates an existing entity (if found)
        # Args: entity(object)
        # Returns: bool: True if entity updated, or false (entity not found)
        # If true, updates in-memory data
        entity_type = type(entity).__name__
        entity_id = getattr(entity, "id")
        if not self.get(entity_type, entity_id):
            return False | print("Entity not found")
        if self.get(entity_id, entity_type):
            self._data[entity_type][entity_id] = entity
            self._save_data() # updates the JSON
            return True

    def delete(self, entity_type: str, entity_id: str):
        # Deletes entity from data store and persist changes to JSON
        # Args: entity_type (str)
        #        entity_id (str)
        # Returns: bool: True if deleted successfully or False
        # Raises KeyError if ID doesn't exist
        if entity_type not in self._data:
            return False
        try:
            del self._data[entity_type][entity_id]
        except KeyError:
            return False
        # After deleting entity, checks if entity_type is in _data dict is empty to remove it so it stays clean
        if not self._data[entity_type]:
                del self._data[entity_type]
                self._save_data()
                return True

