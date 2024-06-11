#!/usr/bin/python3

from dataclasses import dataclass
from base_model import BaseModel

@dataclass
class Amenity(BaseModel):
    name: str
