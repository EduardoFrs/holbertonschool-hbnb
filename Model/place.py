#!/usr/bin/python3

import dataclasses

@dataclasses.dataclass
class Place:
    square_meters: int | float
    number_of_rooms: int
    max_guests: int
    number_of_rooms: int
    city: str
    gps: str
    country: str
    host_username: str
    host_uuid: str

@dataclasses.dataclass
class Appartment(Place):
    floor_number: int

@dataclasses.dataclass
class Room(Place):
    i_dont_know: bool


@dataclasses.dataclass
class House(Place):
    pool: bool

