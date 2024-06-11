#!/usr/bin/python3

from dataclasses import dataclass

@dataclass
class User:
    email: str
    password: str
    first_name: str
    last_name: str
    places_hosted: list[dict] = None
    reviews_written: list[dict] = None
