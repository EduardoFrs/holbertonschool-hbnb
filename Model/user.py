#!/usr/bin/python3

from dataclasses import dataclass
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.base_model import BaseModel

@dataclass
class User(BaseModel):

    email: str = None
    password: str = None # Implement hashing for secured password
    first_name: str = None
    last_name: str = None
    places_hosted: list[dict] = None
    reviews_written: list[dict] = None

    """
    Il faut déclarer les var comme ça sinon "TypeError: User.__init__() takes from 1 to 2 positional arguments but 3 were given"
    quand on veut register un nouvel user.
    """
