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
    created_at: str
    updated_at: str

user_uuid = str(uuid.uuid4()) #creating the UUID
