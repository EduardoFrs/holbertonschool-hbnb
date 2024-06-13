#!/usr/bin/python3

from dataclasses import dataclass
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.base_model import BaseModel

@dataclass
class User(BaseModel):
    email: str
    password: str # Implement hashing for secured password
    first_name: str
    last_name: str
    places_hosted: list[dict] = None
    reviews_written: list[dict] = None # Placeholder for place references

print(sys.path)

User()
