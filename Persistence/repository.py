
import sys
import os
import json
from configparser import ConfigParser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class BASE_PATH:
    pass

class DataManager(IPersistenceManager):
    """
    Concrete implementation of persistence manager using in-memory dictionary
    """
    def __init__(self):
        config = ConfigParser()
        config.read("config.json")
        self._data_path = config["DEFAULT"]["data_path"]
        self._loacd_data()

    def _load_data(self):
        pass


    def save(self, entity: object):
        # Gets entity's Type/ID then stores it in dictionary

        entity_type = type(entity).__name__ # Get entity type from oject
        entity_id = getattr(entity, "id") # Assuming entities have an ID attribute
        self._data.setdefault(entity_type, {}).get(entity_id)

    def get(self, entity_id: str, entity_type: str):
        # Retrieve entity based on ID / type
        return self._data.get(entity_type, {}).get(entity_id)

    def update(self, entity: object):
        # Updates an existing entity (if found)
        entity_type = type(entity).__name__
        entity_id = getattr(entity, "id")
        if self.get(entity_id, entity_type):
            self._data[entity_type][entity_id] = entity

    def delete(self, entity_id: str, entity_type: str):
        # Deletes entity based on type/ID
        # Removes the key
        if entity_type in self._data:
            del self._data[entity_type][entity_id]
            if not self._data[entity_type]:
                del self._data[entity_type]
