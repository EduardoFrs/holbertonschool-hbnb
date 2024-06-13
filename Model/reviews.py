#!/usr/bin/python3

from dataclasses import dataclass
from user import User
from base_model import BaseModel

@dataclass
class Review(BaseModel):
    user: User = None
    place: dict = None
    rating: float = None
    content: str = None
