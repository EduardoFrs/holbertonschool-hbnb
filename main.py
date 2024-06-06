#!/usr/bin/python3

import uuid


class User:
    def __init__(self, email, first_name, last_name, password, id, created_at, updated_at):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password

#        if self.email is True:
#            raise ValueError("This e-mail adress is already associated to a user.")
        self.id = str(uuid.uuid4())

class Place:
    pass

class Review:
    pass

class Amenities:
    pass

class Country:
    pass

class City:
    pass

