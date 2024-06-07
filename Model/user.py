#!/usr/bin/python3

from dataclasses import dataclass
import uuid

@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_uuid: str
    password: str
