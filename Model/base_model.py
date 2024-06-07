#!/usr/bin/python3

import uuid
from dataclasses import dataclass

"""
All the subclasses will inherit from this module/class
using dataclasses instead of pydantic
"""

@dataclass(slots=True)
class Place:
    square_meter: float | int
    max_guests: int
    city: str
    country: str
    host_username: str
    host_uuid: str

