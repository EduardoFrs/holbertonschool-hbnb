#!/usr/bin/python3

from dataclasses import dataclass
from user import User
from base_model import BaseModel

@dataclass
class Review(BaseModel):
    user: User
    place: dict
    rating: float
    content: str
