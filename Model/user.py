#!/usr/bin/python3

from dataclasses import dataclass
import sys
import os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.base_model import BaseModel

@dataclass
class User(BaseModel):

    id: str = None
    username: str = None
    email: str = None
    password: str = None # Implement hashing for secured password
    first_name: str = None
    last_name: str = None

    def __init__(self, data:dict):
        # data validation
        if not isinstance(data['username'], str):
            raise ValueError("Username must be a string.")
        if not data['username']:
            raise ValueError("Username cannot be empty")
