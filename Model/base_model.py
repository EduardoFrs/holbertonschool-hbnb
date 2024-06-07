#!/usr/bin/python3

import uuid
from pydantic import BaseModel

"""
All the subclasses will inherit from this module/class
"""
class User(BaseModel):
    def __init__(self, )