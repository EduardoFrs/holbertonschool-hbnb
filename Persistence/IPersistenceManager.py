
from abc import ABC, abstractmethod
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class IPersistenceManager(ABC):
    """
    Interface outlining methods for data persistence operations
    """
    @abstractmethod
    def save(self, entity: object):
        pass

    @abstractmethod
    def get(self, entity_id: str, entity_type: str):
        pass

    @abstractmethod
    def update(self, entity: object):
        pass

    @abstractmethod
    def delete(self, entity_id: str, entity_type: str):
        pass
