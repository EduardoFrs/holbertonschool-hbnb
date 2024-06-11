#!/usr/bin/python3

from dataclasses import dataclass

@dataclass
class User:
    email: str
    password: str # Implement hashing for secured password
    first_name: str
    last_name: str
    places_hosted: list[dict] = None
    reviews_written: list[dict] = None # Placeholder for place references
