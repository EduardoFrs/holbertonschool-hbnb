#!/usr/bin/python3

import uuid


class User:
    def __init__(self, email, first_name, last_name, password, id, created_at, updated_at):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password
        self.id = str(uuid.uuid4())

#        if self.email is True:
#            raise ValueError("This e-mail adress is already associated to a user.")

class Place:
    def __init__(self, square_meter, max_guests, city, host_username, host_uuid):
        self.square_meter = square_meter
        self.max_guests = max_guests
        self.city = city
        self.host_username = host_username
        self.host_uuid = str(host_uuid.uuid4())

class Appartment(Place):
    def __init__(self, square_meter, max_guests, host_username, host_uuid, room_count):
        super().__init__(square_meter, max_guests, host_username, host_uuid)
        self.room_count = room_count

class Room(Place):
    def __init__(self, square_meter, max_guests, host_username, host_uuid, bed_count):
        super().__init__(square_meter, max_guests, host_username, host_uuid)
        self.bed_count = bed_count

class House(Place):
    def __init__(self, square_meter, max_guests, host_username, host_uuid, floor_number):
        super().__init__(self, square_meter, max_guests, host_username, host_uuid)
        self.floor_number = floor_number


class Review:
    def __init__(self, note)
    pass

class Amenities:
    pass

class Country:
    pass

class City:
    pass

